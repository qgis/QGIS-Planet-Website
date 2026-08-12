---
source: "blog"
title: "Soar.Earth Digital Atlas QGIS Plugin"
date: "2023-08-24T07:06:45+0000"
link: "https://north-road.com/2023/08/24/soar-earth-digital-atlas-qgis-plugin/"
draft: "false"
showcase: "planet"
subscribers: ["north_road"]
author: "North Road"
tags: ["integrations", "partners", "qgis", "atlas", "cartography", "plugins", "qgis"]
languages: ["en_gb"]
available_languages: ["en_gb"]
---

<p><img alt="Soar banner" class="alignnone size-large wp-image-212592" height="296" src="/img/subscribers/north_road/soar-earth-digital-atlas-qgis-plugin/soar_banner-1024x296.webp" width="1024"/></p>
<p>Growing up, I would spend hours lost in National Geographic maps. The feeling of discovering new regions and new ways to view the world was addictive! It’s this same feeling of discovery and exploration which has made me super excited about <a href="https://soar.earth/">Soar’s Digital Atlas</a>. Soar is the brainchild of Australian, <a href="https://about.soar.earth/team">Amir Farhand</a>, and is fuelled by the talents of staff located across the globe to build a comprehensive digital atlas of the world’s maps and images. Soar has been designed to be an easy to use, expansive collection of diverse maps from all over the Earth. A great aspect of Soar is that it has implemented Strong Community Guidelines and moderation to ensure the maps are fit for purpose.</p>
<p>Recently, North Road collaborated with Soar to help facilitate their digital atlas goals by creating a QGIS plugin for <strong>Soar</strong>. The <a href="https://plugins.qgis.org/plugins/soar/">Soar plugin</a> allows QGIS users to directly:</p>
<ul>
<li>Export their QGIS maps and images straight to Soar</li>
<li>Browse and load maps from the entire Soar public catalogue into their QGIS projects</li>
</ul>
<p>There’s lots of extra tweaks we’ve added to help make the plugin user friendly, whilst offering tons of functionality that power users want. For instance, users can:</p>
<ul>
<li>Filter Soar maps by their current project extent and/or by category</li>
<li>Export raw or rendered raster data directly to Soar via a Processing tool</li>
<li>Batch upload multiple maps to Soar</li>
<li>Incorporate Soar map publishing into a Processing model or Python based workflow</li>
</ul>
<p><em>Soar will be presenting their new plugin at the <a href="https://github.com/qgis/QGIS/wiki/QOD-August-2023">QGIS Open Day</a> in August so check out the details <a href="https://github.com/qgis/QGIS/wiki/QOD-August-2023">here</a> and tune in at 2300 AEST or 1300 HR UTC. You can follow along via either <a href="https://youtube.com/live/Nm1TeYG4euk?feature=share" rel="nofollow">YouTube</a> or <a href="https://meet.jit.si/OkVillagesRecordHappily" rel="nofollow">Jitsi</a>.</em></p>
<h3>Browsing Soar maps from QGIS</h3>
<p>One of the main goals of the Soar QGIS plugin was to make it very easy to find new datasets and add them to your QGIS projects. There’s two ways users can explore the Soar catalog from QGIS:</p>
<p>You can open the Soar Browser Panel via the Soar toolbar button  <img alt="Soar browser" class="size-full wp-image-212593 alignnone" height="32" src="/img/subscribers/north_road/soar-earth-digital-atlas-qgis-plugin/soar_load_browser.webp" width="32"/> . This opens a floating catalog browser panel which allows you to interactively search Soar’s content while working on your map.</p>
<p><img alt="Soar browser panel" class="alignnone wp-image-212598 size-large" height="387" src="/img/subscribers/north_road/soar-earth-digital-atlas-qgis-plugin/soar-browser-panel-e1692857479233-1024x387.webp" width="1024"/></p>
<p>Alternatively, you can also access the Soar catalog and maps from the standard QGIS Data Source Manager dialog. Just open the “Soar” tab and search away!</p>
<p><img alt="" class="alignnone wp-image-212584 size-large" height="901" src="/img/subscribers/north_road/soar-earth-digital-atlas-qgis-plugin/data_manager-e1692857602162-1024x901.webp" width="1024"/></p>
<p>When you’ve found an interesting map, hit the “Add to Map” button and the map will be added as a new layer into your current project. After the layer is loaded you can freely modify the layer’s style (such as the opacity, colorization, contrast etc) just like any other raster dataset using the standard QGIS Layer Style controls.</p>
<h2>Sharing your maps</h2>
<p>Before you can share your maps on Soar, you’ll need to first <a href="https://soar.earth/register">sign up</a> for a free Soar account.</p>
<p>We’ve designed the Soar plugin with two specific use cases in mind for sharing maps. The first use case is when you want to share an entire map (i.e. QGIS project) to Soar. This will publish all the visible content from your map onto Soar, including all the custom styling, labeling, decorations and other content you’ve carefully designed. To do this, just select the Project menu, Import/Export -&gt; Export map to Soar option.</p>
<p><img alt="Upload via Project to Soar" class="alignnone size-full wp-image-212586" height="499" src="/img/subscribers/north_road/soar-earth-digital-atlas-qgis-plugin/export_from_canvas.webp" width="451"/></p>
<p>You’ll have a chance to enter all the metadata and descriptive text explaining your map, and then the map will be rendered and uploaded directly to Soar.</p>
<p><img alt="Soar Metadata" class="alignnone size-full wp-image-212587" height="668" src="/img/subscribers/north_road/soar-earth-digital-atlas-qgis-plugin/export_from_canvas_2.webp" width="763"/></p>
<p>All content on the Soar atlas is moderated, so your shared maps get added to the moderation queue ready for review by the Soar team. (You’ll be notified as soon as the review is complete and your map is publicly available).</p>
<p>Alternatively, you might have a specific raster layer which you want to publish on Soar. For instance, you’ve completed some flood modelling or vegetation analysis and want to share the outcome widely. To do this, you can use the “Publish dataset to Soar” tool available from the QGIS Processing toolbox:</p>
<p><img alt="Upload product to Soar via processing tools" class="alignnone size-large wp-image-212589" height="628" src="/img/subscribers/north_road/soar-earth-digital-atlas-qgis-plugin/publish_to_soar-1024x628.webp" width="1024"/></p>
<p>Just pick the raster layer you want to upload, enter the metadata information, and let the plugin do the rest! Since this tool is made available through QGIS’ Processing framework, it also allows you to run it as a batch process (eg uploading a whole folder of raster data to Soar), or as a step in your QGIS Graphical Models!</p>
<h4>Some helpful hints</h4>
<p>All maps uploaded to Soar require the following information:</p>
<ul>
<li>Map Title</li>
<li>Description</li>
<li>Tags</li>
<li>Categories</li>
<li>Permission to publish</li>
</ul>
<p>This helps other users to find your maps with ease, and also gives the Soar moderation team the information required for their review process.</p>
<p>We’ve a few other tips to keep in mind to successfully share your maps on Soar:</p>
<ul>
<li>The Soar catalog currently works with raster image formats including GeoTIFF / ECW / JP2 / JPEG / PNG</li>
<li>All data uploaded to Soar must be in the WGS84 Pseudo-Mercator (EPSG: 3857) projection</li>
<li>Check the size of your data before sharing it, as a large size dataset may take a long time to upload</li>
</ul>
<p>So there you have it! So simple to start building up your contribution to Soar’s Digital Atlas. Those who might find this useful to upload maps include:</p>
<ul>
<li>Community groups</li>
<li>Hobbyists</li>
<li>Building a cartographic/geospatial portfolio</li>
<li>Education/research</li>
<li>Contributing to world events (some of the biggest news agencies already use this service i.e. BBC)</li>
</ul>
<p>You can find out more about the QGIS Soar plugin at the QGIS Open Day on August 23rd, 2023 at 2300 HR AEST or 1300 HR UTC. Check <a href="https://github.com/qgis/QGIS/wiki/QOD-August-2023">here</a> for more information or to watch back after.</p>
<p>If you’re interested in exploring how a QGIS plugin can make your service easily accessible to the millions of daily QGIS users, <a href="https://north-road.com/contact/">contact us</a> to discuss how we can help!</p>
