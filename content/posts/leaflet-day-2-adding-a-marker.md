---
source: "blog"
title: "Leaflet Day 2 - Adding a Marker"
date: "2019-01-24T06:13:17-0900"
link: "http://spatialgalaxy.net/2019/01/24/leaflet-day-2-adding-a-marker/"
draft: "false"
showcase: "planet"
subscribers: ["spatialgalaxy_net"]
author: "Spatial Galaxy"
tags: []
---

I&rsquo;m starting off slow, so today we&rsquo;ll add a marker with some extra features. Since the map from yesterday is already centered on the big earthquake, lets add a marker there.
Adding a Marker To create a marker, Leaflet uses the L.marker class:
var earthquakeMarker = L.marker([61.346, -149.955]); This creates the marker, but it needs to be added to the map:
earthquakeMarker.addTo(map); This gives us:
Good so far, but looking at the map tells us nothing about the marker.
