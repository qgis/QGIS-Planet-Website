---
source: "blog"
title: "Why QGIS Class Names Start with Qgs"
date: "2014-03-29T10:50:00+0000"
link: "http://spatialgalaxy.net/2014/03/29/why-qgis-class-names-start-with-qgs/"
draft: "false"
showcase: "planet"
subscribers: ["spatialgalaxy_net"]
author: "Spatial Galaxy"
tags: []
---

If you&rsquo;re a developer, or have looked at the QGIS source code, you&rsquo;ve likely noticed that most C++ classes in the project start with Qgs.
Back before the dark ages of QGIS, Trolltech (now Digia) allowed you to reserve name prefixes for classes that used the Qt framework.
Shortly afterwards, I reserved the gs prefix for my use, resulting in class names that start with Qgs.
You might think this is based on some mangling of words like QGIS or perhaps GIS, but it was purely egocentric:
