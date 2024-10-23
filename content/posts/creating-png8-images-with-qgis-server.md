---
source: "blog"
title: "Creating png8 images with QGIS server"
date: "2012-10-02T00:00:00+0000"
link: "https://blog.sourcepole.ch/2012/10/02/creating-png8-images-with-qgis-server/"
draft: "false"
showcase: "planet"
subscribers: ["sourcepole"]
author: "Sourcepole"
tags: []
---

For providing maps via WMS over the internet, it is important to generate image files with a small size. Because normally, most of the perceived WMS delay comes from transfering large images files over the internet (and not from map rendering itself). Therefore, QGIS server supports the conversion of png24 and png32 images into png8, therefore generating a file with only 1/3 resp. 1/4 of the original size (but with lower quality).
