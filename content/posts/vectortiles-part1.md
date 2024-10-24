---
source: "blog"
title: "Working with vector tiles - Part 1"
date: "2020-06-10T01:00:00-0500"
link: "https://lutraconsulting.co.uk/blog/2020/06/10/vectortiles-part1/"
draft: "false"
showcase: "planet"
subscribers: ["lutragis"]
author: "Lutra Consulting"
tags: []
---

<p>After a successful crowdfunding campaign to <a href="https://www.lutraconsulting.co.uk/crowdfunding/vectortile-qgis/">support Vector Tiles in QGIS</a>, we have been busy adding new features for the upcoming release (3.14).</p>

<p>In this blog post, we are exploring different methods to add your vector tiles and style them.</p>

<!-- more -->

<h2 id="loading-data---local-files">Loading data - local files</h2>

<p>If you have an MBTiles file containing vector tiles, you can simply drag and drop the layer in QGIS. Alternatively, you can connect to a local vector tile file(s) from the Data Source Manager or the Browser Panel. As an example, you can use this <a href="https://merginmaps.com/projects/saber/blogpost-vectortile/tree">QGIS project</a> which contains Switzerland vector tiles (maximum zoom level =14).</p>

<p><img alt="Vector tile file" src="https://www.lutraconsulting.co.uk/img/posts/add-vector-tile-file.png" /></p>

<p>You can also test this project on your mobile device. Download <a href="https://merginmaps.com">Input app</a> (for iOS you need the <a href="https://testflight.apple.com/join/JO5EIywn">TestFlight</a> version of the app), head to <strong>Projects</strong> &gt; <strong>Explore</strong> and download <strong>saber\blogpost-vectortile</strong>.</p>

<p align="center">
  <img src="https://www.lutraconsulting.co.uk/img/posts/vectortile_mobile.png" />
</p>

<h2 id="loading-data---web-resources">Loading data - web resources</h2>

<p>You can access vector tiles served through the web. You need to have the URL and possibly API key to add them in your QGIS. In the example below, vector tiles from <a href="https://cloud.maptiler.com/tiles/v3/">MapTiler</a> are added to QGIS:</p>

<p><img alt="Vector tile file" src="https://www.lutraconsulting.co.uk/img/posts/add-vector-tile-url.png" /></p>

<p>To use <a href="https://cloud.maptiler.com/tiles/v3/">MapTiler</a> data, we recommend using their dedicated <a href="https://www.maptiler.com/qgis-plugin/">QGIS plugin</a>, which comes with vector tiles in <a href="https://github.com/maptiler/qgis-maptiler-plugin">different styles</a>. The plugin should be available on the QGIS plugin repository.</p>

<h2 id="styling-data">Styling data</h2>

<p>Vector tiles contain points, line and polygon geometries. You can define a set of rules for features and apply style and label. Style and labelling can be dependent on the zoom level. Similar to vectors and rasters, styles for vector tiles can be stored in QML format. To set up filters, you can use the identify tool in QGIS to inspect geometries of your vector tile:</p>

<p><img alt="Vector tile file" src="https://www.lutraconsulting.co.uk/img/posts/vectortile_identify.png" /></p>

<p>Currently, the most common format to store vector tiles styles are Mapbox GL (json). The <a href="https://github.com/openmaptiles">OpenMapTiles repo</a> contains some excellent Mapbox GL styles. <a href="https://github.com/wonder-sk/mapbox2qgis">We initially developed a tool to convert the json files to QGIS style</a>. The plugin has been further extended and developed by <a href="https://github.com/maptiler/qgis-maptiler-plugin">MapTiler</a> to better handle the <a href="https://github.com/openmaptiles">OpenMapTiles</a> data schema. This will ensure future changes to the data schema will be addressed by the plugin.</p>

<p>Example of styles converted from Mapbox GL to QGIS from <a href="https://www.maptiler.com/qgis-plugin/">Maptiler QGIS plugin</a></p>

<p><img alt="Vector tile file" src="https://www.lutraconsulting.co.uk/img/posts/vectortile_basic.png" /></p>

<p><img alt="Vector tile file" src="https://www.lutraconsulting.co.uk/img/posts/vectortile_bright.png" /></p>

<p><img alt="Vector tile file" src="https://www.lutraconsulting.co.uk/img/posts/vectortile_toner.png" /></p>

<p><img alt="Vector tile file" src="https://www.lutraconsulting.co.uk/img/posts/vectortile_streets.png" /></p>

<p>In the next post, we will explore different options within QGIS or other 3rd party tools to generate vector tiles.</p>

<h2 id="credits">Credits</h2>

<p>All the data used in this blog post was from <a href="https://www.openstreetmap.org/">OpenStreetMap</a> server by <a href="https://download.geofabrik.de/">Geofabrik</a>. <a href="https://github.com/openmaptiles/openmaptiles/blob/master/LICENSE.md">OpenMapTiles</a> conversion tool was used to generate the tiles from OpenStreetMap to vector tiles. See <a href="https://github.com/openmaptiles/openmaptiles/blob/master/LICENSE.md">software license</a> for more details.</p>

<p>The following <a href="https://github.com/openmaptiles">OpenMapTiles</a> Mapbox GL styles <a href="https://github.com/openmaptiles/maptiler-basic-gl-style/blob/master/LICENSE.md">Bright</a>, <a href="https://github.com/openmaptiles/positron-gl-style/blob/master/LICENSE.md">Positron</a>, <a href="https://github.com/openmaptiles/maptiler-basic-gl-style/blob/master/LICENSE.md">Basic</a> and <a href="https://github.com/openmaptiles/fiord-color-gl-style#license">Fiord</a> were converted using <a href="https://github.com/wonder-sk/mapbox2qgis">mapbox2qgis</a> and <a href="https://github.com/maptiler/qgis-maptiler-plugin">QGIS MapTiler plugin</a>.</p>

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
