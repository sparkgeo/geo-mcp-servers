# Geospatial MCP Servers

A curated, tracked list of [Model Context Protocol](https://modelcontextprotocol.io) (MCP) servers for **geospatial, GIS, mapping, and earth-observation** work — geocoding, routing, PostGIS, STAC/imagery, QGIS/ArcGIS, weather, and the commercial location platforms.

The tables below are **generated** from [`servers.yaml`](servers.yaml) — the single source of truth.

## Add a server

- **Quick:** open a [New server issue](../../issues/new?template=new-server.yml).
- **Direct:** add an entry to [`servers.yaml`](servers.yaml) and regenerate — see [CONTRIBUTING.md](CONTRIBUTING.md).

  ```bash
  python3 -m venv .venv && ./.venv/bin/pip install -r requirements.txt   # first time
  ./.venv/bin/python scripts/generate_readme.py                          # regenerate tables
  ```

> **Legend** — *Type* is `official` (published by the platform/data vendor) or `community` (independent). *Health* comes from [`health.json`](health.json), refreshed by `python scripts/check_health.py`: 🟢 **active** (repo pushed within 12 months) · 🟡 **stale** (real but dormant) · ⚪ **hosted** (a hosted service, no repo activity signal) · 🔴 **archived/dead**. A few entries carry a `note:` in `servers.yaml` flagging a URL still to be confirmed.

## Use it as a Claude skill

This repo ships a [Claude Code](https://claude.com/claude-code) skill in [`skill/`](skill/) that searches/recommends servers from the catalog and adds new ones. Install it by symlinking into your skills directory (the skill resolves the repo location from this symlink — no hard-coded paths):

```bash
git clone https://github.com/sparkgeo/geo-mcp-servers.git
ln -sfn "$(pwd)/geo-mcp-servers/skill" ~/.claude/skills/geo-mcp-servers
```

Then ask Claude things like *"is there an MCP server for STAC imagery?"* or *"track this new geo MCP server: <url>"*.

<!-- AUTOGEN:START -->

**87 servers tracked** across 11 categories.

_Health checked 2026-09-03 (active = repo pushed within 12 months): 🟢 active 57 · 🟡 stale 15 · ⚪ hosted 15._

### Categories

- [Geocoding & place search](#geocoding--place-search) (14)
- [Routing, isochrones & navigation](#routing-isochrones--navigation) (2)
- [Maps, tiles & commercial platforms](#maps-tiles--commercial-platforms) (17)
- [Spatial databases & analytics](#spatial-databases--analytics) (3)
- [Remote sensing, STAC & earth observation](#remote-sensing-stac--earth-observation) (13)
- [Weather & climate](#weather--climate) (11)
- [Desktop & enterprise GIS (QGIS, ArcGIS)](#desktop--enterprise-gis-qgis-arcgis) (9)
- [General GIS / geoprocessing toolkits](#general-gis--geoprocessing-toolkits) (5)
- [Geospatial data access & catalogs](#geospatial-data-access--catalogs) (2)
- [Aviation & maritime tracking (ADS-B, AIS)](#aviation--maritime-tracking-ads-b-ais) (5)
- [Other (IP geolocation, misc)](#other-ip-geolocation-misc) (6)

### Geocoding & place search

| Server | Description | Lang | By | Type | Health |
| --- | --- | --- | --- | --- | --- |
| [Geoapify MCP Server](https://github.com/OriShmila/geoapify-mcp-server) | Geoapify geocoding, reverse geocoding, places, routing, isolines & travel-time | Python | OriShmila | community | 🟡 stale |
| [geocode-mcp](https://github.com/X-McKay/geocode-mcp) | Lat/long for places via free Nominatim, no API key | Python | X-McKay | community | 🟡 stale |
| [HERE Maps MCP Server](https://github.com/limingchina/heremaps-mcp-server) | HERE Platform geocoding, reverse geocoding, routing, places search & traffic | TypeScript | limingchina | community | 🟡 stale |
| [MCP-Geo](https://github.com/webcoderz/MCP-Geo) | Geocoding MCP built on GeoPy — multi-provider (Nominatim, ArcGIS, Bing) | Python | webcoderz | community | 🟡 stale |
| [mcp-nominatim](https://github.com/pipeworx-io/mcp-nominatim) | Geocoding / reverse geocoding via OSM Nominatim | Python | pipeworx-io | community | 🟢 active |
| [open-streetmap-mcp](https://github.com/jagan-shanmugam/open-streetmap-mcp) | OSM location services — geocode/reverse, POI, directions, meeting points, neighborhood analysis | Python | Jagan Shanmugam | community | 🟡 stale |
| [OpenCage Geocoding MCP](https://github.com/OpenCageData/opencage-geocoding-mcp) | Forward/reverse geocoding via the OpenCage API, plus API-status/quota checks | TypeScript | OpenCage | official | 🟢 active |
| [openstreetmap-mcp-server](https://github.com/cyanheads/openstreetmap-mcp-server) | Geocode, reverse geocode, and Overpass spatial queries (STDIO or Streamable HTTP) | TypeScript | cyanheads | community | 🟢 active |
| [OSM-GeoJSON-MCP-Server](https://github.com/shimizu/OSM-GeoJSON-MCP-Server) | Fetches OSM data as GeoJSON via Overpass | JavaScript | shimizu | community | 🟢 active |
| [osmmcp](https://github.com/NERVsystems/osmmcp) | OSM geospatial tools — geocoding, routing, nearby places, neighborhood analysis, EV charging | Go | NERV Systems | community | 🟢 active |
| [PlaceRoot](https://github.com/chuofringer/placeroot) | Overture Maps places, geocoding, admin boundaries, buildings & isochrones via DuckDB (no ETL, no API key); token-budgeted responses with GERS ids | Python | chuofringer | community | 🟢 active |
| [Smarty MCP Server](https://www.smarty.com/docs/mcp) | 20 tools for US/international address verification, ZIP lookup, reverse geocoding & property/census enrichment | — | Smarty | official | ⚪ hosted |
| [what3words MCP](https://github.com/pipeworx-io/mcp-what3words) | Convert 3-word addresses to lat/long + bounding box | — | Pipeworx (uses what3words API) | community | 🟢 active |
| [Zephr Places Grounding MCP](https://zephr.xyz/places-grounding) | Places grounding for local AI — nearest-place search, rich place details & walking navigation (find_nearest_to_me, get_place_details, navigate_to_place) | — | Zephr | official | ⚪ hosted |

### Routing, isochrones & navigation

| Server | Description | Lang | By | Type | Health |
| --- | --- | --- | --- | --- | --- |
| [OSRM MCP](https://github.com/pipeworx-io/mcp-osrm) | Routing, distances & travel times via OSRM, with map-matching & trip optimization | TypeScript | Pipeworx (uses OSRM) | community | 🟢 active |
| [valhalla-mcp](https://github.com/aatakansalar/valhalla-mcp) | Valhalla OSM routing engine — routing, isochrones, tiles, matrix | TypeScript | Atakan Salar | community | 🟡 stale |

### Maps, tiles & commercial platforms

| Server | Description | Lang | By | Type | Health |
| --- | --- | --- | --- | --- | --- |
| [ArcGIS Location Services MCP (beta)](https://developers.arcgis.com/ai-tools/mcp-arcgis-location-services/) | Official Esri MCP exposing ArcGIS Location Platform services — geocoding, routing, static maps | — | Esri | official | ⚪ hosted |
| [ArcGIS Location Services MCP (community)](https://github.com/lwsinclair/arcgis-location-services-mcp) | Community wrapper over the Esri ArcGIS Location Platform — geocoding, routing, places | — | lwsinclair | community | 🟡 stale |
| [baidu-maps/mcp](https://github.com/baidu-maps/mcp) | Official Baidu Map — geocoding, POI, route planning, weather, IP location, traffic (China) | Python / TypeScript | Baidu | official | 🟡 stale |
| [CARTO MCP Server](https://docs.carto.com/carto-for-agents/mcp-server) | Remote MCP over CARTO — explore data, render Builder maps inline, run saved spatial Workflows on your cloud warehouse | — | CARTO | official | ⚪ hosted |
| [Cesium AI Integrations](https://github.com/CesiumGS/cesium-ai-integrations) | Official Cesium MCP servers & agent skills connecting the Cesium 3D geospatial ecosystem (CesiumJS, 3D Tiles) to AI assistants | TypeScript | Cesium (CesiumGS) | official | 🟢 active |
| [Felt MCP Server](https://felt.com/blog/introducing-felt-mcp-server) | Remote MCP — create maps, query warehouse, run spatial SQL, style layers, publish live URLs | — | Felt | official | ⚪ hosted |
| [foursquare-places-mcp](https://github.com/foursquare/foursquare-places-mcp) | Official Foursquare Places API v3 — venue search, place details, location context | TypeScript | Foursquare | official | 🟡 stale |
| [GIS Cloud MCP Server](https://manual.giscloud.com/knowledge-base/gis-cloud-ai-mcp/) | Remote read & write MCP for the GIS Cloud platform — 55 tools covering maps, layers, features, spatial queries, forms, tables, file import & map rendering, with OAuth 2.1 sign-in and two-phase confirmation for destructive tools | — | GIS Cloud | official | ⚪ hosted |
| [Google Maps MCP (reference)](https://github.com/modelcontextprotocol/servers) | Reference server — geocoding, places, directions, distance matrix, elevation (now archived) | TypeScript | Anthropic / MCP project | community | 🟢 active |
| [google-maps-mcp-server](https://github.com/david-pivonka/google-maps-mcp-server) | STDIO server on the new Google Places (New) + Routes APIs | TypeScript | david-pivonka | community | 🟢 active |
| [google-maps-places-mcp](https://github.com/domdomegg/google-maps-places-mcp) | Google Places search + photos | TypeScript | domdomegg | community | 🟢 active |
| [Mapbox MCP Server](https://github.com/mapbox/mcp-server) | Official Mapbox web services — geocoding, POI search, multimodal routing, matrix, isochrones, static maps | TypeScript | Mapbox | official | 🟢 active |
| [MapTiler MCP](https://github.com/pipeworx-io/mcp-maptiler) | MapTiler geocoding, elevation and mapping APIs as MCP tools | — | Pipeworx (uses MapTiler API) | community | 🟢 active |
| [mcp-google-map](https://github.com/cablate/mcp-google-map) | Google Places (New), Routes, geocoding, distance matrix | TypeScript | cablate | community | 🟢 active |
| [Stadia Maps MCP Server](https://github.com/stadiamaps/stadiamaps-mcp-server-ts) | Official Stadia Maps APIs - geocoding, search, routing, isochrones, map tiles, time zone lookup | TypeScript | Stadia Maps | official | 🟡 stale |
| [TomTom Maps MCP Server](https://github.com/tomtom-international/tomtom-maps-mcp) | Official TomTom location services — search, geocoding, routing, traffic | TypeScript | TomTom | official | 🟢 active |
| [TomTom Traffic Analytics MCP](https://github.com/tomtom-international/tomtom-traffic-analytics-mcp) | TomTom MOVE traffic analytics — past, present & predicted traffic | — | TomTom | official | 🟢 active |

### Spatial databases & analytics

| Server | Description | Lang | By | Type | Health |
| --- | --- | --- | --- | --- | --- |
| [Overture Maps MCP Server](https://github.com/srivinod1/overture-mcp-server) | Query Overture Maps GeoParquet directly from S3 via DuckDB spatial — buildings, place density, land-use analytics | Python | srivinod1 | community | 🟢 active |
| [postgis-mcp](https://github.com/receptopalak/postgis-mcp) | PostGIS database connection over MCP — multi-connection via env vars | Node.js | receptopalak | community | 🟢 active |
| [Wherobots MCP Server](https://wherobots.com) | Direct access to WherobotsDB (Apache Sedona) — design & run spatial SQL over S3 & Unity Catalog data | Python | Wherobots | official | ⚪ hosted |

### Remote sensing, STAC & earth observation

| Server | Description | Lang | By | Type | Health |
| --- | --- | --- | --- | --- | --- |
| [Arraylake MCP Server](https://docs.earthmover.io/mcp/) | Browse Arraylake repos, inspect schemas, run OGC EDR queries & render maps over Zarr/Icechunk scientific arrays | — | Earthmover | official | ⚪ hosted |
| [Axion-MCP](https://github.com/Dhenenjay/Axion-MCP) | Earth Engine analysis platform for Claude Desktop — NDVI/NDWI, classification, maps | TypeScript | Dhenenjay | community | 🟢 active |
| [copernicus-mcp](https://github.com/wb1016/copernicus-mcp) | Access ESA Copernicus OData API — search/download Sentinel-1/2/3/5P/6 imagery | Python | wb1016 | community | 🟢 active |
| [earthdata-mcp](https://github.com/nasa/earthdata-mcp) | LLM access to NASA Common Metadata Repository — discover/verify/access Earth science datasets | Python | NASA | official | 🟢 active |
| [google-earth-engine-mcp](https://github.com/cameronking4/google-earth-engine-mcp) | Query Google Earth Engine with natural language — fetch datasets, run tasks, visualize in chat | TypeScript | cameronking4 | community | 🟡 stale |
| [Microsoft Planetary Computer Pro MCP Tools](https://techcommunity.microsoft.com/blog/microsoft-planetary-computer-blog/introducing-microsoft-planetary-computer-pro-model-context-protocol-tools-on-vs-/4522346) | 35+ tools connecting Planetary Computer + Planetary Computer Pro, shipped for VS Code / Copilot | — | Microsoft | official | ⚪ hosted |
| [NASA-MCP-server](https://github.com/ProgramComputer/NASA-MCP-server) | Standardized interface to many NASA APIs incl. Earth observations & imagery | TypeScript | ProgramComputer | community | 🟢 active |
| [Planet MCP Server (beta)](https://community.planet.com/product-updates/beta-planet-mcp-server-for-ai-agents-6403) | Natural-language search/preview/order over the Planet Insights Platform Data API using existing Planet SDK creds | — | Planet Labs | official | ⚪ hosted |
| [planetary-computer-mcp](https://github.com/isaaccorley/planetary-computer-mcp) | Query & download satellite imagery from the Microsoft Planetary Computer STAC API | Python | Isaac Corley | community | 🟢 active |
| [SkyFi MCP](https://github.com/jpwilson/skyfi-mcp) | Search 150+ satellites from 12+ providers, compare pricing, order archive or tasking imagery in natural language | — | jpwilson (SkyFi platform) | community | 🟢 active |
| [stac-mcp](https://github.com/BnJam/stac-mcp) | Natural-language search of any STAC-compliant catalog (defaults to Planetary Computer) | Python | BnJam | community | 🟢 active |
| [Tilebox MCP Server](https://docs.tilebox.com/onboard-your-agent) | Create and manage geospatial datasets and distributed workflows, with docs search + CLI and Skills for coding agents | Python / Go | Tilebox | official | ⚪ hosted |
| [unicef-gee-mcp](https://github.com/tryolabs/unicef-gee-mcp) | Google Earth Engine access/analysis for UNICEF workflows | Python | Tryolabs (for UNICEF) | community | 🟢 active |

### Weather & climate

| Server | Description | Lang | By | Type | Health |
| --- | --- | --- | --- | --- | --- |
| [aqicn-mcp](https://github.com/mattmarcin/aqicn-mcp) | Real-time air quality from the World Air Quality Index (AQICN) by city or coordinates | — | mattmarcin | community | 🟡 stale |
| [dynamical.org Weather & Climate Catalog](https://github.com/dynamical-org/mcp) | Hosted server over dynamical.org's open STAC catalog of cloud-optimized weather & climate archives and forecasts (GFS, HRRR, ECMWF/AIFS) — dataset search & docs, ready-to-run xarray/Zarr/Icechunk snippets, forecast-run freshness | Python | dynamical.org | official | 🟢 active |
| [mcp_weather_server](https://github.com/isdaniel/mcp_weather_server) | Weather info via the Open-Meteo API | Python | isdaniel | community | 🟢 active |
| [NOAA Marine MCP Server](https://github.com/cyanheads/noaa-marine-mcp-server) | NOAA CO-OPS tide stations + NDBC buoys — tide predictions, water levels, tidal currents, live buoy conditions | — | cyanheads | community | 🟢 active |
| [NOAA-TidesAndCurrents-MCP](https://github.com/RyanCardin15/NOAA-TidesAndCurrents-MCP) | NOAA Data/Metadata/Derived-Products APIs for tides and currents | TypeScript | RyanCardin15 | community | 🟢 active |
| [nws-mcp-server](https://github.com/nitvob/nws-mcp-server) | Quickstart NWS server — get-alerts + get-forecast from the National Weather Service | TypeScript | nitvob | community | 🟢 active |
| [open-meteo-mcp](https://github.com/cmer81/open-meteo-mcp) | Full Open-Meteo API — forecast, ERA5 archive, air quality, marine, seasonal | TypeScript | cmer81 | community | 🟢 active |
| [open-meteo-mcp-server (cyanheads)](https://github.com/cyanheads/open-meteo-mcp-server) | Open-Meteo forecasts + geocoding, ERA5 historical climate, marine, air quality & terrain elevation | TypeScript | cyanheads | community | 🟢 active |
| [OpenAQ MCP Server](https://github.com/cyanheads/openaq-mcp-server) | Global air-quality stations & pollutant observations (PM2.5, PM10, O3, NO2, SO2, CO) via OpenAQ v3, with SQL over history | — | cyanheads | community | 🟢 active |
| [weather-mcp](https://github.com/weather-mcp/weather-mcp) | 17 weather tools — forecasts, alerts, air quality, marine, radar, lightning, rivers, wildfires, history to 1940 (NOAA + Open-Meteo) | Python | weather-mcp | community | 🟢 active |
| [weather-mcp (Fahrenheit)](https://github.com/FahrenheitResearch/weather-mcp) | 12 tools — NWS data, NWP model imagery, NEXRAD radar, 205 meteorological calculations | Python | FahrenheitResearch | community | 🟢 active |

### Desktop & enterprise GIS (QGIS, ArcGIS)

| Server | Description | Lang | By | Type | Health |
| --- | --- | --- | --- | --- | --- |
| [ArcGISMCP](https://github.com/GarrickGarcia/ArcGISMCP) | Integrates ArcGIS Online — search/query geospatial feature layers | Python | GarrickGarcia | community | 🟡 stale |
| [esri-mcp](https://github.com/eKerney/esri-mcp) | Query & map Esri Living Atlas data, focus on water resources | Python | eKerney | community | 🟢 active |
| [MCP-ArcGISPro](https://github.com/geo2004/MCP-ArcGISPro) | Control and automate ArcGIS Pro from Claude Desktop | Python | geo2004 | community | 🟢 active |
| [MCP-Server-ArcGIS-Pro-AddIn](https://github.com/nicogis/MCP-Server-ArcGIS-Pro-AddIn) | MCP server delivered as an ArcGIS Pro add-in | C#/.NET | nicogis | community | 🟢 active |
| [qgis-mcp (nkarasiak)](https://github.com/nkarasiak/qgis-mcp) | 117 QGIS tools — layer mgmt, feature editing, processing, styling, layout/atlas, cross-layer SQL | Python | nkarasiak | community | 🟢 active |
| [qgis-mcp-1](https://github.com/Sir-Adrien-Claudington/qgis-mcp-1) | Fork connecting QGIS to Claude via MCP | Python | Sir-Adrien-Claudington | community | 🟢 active |
| [QGIS2OllamaMCP](https://github.com/anitagraser/qgis_mcp) | Lets LLMs (via Ollama) drive QGIS Desktop | Python | Anita Graser | community | 🟢 active |
| [qgis_mcp](https://github.com/jjsantos01/qgis_mcp) | Links QGIS Desktop to Claude — project setup, layer management, spatial ops via PyQGIS | Python | jjsantos01 | community | 🟢 active |
| [QgisStreamMCP](https://github.com/nic01asFr/QgisStreamMCP) | Full QGIS Desktop in Docker via noVNC — 1000+ Processing algorithms (Native/GDAL/GRASS/SAGA) | Python | nic01asFr | community | 🟢 active |

### General GIS / geoprocessing toolkits

| Server | Description | Lang | By | Type | Health |
| --- | --- | --- | --- | --- | --- |
| [fastgeoapi MCP server](https://github.com/geobeyond/fastgeoapi) | Optional integrated MCP server exposing a secured pygeoapi (OGC API) instance's endpoints as LLM tools, auto-generated from its OpenAPI spec | Python | Geobeyond | community | 🟢 active |
| [gdal-mcp](https://github.com/JordanGunn/gdal-mcp) | GDAL-style raster/vector workflows (Rasterio, GeoPandas, PyProj) — conversion, reprojection, COG, metadata | Python | JordanGunn / Wayfinder-Foundry | community | 🟢 active |
| [geoserver-mcp](https://github.com/mahdin75/geoserver-mcp) | Drives the GeoServer REST API — manage workspaces/layers/styles, CQL spatial queries, WMS/WFS access | Python | mahdin75 | community | 🟢 active |
| [gis-mcp](https://github.com/mahdin75/gis-mcp) | Connects LLMs to core GIS libraries (Shapely, PyProj, GeoPandas, Rasterio, PySAL) for geometry, projections, raster & spatial stats | Python | mahdin75 | community | 🟢 active |
| [MapSmith](https://github.com/mapsmith-ai/MapSmith) | Deterministic GIS geoprocessing for AI agents — buffers, overlays, reprojection, zonal stats, terrain & hydrology (GeoPandas/DuckDB/Whitebox), with a verifiable provenance manifest on every output | Python | mapsmith-ai | community | 🟢 active |

### Geospatial data access & catalogs

| Server | Description | Lang | By | Type | Health |
| --- | --- | --- | --- | --- | --- |
| [GeoLens MCP](https://github.com/geolens-io/geolens/tree/main/mcp) | Read-only access to a self-hosted GeoLens instance: catalog search, dataset schemas, GeoJSON features, saved maps & sandboxed read-only SQL | Python | GeoLens | official | 🟢 active |
| [Scigantic MCP](https://github.com/Scigantic/scigantic-mcp) | Cross-domain scientific dataset catalog and schema cards (genomics, proteomics, imaging, and a large Earth-observation/geospatial footprint), with per-dataset access snippets for agents | Python | Scigantic | official | 🟢 active |

### Aviation & maritime tracking (ADS-B, AIS)

| Server | Description | Lang | By | Type | Health |
| --- | --- | --- | --- | --- | --- |
| [ADS-B MCP Server](https://github.com/dirkhh/adsb-mcp-server) | Exposes a local ADS-B feeder (readsb/tar1090) — aircraft positions, callsigns, altitudes, routes | Python | dirkhh | community | 🟢 active |
| [Flightradar24 API MCP](https://github.com/Flightradar24/fr24api-mcp) | Official Flightradar24 flight-tracking API access | — | Flightradar24 | official | 🟢 active |
| [MarineTraffic MCP Server](https://github.com/Cyreslab-AI/marinetraffic-mcp-server) | Vessel positions/details, search & vessels-in-area via MarineTraffic | — | Cyreslab-AI | community | 🟡 stale |
| [SignalK MCP Server](https://signalk.org/2025/introducing-signalk-mcp-server-ai-powered-marine-data-access/) | Conversational access to live boat/marine sensor data over Signal K | — | Signal K project | community | ⚪ hosted |
| [Vessel Traffic MCP](https://github.com/tools-mcp/vessel-traffic-mcp) | Read-only vessel identity, AIS-style positions/tracks, port calls & schedules (BYOK maritime providers) | — | tools-mcp | community | 🟢 active |

### Other (IP geolocation, misc)

| Server | Description | Lang | By | Type | Health |
| --- | --- | --- | --- | --- | --- |
| [ipgeolocation-io-mcp](https://github.com/ipgeolocation/ipgeolocation-io-mcp) | Official ipgeolocation.io — IP geolocation, VPN/proxy detection, timezone, astronomy, ASN | — | IPGeolocation.io | official | 🟢 active |
| [IPinfo MCP Server](https://mcp.ipinfo.io/) | Hosted IPinfo MCP — country/continent (free), city/coords/timezone/postal (detailed) | — | IPinfo | official | ⚪ hosted |
| [LandRecords.us MCP Server](https://landrecords.us/documentation/mcp-server) | Query 160M+ US land parcels by attribute, address, radius, bbox or GeoJSON polygon — ownership, assessed value, land use, acreage & geometry | — | landrecords.us | official | ⚪ hosted |
| [mcp-server-ipinfo](https://github.com/briandconnelly/mcp-server-ipinfo) | IP geolocation via the IPInfo API (location + network details) | Python | briandconnelly | community | 🟢 active |
| [Regrid MCP Server](https://regrid.com/mcp) | 160M+ US/Canada land parcels — query by location, zoning, acreage, ownership & building criteria | — | Regrid | official | ⚪ hosted |
| [TimezoneToolkit](https://github.com/Cicatriiz/timezone-toolkit) | Timezone conversion plus sunrise/sunset/twilight from lat/long | TypeScript | Cicatriiz | community | 🟡 stale |

<!-- AUTOGEN:END -->

## License

[MIT](LICENSE) © Sparkgeo — the catalog data and tooling are free to use, share, and adapt.
