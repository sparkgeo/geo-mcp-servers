# Geospatial MCP landscape: strategic overview

Snapshot of the catalog on 2026-11-27: 123 servers, health checked 2026-11-27.
The tables in `README.md` are generated and stay current. This file is a hand-written analysis and does not update itself, so re-run the numbers before relying on them later.

## Summary

The catalog shows a market that is broad but uneven. Everyday location tasks (geocoding, routing, place search, weather) are well covered, mostly by open-source servers over OpenStreetMap and public data. Commercial value is concentrating in two places: hosted servers run by data vendors, and the large mapping platforms, which now publish their own servers. Analysis-heavy work (spatial databases, desktop GIS, geoprocessing) has fewer servers and almost no vendor involvement. Some capability areas have no servers in the catalog at all.

| Measure | Value |
| --- | --- |
| Servers | 123 across 14 categories |
| Access | 50 open · 7 free · 56 commercial · 10 paywalled |
| Published by the vendor (`official`) | 55 (45%) |
| Health | 64 active · 34 hosted · 21 stale · 2 pending · 2 archived |
| Marked experimental (🧪) | 6 |
| Deployment | 55 local · 36 hosted · 18 local+hosted · 5 self-hosted · 1 add-in · 8 unknown |
| Usable from web clients (hosted or local+hosted) | 54 (44%) |
| Implementation language, where known | Python 40 · TypeScript 27 · JavaScript/Node 4 · other 6 |

## Coverage by category

| Category | Servers | Open or free | Commercial or paywalled | Official | Stale or archived |
| --- | ---: | ---: | ---: | ---: | ---: |
| Geocoding & place search | 19 | 9 | 10 | 7 | 5 |
| Maps, tiles & commercial platforms | 19 | 0 | 19 | 13 | 6 |
| Remote sensing (STAC / EO) | 17 | 6 | 11 | 9 | 3 |
| Weather & climate | 13 | 13 | 0 | 2 | 2 |
| Geospatial data access & catalogs | 12 | 7 | 5 | 9 | 0 |
| Desktop & enterprise GIS | 11 | 6 | 5 | 0 | 3 |
| GIS / geoprocessing toolkits | 8 | 6 | 2 | 3 | 0 |
| Parcels & property | 6 | 0 | 6 | 5 | 0 |
| Aviation & maritime tracking | 6 | 3 | 3 | 1 | 1 |
| Other (IP geolocation, misc) | 4 | 1 | 3 | 2 | 2 |
| Spatial databases | 3 | 2 | 1 | 1 | 0 |
| Routing, isochrones & navigation | 2 | 2 | 0 | 0 | 1 |
| Specialist location directories | 2 | 2 | 0 | 2 | 0 |
| General tools with geospatial capability | 1 | 0 | 1 | 1 | 0 |

The category counts understate some capabilities. Routing is the clearest case: only 2 servers sit in the routing category, but 16 servers carry the `routing` tag, because most mapping platforms bundle routing with geocoding and search.

## Patterns

### Commodity location services are saturated

