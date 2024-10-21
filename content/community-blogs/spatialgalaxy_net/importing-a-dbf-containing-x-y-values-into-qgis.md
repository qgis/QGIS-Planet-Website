---
source: "blog"
title: "Importing a DBF containing X-Y Values into QGIS"
image: "importing-a-dbf-containing-x-y-values-into-qgis"
date: "2011-01-29T10:49:16+0000"
link: "http://spatialgalaxy.net/2011/01/29/importing-a-dbf-containing-x-y-values-into-qgis/"
draft: "true"
showcase: "planet"
folder: "spatialgalaxy_net"
author: "Spatial Galaxy"
---

Suppose you have a DBF (.dbf) file containing X and Y values that you want to import and save as a spatial layer.
QGIS doesn&rsquo;t support direct import of a DBF file as a map layer, however, we can use some command line magic to convert it to a CSV file and then use the Delimited Text plugin to get the job done.
Your DBF file should have an id for each record and fields containing X and Y values.
