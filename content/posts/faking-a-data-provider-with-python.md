---
source: "blog"
title: "Faking a Data Provider with Python"
date: "2015-03-13T00:00:00+0000"
link: "http://spatialgalaxy.net/2015/03/13/faking-a-data-provider-with-python/"
draft: "false"
showcase: "planet"
subscribers: ["spatialgalaxy_net"]
author: "Spatial Galaxy"
tags: []
---

QGIS data providers are written in C++, however it is possible to simulate a data provider in Python using a memory layer and some code to interface with your data.
Why would you want to do this? Typically you should use the QGIS data providers, but here are some reasons why you may want to give it a go:
 There is no QGIS data provider The generic access available through OGR doesn&rsquo;t provide all the features you need You have no desire to write a provider in C++ No one will write a C++ provider for you, for any amount of money  If you go this route you are essentially creating a bridge that connects QGIS and your data store, be it flat file, database, or some other binary format.
