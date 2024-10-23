---
source: "blog"
title: "Raster resampling in QGIS"
date: "2011-12-30T00:00:00+0000"
link: "https://blog.sourcepole.ch/2011/12/30/raster-resampling-in-qgis/"
draft: "false"
showcase: "planet"
subscribers: ["sourcepole"]
author: "Sourcepole"
tags: []
---

QGIS already offers a lot of possibilities to visualize raster data (contrast enhancement, color map, handling of transparent pixels, &hellip;) Last year, Radim Blazek refactored the raster provider interface and added on-the-fly reprojection support for rasters to QGIS. Very cool!
One of the few things currently missing in QGIS raster layer is the possibility to have other resampling types than nearest neighbour. The problem is that rasters appear pixelated when zooming further than the source raster resolution.
