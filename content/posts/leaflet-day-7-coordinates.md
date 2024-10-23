---
source: "blog"
title: "Leaflet Day 7 - Coordinates"
date: "2019-01-30T06:39:24-0900"
link: "http://spatialgalaxy.net/2019/01/30/leaflet-day-7-coordinates/"
draft: "false"
showcase: "planet"
subscribers: ["spatialgalaxy_net"]
author: "Spatial Galaxy"
tags: []
---

In this post, we&rsquo;ll do a couple of things:
 Clean up the display of coordinate precision in our popups Add the current coordinates to the map as the mouse moves  Coordinate Precision Display The current map displays the latitude and longitude with seven decimal places. This is more than we need to see when displaying information about locations:
Fixing this is easy to do using the JavaScript function toFixed.
