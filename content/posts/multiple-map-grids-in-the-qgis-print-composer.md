---
source: "blog"
title: "Multiple map grids in the QGIS print composer"
date: "2014-07-10T00:00:00+0000"
link: "https://blog.sourcepole.ch/2014/07/10/multiple-map-grids-in-the-qgis-print-composer/"
draft: "false"
showcase: "planet"
subscribers: ["sourcepole"]
author: "Sourcepole"
tags: []
---

In printed maps, having several coordinate grids over one map is a very usefull feature. For instance using a meter system as output CRS, it is nice to display a latitude / longitude grid as well. Until now, the QGIS print composer allowed only one coordinate grid per composer map and it was restricted to the map output CRS.
Having that multigrid / multiCRS feature in QGIS Enterprise since 13.04 already, I&rsquo;ve recently found the time to port it into the QGIS developer version.
