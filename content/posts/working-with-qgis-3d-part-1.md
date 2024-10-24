---
source: "blog"
title: "Working with QGIS 3D - Part 1"
date: "2018-03-01T07:00:00-0600"
link: "https://lutraconsulting.co.uk/blog/2018/03/01/working-with-qgis-3d-part-1/"
draft: "false"
showcase: "planet"
subscribers: ["lutragis"]
author: "Lutra Consulting"
tags: []
---

<p>In QGIS 3, we have introduced support for 3D canvas. Most of the functionalities are intuitive and easy to use. But there are some configuration options which are hidden and require a bit of more in-depth explanation for users and developers.</p>

<p>This blog post and the follow-up ones will discuss a range of topics: data sources, 3D canvas navigation, configuration, working with various types of layers, styling and more!</p>

<!-- more -->

<h1 id="data-sources">Data Sources</h1>

<p>To work with QGIS 3D, you need data: rasters and vectors. We will use digital terrain model rasters for 3D visualisation purpose. You can download SRTM data from the <a href="http://dwtkns.com/srtm30m/">SRTM Tile Downloader</a>.</p>

<p>For vectors, you can use any point, line and polygon data. There are different methods of creating 3D objects from each data type in the 3D canvas. If you want true 3D data representing buildings, you can download CityGML data from the <a href="https://www.citygml.org/3dcities/">list of open CityGML datasets</a>.</p>

<p>For the purpose of these blog posts, we will use SRTM data for Mont Blanc and CityGML data for Berlin.</p>

<p><strong>Note:</strong> You need to use a projected coordinate reference system in metres (or feet in case you belong to one of <a href="https://static.independent.co.uk/s3fs-public/styles/article_small/public/thumbnails/image/2017/04/04/16/p7rri0trqbpy.jpg">these countries</a>) for your data and canvas to be able to use QGIS 3D.</p>

<h1 id="3d-canvas-and-navigation">3D Canvas and Navigation</h1>

<p>To start with, we are going to add the terrain model for Mont Blanc to the QGIS canvas. Bing Aerial photo (as XYZ tiles layer) was also loaded in QGIS.</p>

<center>
<a href="https://www.lutraconsulting.co.uk/img/posts/qgis_3d_1.png" rel="lightbox"><img src="https://www.lutraconsulting.co.uk/img/posts/qgis_3d_1_499h.png" title="Raster data in QGIS 2D canvas (Click to enlarge)" /></a>
<p class="caption">Mont Blanc terrain model with Bing aerial in QGIS.<br />(Click to enlarge)</p>
</center>

<p>To view the 3D canvas, in the main menu select <strong>View</strong> &gt; <strong>New 3D Map View</strong></p>

<p>A floating QGIS panel will appear. You can drag the panel to the bottom part of your canvas to dock it.</p>

<center>
<a href="https://www.lutraconsulting.co.uk/img/posts/qgis_3d_2.png" rel="lightbox"><img src="https://www.lutraconsulting.co.uk/img/posts/qgis_3d_2_499h.png" title="Raster data in QGIS 2D and 3D canvases (Click to enlarge)" /></a>
<p class="caption">3D and 2D canvases in QGIS 3.<br />(Click to enlarge)</p>
</center>

<p>To start with, the 3D view shows the same extent and view as seen in the 2D canvas. Also note that there is no dedicated toolbar for navigation in the 3D canvas. You can zoom in/out and pan in the 3D canvas in the same way as in the main 2D canvas:</p>

<ul>
  <li>Move around map
    <ul>
      <li>by dragging the map with left mouse button pressed</li>
      <li>by using up/down/left/right keys</li>
    </ul>
  </li>
  <li>Zoom map in/out
    <ul>
      <li>by using the mouse wheel</li>
      <li>by dragging mouse up/down with right mouse button pressed</li>
    </ul>
  </li>
</ul>

<p>The following additional options allow you to explore the map in 3D:</p>

<ul>
  <li>Tilt / rotate camera
    <ul>
      <li>by dragging the mouse with middle mouse button pressed</li>
      <li>by pressing Shift and dragging the mouse with left mouse button pressed</li>
      <li>by pressing Shift and using up/down/left/right keys</li>
    </ul>
  </li>
