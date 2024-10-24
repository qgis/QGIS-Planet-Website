---
source: "blog"
title: "Plugin Builder 3.1"
date: "2019-01-02T00:00:00+0000"
link: "http://spatialgalaxy.net/2019/01/02/plugin-builder-3.1/"
draft: "false"
showcase: "planet"
subscribers: ["spatialgalaxy_net"]
author: "Spatial Galaxy"
tags: []
---

We&rsquo;ve released version 3.1 of the Plugin Builder for QGIS 3.x. This version contains a number of bug fixes and performance enhancements.
Here are some of the changes included since version 3.0.3:
 Fix issue with reload on generated plugins Move dialog creation to run method to improve startup performance Move help file generation files to proper method Include missing tags file Attempt to compile resources.qrc when plugin is generated (requires pyrcc5 in path) Set deployment directory in Makefile based on user OS (pb_tool is recommended over make) Check for valid URL format for tracker and repository  Compiling Resource File If you have the resource compiler pyrcc5 in your path, the resource file will be compiled automatically when you generate your new plugin.
