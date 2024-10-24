---
source: "blog"
title: "Littering Your Python Path: The Road to Destruction"
date: "2012-12-05T16:59:00+0000"
link: "http://spatialgalaxy.net/2012/12/05/littering-your-python-path-the-road-to-destruction/"
draft: "false"
showcase: "planet"
subscribers: ["spatialgalaxy_net"]
author: "Spatial Galaxy"
tags: []
---

Well not quite destruction, but a bit of hair pulling&hellip;
While working on an update to the Plugin Builder, I encountered a small problem. The Plugin Builder displays the version number in the title bar of its main window. After bumping the version number to 1.8.4 in all the requisite places, it still showed 1.8.3 when testing.
Using grep on all the source files revealed no instance of 1.8.3 in any file.
