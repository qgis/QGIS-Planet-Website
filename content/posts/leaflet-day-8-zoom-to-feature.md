---
source: "blog"
title: "Leaflet Day 8 - Zoom to Feature"
date: "2019-02-01T14:40:12-0900"
link: "http://spatialgalaxy.net/2019/02/01/leaflet-day-8-zoom-to-feature/"
draft: "false"
showcase: "planet"
subscribers: ["spatialgalaxy_net"]
author: "Spatial Galaxy"
tags: []
---

In this post we&rsquo;ll add a zoom button to pan the map to one of the towns in the trail stops layer.
Adding a Dropdown Box and Button The first thing to do is add the select element and a button to the HTML:
&lt;select id='zoombox'&gt; &lt;/select&gt; &lt;input type="button" id="zoomTo" value="Zoom to town"&gt; We&rsquo;ll populate the options for the select element using the town GeoJSON.
Creating a Dictionary and Populating the Select Box Next we loop through the towns in the GeoJSON layer and create a dictionary that maps the town name to its data, then add each as an option to a select element:
