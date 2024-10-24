---
source: "blog"
title: "Overview of QGIS 3.14 Mesh Features"
date: "2020-06-17T04:00:00-0500"
link: "https://lutraconsulting.co.uk/blog/2020/06/17/crayfish-3-4-4/"
draft: "false"
showcase: "planet"
subscribers: ["lutragis"]
author: "Lutra Consulting"
tags: []
---

<p>Mesh layer is now supported for the 1D, 2D and 3D data frames. It also comes with integration to the temporal controller in QGIS 3.14.</p>

<!-- more -->

<p>The releases of QGIS 3.14, MDAL 0.6.1 and Crayfish 3.4.4 are planned for this Friday
We are delighted to have made improvements for the upcoming release:</p>
<ul>
  <li>full integration with the new temporal controller</li>
  <li>1D meshes support (e.g. to support urban drainage system models)</li>
  <li>New rendering and styling options for mesh layers</li>
  <li>improving greatly rendering speed for large datasets</li>
  <li>various other enhancements and bug-fixes</li>
</ul>

<p>If you are eager to try the latest features, you can always install QGIS nightlies/master.</p>

<p>Special thanks to all contributors and the sponsors of these features</p>
<ul>
  <li><a href="https://www.deltares.nl/en/">Deltares</a></li>
  <li><a href="https://www.bmt.org/">BMT</a></li>
  <li><a href="https://www.arteliagroup.com/en">Artelia Group</a></li>
</ul>

<p>Do you want to use QGIS Mesh Layers in your projects? <a href="https://www.lutraconsulting.co.uk/projects/mdal/">Read more…</a></p>

<h2 id="native-qgis-temporal-controller">Native QGIS Temporal Controller</h2>

<p>The long awaited native temporal support in QGIS is finally materialised. We managed to port all QGIS Mesh Layer code to the 
new infrastructure and remove the custom time slider in the Mesh Layer properties/styling dialog. The native temporal 
support will greatly benefit users in the long run. We can now share the code components for time handing with 
raster, vector and WMS-T and other temporal data types. Also user can load multiple temporal layers and change time-domain for all of them
at the same time.</p>

<p><img alt="mesh 3d in time" src="https://www.lutraconsulting.co.uk/img/posts/time3d.gif" /></p>

<p>Unfortunately, the new temporal framework changed the API, so if you use QgsMeshLayer in your plugins, consult the 
QGIS documentation for required changes.</p>

<h2 id="new-mdal-logo-and-docs">New MDAL logo and docs</h2>

<p>We have started writing the proper documentation for all supported formats and also reference documentation for developers. We welcome 
all contributions to improve the documentations. 
Just go to <a href="https://www.mdal.xyz">https://www.mdal.xyz</a> and click “Edit on GitHub”!</p>

<p><img alt="mdal logo" src="https://www.lutraconsulting.co.uk/img/OS_projects/LogoHorizontal_01_color_400x123.png" /></p>

<h2 id="support-for-1d-meshes">Support for 1d meshes</h2>

<p>MDAL and QGIS now supports 1D meshes, currently for UGRID and 3Di formats. Other formats should be easy to add. If you are interested in supporting a format, drop us a line.</p>

<p>You can read the full technical description in the 
following <a href="https://github.com/qgis/QGIS-Enhancement-Proposals/issues/164">QGIS Enhancement Proposal</a>.</p>

<p>The 1D meshes can be styled with the various renderers, for example use of pressure data to calculate line width:
<img alt="variable with 1D mesh" src="https://www.lutraconsulting.co.uk/img/posts/variablewidth.gif" /></p>

<p>Furthermore, Crayfish plugin has been extended to support such mesh data frames. For example, 1D plots in Crayfish with the snapping and routing along the network can be used:
<img alt="snapping 1D mesh" src="https://www.lutraconsulting.co.uk/img/posts/snapping1d.gif" /></p>

<h2 id="2d-mesh-rendering-improvement">2D mesh rendering improvement</h2>

<p>2D meshes streamlines/particles/arrows can be now styled by the colour ramp. You can better display streamlines and mesh vectoral data varaition: 
<img alt="streamline colorram" src="https://www.lutraconsulting.co.uk/img/posts/streamlines_colorramp.png" /></p>

<h2 id="meshes-in-3d-map-view">Meshes in 3D map view</h2>

<p>The mesh layer is now fully supported in the 3D map view. You can visualise your terrain and overlay vector arrows (e.g. velocity) and other mesh quantities (e.g. water surface) in the 3D map view.</p>

<p><img alt="meshes 3D" src="https://www.lutraconsulting.co.uk/img/posts/meshin3d.gif" /></p>

<h2 id="other-features-and-bugfixes">Other features and bugfixes</h2>

<h3 id="qgis">QGIS</h3>
<ul>
  <li>The mesh rendering speed increased by 2-20 times depending on various mesh/zoom/map/data combinations</li>
  <li>Ability to show only subset of dataset groups in the Mesh styling window</li>
  <li>Support for reading multiple meshes in one file (e.g. UGRID)</li>
  <li>Ability to resample vertex values to faces</li>
  <li>Support for saving/loading of QML styles</li>
  <li>Full usage of temporal controller, even in print templates, animation, …</li>
</ul>

<h3 id="mdal">MDAL</h3>
<ul>
  <li>The GRIB and NetCDF datasets are now loaded twice as fast</li>
  <li>Support for UGRID datasets with magnitude and direction</li>
  <li>Support for reading of UGRID classified data and its usage in QGIS color ramps</li>
  <li>Renamed the pointers and functions in the API for consistency</li>
  <li>Created brand new logo and started the online-docs</li>
  <li>Support XMS Tin</li>
</ul>

<h3 id="crayfish">Crayfish</h3>
<ul>
  <li>Ported to new temporal API</li>
  <li>Added 1D plots</li>
  <li>Fixed various UI bugs</li>
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
