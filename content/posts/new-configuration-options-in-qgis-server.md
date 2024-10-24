---
source: "blog"
title: "New configuration options in QGIS server"
date: "2012-10-30T00:00:00+0000"
link: "https://blog.sourcepole.ch/2012/10/30/new-configuration-options-in-qgis-server/"
draft: "false"
showcase: "planet"
subscribers: ["sourcepole"]
author: "Sourcepole"
tags: []
---

In QGIS server, it is now possible to selectively exclude layers from WMS publication. These layers will be available only on the desktop and hidden from WMS clients. Similarly, print layouts can be excluded from WMS publication. Of course, these settings are conveniently accessible from the project properties dialog of QGIS (but you need to have a nightly build or a recent compile):
Additionally, attributes per layer can be excluded from WMS or WFS publication in the vector properties dialog:
