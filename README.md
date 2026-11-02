# Geospatial MCP Servers

A curated, tracked list of [Model Context Protocol](https://modelcontextprotocol.io) (MCP) servers for **geospatial, GIS, mapping, and earth-observation** work — geocoding, routing, PostGIS, STAC/imagery, QGIS/ArcGIS, weather, and the commercial location platforms. For a strategic overview of what the catalog covers, where the market is heading, and the gaps, see [ANALYSIS.md](ANALYSIS.md).

The tables below are **generated** from [`servers.yaml`](servers.yaml) — the single source of truth.

## Add a server

- **Quick:** open a [New server issue](../../issues/new?template=new-server.yml).
- **Direct:** add an entry to [`servers.yaml`](servers.yaml) and regenerate — see [CONTRIBUTING.md](CONTRIBUTING.md).

  ```bash
  python3 -m venv .venv && ./.venv/bin/pip install -r requirements.txt   # first time
  ./.venv/bin/python scripts/generate_readme.py                          # regenerate tables
  ```

> **Legend** — *Lang / Deployment* gives the implementation language and where the server runs: **local** (you install it; your client starts it), **hosted** (the vendor runs it; you connect to their URL), **local+hosted** (run it yourself, or use a public endpoint), **self-hosted** (you deploy it as an HTTP service), **addin** (runs inside a desktop app) or **unknown**. Only hosted and local+hosted servers work from web clients such as claude.ai. *Type* is `official` (published by the platform/data vendor) or `community` (independent). *Health* comes from [`health.json`](health.json), refreshed by `python scripts/check_health.py`: 🟢 **active** (repo pushed within 12 months) · 🟡 **stale** (real but dormant) · ⚪ **hosted** (a hosted service, no repo activity signal) · ⏳ **pending** (early access / not generally available yet — on the health-check watchlist) · 🔴 **archived/dead**. *Access* is how the underlying service can be used: 🟩 **open** (open-source on free/open data) · 🟨 **free** (free, not open source) · 🟦 **commercial** (a commercial product with a usable free tier) · 🟥 **paywalled** (no free tier — payment required). A few entries carry a `note:` in `servers.yaml` flagging a URL still to be confirmed.

## Use it as a Claude skill

This repo ships a [Claude Code](https://claude.com/claude-code) skill in [`skill/`](skill/) that searches/recommends servers from the catalog and adds new ones. Install it by symlinking into your skills directory (the skill resolves the repo location from this symlink — no hard-coded paths):

```bash
git clone https://github.com/sparkgeo/geo-mcp-servers.git
ln -sfn "$(pwd)/geo-mcp-servers/skill" ~/.claude/skills/geo-mcp-servers
```

Then ask Claude things like *"is there an MCP server for STAC imagery?"* or *"track this new geo MCP server: <url>"*.

<!-- AUTOGEN:START -->

**113 servers tracked** across 12 categories.

_Health checked 2026-11-01 (active = repo pushed within 12 months): 🟢 active 64 · 🟡 stale 18 · ⚪ hosted 28 · ⏳ pending 2 · 🔴 archived 1._


_Access: 🟩 open 48 · 🟨 free 4 · 🟦 commercial 53 · 🟥 paywalled 8._

### Categories

- [Geocoding & place search](#geocoding--place-search) (18)
- [Routing, isochrones & navigation](#routing-isochrones--navigation) (2)
- [Maps, tiles & commercial platforms](#maps-tiles--commercial-platforms) (19)
- [Spatial databases & analytics](#spatial-databases--analytics) (3)
- [Remote sensing, STAC & earth observation](#remote-sensing-stac--earth-observation) (17)
- [Weather & climate](#weather--climate) (12)
- [Desktop & enterprise GIS (QGIS, ArcGIS)](#desktop--enterprise-gis-qgis-arcgis) (10)
- [General GIS / geoprocessing toolkits](#general-gis--geoprocessing-toolkits) (7)
- [Geospatial data access & catalogs](#geospatial-data-access--catalogs) (10)
- [Parcels & property](#parcels--property) (5)
- [Aviation & maritime tracking (ADS-B, AIS)](#aviation--maritime-tracking-ads-b-ais) (6)
- [Other (IP geolocation, misc)](#other-ip-geolocation-misc) (4)

### Geocoding & place search

| Server | Description | Lang / Deployment | By | Type | Access | Health |
| --- | --- | --- | --- | --- | --- | --- |
| [Geoapify MCP Server (community)](https://github.com/OriShmila/geoapify-mcp-server) | Geoapify geocoding, reverse geocoding, places, routing, isolines & travel-time | Python<br>local | OriShmila | community | 🟦 commercial | 🟡 stale |
| [Geoapify MCP Server (official)](https://apidocs.geoapify.com/mcp) | Geocoding, reverse geocoding, place search, routing, route matrices, and GeoJSON geometry operations | hosted | Geoapify | official | 🟦 commercial | ⚪ hosted |
| [geocode-mcp](https://github.com/X-McKay/geocode-mcp) | Lat/long for places via free Nominatim, no API key | Python<br>local | X-McKay | community | 🟩 open | 🟡 stale |
| [GridPin MCP](https://github.com/gridpin/gridpin/tree/main/mcp) | Offline forward and reverse geocoding from one local file per country (US, CA, MX, BR, DE, ES, FR, IT, NL, RS); no API key, queries stay on the machine | Python / Rust<br>local | GridPin | official | 🟩 open | 🟢 active |
| [HERE Maps MCP Server](https://github.com/limingchina/heremaps-mcp-server) | HERE Platform geocoding, reverse geocoding, routing, places search & traffic | TypeScript<br>local | limingchina | community | 🟦 commercial | 🟡 stale |
| [MCP-Geo](https://github.com/webcoderz/MCP-Geo) | Geocoding MCP built on GeoPy — multi-provider (Nominatim, ArcGIS, Bing) | Python<br>unknown | webcoderz | community | 🟩 open | 🟡 stale |
| [mcp-nominatim](https://github.com/pipeworx-io/mcp-nominatim) | Geocoding / reverse geocoding via OSM Nominatim | Python<br>local+hosted | pipeworx-io | community | 🟩 open | 🟢 active |
| [open-streetmap-mcp](https://github.com/jagan-shanmugam/open-streetmap-mcp) | OSM location services — geocode/reverse, POI, directions, meeting points, neighborhood analysis | Python<br>local | Jagan Shanmugam | community | 🟩 open | 🟡 stale |
| [OpenCage Geocoding MCP](https://github.com/OpenCageData/opencage-geocoding-mcp) | Forward/reverse geocoding via the OpenCage API, plus API-status/quota checks | TypeScript<br>local | OpenCage | official | 🟦 commercial | 🟢 active |
| [openstreetmap-mcp-server](https://github.com/cyanheads/openstreetmap-mcp-server) | Geocode, reverse geocode, and Overpass spatial queries (STDIO or Streamable HTTP) | TypeScript<br>local+hosted | cyanheads | community | 🟩 open | 🟢 active |
| [OSM-GeoJSON-MCP-Server](https://github.com/shimizu/OSM-GeoJSON-MCP-Server) | Fetches OSM data as GeoJSON via Overpass | JavaScript<br>unknown | shimizu | community | 🟩 open | 🟢 active |
| [osmmcp](https://github.com/NERVsystems/osmmcp) | OSM geospatial tools — geocoding, routing, nearby places, neighborhood analysis, EV charging | Go<br>unknown | NERV Systems | community | 🟩 open | 🟢 active |
| [PlaceRoot](https://github.com/chuofringer/placeroot) | Overture Maps places, geocoding, admin boundaries, buildings & isochrones via DuckDB (no ETL, no API key); token-budgeted responses with GERS ids | Python<br>local | chuofringer | community | 🟩 open | 🟢 active |
| [Smarty MCP Server](https://www.smarty.com/docs/mcp) | 20 tools for US/international address verification, ZIP lookup, reverse geocoding & property/census enrichment | hosted | Smarty | official | 🟦 commercial | ⚪ hosted |
| [what3words MCP](https://github.com/pipeworx-io/mcp-what3words) | Convert 3-word addresses to lat/long + bounding box | local+hosted | Pipeworx (uses what3words API) | community | 🟦 commercial | 🟢 active |
| [Wheremind](https://wheremind.ai) | Hosted remote MCP for live place search, place details, nearby search, geocoding & turn-by-turn directions for Claude, ChatGPT, Cursor and Claude Code — no Maps API key to manage | hosted | Wheremind | community | 🟦 commercial | ⏳ pending |
| [Zephr Places Grounding MCP](https://zephr.xyz/places-grounding) | Places grounding for local AI — nearest-place search, rich place details & walking navigation (find_nearest_to_me, get_place_details, navigate_to_place) | hosted | Zephr | official | 🟦 commercial | ⚪ hosted |
| [Zip-Codes.com ZIP & Postal Code MCP](https://www.zip-codes.com/api/mcp) | US address validation and standardization to ZIP+4, ZIP and Canadian postal code lookup, reverse geocoding to postal code, radius search, and census tract and district enrichment | hosted | Zip-Codes.com | official | 🟦 commercial | ⚪ hosted |

### Routing, isochrones & navigation

| Server | Description | Lang / Deployment | By | Type | Access | Health |
| --- | --- | --- | --- | --- | --- | --- |
| [OSRM MCP](https://github.com/pipeworx-io/mcp-osrm) | Routing, distances & travel times via OSRM, with map-matching & trip optimization | TypeScript<br>local+hosted | Pipeworx (uses OSRM) | community | 🟩 open | 🟢 active |
| [valhalla-mcp](https://github.com/aatakansalar/valhalla-mcp) | Valhalla OSM routing engine — routing, isochrones, tiles, matrix | TypeScript<br>local | Atakan Salar | community | 🟩 open | 🟡 stale |

### Maps, tiles & commercial platforms

| Server | Description | Lang / Deployment | By | Type | Access | Health |
| --- | --- | --- | --- | --- | --- | --- |
| [ArcGIS Location Services MCP (beta)](https://developers.arcgis.com/ai-tools/mcp-arcgis-location-services/) | Official Esri MCP exposing ArcGIS Location Platform services — geocoding, routing, static maps | hosted | Esri | official | 🟦 commercial | ⚪ hosted |
| [ArcGIS Location Services MCP (community)](https://github.com/lwsinclair/arcgis-location-services-mcp) | Community wrapper over the Esri ArcGIS Location Platform — geocoding, routing, places | local | lwsinclair | community | 🟦 commercial | 🟡 stale |
| [baidu-maps/mcp](https://github.com/baidu-maps/mcp) | Official Baidu Map — geocoding, POI, route planning, weather, IP location, traffic (China) | Python / TypeScript<br>local | Baidu | official | 🟦 commercial | 🟡 stale |
| [CARTO MCP Server](https://docs.carto.com/carto-for-agents/mcp-server) | Remote MCP over CARTO — explore data, render Builder maps inline, run saved spatial Workflows on your cloud warehouse | hosted | CARTO | official | 🟦 commercial | ⚪ hosted |
| [Cesium AI Integrations](https://github.com/CesiumGS/cesium-ai-integrations) | Official Cesium MCP servers & agent skills connecting the Cesium 3D geospatial ecosystem (CesiumJS, 3D Tiles) to AI assistants | TypeScript<br>local | Cesium (CesiumGS) | official | 🟦 commercial | 🟢 active |
| [Felt MCP Server](https://felt.com/blog/introducing-felt-mcp-server) | Remote MCP — create maps, query warehouse, run spatial SQL, style layers, publish live URLs | hosted | Felt | official | 🟦 commercial | ⚪ hosted |
| [foursquare-places-mcp](https://github.com/foursquare/foursquare-places-mcp) | Official Foursquare Places API v3 — venue search, place details, location context | TypeScript<br>unknown | Foursquare | official | 🟦 commercial | 🟡 stale |
| [Geobble](https://api.geobble.com/mcp) | Hosted geospatial workspace — import GIS files and PostGIS data, run spatial analysis, refine cartography, and publish interactive web maps to a stable URL | TypeScript<br>hosted | Geobble | official | 🟦 commercial | ⚪ hosted |
| [GIS Cloud MCP Server](https://manual.giscloud.com/knowledge-base/gis-cloud-ai-mcp/) | Remote read & write MCP for the GIS Cloud platform — 55 tools covering maps, layers, features, spatial queries, forms, tables, file import & map rendering, with OAuth 2.1 sign-in and two-phase confirmation for destructive tools | hosted | GIS Cloud | official | 🟦 commercial | ⚪ hosted |
| [Google Maps MCP (reference)](https://github.com/modelcontextprotocol/servers-archived/tree/main/src/google-maps) | Reference server — geocoding, places, directions, distance matrix, elevation (now archived) | TypeScript<br>local | Anthropic / MCP project | community | 🟦 commercial | 🔴 archived |
| [google-maps-mcp-server](https://github.com/david-pivonka/google-maps-mcp-server) | STDIO server on the new Google Places (New) + Routes APIs | TypeScript<br>local | david-pivonka | community | 🟦 commercial | 🟡 stale |
| [google-maps-places-mcp](https://github.com/domdomegg/google-maps-places-mcp) | Google Places search + photos | TypeScript<br>self-hosted | domdomegg | community | 🟦 commercial | 🟢 active |
| [Mapbox MCP Server](https://github.com/mapbox/mcp-server) | Official Mapbox web services — geocoding, POI search, multimodal routing, matrix, isochrones, static maps | TypeScript<br>local+hosted | Mapbox | official | 🟦 commercial | 🟢 active |
| [MapQuest MCP](https://developer.mapquest.com/documentation/mcp/) | Official MapQuest Location Intelligence Suite — geocoding, routing, place search, traffic & truck-safe routing profiles | hosted | MapQuest | official | 🟦 commercial | ⚪ hosted |
| [MapTiler MCP](https://github.com/pipeworx-io/mcp-maptiler) | MapTiler geocoding, elevation and mapping APIs as MCP tools | local+hosted | Pipeworx (uses MapTiler API) | community | 🟦 commercial | 🟢 active |
| [mcp-google-map](https://github.com/cablate/mcp-google-map) | Google Places (New), Routes, geocoding, distance matrix | TypeScript<br>local | cablate | community | 🟦 commercial | 🟢 active |
| [Stadia Maps MCP Server](https://github.com/stadiamaps/stadiamaps-mcp-server-ts) | Official Stadia Maps APIs - geocoding, search, routing, isochrones, map tiles, time zone lookup | TypeScript<br>unknown | Stadia Maps | official | 🟦 commercial | 🟡 stale |
| [TomTom Maps MCP Server](https://github.com/tomtom-international/tomtom-maps-mcp) | Official TomTom location services — search, geocoding, routing, traffic | TypeScript<br>local | TomTom | official | 🟦 commercial | 🟢 active |
| [TomTom Traffic Analytics MCP](https://github.com/tomtom-international/tomtom-traffic-analytics-mcp) | TomTom MOVE traffic analytics — past, present & predicted traffic | local | TomTom | official | 🟦 commercial | 🟢 active |

### Spatial databases & analytics

| Server | Description | Lang / Deployment | By | Type | Access | Health |
| --- | --- | --- | --- | --- | --- | --- |
| [Overture Maps MCP Server](https://github.com/srivinod1/overture-mcp-server) | Query Overture Maps GeoParquet directly from S3 via DuckDB spatial — buildings, place density, land-use analytics | Python<br>local | srivinod1 | community | 🟩 open | 🟢 active |
| [postgis-mcp](https://github.com/receptopalak/postgis-mcp) | PostGIS database connection over MCP — multi-connection via env vars | Node.js<br>local | receptopalak | community | 🟩 open | 🟢 active |
| [Wherobots MCP Server](https://wherobots.com) | Direct access to WherobotsDB (Apache Sedona) — design & run spatial SQL over S3 & Unity Catalog data | Python<br>hosted | Wherobots | official | 🟦 commercial | ⚪ hosted |

### Remote sensing, STAC & earth observation

| Server | Description | Lang / Deployment | By | Type | Access | Health |
| --- | --- | --- | --- | --- | --- | --- |
| [Arraylake MCP Server](https://docs.earthmover.io/mcp/) | Browse Arraylake repos, inspect schemas, run OGC EDR queries & render maps over Zarr/Icechunk scientific arrays | hosted | Earthmover | official | 🟦 commercial | ⚪ hosted |
| [Axion-MCP](https://github.com/Dhenenjay/Axion-MCP) | Earth Engine analysis platform for Claude Desktop — NDVI/NDWI, classification, maps | TypeScript<br>local | Dhenenjay | community | 🟦 commercial | 🟢 active |
| [copernicus-mcp](https://github.com/wb1016/copernicus-mcp) | Access ESA Copernicus OData API — search/download Sentinel-1/2/3/5P/6 imagery | Python<br>local | wb1016 | community | 🟩 open | 🟢 active |
| [earthdata-mcp](https://github.com/nasa/earthdata-mcp) | LLM access to NASA Common Metadata Repository — discover/verify/access Earth science datasets | Python<br>local | NASA | official | 🟩 open | 🟢 active |
| [google-earth-engine-mcp](https://github.com/cameronking4/google-earth-engine-mcp) | Query Google Earth Engine with natural language — fetch datasets, run tasks, visualize in chat | TypeScript<br>self-hosted | cameronking4 | community | 🟦 commercial | 🟡 stale |
| [LGND Developer MCP](https://github.com/EarthLegend/developer_resources/tree/main/mcp) | Search Earth-embedding collections by text, image chip or coordinates, run inference to create new collections, and inspect chip/cell metadata | local+hosted | LGND AI | official | 🟦 commercial | 🟢 active |
| [LGND Geo](https://lgnd.ai/resources/lgnd-geo) | Hosted MCP for Earth questions over satellite/aerial imagery — find similar locations, analyze change over time, build land-cover classifiers & verify imagery claims (Sentinel-2 + US NAIP) | hosted | LGND AI | official | 🟨 free | ⚪ hosted |
| [Microsoft Planetary Computer Pro MCP Tools](https://techcommunity.microsoft.com/blog/microsoft-planetary-computer-blog/introducing-microsoft-planetary-computer-pro-model-context-protocol-tools-on-vs-/4522346) | 35+ tools connecting Planetary Computer + Planetary Computer Pro, shipped for VS Code / Copilot | hosted | Microsoft | official | 🟥 paywalled | ⚪ hosted |
| [NASA-MCP-server](https://github.com/ProgramComputer/NASA-MCP-server) | Standardized interface to many NASA APIs incl. Earth observations & imagery | TypeScript<br>local | ProgramComputer | community | 🟩 open | 🟢 active |
| [Planet MCP Server (beta)](https://community.planet.com/product-updates/beta-planet-mcp-server-for-ai-agents-6403) | Natural-language search/preview/order over the Planet Insights Platform Data API using existing Planet SDK creds | hosted | Planet Labs | official | 🟥 paywalled | ⚪ hosted |
| [planetary-computer-mcp](https://github.com/isaaccorley/planetary-computer-mcp) | Query & download satellite imagery from the Microsoft Planetary Computer STAC API | Python<br>unknown | Isaac Corley | community | 🟩 open | 🟢 active |
| [SkyFi MCP](https://github.com/jpwilson/skyfi-mcp) | Search 150+ satellites from 12+ providers, compare pricing, order archive or tasking imagery in natural language | local | jpwilson (SkyFi platform) | community | 🟦 commercial | 🟢 active |
| [SkyWatch MCP](https://docs.skywatch.com/docs/mcp/mcp-server/) | Search SkyWatch's commercial satellite imagery archive (700+ sensors from 25+ providers) in natural language, with provider and pricing reference; results link to SkyWatch Explore for viewing and ordering | hosted | SkyWatch | official | 🟦 commercial | ⚪ hosted |
| [stac-mcp](https://github.com/BnJam/stac-mcp) | Natural-language search of any STAC-compliant catalog (defaults to Planetary Computer) | Python<br>local | BnJam | community | 🟩 open | 🟢 active |
| [Tilebox MCP Server](https://tilebox.com/docs/ai/onboard-your-agent) | Create and manage geospatial datasets and distributed workflows, with docs search + CLI and Skills for coding agents | Python / Go<br>hosted | Tilebox | official | 🟦 commercial | ⚪ hosted |
| [unicef-gee-mcp](https://github.com/tryolabs/unicef-gee-mcp) | Google Earth Engine access/analysis for UNICEF workflows | Python<br>self-hosted | Tryolabs (for UNICEF) | community | 🟦 commercial | 🟢 active |
| [Vexcel MCP](https://vexceldata.com/platform/vexcel-mcp/) | Official Vexcel aerial & oblique imagery, DSM/DTM elevation, roof/solar/pool property metadata & post-disaster damage assessments for AI agents | hosted | Vexcel | official | 🟥 paywalled | ⚪ hosted |

### Weather & climate

| Server | Description | Lang / Deployment | By | Type | Access | Health |
| --- | --- | --- | --- | --- | --- | --- |
| [aqicn-mcp](https://github.com/mattmarcin/aqicn-mcp) | Real-time air quality from the World Air Quality Index (AQICN) by city or coordinates | local | mattmarcin | community | 🟨 free | 🟡 stale |
| [dynamical.org Weather & Climate Catalog](https://github.com/dynamical-org/mcp) | Hosted server over dynamical.org's open STAC catalog of cloud-optimized weather & climate archives and forecasts (GFS, HRRR, ECMWF/AIFS) — dataset search & docs, ready-to-run xarray/Zarr/Icechunk snippets, forecast-run freshness | Python<br>local+hosted | dynamical.org | official | 🟩 open | 🟢 active |
| [Government of Canada Weather MCP](https://github.com/SeanLF/weather-mcp) | 5-day weather forecasts for any location in Canada (by latitude/longitude) via the Government of Canada Weather API | Python<br>local | SeanLF | community | 🟩 open | 🟡 stale |
| [mcp_weather_server](https://github.com/isdaniel/mcp_weather_server) | Weather info via the Open-Meteo API | Python<br>local | isdaniel | community | 🟩 open | 🟢 active |
| [NOAA Marine MCP Server](https://github.com/cyanheads/noaa-marine-mcp-server) | NOAA CO-OPS tide stations + NDBC buoys — tide predictions, water levels, tidal currents, live buoy conditions | local+hosted | cyanheads | community | 🟩 open | 🟢 active |
| [NOAA-TidesAndCurrents-MCP](https://github.com/RyanCardin15/NOAA-TidesAndCurrents-MCP) | NOAA Data/Metadata/Derived-Products APIs for tides and currents | TypeScript<br>local | RyanCardin15 | community | 🟩 open | 🟢 active |
| [nws-mcp-server](https://github.com/nitvob/nws-mcp-server) | Quickstart NWS server — get-alerts + get-forecast from the National Weather Service | TypeScript<br>local | nitvob | community | 🟩 open | 🟢 active |
| [open-meteo-mcp](https://github.com/cmer81/open-meteo-mcp) | Full Open-Meteo API — forecast, ERA5 archive, air quality, marine, seasonal | TypeScript<br>local | cmer81 | community | 🟩 open | 🟢 active |
| [open-meteo-mcp-server (cyanheads)](https://github.com/cyanheads/open-meteo-mcp-server) | Open-Meteo forecasts + geocoding, ERA5 historical climate, marine, air quality & terrain elevation | TypeScript<br>local+hosted | cyanheads | community | 🟩 open | 🟢 active |
| [OpenAQ MCP Server](https://github.com/cyanheads/openaq-mcp-server) | Global air-quality stations & pollutant observations (PM2.5, PM10, O3, NO2, SO2, CO) via OpenAQ v3, with SQL over history | local+hosted | cyanheads | community | 🟩 open | 🟢 active |
| [weather-mcp](https://github.com/weather-mcp/weather-mcp) | 17 weather tools — forecasts, alerts, air quality, marine, radar, lightning, rivers, wildfires, history to 1940 (NOAA + Open-Meteo) | Python<br>local | weather-mcp | community | 🟩 open | 🟢 active |
| [weather-mcp (Fahrenheit)](https://github.com/FahrenheitResearch/weather-mcp) | 12 tools — NWS data, NWP model imagery, NEXRAD radar, 205 meteorological calculations | Python<br>unknown | FahrenheitResearch | community | 🟩 open | 🟢 active |

### Desktop & enterprise GIS (QGIS, ArcGIS)

| Server | Description | Lang / Deployment | By | Type | Access | Health |
| --- | --- | --- | --- | --- | --- | --- |
| [ArcGISMCP](https://github.com/GarrickGarcia/ArcGISMCP) | Integrates ArcGIS Online — search/query geospatial feature layers | Python<br>local | GarrickGarcia | community | 🟦 commercial | 🟡 stale |
| [esri-mcp](https://github.com/eKerney/esri-mcp) | Query & map Esri Living Atlas data, focus on water resources | Python<br>unknown | eKerney | community | 🟦 commercial | 🟡 stale |
| [gis-agent-bridges](https://github.com/YUYU20061107/gis-agent-bridges) | Safety-gated MCP bridges for mainstream desktop GIS (SuperMap, ArcGIS Pro/ArcMap, QGIS, GeoScene, MapGIS, ENVI, Global Mapper, FME) - localhost-only, confirm-gated writes, originals read-only, no arbitrary code execution | Python<br>local | YUYU20061107 | community | 🟦 commercial | 🟢 active |
| [MCP-ArcGISPro](https://github.com/geo2004/MCP-ArcGISPro) | Control and automate ArcGIS Pro from Claude Desktop | Python<br>local | geo2004 | community | 🟥 paywalled | 🟢 active |
| [MCP-Server-ArcGIS-Pro-AddIn](https://github.com/nicogis/MCP-Server-ArcGIS-Pro-AddIn) | MCP server delivered as an ArcGIS Pro add-in | C#/.NET<br>addin | nicogis | community | 🟥 paywalled | 🟢 active |
| [qgis-mcp (nkarasiak)](https://github.com/nkarasiak/qgis-mcp) | 117 QGIS tools — layer mgmt, feature editing, processing, styling, layout/atlas, cross-layer SQL | Python<br>local | nkarasiak | community | 🟩 open | 🟢 active |
| [qgis-mcp-1](https://github.com/Sir-Adrien-Claudington/qgis-mcp-1) | Fork connecting QGIS to Claude via MCP | Python<br>local | Sir-Adrien-Claudington | community | 🟩 open | 🟢 active |
| [QGIS2OllamaMCP](https://github.com/anitagraser/qgis_mcp) | Lets LLMs (via Ollama) drive QGIS Desktop | Python<br>self-hosted | Anita Graser | community | 🟩 open | 🟢 active |
| [qgis_mcp](https://github.com/jjsantos01/qgis_mcp) | Links QGIS Desktop to Claude — project setup, layer management, spatial ops via PyQGIS | Python<br>local | jjsantos01 | community | 🟩 open | 🟡 stale |
| [QgisStreamMCP](https://github.com/nic01asFr/QgisStreamMCP) | Full QGIS Desktop in Docker via noVNC — 1000+ Processing algorithms (Native/GDAL/GRASS/SAGA) | Python<br>local | nic01asFr | community | 🟩 open | 🟢 active |

### General GIS / geoprocessing toolkits

| Server | Description | Lang / Deployment | By | Type | Access | Health |
| --- | --- | --- | --- | --- | --- | --- |
| [fastgeoapi MCP server](https://github.com/geobeyond/fastgeoapi) | Optional integrated MCP server exposing a secured pygeoapi (OGC API) instance's endpoints as LLM tools, auto-generated from its OpenAPI spec | Python<br>local | Geobeyond | community | 🟩 open | 🟢 active |
| [gdal-mcp](https://github.com/JordanGunn/gdal-mcp) | GDAL-style raster/vector workflows (Rasterio, GeoPandas, PyProj) — conversion, reprojection, COG, metadata | Python<br>local | JordanGunn / Wayfinder-Foundry | community | 🟩 open | 🟢 active |
| [geoserver-mcp](https://github.com/mahdin75/geoserver-mcp) | Drives the GeoServer REST API — manage workspaces/layers/styles, CQL spatial queries, WMS/WFS access | Python<br>local | mahdin75 | community | 🟩 open | 🟢 active |
| [Geospatial Power Pack (Kiro)](https://github.com/aws-samples/sample-geospatial-kiro-power-pack) | 19 modular MCP servers with a Kiro hub power — STAC/vector/geocoding connectors, CRS/geometry/raster/point-cloud/3D processing, H3/S2 indexing, and GeoAI embeddings & similarity search over open data on AWS | Python<br>local | AWS | official | 🟩 open | 🟢 active |
| [gis-mcp](https://github.com/mahdin75/gis-mcp) | Connects LLMs to core GIS libraries (Shapely, PyProj, GeoPandas, Rasterio, PySAL) for geometry, projections, raster & spatial stats | Python<br>local | mahdin75 | community | 🟩 open | 🟢 active |
| [MapSmith](https://github.com/mapsmith-ai/MapSmith) | Deterministic GIS geoprocessing for AI agents — buffers, overlays, reprojection, zonal stats, terrain & hydrology (GeoPandas/DuckDB/Whitebox), with a verifiable provenance manifest on every output | Python<br>local | mapsmith-ai | community | 🟩 open | 🟢 active |
| [TerraLab MCP](https://terra-lab.ai/mcp) | Geodata for any place, inside your agent: map data extracts, a hosted open-data catalogue, terrain, routes, isochrones and travel-time matrices, satellite images and NDVI, population, natural risks and French parcels, with sources & licences | hosted | TerraLab | official | 🟦 commercial | ⚪ hosted |

### Geospatial data access & catalogs

| Server | Description | Lang / Deployment | By | Type | Access | Health |
| --- | --- | --- | --- | --- | --- | --- |
| [DC Hub](https://github.com/azmartone67/dchub-mcp-server) | Data-center site selection data — Data Center Power Index (DCPI) daily grid-power availability scores across 300+ markets, plus grid, fiber, gas and interconnection-queue data | JavaScript<br>local+hosted | DC Hub | official | 🟦 commercial | 🟢 active |
| [Factori MCP](https://factori.ai/mcp/) | Location intelligence from mobility data — POI visits and trends, visitor profiles, market saturation and demographics, for site selection, audience building and out-of-home (OOH) planning | hosted | Factori | official | 🟥 paywalled | ⚪ hosted |
| [Fotoshi MCP](https://fotoshi.com/developer/mcp) | Search public geotagged Fotoshi photos within a bounded area, resolve place names, and get each photo's licence and attribution; signed-in users can also retrieve their own public photos | hosted | Fotoshi | official | 🟨 free | ⚪ hosted |
| [GeoAI Tools](https://geoai.tools) | Hosted MCP platform bridging AI agents to ArcGIS Online/Enterprise data — 35 tools: service discovery, AI service guides, geocoding, spatial analysis, feature editing & server-side pipelines | hosted | GeoAI Tools | official | 🟦 commercial | ⏳ pending |
| [geoDB (mineral exploration)](https://geodb.io/connect-ai/) | Hosted remote MCP over a mineral-exploration system of record, reading and writing drill holes, assays, QA/QC, geophysics and claims through a scoped, revocable, logged grant, with dry run, confirm and undo on every write | hosted | geoDB | official | 🟥 paywalled | ⚪ hosted |
| [GeoLens MCP](https://github.com/geolens-io/geolens) | Read-only access to a self-hosted GeoLens instance: catalog search, dataset schemas, GeoJSON features, saved maps & sandboxed read-only SQL | Python<br>local | GeoLens | official | 🟩 open | 🟢 active |
| [geonode-mcp](https://github.com/christianbraun/geonode-mcp) | Search, edit metadata/permissions, upload datasets and transfer ownership on a GeoNode catalogue, every call made as the logged-in user via OAuth2 | Python<br>self-hosted | Christian Braun | community | 🟩 open | 🟢 active |
| [mcp-earthscope-fdsn](https://github.com/pipeworx-io/mcp-earthscope-fdsn) | FDSN seismic web services (EarthScope endpoints) — seismometer station metadata, waveform data availability & regional earthquake catalogues | TypeScript<br>local+hosted | Pipeworx (uses EarthScope FDSN services) | community | 🟩 open | 🟢 active |
| [Registry of Open Data on AWS MCP (RODA)](https://github.com/awslabs/mcp/tree/main/src/roda-mcp-server) | Search and explore the Registry of Open Data on AWS — 1,000+ public S3 datasets incl. satellite imagery, climate & weather: tag/org/licence search, STAC-endpoint discovery, bucket preview and file sampling | Python<br>local | AWS (awslabs) | official | 🟩 open | 🟢 active |
| [Scigantic MCP](https://github.com/Scigantic/scigantic-mcp) | Cross-domain scientific dataset catalog and schema cards (genomics, proteomics, imaging, and a large Earth-observation/geospatial footprint), with per-dataset access snippets for agents | Python<br>local+hosted | Scigantic | official | 🟨 free | 🟢 active |

### Parcels & property

| Server | Description | Lang / Deployment | By | Type | Access | Health |
| --- | --- | --- | --- | --- | --- | --- |
| [ATTOM MCP](https://github.com/pipeworx-io/mcp-attom) | Premium US real-estate & property data from ATTOM Data Solutions — property details, valuations, ownership & sales history | TypeScript<br>local+hosted | Pipeworx (uses ATTOM API) | community | 🟥 paywalled | 🟢 active |
| [LandRecords.us MCP Server](https://landrecords.us/documentation/mcp-server) | Query 160M+ US land parcels by attribute, address, radius, bbox or GeoJSON polygon — ownership, assessed value, land use, acreage & geometry | hosted | landrecords.us | official | 🟦 commercial | ⚪ hosted |
| [MAIA MCP](https://maia-analytics.com/docs/mcp/connect) | Hosted connector that builds US location datasets as map + table projects — parcels, owners, zoning, buildings, businesses & contacts — from plain-language requests, with CSV/GeoJSON import and project querying | hosted | MAIA Analytics | official | 🟦 commercial | ⚪ hosted |
| [Pluia (PLU IA) MCP Server](https://pluia.fr/ia) | French zoning (PLU) for any address or parcel in France, rules cited with the official PDF page | hosted | AZERIA IT | official | 🟦 commercial | ⚪ hosted |
| [Regrid MCP Server](https://regrid.com/mcp) | 160M+ US/Canada land parcels — query by location, zoning, acreage, ownership & building criteria | hosted | Regrid | official | 🟦 commercial | ⚪ hosted |

### Aviation & maritime tracking (ADS-B, AIS)

| Server | Description | Lang / Deployment | By | Type | Access | Health |
| --- | --- | --- | --- | --- | --- | --- |
| [ADS-B MCP Server](https://github.com/dirkhh/adsb-mcp-server) | Exposes a local ADS-B feeder (readsb/tar1090) — aircraft positions, callsigns, altitudes, routes | Python<br>local | dirkhh | community | 🟩 open | 🟢 active |
| [Flightradar24 API MCP](https://github.com/Flightradar24/fr24api-mcp) | Official Flightradar24 flight-tracking API access | local | Flightradar24 | official | 🟦 commercial | 🟢 active |
| [God's Eye View](https://github.com/bilawalsidhu/gods-eye-view) | Live open-source spatial intelligence on a photorealistic 3D globe — show a place with live flights (incl. military ADS-B), vessels, satellites, earthquakes, traffic & public CCTV, rendered in-conversation | JavaScript<br>local | Bilawal Sidhu | community | 🟩 open | 🟢 active |
| [MarineTraffic MCP Server](https://github.com/Cyreslab-AI/marinetraffic-mcp-server) | Vessel positions/details, search & vessels-in-area via MarineTraffic | local | Cyreslab-AI | community | 🟦 commercial | 🟢 active |
| [SignalK MCP Server](https://signalk.org/2025/introducing-signalk-mcp-server-ai-powered-marine-data-access/) | Conversational access to live boat/marine sensor data over Signal K | hosted | Signal K project | community | 🟩 open | ⚪ hosted |
| [Vessel Traffic MCP](https://github.com/tools-mcp/vessel-traffic-mcp) | Read-only vessel identity, AIS-style positions/tracks, port calls & schedules (BYOK maritime providers) | local | tools-mcp | community | 🟦 commercial | 🟢 active |

### Other (IP geolocation, misc)

| Server | Description | Lang / Deployment | By | Type | Access | Health |
| --- | --- | --- | --- | --- | --- | --- |
| [ipgeolocation-io-mcp](https://github.com/ipgeolocation/ipgeolocation-io-mcp) | Official ipgeolocation.io — IP geolocation, VPN/proxy detection, timezone, astronomy, ASN | local | IPGeolocation.io | official | 🟦 commercial | 🟢 active |
| [IPinfo MCP Server](https://mcp.ipinfo.io/) | Hosted IPinfo MCP — country/continent (free), city/coords/timezone/postal (detailed) | hosted | IPinfo | official | 🟦 commercial | ⚪ hosted |
| [mcp-server-ipinfo](https://github.com/briandconnelly/mcp-server-ipinfo) | IP geolocation via the IPInfo API (location + network details) | Python<br>local | briandconnelly | community | 🟦 commercial | 🟢 active |
| [TimezoneToolkit](https://github.com/Cicatriiz/timezone-toolkit) | Timezone conversion plus sunrise/sunset/twilight from lat/long | TypeScript<br>local | Cicatriiz | community | 🟩 open | 🟡 stale |

<!-- AUTOGEN:END -->

## License

[MIT](LICENSE) © Sparkgeo — the catalog data and tooling are free to use, share, and adapt.
