---
source: "blog"
title: "QGIS: Running Scripts in the Python Console"
date: "2012-01-27T08:10:51+0000"
link: "http://spatialgalaxy.net/2012/01/27/qgis-running-scripts-in-the-python-console/"
draft: "false"
showcase: "planet"
subscribers: ["spatialgalaxy_net"]
author: "Spatial Galaxy"
tags: []
---

The QGIS Python console is great for doing one-off tasks or experimenting with the API. Sometimes you might want to automate a task using a script, and do it without writing a full blown plugin. Currently QGIS does not have a way to load an arbitrary Python script and run it.[1] Until it does, this post illustrates a way you can create a script and run it from the console.
