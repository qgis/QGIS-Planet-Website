---
source: "blog"
title: "Multithreaded rendering with QGIS"
date: "2013-11-26T00:00:00+0000"
link: "https://blog.sourcepole.ch/2013/11/26/multithreaded-rendering-with-qgis-enterprise/"
draft: "false"
showcase: "planet"
subscribers: ["sourcepole"]
author: "Sourcepole"
tags: []
---

Nowadays, most computers have several processor cores. However, most computer programs are still designed to only use one processing unit. As a convenient and portable way of writing software using all the available processing power, Qt provides the excellent QtConcurrent framework.
In 2010, a Google Summer of Code project examined the suitabilty of using Qt concurrent for rendering the map image in QGIS using several processor cores. Following that approach, each layer renders its image in a separate thread.
