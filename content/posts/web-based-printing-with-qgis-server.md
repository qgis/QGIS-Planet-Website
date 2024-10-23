---
source: "blog"
title: "Web based printing with QGIS server"
date: "2011-02-03T00:00:00+0000"
link: "https://blog.sourcepole.ch/2011/02/03/web-based-printing-with-qgis-server/"
draft: "false"
showcase: "planet"
subscribers: ["sourcepole"]
author: "Sourcepole"
tags: []
---

QGIS server is already known as a full featured, WMS 1.3 compliant map server (see e.g. ETHZ, Linfiniti or 3LIZ).
For the city of Uster, Switzerland, Sourcepole recently extended QGIS server with the possibility to use the print composer via WMS in order to offer printing functionality for web maps. A very nice GeoExt based client can be found at http://gis.uster.ch/webgis/. Andreas Neumann used and extended the GeoExt PrintProvider and PrintExtent classes which allows the user to intuitively select a layout, extent, scale, rotation and resolution for printing.
