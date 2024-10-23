---
source: "blog"
title: "New label tools in QGIS"
date: "2010-11-17T00:00:00+0000"
link: "https://blog.sourcepole.ch/2010/11/17/new-label-tools-in-qgis/"
draft: "false"
showcase: "planet"
subscribers: ["sourcepole"]
author: "Sourcepole"
tags: []
---

In cartography, it is a frequent operation to set labels to fixed positions, together with the position of the fix point (left/middle/right, Top, Half, Bottom) that is kept constant in case of font change, rotation or zoom. Therefore, three new editing tools to manipulate text labels are now in the QGIS developer version:
the move label tool drags text labels to a new position the rotate label tool is for interactive rotation of labels the label property tools opens a dialog that lets the user manipulate the data defined properties of a label (and also the text of the label attribute) All three tools work on the new labeling engine and data defined labeling needs to be enabled for the layer (e.
