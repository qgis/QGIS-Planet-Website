---
source: "blog"
title: "Support for Point Clouds Released in QGIS 3.18"
date: "2021-02-18T18:00:01-0600"
link: "https://lutraconsulting.co.uk/blog/2021/02/18/qgis-3-18-point-cloud/"
draft: "false"
showcase: "planet"
subscribers: ["lutragis"]
author: "Lutra Consulting"
tags: []
---

<p>QGIS 3.18 is finally here. This will be the first release of QGIS with native support for point cloud data. This work was made possible by generous contributions from the community.</p>

<p><img alt="Point cloud data in QGIS 3D" src="https://www.lutraconsulting.co.uk/img/posts/pc_qgis_3d.jpg" />
(Data from <a href="https://www.geoportal.sk/en/zbgis/als-dtm.html">UGKK SR</a>, made by <a href="https://www.researchgate.net/profile/Tibor_Lieskovsky/research">Tibor Lieskovsky</a>)</p>

<h2 id="contributors">Contributors</h2>

<p>When we announced the <a href="https://www.lutraconsulting.co.uk/crowdfunding/pointcloud-qgis/">campaign in August 2020</a>, the response was overwhelming and within weeks, we managed to reach and then exceed the amount required.</p>

<p>Below is the list of contributors in no particular order:</p>

<p><a href="http://mapfly.fr/">Mapfly</a>, Ujaval Gandhi from <a href="https://spatialthoughts.com/">Spatial Thoughts</a>, <a href="https://www.maanmittauslaitos.fi">National Land Survey of Finland</a>, Daniel Löwenborg, <a href="https://bnhr.xyz/">BNHR</a>, <a href="http://impactgis.com/">Imapct GIS</a>, Andreas Neumann, <a href="https://standortsolothurn.so.ch">Kanton Solothurn, Switzerland</a>, <a href="https://www.vevey.ch/">City of Vevey</a>, <a href="http://www.mappingautomation.com/">Mapping Automation</a>, <a href="https://www.ne.ch/Pages/accueil.aspx">Service de la géomatique du canton de Neuchâtel</a>, <a href="https://linktr.ee/hansakwast">Hans van der Kwast</a>, 3DGeoCloud,
<a href="https://www.rudaz.ch/index.php/en/">Rudaz+Partner AG</a>, Leonard Gouzin, <a href="https://tiledb.com/">TileDB, Inc.</a></p>

<p>We wish to also thank the many anonymous contributors who do not appear in this list.</p>

<p><strong>Note</strong>: if you have contributed to the campaign but your name does not appear here, you may not have selected the option to be listed in the campaign form. Please contact us if you’d like to be listed.</p>

<p>In addition to financial contributions, we’d like to extend our gratitude to all those who helped spread the word, helped with the testing and provided feedback and sample data.</p>

<h2 id="new-features">New features</h2>
<p style="text-align: center;">
<a href="https://www.lutraconsulting.co.uk/"><img alt="Lutra Consulting" class="left" src="https://www.lutraconsulting.co.uk/img/lutra-logo.png" /></a>
<a href="https://north-road.com/"><img alt="North Road" src="https://www.lutraconsulting.co.uk/img/nr_header_logo.png" /></a>
<a href="https://hobu.co/"><img alt="Hobu" src="https://www.lutraconsulting.co.uk/img/hobulogo.png" /></a>
</p>

<p>This is a brief summary of new features from our joint work with <a href="https://north-road.com/">North Road</a> and <a href="https://hobu.co/">Hobu</a>:</p>
<ul>
  <li>Introduction of a new map layer type: a point cloud layer</li>
  <li>Load LAS or LAZ files (either by drag’n’drop or by opening files in Data Sources Manager)</li>
  <li>Load <a href="https://entwine.io/entwine-point-tile.html">EPT datasets</a> by pointing QGIS to their <code class="highlighter-rouge">ept.json</code> file (currently only supporting datasets on the local drive)</li>
  <li>Support for rendering point cloud data in 2D and 3D map views</li>
  <li>Apply various rendering styles in 2D and 3D:
    <ul>
      <li>“Attribute by Ramp” - draw data based on a single attribute and a color ramp (similar to “Graduated” styling for vector layers)</li>
      <li>“RGB” - draw data using colors assigned to the points (combining red/green/blue attributes)</li>
      <li>“Classification” - draw data using different colors for different classes (ground, buildings, vegetation, …), also allowing display of only desired classes</li>
      <li>“Extent only” (2D only) - draw only bounding box of the point cloud</li>
      <li>“Single color” (3D only) - draw all points with a single color</li>
    </ul>
  </li>
  <li>Set size and shape of points</li>
  <li>Manually adjust scaling and offset of elevation (Z values) - if needed to match with elevation of other data</li>
  <li>Point cloud layer properties dialog to see metadata of the point clouds</li>
  <li>Identify tool supports point cloud layers and shows all attributes of picked points</li>
  <li>2D and 3D views only render a subset of the point cloud for the best performance for the given view (for geeks - this is thanks to indexing to octree data structure, using EPT format written by <a href="https://github.com/hobu/untwine">untwine tool</a> packaged with QGIS)</li>
  <li>Optimize the quality and performance of the 3D view using point budget configuration, which limits maximum amount of point rendered at any time (set to 1 million by default)</li>
  <li>Enable eye-dome lighting in 3D views for much better depth perception of point clouds</li>
  <li>New “Walk mode” camera navigation in 3D views - there is now a switch between the original “Terrain based” navigation mode and the new mode, which allow easier navigation through point cloud data</li>
</ul>

<p>Please note that as this is the initial release (with over 10 thousand lines of new code related to point clouds), there may be still some rough edges here and there, or some data may not load or display correctly. In case you encounter any issues with the new functionality, please let us know - do not hesitate to create a <a href="https://github.com/qgis/QGIS/issues">new QGIS issue</a></p>

<p><img alt="Point cloud in action" src="https://www.lutraconsulting.co.uk/img/posts/point_cloud_in_qgis.png" />
(Data from <a href="https://kartta.hel.fi/link/9qyfgF">Helsinki City</a>)</p>

<h2 id="future-work">Future work</h2>

<p>This has been the start of a larger effort to bring full support for point cloud data into QGIS. We, in collaboration with <a href="https://north-road.com/">North Road</a> and <a href="https://hobu.co/">Hobu</a> are developing requirements for integrating point cloud data processing and analysis, more data formats, better visualisation, profile tools etc. in future releases of QGIS.</p>

<p>If you’re interested in helping shape those requirements or funding such features, please <a href="https://www.lutraconsulting.co.uk/blog/categories/qgis/info@lutraconsulting.co.uk">contact us at info@lutraconsulting.co.uk</a>.</p>

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
