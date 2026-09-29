---
source: "blog"
title: "Why QGIS will not open your DWG, and three ways around it"
date: "2026-09-14T18:40:00+0000"
link: "https://echocad.pages.dev/why-dwg-wont-open-in-qgis"
draft: "false"
showcase: "planet"
subscribers: ["echocad"]
author: "EchoCad"
tags: ["qgis", "dwg", "dxf"]
languages: ["en_gb"]
available_languages: ["en_gb"]
---

You used Project -&gt; Import/Export -&gt; Import Layers from DWG/DXF and either got "Drawing import
failed (unsupported version)", or waited two minutes for zero layers. Nothing is wrong with the
drawing or with the settings.

QGIS opens DWG through libdxfrw, which understands DWG up to the AutoCAD 2000 format. Drawings
saved as 2004, 2007, 2010, 2013 or 2018 do not open, and most drawings handed over today are
2013 or 2018. This is known upstream (qgis/QGIS#48637, open since 2022); in a sample of 44
public drawings we ran through QGIS, none opened. Even when a file does import, text placement
and hatch patterns are commonly lost.

The post then compares the three ways around it, with what each one actually costs:

1. Save as DXF from the CAD you already use. Free, but one file at a time, and the resulting
   DXF arrives as one layer per geometry type rather than per CAD layer.
2. ODA File Converter, which the free DWG plugins in the QGIS repository ask you to install.
   Whole folders at a time, but its licence restricts commercial use for non-members and it is
   awkward to get onto an offline machine.
3. A plugin that opens DWG directly inside QGIS, which is what EchoCad Pro does; the free
   edition covers the DXF side of options 1 and 2, including per-CAD-layer output, colours,
   line types, hatches and text.
