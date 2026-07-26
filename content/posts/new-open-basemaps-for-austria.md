---
source: "blog"
title: "New Open Basemaps for Austria"
date: "2026-07-26T12:02:33+0000"
link: "https://anitagraser.com/2026/07/26/new-open-basemaps-for-austria/"
draft: "false"
showcase: "planet"
subscribers: ["anita_graser"]
author: "Anita Graser"
tags: ["cartography", "gis", "opengovermentdata", "qgis", "cartography", "ogd"]
languages: ["en_gb"]
available_languages: ["en_gb"]
---

<p class="wp-block-paragraph">For many years now, we have been enjoying the <a href="https://basemap.at">basemap.at</a> service with it’s various basemap options (color, gray, with/without labels, …) in WMTS and vector tiles.</p>
<figure class="wp-block-image size-large"><a href="https://anitagraser.com/wp-content/uploads/2026/07/image-3.png"><img alt="" class="wp-image-9749" height="658" src="/img/subscribers/anita_graser/new-open-basemaps-for-austria/image-3.webp" width="1024"/></a><figcaption class="wp-element-caption">Basemap.at Standard WMTS in QGIS (<a href="https://cdn.basemap.at/QGIS-Integration.pdf">instructions here</a>)</figcaption></figure>
<p class="wp-block-paragraph">For a few weeks now, there is an additional service by BEV: Their cartographic models “Kartographischen Modelle (KM)” are now available as <a href="https://data.bev.gv.at/geonetwork/srv/ger/catalog.search#/metadata/0651d416-2ce0-40c2-88a1-3f7c6e1f484a">raster (KM-R) in COG-TIFF</a> format. </p>
<figure class="wp-block-image size-large"><a href="https://anitagraser.com/wp-content/uploads/2026/07/image-4.png"><img alt="" class="wp-image-9751" height="403" src="/img/subscribers/anita_graser/new-open-basemaps-for-austria/image-4.webp" width="776"/></a><figcaption class="wp-element-caption">Adding the COG-TIFF URI </figcaption></figure>
<p class="wp-block-paragraph">The downloads come with proper instructions:</p>
<ul class="wp-block-list">
<li><a href="https://data.bev.gv.at/download/KM_R/KM_QGIS_Anleitung_202603.pdf"><strong>KM_QGIS_Anleitung_202603</strong></a> including tips to switch to bilinear resampling for better rendering:</li>
</ul>
<figure class="wp-block-image size-large"><a href="https://anitagraser.com/wp-content/uploads/2026/07/image-1.png"><img alt="" class="wp-image-9738" height="659" src="/img/subscribers/anita_graser/new-open-basemaps-for-austria/image-1.webp" width="1024"/></a><figcaption class="wp-element-caption">BEV KM-R in QGIS</figcaption></figure>
<p class="wp-block-paragraph">Some <a href="https://www.bev.gv.at/Services/Produkte/Kartographische-Modelle/KM50-V.html#download-04-1">vector (KM-V)</a> in GeoPackages with QGIS projects providing the layer style and label settings are already available for the <a href="https://data.bev.gv.at/geonetwork/srv/ger/catalog.search#/metadata/5d438a91-b745-4a79-983c-74015ee2fa10">Stichtag 30.01.2026</a> downloads. And they look awesome:</p>
<figure class="wp-block-image size-large"><a href="https://anitagraser.com/wp-content/uploads/2026/07/image-8.png"><img alt="" class="wp-image-9763" height="657" src="/img/subscribers/anita_graser/new-open-basemaps-for-austria/image-8.webp" width="1024"/></a><figcaption class="wp-element-caption">BEV KM-V project defaults</figcaption></figure>
<figure class="wp-block-image size-large"><a href="https://anitagraser.com/wp-content/uploads/2026/07/image-9.png"><img alt="" class="wp-image-9765" height="657" src="/img/subscribers/anita_graser/new-open-basemaps-for-austria/image-9.webp" width="1024"/></a><figcaption class="wp-element-caption">And without labels</figcaption></figure>
<p class="wp-block-paragraph">KM-V downloads are provided in tiles, so it’s not quite as simple as grabbing the COG URI:</p>
<figure class="wp-block-image size-large"><a href="https://data.bev.gv.at/download/KM_V/KM50/KM50_Kacheln_Uebersicht_202603.pdf"><img alt="" class="wp-image-9758" height="576" src="/img/subscribers/anita_graser/new-open-basemaps-for-austria/image-7.webp" width="1024"/></a></figure>
<p class="wp-block-paragraph">It’s worth noting though, that the KM-V GeoPackages are still a work in progress and not all tiles are available for download yet. </p>
<p class="wp-block-paragraph">I’ll keep an eye on the downloads to see when the rest of the tiles become available. </p>
<p class="wp-block-paragraph">Until then, I leave you with a couple of examples of the Großglockner (highest mountain in Austria) area in basemap.at and KM-R side-by-side: </p>
<div class="wp-block-jetpack-tiled-gallery aligncenter is-style-rectangular"><div class=""><div class="tiled-gallery__gallery"><div class="tiled-gallery__row"><div class="tiled-gallery__col"><figure class="tiled-gallery__item"><img alt="" src="/img/subscribers/anita_graser/new-open-basemaps-for-austria/image-6.webp" tabindex="0"/></figure></div><div class="tiled-gallery__col"><figure class="tiled-gallery__item"><img alt="" src="/img/subscribers/anita_graser/new-open-basemaps-for-austria/image-5.webp" tabindex="0"/></figure></div></div></div></div></div>
<p class="wp-block-paragraph"></p>
