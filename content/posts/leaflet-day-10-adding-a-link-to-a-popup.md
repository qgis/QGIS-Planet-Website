---
source: "blog"
title: "Leaflet Day 10 - Adding a Link to a Popup"
date: "2019-02-06T07:21:58-0900"
link: "http://spatialgalaxy.net/2019/02/06/leaflet-day-10-adding-a-link-to-a-popup/"
draft: "false"
showcase: "planet"
subscribers: ["spatialgalaxy_net"]
author: "Spatial Galaxy"
tags: []
---

In this post we&rsquo;ll add a link to the towns popup that will display the satellite view on Google Maps.
The API for working with Google Maps URLs can be found here: https://developers.google.com/maps/documentation/urls/guide.
To add a link to the town name in the popup, we modify the JavaScript code that creates the towns layer:
1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20  var towns = L.
