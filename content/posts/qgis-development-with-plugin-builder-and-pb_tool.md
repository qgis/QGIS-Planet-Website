---
source: "blog"
title: "QGIS Development with Plugin Builder and pb_tool"
date: "2014-10-09T09:50:00+0000"
link: "http://spatialgalaxy.net/2014/10/09/qgis-development-with-plugin-builder-and-pb_tool/"
draft: "false"
showcase: "planet"
subscribers: ["spatialgalaxy_net"]
author: "Spatial Galaxy"
tags: []
---

The Plugin Builder is a great tool for generating a working plugin project that you can customize.
One of the main tasks in the development cycle is deploying the plugin to the QGIS plugin directory for testing. Plugin Builder comes with a Makefile that can be used on Linux and OS X to aid in development. Depending on your configuration, the Makefile may work on Windows.
To help in managing development of your projects, we&rsquo;ve come up with another option&mdash;a Python tool called pb_tool, which works anywhere QGIS runs.
