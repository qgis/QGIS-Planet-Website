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
---

<p><img alt="Soar banner" class="alignnone size-large wp-image-212592" height="296" src="https://north-road.com/wp-content/uploads/2023/08/soar_banner-1024x296.png" width="1024" /></p>
<p>Growing up, I would spend hours lost in National Geographic maps. The feeling of discovering new regions and new ways to view the world was addictive! It&#8217;s this same feeling of discovery and exploration which has made me super excited about <a href="https://soar.earth/">Soar’s Digital Atlas</a>. Soar is the brainchild of Australian, <a href="https://about.soar.earth/team">Amir Farhand</a>, and is fuelled by the talents of staff located across the globe to build a comprehensive digital atlas of the world’s maps and images. Soar has been designed to be an easy to use, expansive collection of diverse maps from all over the Earth. A great aspect of Soar is that it has implemented Strong Community Guidelines and moderation to ensure the maps are fit for purpose.</p>
<p>Recently, North Road collaborated with Soar to help facilitate their digital atlas goals by creating a QGIS plugin for <strong>Soar</strong>. The <a href="https://plugins.qgis.org/plugins/soar/">Soar plugin</a> allows QGIS users to directly:</p>
<ul>
<li>Export their QGIS maps and images straight to Soar</li>
<li>Browse and load maps from the entire Soar public catalogue into their QGIS projects</li>
</ul>
<p>There&#8217;s lots of extra tweaks we&#8217;ve added to help make the plugin user friendly, whilst offering tons of functionality that power users want. For instance, users can:</p>
<ul>
<li>Filter Soar maps by their current project extent and/or by category</li>
<li>Export raw or rendered raster data directly to Soar via a Processing tool</li>
<li>Batch upload multiple maps to Soar</li>
<li>Incorporate Soar map publishing into a Processing model or Python based workflow</li>
</ul>
<p><em>Soar will be presenting their new plugin at the <a href="https://github.com/qgis/QGIS/wiki/QOD-August-2023">QGIS Open Day</a> in August so check out the details <a href="https://github.com/qgis/QGIS/wiki/QOD-August-2023">here</a> and tune in at 2300 AEST or 1300 HR UTC. You can follow along via either <a href="https://youtube.com/live/Nm1TeYG4euk?feature=share" rel="nofollow">YouTube</a> or <a href="https://meet.jit.si/OkVillagesRecordHappily" rel="nofollow">Jitsi</a>.</em></p>
<h3>Browsing Soar maps from QGIS</h3>
<p>One of the main goals of the Soar QGIS plugin was to make it very easy to find new datasets and add them to your QGIS projects. There&#8217;s two ways users can explore the Soar catalog from QGIS:</p>
<p>You can open the Soar Browser Panel via the Soar toolbar button  <img alt="Soar browser" class="size-full wp-image-212593 alignnone" height="32" src="https://north-road.com/wp-content/uploads/2023/08/soar_load_browser.png" width="32" /> . This opens a floating catalog browser panel which allows you to interactively search Soar&#8217;s content while working on your map.</p>
<p><img alt="Soar browser panel" class="alignnone wp-image-212598 size-large" height="387" src="https://north-road.com/wp-content/uploads/2023/08/soar-browser-panel-e1692857479233-1024x387.png" width="1024" /></p>
<p>Alternatively, you can also access the Soar catalog and maps from the standard QGIS Data Source Manager dialog. Just open the &#8220;Soar&#8221; tab and search away!</p>
<p><img alt="" class="alignnone wp-image-212584 size-large" height="901" src="https://north-road.com/wp-content/uploads/2023/08/data_manager-e1692857602162-1024x901.png" width="1024" /></p>
<p>When you&#8217;ve found an interesting map, hit the &#8220;Add to Map&#8221; button and the map will be added as a new layer into your current project. After the layer is loaded you can freely modify the layer&#8217;s style (such as the opacity, colorization, contrast etc) just like any other raster dataset using the standard QGIS Layer Style controls.</p>
<h2>Sharing your maps</h2>
<p>Before you can share your maps on Soar, you&#8217;ll need to first <a href="https://soar.earth/register?">sign up</a> for a free Soar account.</p>
<p>We&#8217;ve designed the Soar plugin with two specific use cases in mind for sharing maps. The first use case is when you want to share an entire map (i.e. QGIS project) to Soar. This will publish all the visible content from your map onto Soar, including all the custom styling, labeling, decorations and other content you&#8217;ve carefully designed. To do this, just select the Project menu, Import/Export -&gt; Export map to Soar option.</p>
<p><img alt="Upload via Project to Soar" class="alignnone size-full wp-image-212586" height="499" src="https://north-road.com/wp-content/uploads/2023/08/export_from_canvas.png" width="451" /></p>
<p>You&#8217;ll have a chance to enter all the metadata and descriptive text explaining your map, and then the map will be rendered and uploaded directly to Soar.</p>
<p><img alt="Soar Metadata" class="alignnone size-full wp-image-212587" height="668" src="https://north-road.com/wp-content/uploads/2023/08/export_from_canvas_2.png" width="763" /></p>
<p>All content on the Soar atlas is moderated, so your shared maps get added to the moderation queue ready for review by the Soar team. (You&#8217;ll be notified as soon as the review is complete and your map is publicly available).</p>
<p>Alternatively, you might have a specific raster layer which you want to publish on Soar. For instance, you&#8217;ve completed some flood modelling or vegetation analysis and want to share the outcome widely. To do this, you can use the &#8220;Publish dataset to Soar&#8221; tool available from the QGIS Processing toolbox:</p>
<p><img alt="Upload product to Soar via processing tools" class="alignnone size-large wp-image-212589" height="628" src="https://north-road.com/wp-content/uploads/2023/08/publish_to_soar-1024x628.png" width="1024" /></p>
<p>Just pick the raster layer you want to upload, enter the metadata information, and let the plugin do the rest! Since this tool is made available through QGIS&#8217; Processing framework, it also allows you to run it as a batch process (eg uploading a whole folder of raster data to Soar), or as a step in your QGIS Graphical Models!</p>
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
<p>We&#8217;ve a few other tips to keep in mind to successfully share your maps on Soar:</p>
<ul>
<li>The Soar catalog currently works with raster image formats including GeoTIFF / ECW / JP2 / JPEG / PNG</li>
<li>All data uploaded to Soar must be in the WGS84 Pseudo-Mercator (EPSG: 3857) projection</li>
<li>Check the size of your data before sharing it, as a large size dataset may take a long time to upload</li>
</ul>
<p>So there you have it! So simple to start building up your contribution to Soar&#8217;s Digital Atlas. Those who might find this useful to upload maps include:</p>
<ul>
<li>Community groups</li>
<li>Hobbyists</li>
<li>Building a cartographic/geospatial portfolio</li>
<li>Education/research</li>
<li>Contributing to world events (some of the biggest news agencies already use this service i.e. BBC)</li>
</ul>
<p>You can find out more about the QGIS Soar plugin at the QGIS Open Day on August 23rd, 2023 at 2300 HR AEST or 1300 HR UTC. Check <a href="https://github.com/qgis/QGIS/wiki/QOD-August-2023">here</a> for more information or to watch back after.</p>
<p>If you&#8217;re interested in exploring how a QGIS plugin can make your service easily accessible to the millions of daily QGIS users, <a href="https://north-road.com/contact/">contact us</a> to discuss how we can help!</p>
<div class="supsystic-social-sharing supsystic-social-sharing-package-flat supsystic-social-sharing-hide-on-homepage supsystic-social-sharing-spacing supsystic-social-sharing-content supsystic-social-sharing-content-align-left" style="font-size: 0.7em!important; display: none;"><a class="social-sharing-button sharer-flat sharer-flat-1 counter-standard without-counter twitter" href="https://twitter.com/share?url=https%3A%2F%2Fnorth-road.com%2F2023%2F08%2F24%2Fsoar-earth-digital-atlas-qgis-plugin%2F&amp;text=Soar.Earth+Digital+Atlas+QGIS+Plugin" rel="nofollow" target="_blank" title="Twitter"><i class="fa-ssbs fa-ssbs-fw fa-ssbs-twitter"></i><div class="counter-wrap standard"><span class="counter">0</span></div></a><a class="social-sharing-button sharer-flat sharer-flat-1 counter-standard without-counter linkedin" href="https://www.linkedin.com/shareArticle?mini=true&amp;title=Soar.Earth+Digital+Atlas+QGIS+Plugin&amp;url=https%3A%2F%2Fnorth-road.com%2F2023%2F08%2F24%2Fsoar-earth-digital-atlas-qgis-plugin%2F" rel="nofollow" target="_blank" title="Linkedin"><i class="fa-ssbs fa-ssbs-fw fa-ssbs-linkedin"></i><div class="counter-wrap standard"><span class="counter">0</span></div></a><a class="social-sharing-button sharer-flat sharer-flat-1 counter-standard without-counter facebook" href="http://www.facebook.com/sharer.php?u=https%3A%2F%2Fnorth-road.com%2F2023%2F08%2F24%2Fsoar-earth-digital-atlas-qgis-plugin%2F" rel="nofollow" target="_blank" title="Facebook"><i class="fa-ssbs fa-ssbs-fw fa-ssbs-facebook"></i><div class="counter-wrap standard"><span class="counter">0</span></div></a></div>
