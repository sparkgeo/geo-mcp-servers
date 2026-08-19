---
name: geo-mcp-servers
description: Browse, search, and recommend geospatial / GIS / mapping / earth-observation MCP servers, and add newly discovered ones to the tracked list. Use when the user asks "is there an MCP server for <geospatial thing>", wants to find a geocoding/routing/PostGIS/STAC/imagery/weather MCP server, or says they found a new geo MCP server to track.
license: MIT
---

# Geospatial MCP Servers

This skill wraps a curated, version-controlled catalog of MCP servers for
geospatial work. `servers.yaml` is the source of truth; `README.md` is
generated from it.

## Locate the catalog

The skill is installed at `~/.claude/skills/geo-mcp-servers`, a symlink into
the cloned repo's `skill/` directory. Resolve the repo root from it — do not
assume any absolute path:

```bash
REPO="$(cd "$(dirname "$(readlink ~/.claude/skills/geo-mcp-servers)")" && pwd -P)"
echo "$REPO"   # repo root — parent of the skill dir
```

If `readlink` returns nothing (the skill was copied rather than symlinked), ask
the user where they cloned `geo-mcp-servers`, or search for it, e.g.
`find ~ -name servers.yaml -path '*geo-mcp-servers*' 2>/dev/null`. Use the
resolved `$REPO` in every command below.

## Find / recommend a server

1. Read the catalog data:

   ```bash
   REPO="$(cd "$(dirname "$(readlink ~/.claude/skills/geo-mcp-servers)")" && pwd -P)"
   cat "$REPO/servers.yaml"
   ```

2. Match the user's need to a `category` and to entry `tags`/`description`.
   Categories include: geocoding, routing, mapping, database (PostGIS/DuckDB),
   remote_sensing (STAC/EO), weather, desktop_gis (QGIS/ArcGIS), toolkit,
   data_access, other.

3. Recommend the closest 1–3 servers with their URLs and a one-line why. If
   nothing fits, say so plainly rather than inventing a server.

## Add a newly discovered server

When the user points you at a new geospatial MCP server (a URL, a name, "track
this one"):

1. Confirm it's real and geospatial — fetch/inspect the source URL if needed.
2. Check it isn't already in `servers.yaml` (match on url and name).
3. Append an entry under `servers:` in `$REPO/servers.yaml`:

   ```yaml
     - name: <Name>
       url: <canonical source URL, prefer GitHub repo>
       description: <one line>
       category: <one of the keys in the categories map>
       author: <person/org>
       language: <Python|TypeScript|...>
       official: <true only for vendor-published>
       tags: [<keywords>]
       added: <YYYY-MM-DD>
   ```

4. Regenerate the README (the repo ships a `.venv` with PyYAML):

   ```bash
   REPO="$(cd "$(dirname "$(readlink ~/.claude/skills/geo-mcp-servers)")" && pwd -P)"
   "$REPO/.venv/bin/python" "$REPO/scripts/generate_readme.py"
   ```

   If `$REPO/.venv` is missing (fresh clone), create it once:
   `python3 -m venv "$REPO/.venv" && "$REPO/.venv/bin/pip" install -r "$REPO/requirements.txt"`.

5. Report what you added, and offer to commit `servers.yaml` + `README.md`
   together (don't push without asking).

## Notes

- Never edit the tables in `README.md` by hand — the generator overwrites them.
- Only add `official: true` when the vendor/owner of the underlying service
  publishes the server.
- Prefer one canonical URL per server (the GitHub repo).
