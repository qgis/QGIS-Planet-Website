---
source: "blog"
title: "Where's my .qgis3 Folder?"
date: "2018-03-12T00:00:00+0000"
link: "http://spatialgalaxy.net/2018/03/12/wheres-my-.qgis3-folder/"
draft: "false"
showcase: "planet"
subscribers: ["spatialgalaxy_net"]
author: "Spatial Galaxy"
tags: []
---

There&rsquo;s been several posts to GIS StackExchange along the lines of:
Where&rsquo;s my .qgis3 folder?
Prior to QGIS 3, the .qgis/.qgis2 folder was found under your home directory. At version 3, the folder has moved to a more standard profile location for your operating system.
There are a couple of ways to determine where the folder is located:
 Use the Settings-&gt;User Profiles-&gt;Open active profile folder menu item Use QgsApplication.qgisSettingsDirPath from Python or the console  Here are the &ldquo;standard&rdquo; locations for Linux, Mac, and Windows, as found under your HOME directory:
