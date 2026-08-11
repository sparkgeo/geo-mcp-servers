# Contributing

This list is generated. **Do not edit the tables in `README.md` directly** —
they are overwritten by the generator.

## Add a server

1. Open [`servers.yaml`](servers.yaml).
2. Append an entry under `servers:`:

   ```yaml
     - name: Example Geo MCP
       url: https://github.com/someone/example-geo-mcp
       description: One line on what it does.
       category: geocoding        # see the `categories:` map at the top of the file
       author: Someone
       language: Python
       official: false            # true only for vendor/official servers
       tags: [geocoding, places]
       added: 2026-08-02
   ```

3. Regenerate the README:

   ```bash
   # first time only:
   python3 -m venv .venv && ./.venv/bin/pip install -r requirements.txt
   # every time:
   ./.venv/bin/python scripts/generate_readme.py
   ```

   To refresh the **Health** column (needs the `gh` CLI, authenticated), run the
   health check first — it rewrites `health.json`, which the generator reads:

   ```bash
   ./.venv/bin/python scripts/check_health.py && ./.venv/bin/python scripts/generate_readme.py
   ```

4. Commit `servers.yaml`, `README.md` (and `health.json` if you refreshed it).

## Rules of thumb

- **One canonical URL**, preferably the GitHub repo.
- Pick the closest existing `category`. Add a new category (in `servers.yaml`)
  only if several servers would share it.
- Keep `description` to a single line, present tense, no trailing period needed.
- Mark `official: true` only when the vendor/owner of the underlying service
  publishes it (e.g. Mapbox's own MCP server).

## No-code option

Not comfortable with YAML? Open a
[New server issue](../../issues/new?template=new-server.yml) with the details
and a maintainer will add it.
