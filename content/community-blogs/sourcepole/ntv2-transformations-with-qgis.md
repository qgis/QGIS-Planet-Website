---
source: "blog"
title: "NTv2 transformations with QGIS"
image: "ntv2-transformations-with-qgis"
date: "2014-02-18T00:00:00+0000"
link: "https://blog.sourcepole.ch/2014/02/18/ntv2-transformations-with-qgis/"
draft: "true"
showcase: "planet"
folder: "sourcepole"
author: "Sourcepole"
---

Datum transformations with grid shift files are used in several countries to convert coordinates between different datums. In Switzerland, datum transformation using the NTv2 method is important because of the upcoming conversion between the LV03 system and the new LV95 system. Up to now, doing coordinate transformations with grid shift files was possible in QGIS, but unconvenient.
To use an NTv2 transformation in QGIS, the grid shift file needs to be placed in a directory where proj4 can find it (usually /usr/share/proj on Linux and OSGeo4W\share\proj on Windows).
