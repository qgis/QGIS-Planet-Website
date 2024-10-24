---
source: "blog"
title: "Web based editing in QGIS cloud"
date: "2020-02-29T00:00:00+0000"
link: "https://blog.sourcepole.ch/2020/02/29/qgiscloud-edit/"
draft: "false"
showcase: "planet"
subscribers: ["sourcepole"]
author: "Sourcepole"
tags: []
---

QGIS Cloud (www.qgiscloud.com) is a platform which provides a convenient geodata infrastructure including database, web services and web maps in the cloud. Recently, Sourcepole implemented the possibility to enable web-based editing in published maps. This blog post shows how to enable editing in QGIS cloud pro maps.
We start with my_edit_project.qgs, a project in QGIS desktop containing a background layer and a point vector layer (trees).
We upload the data to QGIS Cloud using the QGIS Cloud plugin and publish the project.
