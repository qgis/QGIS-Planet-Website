---
source: "blog"
title: "QGIS to (Geo)Pandas follow-up"
date: "2025-10-31T20:43:27+0000"
link: "https://anitagraser.com/2025/10/31/qgis-to-geopandas-follow-up/"
draft: "false"
showcase: "planet"
subscribers: ["anita_graser"]
author: "Anita Graser"
tags: ["qgis", "geopandas", "pandas", "python"]
languages: ["en_gb"]
available_languages: ["en_gb"]
---

<p class="wp-block-paragraph">The conversation around <a href="https://anitagraser.com/2025/10/26/looking-for-better-ways-to-convert-between-qgis-vectorlayer-and-geodataframe/">Looking for better ways to convert between QGIS VectorLayer and (Geo)DataFrame</a> is continuing over at <a href="https://fosstodon.org/@underdarkGIS/115442614331293320">https://fosstodon.org/@underdarkGIS/115442614331293320</a></p>
<p class="wp-block-paragraph">What I’ve learned so far: </p>
<ul class="wp-block-list">
<li>QgsVectorLayer.as_geopandas() has landed <a href="https://github.com/qgis/QGIS/commit/735de087bb3baf9d2e1d6179a7499b29ddb2a1ba">in QGIS master on 13 Oct 2025</a>.</li>
<li>There’s also QgsVectorLayer.field_to_numpy() which will be useful for many applications and has <a href="https://github.com/qgis/QGIS/pull/63532">landed on 29 Oct 2025</a>.</li>
<li><a href="https://github.com/qgis/QGIS/pull/63749">QgsArrowIterator is in the works right now</a>.</li>
</ul>
<p class="wp-block-paragraph">Exciting times for spatial data science tooling <img alt="🤩" class="wp-smiley" src="/img/subscribers/anita_graser/qgis-to-geopandas-follow-up/1f929.webp" style="height: 1em;"/></p>
<p class="wp-block-paragraph"></p>