</ul>

<center>
  
</center>

<p>To reset the camera view, click <img alt="Zoom Full" src="https://raw.githubusercontent.com/qgis/QGIS/master/images/themes/default/mActionZoomFullExtent.svg?sanitize=true" /> button in the 3D canvas panel.</p>

<h1 id="terrain-configuration">Terrain Configuration</h1>

<p>You can use a terrain raster to represent 3D elevation in your canvas. It is expected that such raster layer contains one band where each raster cell represents elevation.
To do that, click <img alt="Options" src="https://raw.githubusercontent.com/qgis/QGIS/master/images/themes/default/mActionOptions.svg?sanitize=true" /> button to open a new window with 3D view configuration. After selecting your raster layer for <strong>Elevation</strong> and clicking OK, you should be able to see Mont Blanc in the 3D view:</p>

<center>
<a href="https://www.lutraconsulting.co.uk/img/posts/qgis_3d_4.png" rel="lightbox"><img src="https://www.lutraconsulting.co.uk/img/posts/qgis_3d_4_499h.png" title="3D view of Mont Blanc (Click to enlarge)" /></a>
<p class="caption">3D view of Mont Blanc.<br />(Click to enlarge)</p>
</center>

<center>
  
</center>

<h1 id="advanced-configuration">Advanced Configuration</h1>

<p>In the configuration window there are various other options to fine-tune the 3D scene - let’s have a closer look at their meaning.
Before diving into the details, it is worth noting that terrain in 3D view is represented by a hierarchy of terrain tiles and
as the camera moves closer to the terrain, existing tiles that do not have sufficient detail are replaced by smaller tiles with more details.
Each tile has mesh geometry derived from the elevation raster layer and texture created by rendering 2D map for the extent of the tile.</p>

<p><img alt="QGIS 3D configuration" src="https://www.lutraconsulting.co.uk/img/posts/qgis_3d_3.png" /></p>

<p>Here is the complete list of the configuration options and their meaning:</p>

<ul>
  <li><strong>Elevation</strong>: Raster to be used for generation of terrain.</li>
  <li><strong>Vertical scale</strong>: Scale factor for vertical axis. Raising the scale will make even small hills look like mountains!</li>
  <li><strong>Tile resolution</strong>: How many samples from the terrain raster layer to use for each tile. The value of 16 px means that geometry of each tile will be built from 16x16 elevation samples. Higher number creates more detailed terrain tiles at the expense of increased rendering complexity.</li>
  <li><strong>Skirt height</strong>: Sometimes it is possible to see small cracks between tiles of the terrain. Raising this value will add vertical walls (“skirts”) around terrain tiles to hide the cracks.</li>
  <li><strong>Map tile resolution</strong>: Width and height of 2D map images used as textures for terrain tiles. The value of 256 px means that each tile will have map rendered into image of 256x256 pixels. Higher number creates more detailed terrain tiles at the expense of increased rendering complexity.</li>
  <li><strong>Max. screen error</strong>: Determines threshold when existing terrain tiles are swapped to more detailed ones (and vice versa) - i.e. how soon 3D view will use higher quality tiles. Lower number means more details in the scene at the expense of increased rendering complexity.</li>
  <li><strong>Max. ground error</strong>: Tells the 3D view at what resolution of terrain tiles it is fine to stop dividing them into more detailed tiles (because splitting them would not introduce any extra detail anyway). This value limits the depth of the hierarchy of tiles: lower value makes the hierarchy depth, increasing rendering complexity.</li>
  <li><strong>Zoom levels</strong>: Show how many zoom levels will be used (depends on map tile resolution and max. ground error).</li>
  <li><strong>Show labels</strong>: Toggles the map labels on/off</li>
  <li><strong>Show map tile info</strong>: Adds border and tile numbers to terrain tiles (useful for troubleshooting terrain issues)</li>
  <li><strong>Show bounding boxes</strong>: Shows 3D bounding boxes of terrain tiles (useful for troubleshooting terrain issues)</li>
</ul>

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
