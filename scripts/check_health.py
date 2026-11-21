#!/usr/bin/env python3
"""Probe every catalog URL and write health.json — a cache the README generator
reads to render the Health column.

    python scripts/check_health.py

Classification:
  active      GitHub repo pushed within ACTIVE_MONTHS
  stale       GitHub repo not pushed in ACTIVE_MONTHS (real, but dormant)
  archived    GitHub repo flagged archived
  dead        GitHub repo returns 404
  hosted      non-GitHub URL that responds (a hosted service — no push signal)
  unreachable non-GitHub URL that does not respond
  pending     watch:true — early access / not GA yet (URL is not probed); the run
              prints a watchlist reminder to re-check for a public endpoint

Requires the `gh` CLI (authenticated) for GitHub repos. Re-run periodically;
commit the refreshed health.json alongside README.md.

For entries with no `deployment`, or `deployment: unknown`, the run also reads
the repo README and prints a suggested value with the evidence for it. It never edits servers.yaml: review
each suggestion and copy the ones you accept.
"""
from __future__ import annotations

import json
import re
import subprocess
import urllib.error
import urllib.request
from concurrent.futures import ThreadPoolExecutor
from datetime import date, datetime, timezone
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parent.parent
ACTIVE_MONTHS = 12  # GitHub repos pushed within this window count as "active"
NOW = datetime.now(timezone.utc)
GH = re.compile(r"https?://github\.com/([^/]+)/([^/#?]+)")
GH_SUBDIR = re.compile(r"https?://github\.com/[^/]+/[^/]+/tree/[^/]+/(.+?)/?$")

# README signals used to suggest a `deployment` value. Heuristic: a human confirms.
LOCAL_HINT = re.compile(r"\bstdio\b|StdioServerTransport|\buvx\b|\bnpx\b|claude_desktop_config", re.I)
HTTP_HINT = re.compile(r"streamable[- ]?http|\bSSE\b|--transport[ =]+(?:http|sse|streamable)", re.I)
# An MCP endpoint URL ends in /mcp or /sse, e.g. https://mcp.mapbox.com/mcp.
ENDPOINT = re.compile(r"https?://([a-z0-9.-]+\.[a-z]{2,}|localhost|127\.0\.0\.1|0\.0\.0\.0)(?::\d+)?(?:/[^\s)\"'`<>?#]*)?/(?:mcp|sse)/?(?=$|[\s)\"'`<>?#\]])", re.I | re.M)
LOOPBACK = {"localhost", "127.0.0.1", "0.0.0.0"}
# Hosts that show up in MCP READMEs but are not the server's own endpoint.
class _Redirect308(urllib.request.HTTPRedirectHandler):
    """Follow 308 Permanent Redirect too; urllib before Python 3.11 does not."""

    def http_error_308(self, req, fp, code, msg, headers):
        return self.http_error_307(req, fp, code, msg, headers)


OPENER = urllib.request.build_opener(_Redirect308)

NOT_ENDPOINTS = ("github.com", "githubusercontent.com", "modelcontextprotocol.io", "npmjs.com",
                 "pypi.org", "smithery.ai", "glama.ai", "example.com", "anthropic.com", "claude.ai",
                 "shields.io", "badge.fury.io", "pepy.tech", "star-history.com", "contrib.rocks",
                 "cursor.com", "vscode.dev", "visualstudio.com", "deepwiki.com", "mcp.so", "mseep.ai")
PLACEHOLDER = re.compile(r"your-|example|<|\{")


def classify(server: dict) -> dict:
    if server.get("watch"):
        return {"status": "pending"}  # not GA yet — surfaced on the watchlist
    url = server.get("url", "")
    m = GH.match(url)
    if m:
        owner, repo = m.group(1), m.group(2).removesuffix(".git")
        r = subprocess.run(
            ["gh", "api", f"repos/{owner}/{repo}", "--jq", "{a:.archived,p:.pushed_at}"],
            capture_output=True, text=True, timeout=30,
        )
        if r.returncode != 0:
            return {"status": "dead" if "Not Found" in r.stderr else "unreachable"}
        info = json.loads(r.stdout)
        if info["a"]:
            return {"status": "archived", "pushed": info["p"][:7]}
        months = (NOW - datetime.fromisoformat(info["p"].replace("Z", "+00:00"))).days / 30.44
        return {"status": "active" if months <= ACTIVE_MONTHS else "stale", "pushed": info["p"][:7]}
    # Non-GitHub (hosted service / vendor docs)
    try:
        req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
        with OPENER.open(req, timeout=20) as resp:
            entry = {"status": "hosted" if resp.status < 400 else "unreachable"}
            if resp.url.rstrip("/") != url.rstrip("/"):
                entry["moved_to"] = resp.url  # the catalog URL redirects; update servers.yaml
            return entry
    except urllib.error.HTTPError as e:
        # Auth/bot-block codes mean the server is up but declines automated GETs;
        # an unfollowable redirect (3xx) also means the server answered.
        up = e.code in (401, 403, 405, 406, 429) or 300 <= e.code < 400
        return {"status": "hosted" if up else "unreachable"}
    except Exception:  # noqa: BLE001
        return {"status": "unreachable"}


