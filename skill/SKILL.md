---
name: geo-mcp-servers
description: Browse, search, and recommend geospatial / GIS / mapping / earth-observation MCP servers, and add newly discovered ones to the tracked list. Use when the user asks "is there an MCP server for <geospatial thing>", wants to find a geocoding/routing/PostGIS/STAC/imagery/weather MCP server, or says they found a new geo MCP server to track.
license: MIT
---

# Geospatial MCP Servers

This skill wraps a curated, version-controlled catalog of MCP servers for
geospatial work. `servers.yaml` is the source of truth; `README.md` is generated
from it; `health.json` caches per-entry health; and `servers.schema.json`
(enforced by CI in `.github/workflows/verify.yml`) defines the entry shape.

## Locate the catalog

The skill is installed at `~/.claude/skills/geo-mcp-servers`, a symlink into the
cloned repo's `skill/` directory. Resolve the repo root from it — never assume an
absolute path:

```bash
REPO="$(cd "$(dirname "$(readlink ~/.claude/skills/geo-mcp-servers)")" && pwd -P)"
echo "$REPO"   # repo root — parent of the skill dir
```

If `readlink` returns nothing (the skill was copied, not symlinked), ask where
they cloned `geo-mcp-servers` or search:
`find ~ -name servers.yaml -path '*geo-mcp-servers*' 2>/dev/null`. Use the
resolved `$REPO` in every command below.

## Find / recommend a server

1. Read the data: `cat "$REPO/servers.yaml"`.
2. Match the need to a `category` and to entry `tags`/`description`. Categories:
   `geocoding`, `routing`, `mapping`, `database` (PostGIS/DuckDB), `remote_sensing`
   (STAC/EO), `weather`, `desktop_gis` (QGIS/ArcGIS), `toolkit`, `data_access`,
   `property` (parcels, ownership, real estate), `tracking` (aviation/maritime — ADS-B/AIS),
   `directory` (specialist location directories, e.g. music venues or gyms), `other`.
3. Each entry also carries **`access`** (🟩 open / 🟨 free / 🟦 commercial /
   🟥 paywalled) and a generated **health** status (🟢 active / 🟡 stale /
   ⚪ hosted / ⏳ pending / 🔴 archived|dead) — use these when recommending
   (e.g. prefer active + open/free unless the user wants a specific vendor).
4. Filter on **`deployment`** (where the server runs). If you do not know how the
   user will connect, ask whether they use a desktop client (Claude Desktop,
   Claude Code, an IDE) or a web client (claude.ai, ChatGPT).
   - Web client: only `hosted` and `local+hosted` servers work. For a
     `local+hosted` server, give the public endpoint from its `note` and say who
     runs it, because queries go to that operator.
   - Desktop client: any value works. Prefer `local` when the user's data must
     stay on their machine.
   - `self-hosted` means the user must deploy an HTTP service; `addin` runs
     inside a desktop app; `unknown` means the README does not say, so tell the
     user to check before relying on it.
5. Recommend the closest 1–3 with URLs, their deployment, and a one-line why. If
   nothing fits, say so rather than inventing a server.

## Add a newly discovered server

1. **Verify it's real and geospatial.** Fabricated/404 URLs have been submitted —
   confirm the source exists before adding: for GitHub, `gh api repos/<owner>/<repo>`;
   for a hosted service, an MCP `initialize` POST to its endpoint should respond
   (200, or 401 if auth-gated). Make sure it's actually an MCP *server*, not just
   an SDK/docs.
2. **Dedup** against `servers.yaml` (match on url and name).
3. **Append an entry** under `servers:` using the current field set:

   ```yaml
     - name: <Name>
       access: <open | free | commercial | paywalled>
       url: <canonical URL — the GitHub repo, or the vendor product/docs page for a hosted service>
       description: <one line, 10–250 chars>
       category: <a key from the categories map above>
       author: <person/org>
       language: <Python | TypeScript | ...>        # optional
       official: true                                # ONLY if the vendor that owns the service publishes it
       vendor_orgs: [<github-org>]                   # REQUIRED when official + a github.com URL (must equal the repo owner)
       vendor_domain: <example.com>                  # REQUIRED when official + non-GitHub URL, AND for any hosted entry (URL host must equal it or be a subdomain)
       deployment: <local | hosted | local+hosted | self-hosted | addin | unknown>   # optional; see below
       watch: true                                   # ONLY if not generally available yet (beta/waitlist) — renders ⏳ pending
       tags: [<keywords>]
       note: <caveat — endpoint URL, API-key need, version support, etc.>   # optional, ≤300 chars
       added: <YYYY-MM-DD>
   ```

   Rules the schema/CI enforce (get these right or the PR fails):
   - **`access`**: `open` = open-source server on free/open data; `free` = free but
     not open source; `commercial` = commercial product *with* a usable free tier;
     `paywalled` = must pay, no free tier.
   - **`official` must be backed.** CI checks the repo owner against `vendor_orgs`
     (GitHub) or the URL host against `vendor_domain` (otherwise). A community
     wrapper of a vendor's paid API is **not** official — leave `official` off.
   - **`deployment`** says where the server runs: `local` (you install it; your client starts it over stdio),
     `hosted` (the vendor runs it; you connect to their URL), `local+hosted` (source you can run, plus a
     public endpoint the vendor runs), `self-hosted` (you deploy it as an HTTP service), `addin` (runs inside
     a desktop app). `check_health.py` suggests a value for entries that have none.
   - **Hosted services**: set `deployment: hosted` + `vendor_domain`.
   - **Not yet GA** (private beta / waitlist): set `watch: true`.

4. **Regenerate the README** (the repo ships a `.venv` with PyYAML):

   ```bash
   "$REPO/.venv/bin/python" "$REPO/scripts/generate_readme.py"
   ```

   If `$REPO/.venv` is missing (fresh clone):
   `python3 -m venv "$REPO/.venv" && "$REPO/.venv/bin/pip" install -r "$REPO/requirements.txt"`.

5. **Refresh health** so the new entry gets a status (needs the `gh` CLI on PATH):

   ```bash
   "$REPO/.venv/bin/python" "$REPO/scripts/check_health.py"   # rewrites health.json; prints a ⏳ watchlist of not-GA entries
   "$REPO/.venv/bin/python" "$REPO/scripts/generate_readme.py"
   ```

6. **Report** what you added and offer to commit `servers.yaml` + `README.md`
   (+ `health.json` if refreshed) together. It's a shared org repo — `git pull
   --rebase` before pushing, and **don't push without asking**.

## Notes

- Never hand-edit the tables in `README.md` — the generator overwrites them, and
  `readme-check.yml` fails the build if the README is stale. Always regenerate
  after editing `servers.yaml`.
- Validate locally before committing (mirrors CI): the entry must satisfy
  `servers.schema.json` and use a real `category` key.
- Prefer one canonical URL per server (the GitHub repo, or the vendor product
  page for hosted-only services).
