#!/usr/bin/env python3
"""Regenerate README.md tables from servers.yaml.

Usage:
    python scripts/generate_readme.py          # rewrite README.md in place
    python scripts/generate_readme.py --check   # exit 1 if README is stale (CI)

The script only touches the block between the AUTOGEN markers in README.md,
so prose above/below the tables is preserved.
"""
from __future__ import annotations

import json
import re
import sys
from pathlib import Path

try:
    import yaml
except ImportError:
    sys.exit("PyYAML is required: pip install pyyaml")

ROOT = Path(__file__).resolve().parent.parent
DATA = ROOT / "servers.yaml"
README = ROOT / "README.md"
HEALTH = ROOT / "health.json"

START = "<!-- AUTOGEN:START -->"
END = "<!-- AUTOGEN:END -->"

# Health status -> column label. Populated by scripts/check_health.py -> health.json.
HEALTH_LABELS = {
    "active": "🟢 active",
    "stale": "🟡 stale",
    "archived": "🔴 archived",
    "dead": "🔴 dead",
    "unreachable": "🔴 unreachable",
    "hosted": "⚪ hosted",
}


def load_health() -> dict:
    """health.json is optional — the README still generates without it."""
    if HEALTH.exists():
        try:
            return json.loads(HEALTH.read_text())
        except (ValueError, OSError):
            return {}
    return {}


def esc(text: str) -> str:
    return str(text).replace("|", "\\|").replace("\n", " ").strip()


def slug(title: str) -> str:
    """GitHub heading anchor: lowercase, drop punctuation, spaces -> hyphens."""
    s = title.strip().lower()
    s = re.sub(r"[^\w\s-]", "", s)  # remove punctuation (& / , . ( ) ...)
    return s.replace(" ", "-")


def health_summary(health: dict, servers: list[dict]) -> str:
    """One-line health tally + as-of date, or '' when no health.json is present."""
    hservers = health.get("servers") or {}
    if not hservers:
        return ""
    counts: dict[str, int] = {}
    for s in servers:
        st = hservers.get(s.get("url", ""), {}).get("status")
        if st:
            counts[st] = counts.get(st, 0) + 1
    order = ["active", "stale", "hosted", "archived", "dead", "unreachable"]
    parts = [f"{HEALTH_LABELS.get(k, k)} {counts[k]}" for k in order if counts.get(k)]
    months = health.get("active_months", 12)
    return (f"\n_Health checked {health.get('checked', '?')} "
            f"(active = repo pushed within {months} months): "
            f"{' · '.join(parts)}._\n")


def build_tables(data: dict, health: dict) -> str:
    categories: dict[str, str] = data.get("categories", {})
    servers: list[dict] = data.get("servers") or []
    hservers = health.get("servers") or {}

    by_cat: dict[str, list[dict]] = {key: [] for key in categories}
    for srv in servers:
        cat = srv.get("category", "other")
        by_cat.setdefault(cat, []).append(srv)

    total = len(servers)
    lines = [f"**{total} servers tracked** across {sum(1 for v in by_cat.values() if v)} categories."]
    lines.append(health_summary(health, servers))

    # Table of contents
    lines.append("### Categories\n")
    for key, title in categories.items():
        count = len(by_cat.get(key, []))
        if count:
            lines.append(f"- [{title}](#{slug(title)}) ({count})")
    lines.append("")

    show_health = bool(hservers)
    header = "| Server | Description | Lang | By | Type |"
    sep = "| --- | --- | --- | --- | --- |"
    if show_health:
        header += " Health |"
        sep += " --- |"

    for key, title in categories.items():
        rows = sorted(by_cat.get(key, []), key=lambda s: s.get("name", "").lower())
        if not rows:
            continue
        lines.append(f"### {title}\n")
        lines.append(header)
        lines.append(sep)
        for s in rows:
            name = f"[{esc(s.get('name', '?'))}]({s['url']})" if s.get("url") else esc(s.get("name", "?"))
            desc = esc(s.get("description", ""))
            lang = esc(s.get("language", "")) or "—"
            author = esc(s.get("author", "")) or "—"
            kind = "official" if s.get("official") else "community"
            row = f"| {name} | {desc} | {lang} | {author} | {kind} |"
            if show_health:
                status = hservers.get(s.get("url", ""), {}).get("status")
                row += f" {HEALTH_LABELS.get(status, '—')} |"
            lines.append(row)
        lines.append("")

    return "\n".join(lines).rstrip() + "\n"


def render(data: dict, health: dict) -> str:
    block = build_tables(data, health)
    if README.exists():
        text = README.read_text()
        if START in text and END in text:
            pre = text.split(START)[0]
            post = text.split(END)[1]
            return f"{pre}{START}\n\n{block}\n{END}{post}"
    # No README yet: create a minimal one.
    return (
        "# Geospatial MCP Servers\n\n"
        "A curated, tracked list of Model Context Protocol (MCP) servers for "
        "geospatial, GIS, mapping, and earth-observation work.\n\n"
        "> Edit [`servers.yaml`](servers.yaml), then run "
        "`python scripts/generate_readme.py`. See [CONTRIBUTING.md](CONTRIBUTING.md).\n\n"
        f"{START}\n\n{block}\n{END}\n"
    )


def main() -> int:
    data = yaml.safe_load(DATA.read_text()) or {}
    new = render(data, load_health())
    check = "--check" in sys.argv
    current = README.read_text() if README.exists() else ""
    if check:
        if current != new:
            print("README.md is out of date. Run: python scripts/generate_readme.py")
            return 1
        print("README.md is up to date.")
        return 0
    README.write_text(new)
    print(f"Wrote {README.relative_to(ROOT)} ({len(data.get('servers') or [])} servers).")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
