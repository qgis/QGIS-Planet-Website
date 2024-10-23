---
source: "blog"
title: "Leaflet Day 3 - The Trail"
date: "2019-01-25T09:03:36-0900"
link: "http://spatialgalaxy.net/2019/01/25/leaflet-day-3-the-trail/"
draft: "false"
showcase: "planet"
subscribers: ["spatialgalaxy_net"]
author: "Spatial Galaxy"
tags: []
---

Background In 1902 the only way from the port of Valdez to the Fortymile gold fields was a nearly 400 mile trail through the Alaska wilderness. The Valdez-Eagle trail plays a key role in novels two and three.
Adding the Trail to a Leaflet Map To add the trail to our map, we will convert it from a shapefile to GeoJSON. There is more than one way to do this&mdash;you could use ogr2ogr, but we chose to use QGIS, since it would not only convert it, but transform the coordinate system at the same time.