def suggest_deployment(server: dict) -> dict | None:
    """Suggest a `deployment` value for an entry that has none or `unknown`, from its README."""
    if server.get("deployment") not in (None, "unknown"):
        return None
    url = server.get("url", "")
    m = GH.match(url)
    if not m:
        return {"value": "hosted", "evidence": "non-GitHub URL (vendor page)"}
    owner, repo = m.group(1), m.group(2).removesuffix(".git")
    sub = GH_SUBDIR.match(url)
    path = f"repos/{owner}/{repo}/readme" + (f"/{sub.group(1)}" if sub else "")
    r = subprocess.run(
        ["gh", "api", path, "-H", "Accept: application/vnd.github.raw"],
        capture_output=True, text=True, timeout=30,
    )
    if r.returncode != 0:
        return {"value": None, "evidence": "README not readable"}
    return suggest_from_readme(r.stdout)


def suggest_from_readme(text: str) -> dict:
    hosts = {h.lower() for h in ENDPOINT.findall(text)}
    public = sorted(h for h in hosts - LOOPBACK  # docs.* hosts are documentation, not endpoints
                    if not h.endswith(NOT_ENDPOINTS) and not h.startswith("docs.")
                    and not PLACEHOLDER.search(h))
    # A placeholder endpoint (your-domain.com/mcp) means you deploy it yourself.
    self_run = bool(hosts & LOOPBACK) or any(PLACEHOLDER.search(h) for h in hosts)
    local = bool(LOCAL_HINT.search(text))
    http = bool(HTTP_HINT.search(text)) or self_run
    if public:
        return {"value": "local+hosted", "evidence": f"public endpoint {', '.join(public)}"}
    if local:
        return {"value": "local", "evidence": "stdio/uvx/npx setup" + ("; also serves HTTP" if http else "")}
    if http:
        return {"value": "self-hosted", "evidence": "HTTP/SSE server, no public endpoint"}
    return {"value": None, "evidence": "no clear signal in README"}


def main() -> int:
    servers = yaml.safe_load((ROOT / "servers.yaml").read_text())["servers"]
    with ThreadPoolExecutor(max_workers=12) as ex:
        entries = list(ex.map(classify, servers))
        suggestions = list(ex.map(suggest_deployment, servers))

    result = {
        "checked": date.today().isoformat(),
        "active_months": ACTIVE_MONTHS,
        "servers": {s["url"]: e for s, e in zip(servers, entries) if s.get("url")},
    }
    (ROOT / "health.json").write_text(json.dumps(result, indent=2, sort_keys=True) + "\n")

    counts: dict[str, int] = {}
    for e in entries:
        counts[e["status"]] = counts.get(e["status"], 0) + 1
    summary = " · ".join(f"{k}: {v}" for k, v in sorted(counts.items()))
    print(f"Wrote health.json ({len(entries)} servers, checked {result['checked']})")
    print(summary)
    flagged = [(s.get("name"), e) for s, e in zip(servers, entries)
               if e["status"] in ("stale", "archived", "dead", "unreachable")]
    if flagged:
        print("\nNeeds attention:")
        for name, e in flagged:
            print(f"  [{e['status']}] {name}" + (f"  (pushed {e['pushed']})" if e.get("pushed") else ""))
    moved = [(s.get("name"), e["moved_to"]) for s, e in zip(servers, entries) if e.get("moved_to")]
    if moved:
        print("\nURL redirects — update the url in servers.yaml:")
        for name, target in moved:
            print(f"  {name} -> {target}")
    missing = [(s.get("name"), d) for s, d in zip(servers, suggestions) if d is not None]
    if missing:
        print(f"\nDeployment missing or unknown ({len(missing)}) — suggestions to review, then copy into servers.yaml:")
        for name, d in missing:
            print(f"  {name}: {d['value'] or '?'}  ({d['evidence']})")
    watch = [s.get("name") for s in servers if s.get("watch")]
    if watch:
        print("\n⏳ Watchlist — early access / not GA; re-check for a public endpoint:")
        for name in watch:
            print(f"  {name}")
    experimental = [s.get("name") for s in servers if s.get("experimental")]
    if experimental:
        print("\n🧪 Experimental — re-check whether each is now stable (then drop the flag):")
        for name in experimental:
            print(f"  {name}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
