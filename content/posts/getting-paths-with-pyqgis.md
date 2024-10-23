---
source: "blog"
title: "Getting Paths with PyQGIS"
date: "2013-11-06T14:45:00+0000"
link: "http://spatialgalaxy.net/2013/11/06/getting-paths-with-pyqgis/"
draft: "false"
showcase: "planet"
subscribers: ["spatialgalaxy_net"]
author: "Spatial Galaxy"
tags: []
---

When writing plugins or scripts it is often necessary to get information about the paths QGIS is using. For example, if we are writing a plugin that uses Python templates to create output based on user actions, we need to know the path to our installed plugin so we can find the templates. Fortunately the API provides an easy way to get at the information; here are a few examples:
