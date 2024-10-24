---
source: "blog"
title: "How to view buildings in QGIS3D"
date: "2017-10-16T04:00:00-0500"
link: "https://lutraconsulting.co.uk/blog/2017/10/16/buildings-in-qgis3d/"
draft: "false"
showcase: "planet"
subscribers: ["lutragis"]
author: "Lutra Consulting"
tags: []
---

<p>With support for QGIS3D canvas, you can represent your vectors in a number of ways. In this post, we will walk you through how to render vectors as 3D objects.</p>

<!-- more -->

<h2 id="data">Data</h2>

<p>You can use <a href="https://www.citygml.org/">CityGML</a> or ESRI Multipatch, where the height of buildings are stored within the feature. For the purpose of this example, we are going to view New York buildings using ESRI Multipatch format. You can download the data from here:</p>

<p>http://maps.nyc.gov/download/3dmodel/DA_WISE_Multipatch.zip</p>

<p>After unziping the file, you will have several gdb files. You can use GDAL/OGR to convert gdb to Geopackage (or ESRI Shapefile). We should also convert the geometry type from <strong>multipatch</strong> to <strong>multipolygon</strong>. In Microsoft Windows gdal/ogr commands are available from the OSGEO4W command line.</p>

<div class="highlighter-rouge"><div class="highlight"><pre class="highlight"><code>ogr2ogr -f GPKG ny_buildings3d.gpkg DA1_3D_Buildings_Multipatch.gdb -nlt multipolygon
</code></pre></div></div>
<p>You can append the remaining gdb files to the existing Geopackage:</p>

<div class="highlighter-rouge"><div class="highlight"><pre class="highlight"><code>ogr2ogr -append -f GPKG ny_buildings3d.gpkg DA2_3D_Buildings_Multipatch.gdb -nlt multipolygon
</code></pre></div></div>

<p>Alternatively, you can write a simple batch script to loop through the files.</p>

<p><strong>Note:</strong> we used gdal/ogr from trunk (2.3.0dev).</p>

<p>If you know of any other data sources, please send us an email so we can compile a full list of supported formats.</p>

<h3 id="viewing-data">Viewing data</h3>

<p>To be able to use QGIS3D, you need to install the latest version of QGIS using OSGEO4W or other installer for your platform.</p>

<p>Add the Geopackage containing the buildings to your QGIS. In QGIS, from the main menu, click on **View &gt; New 3D Map View **</p>

<p>A new view, similar to your 2D canvas will be added to the bottom of your canvas. To be able to extrude the buildings, we need to enable 3D styling of the building layer.</p>

<p>Ensure your <strong>Style panel</strong> is enabled (this is usually located on the right hand side of the canvas). Select <strong>3D View</strong> tab and tick the box for <strong>Enable 3D renderer</strong> for building layer.</p>

<p><img alt="Vector 3D styling" src="https://www.lutraconsulting.co.uk/img/posts/qgis3dvectorstyling.png" /></p>

<p>To navigate in 3D canvas, you can use Shift key + the wheel button on your mouse device.</p>

<p><img alt="3D view" src="https://www.lutraconsulting.co.uk/img/posts/qgis3dcanvas.png" /></p>

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
