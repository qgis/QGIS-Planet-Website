---
source: "blog"
title: "WMTS enhancement and XYZ tile native support in QGIS 2.18"
date: "2016-10-26T09:00:00-0500"
link: "https://lutraconsulting.co.uk/blog/2016/10/26/qgis-xyz-tile-wmts-preview/"
draft: "false"
showcase: "planet"
subscribers: ["lutragis"]
author: "Lutra Consulting"
tags: []
---

<p>In this post, we will highlight the new features we have added to QGIS 2.18 …</p>

<!-- more -->

<h2 id="wmts-enhancement">WMTS enhancement</h2>

<p>The WMTS provider had not been benefiting from the the <a href="https://www.lutraconsulting.co.uk/projects/qgis-mtr/">QGIS multi-threaded rendering we did earlier in QGIS 2.4</a>.</p>

<p>In previous versions of QGIS, users had to wait until download of all tiles of a layer has finished in order to view the resulting map. This has now been fixed and the tiles show up in map canvas immediately as they get downloaded, improving the user experience by greatly lowering the time until something is shown.</p>

<p>Moreover, previously downloaded tiles from lower or higher resolutions may be used for the preview functionality in the areas where the tiles with correct resolution have not been downloaded yet.</p>

<p>The screencast <a href="https://www.youtube.com/embed/C3qFj1ULDWI">here</a> shows fetching and rendering a WMTS layer in QGIS 2.14 (left) and the same layer in QGIS 2.18 (right):</p>

<h2 id="support-for-xyz-raster-tiles">Support for XYZ raster tiles</h2>

<p>There are a couple of python plugins allowing users to add <a href="https://en.wikipedia.org/wiki/Tiled_web_map">XYZ tiles</a> (e.g. Bing maps) to QGIS. The plugins only allow certain web services and it is often tricky for supporting the private ones with API keys.</p>

<p>In addition, there are other QGIS applications without python support (e.g. QGIS for Android devices) where they can leverage from having a native support.</p>

<p>Currently, you can only add XYZ tile services from the Browser panel. The video below demonstrates how to add the current precipitation and OpenStreetMap xyz tiles to your QGIS:</p>

<center>
  
</center>

<h2 id="sponsors">Sponsors</h2>
<p>WMTS enhancements was sponsored by <a href="http://www.linz.govt.nz/">Land Information New Zealand</a>. Support for XYZ tiles was funded internally.</p>

    <div class="input-promo">
    <h2>You may also like...</h2>
    <a href="https://merginmaps.com">Mergin Maps, a field data collection app based on QGIS</a>. Mergin Maps makes field work easy with its simple interface and cloud-based sync. Available on Android, iOS and Windows.
    <img alt="Screenshots of the Mergin Maps mobile app for Field Data Collection" src="https://lutraconsulting.co.uk/img/posts/input_app_for_field_data_collection.jpg" /><br />
    <a href="https://play.google.com/store/apps/details?id=uk.co.lutraconsulting&amp;utm_source=lutra-atom&amp;utm_medium=lutra-blog-footer&amp;utm_campaign=input">
      <img alt="Get it on Google Play" src="https://play.google.com/intl/en_us/badges/images/generic/en_badge_web_generic.png" width="180px" />
    </a>
    <a href="https://apps.apple.com/us/app/input/id1478603559?ls=1&amp;utm_source=lutra-atom&amp;utm_medium=lutra-blog-footer&amp;utm_campaign=input">
      <img alt="Get it on Apple store" src="https://www.lutraconsulting.co.uk/img/posts/App_Store.svg" style="padding-top: 0px;" width="144px" />
    </a>
  </div>
