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

Requires the `gh` CLI (authenticated) for GitHub repos. Re-run periodically;
commit the refreshed health.json alongside README.md.
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


def classify(server: dict) -> dict:
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
        with urllib.request.urlopen(req, timeout=20) as resp:
            return {"status": "hosted" if resp.status < 400 else "unreachable"}
    except urllib.error.HTTPError as e:
        # Auth/bot-block codes mean the server is up but declines automated GETs.
        return {"status": "hosted" if e.code in (401, 403, 405, 406, 429) else "unreachable"}
    except Exception:  # noqa: BLE001
        return {"status": "unreachable"}


def main() -> int:
    servers = yaml.safe_load((ROOT / "servers.yaml").read_text())["servers"]
    with ThreadPoolExecutor(max_workers=12) as ex:
        entries = list(ex.map(classify, servers))

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
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