Geocoding, reverse geocoding, place search and routing appear in more servers than any other capability: 24 servers carry the `geocoding` tag. Seven of the 19 geocoding servers wrap OpenStreetMap services (Nominatim or Overpass), and they overlap heavily. Five of the 19 are stale. A new geocoding server adds little unless it brings different data or a different way of working, such as Overture places (PlaceRoot), US address verification and postal enrichment (Smarty, Zip-Codes.com), paid batch geocoding with multi-stop routing (Geloky) or fully offline lookups from a local file (GridPin, the catalog's first offline geocoder).

### The major platforms have arrived, with gaps

13 of the 19 mapping-platform servers are official, including Mapbox, TomTom, MapQuest, CARTO, Felt, Geobble, Cesium and an Esri beta. Two large ecosystems still depend on community work:

- **Google Maps** has four entries and none is official. The reference server has been archived, and the remaining three are community wrappers.
- **Esri / ArcGIS** has seven entries across categories. One is an official beta (ArcGIS Location Services). The rest are community servers or third-party platforms, including both ArcGIS Pro integrations.

Being official does not guarantee upkeep. The Baidu, Foursquare and Stadia Maps servers are official but stale.

Vendors are also starting to replace community wrappers of their own APIs. Geoapify now publishes an official hosted server, which sits beside the older community server for the same API. That community server is stale. In November 2026 the community IPinfo server was archived, leaving IPinfo's own hosted server in its place.

### Data vendors prefer hosted servers

Of the 36 hosted servers, nearly all come from vendors selling data or a platform: parcel, zoning and property data (Regrid, Landstats, MAIA, Pluia, BatchData), imagery (Vexcel, Planet, Planetary Computer Pro, SkyWatch), address and postal data (Smarty, Zip-Codes.com), location services (Geoapify, Geloky), climate data (Climatch), mobility and foot-traffic data (Factori), mineral-exploration data (geoDB), geotagged photos (Fotoshi), specialist directories (No Stairs Please, OpenMapp) and cloud GIS and geodata storage (CARTO, Felt, GIS Cloud, Geobble, Geobox). A hosted server keeps the vendor's data and API keys on their side and lets them update tools without users reinstalling anything. We expect this to become the default delivery model for commercial geodata, and recent additions bear that out: six of the seven servers added between 2026-10-16 and 2026-10-29 are hosted servers published by the vendor, and of the ten added since then, eight are published by their vendors and six are hosted. It also changes what the catalog can check: a hosted server has no source code to scan, so trust rests on the vendor's domain.

### Where servers run

Every entry records a `deployment` value: where the server runs and who runs it.

| Deployment | Servers | Official | Community | What it means for the user |
| --- | ---: | ---: | ---: | --- |
| Local | 55 | 12 | 43 | Install it; your client starts it on your machine. Needs a desktop client. |
| Hosted | 36 | 34 | 2 | Connect to the vendor's URL. Works from web clients; queries go to the vendor. |
| Local + hosted | 18 | 7 | 11 | Run it yourself, or use a public endpoint someone else runs. |
| Self-hosted | 5 | 0 | 5 | Deploy it as an HTTP service yourself. |
| Add-in | 1 | 0 | 1 | Runs inside a desktop application (ArcGIS Pro). |
| Unknown | 8 | 2 | 6 | The README does not say. |

Vendors host and the community ships local servers. More than six in ten official servers (34 of 55) are hosted, while nearly two thirds of the community servers (43 of 68) run locally. Only 54 servers, 44% of the catalog, can be used from a web client such as claude.ai without installing anything.

The public endpoints in the local + hosted group mostly come from two community operators, not from the data vendors. Pipeworx runs gateway endpoints for six servers (MapTiler, Nominatim, what3words, OSRM, ATTOM and EarthScope), and cyanheads runs public instances of four (OpenStreetMap, Open-Meteo, OpenAQ and NOAA Marine). These are convenient, but a user's queries then go to a third party that is neither the user nor the data provider.

Maintenance follows the same split. 15 of the 21 stale servers are local, and all 18 local + hosted servers are active, because someone has to keep a public endpoint running.

By category, the pattern follows the work. Desktop GIS and geoprocessing toolkits are almost entirely local, because they drive software or data on the user's machine. Parcels and property data is entirely remote, because the value is the vendor's dataset.

### Earth observation is the most commercially varied area

Remote sensing has the widest spread of access models in the catalog: open STAC and NASA/ESA access, Earth Engine wrappers, imagery marketplaces (SkyFi, SkyWatch), and paid-only vendor platforms. Three of the catalog's ten paywalled servers are here. Newer entries go beyond search and download to embeddings and similarity search (LGND) and array-data queries over Zarr (Arraylake), which suggests the area is moving from data access towards analysis. Google Earth Engine is the weak spot: all three Earth Engine servers in the catalog are community projects, and all three are now stale, two of them since November 2026. Discovery is improving too: AWS now publishes an official server for its Registry of Open Data, which finds datasets with STAC endpoints and previews public S3 buckets.

### Weather is open and US-heavy

All 13 weather servers are open or free. Most of them draw on NOAA and the US National Weather Service, or on Open-Meteo for global coverage. Outside the US, only Canada has a national service in the catalog. European services such as ECMWF open data, DWD and the Met Office do not appear, except through Open-Meteo's ERA5 data. A search for European options on 2026-10-15 found no official servers: Rainbow.ai offers a precipitation nowcasting API but no MCP server, and the one Buienradar server is a small, unmaintained community project. Climatch, added in November 2026, broadens the category beyond forecasts: it serves global monthly climate normals for 31,000+ towns, with similar-climate search and crop suitability.

### Analysis tools are thin and community-built

Spatial databases (3 servers), desktop GIS (11) and geoprocessing toolkits (8) together make up less than a fifth of the catalog. No desktop GIS server is official: all five QGIS servers and both ArcGIS Pro servers come from the community. The newest, gis-agent-bridges, is a single community project with bridges for nine desktop packages, including SuperMap, GeoScene and MapGIS, which the catalog did not cover before; by its own account, most of those bridges have not yet been tested against the real software. Columbus, a community desktop app with an MCP server, adds governed access to enterprise geodatabases (Oracle, SQL Server, file geodatabases), with per-source permissions, sandboxed scripts and an audit log, but is also a test release. For agents that do GIS analysis beyond lookups, this is the least mature part of the market and the most open to new work.

### Maturity is now marked

Health shows whether a server is maintained, not whether it is ready. Since November 2026 the catalog marks servers whose authors call them beta, a test release or experimental with 🧪. Six carry the mark: gis-agent-bridges, Columbus, the ArcGIS Location Services beta, the Planet beta, LGND Developer and AWS's RODA server. Four of the six are vendor-published, so early releases are not only a community habit; vendors are shipping MCP servers before they are stable.

### Two side categories: specialist directories and general tools

In November 2026 the catalog added a category for directories of one kind of place, after two such servers were submitted: OpenMapp (Brazilian Jiu-Jitsu gyms in the US) and No Stairs Please (independent live-music venues in the US and British Columbia). Location is a filter in these servers rather than their purpose, so they sit apart from the core geospatial categories. To be listed, a directory must be published by whoever runs the data and must have location search as its main function. Both current entries are hosted, free and published by their vendors. If more arrive, they will show how far location search is spreading into services that are not geospatial products in themselves.

A second side category, General tools with geospatial capability, followed later that month for general-purpose servers that expose real geospatial tools. Its first entry is Firecrawl, a web search and scraping server whose Alexandria tools reach public ArcGIS layers, Earth Search STAC imagery, addresses and building footprints. Keeping such servers separate stops general tools from crowding the core categories while still recording where geospatial capability turns up.

## Gaps

These capabilities have no dedicated server in the catalog. Some may exist but not be listed yet, so each gap is a prompt to search before it is a conclusion.

| Capability | What the catalog has today |
| --- | --- |
| Public transit (GTFS, schedules, real-time) | Nothing |
| Fleet and logistics optimisation (vehicle routing, dispatch) | Trip optimisation inside OSRM MCP only |
| Cloud warehouse spatial SQL (BigQuery, Snowflake, Databricks) | Wherobots (Apache Sedona), warehouse access through CARTO and Felt, and DuckDB queries over GeoParquet in Geobox storage |
| Natural hazards (wildfire, flood, earthquake) as a focus | US federal disaster declarations and FEMA aid totals by county/FIPS (FEMA Disaster Declarations & Aid, via OpenFEMA) — the first hazards-focused server, though it covers declared events and aid rather than live hazard modelling; 2D flood simulation in Hydrata (paid runs); natural-risk lookups inside TerraLab; wildfire inside weather-mcp; earthquakes inside God's Eye View and the EarthScope server |
| Demographics and census data | Census tract demographics in Zip-Codes.com, population estimates in TerraLab, mobility-derived demographics in Factori (paid), and census enrichment inside Smarty |
| Elevation and terrain as a service | Spread across MapTiler, TerraLab, MapSmith and Open-Meteo |
| 3D, point clouds and digital twins | Cesium and one module of the Kiro power pack |
| Parcels and property outside the US and Canada | French zoning rules (Pluia) and French cadastral parcels (TerraLab); no ownership or valuation data |
| National weather services outside North America | Nothing (see above) |

## Implications

For someone choosing servers: commodity lookups are a solved problem, so choose on data quality, licence and vendor support rather than features. Prefer official or actively maintained servers, and treat 🧪 servers as previews. Check `deployment` first: if you work in a web client, only the hosted and local + hosted servers are open to you, and for any public endpoint, check who runs the domain.

For someone building servers: the open opportunities are in analysis and in under-served data. Desktop GIS automation, cloud warehouse spatial SQL, transit, and hazard data beyond flood modelling have the clearest demand and the least supply. Another OSM geocoder does not.
