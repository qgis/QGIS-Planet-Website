---
source: "blog"
title: "Leaflet Day 9 - Calculating Distance with Turf.js"
date: "2019-02-04T08:02:03-0900"
link: "http://spatialgalaxy.net/2019/02/04/leaflet-day-9-calculating-distance-with-turf.js/"
draft: "false"
showcase: "planet"
subscribers: ["spatialgalaxy_net"]
author: "Spatial Galaxy"
tags: []
---

Today we&rsquo;re going to use Turf.js to calculate the distance between any two points along the trail. Turf.js is billed as providing &ldquo;Advanced geospatial analysis for browsers and Node.js.&rdquo;
The distance calculated is a straight line (&ldquo;as the crow flies&rdquo;) distance rather than actual trail miles.
Including Turf.js To calculate the distance we need to include Turf.js. Rather than install it locally, just add this line to the head of your HTML:
