---
source: "blog"
title: "SVG symbols in QGIS with modifiable colors"
date: "2011-06-30T00:00:00+0000"
link: "https://blog.sourcepole.ch/2011/06/30/svg-symbols-in-qgis-with-modifiable-colors/"
draft: "false"
showcase: "planet"
subscribers: ["sourcepole"]
author: "Sourcepole"
tags: []
---

SVG markers are a popular way to symbolise points in QGIS. Predefined markers are available in $PREFIX/share/qgis/svg and it is straightforward to add new symbols or to create own symbols with a vector graphics program (e.g. Inkscape). A disadvantage so far was the need to create different versions of an svg file to have the same symbol in several colors. A recent change in QGIS now introduces the possibility to insert parameter tags into the svg file and QGIS is going to replace them with the values for fill color, outline color and outline width.
