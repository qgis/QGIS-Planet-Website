---
source: "blog"
title: "Mesh Data Abstraction Library (MDAL)"
date: "2018-10-18T04:00:00-0500"
link: "https://lutraconsulting.co.uk/blog/2018/10/18/mdal/"
draft: "false"
showcase: "planet"
subscribers: ["lutragis"]
author: "Lutra Consulting"
tags: []
---

<p>In the world of GIS, vector and raster are the most common data types to represent real world features. But not always, vectors and rasters can describe the complexity and nature of the data.</p>

<!-- more -->

<p><img alt="MDAL Mesh" src="https://www.lutraconsulting.co.uk/img/posts/mdal_mesh.png" /></p>

<p>Example of those datasets are:</p>
<ul>
  <li>Metrological data: e.g. temperature and wind speed</li>
  <li>Hydrological data: flood depth and flow velocity</li>
  <li>Oceanography: salinity and wave flux</li>
</ul>

<p><img alt="MDAL arrows and contours" src="https://www.lutraconsulting.co.uk/img/posts/mdal_arrows_contours.png" /></p>

<p>In the past, we introduced <a href="https://www.lutraconsulting.co.uk/projects/crayfish">Crayfish plugin</a> to handle unstructured grids, usually with temporal and other components. The main issues with <a href="https://www.lutraconsulting.co.uk/projects/crayfish">Crayfish plugin</a> were:</p>
<ul>
  <li><a href="https://www.lutraconsulting.co.uk/projects/crayfish">Crayfish plugin</a> had its own renderer. Therefore, we had to create binaries and ship them with the plugin. This was not ideal, as not all the platforms (e.g. MacOS) was not supported.</li>
  <li><a href="https://www.lutraconsulting.co.uk/projects/crayfish">Crayfish plugin</a> loaded all the data in the memory. For small files, this was not an issue. But there was not a solution for larger files.</li>
</ul>

<h1 id="why-mdal">Why MDAL?</h1>

<p>For more details of the rational behind introducing MDAL, see the <a href="https://github.com/qgis/QGIS-Enhancement-Proposals/issues/119">QGIS Enhancement Proposal</a> with great suggestions and feedback from the developers.</p>

<p>TL;DR: we needed a new abstraction library to handle the mesh data formats similar to GDAL/OGR dealing with rasters and vectors.</p>

<h1 id="current-state">Current state</h1>

<p>After the feedback from the QGIS community, we have introduced MDAL library earlier this year. It took us a bit of time to put the <a href="https://github.com/lutraconsulting/MDAL">infrastructure in place</a>. There are already some formats available from MDAL. The library was integrated to <a href="https://github.com/qgis/QGIS/tree/master/external/mdal">QGIS from 3.2</a>. But extensive improvements and new features were added during 3.4.</p>

<p>There are still more formats to support. In QGIS, we will also need to enhance the spatial indexing and performance of the driver in general. For more information visit <a href="http://www.mdal.xyz/">MDAL website</a>.</p>

<h1 id="how-to-work-with-mdal-layer-in-qgis">How to work with MDAL layer in QGIS</h1>

<p><a href="https://www.unidata.ucar.edu/software/netcdf/examples/ECMWF_ERA-40_subset.nc">Here</a> is a mesh layer you can use to load in QGIS. For more data, you can visit the <a href="http://apps.ecmwf.int/datasets/">ECMWF</a>(or <a href="https://atmosphere.copernicus.eu/catalogue#/">Copernicus</a>) or <a href="https://disc.gsfc.nasa.gov/mirador-guide">NASA</a> websites.</p>

<p>In QGIS, from the main menu &gt; <strong>Layer &gt; Data Source Manager</strong>. A new window will appear. From the left panel, click on <img alt="Mesh layer" src="https://raw.githubusercontent.com/qgis/QGIS/master/images/themes/default/mIconMeshLayer.svg?sanitize=true" /> <strong>Mesh</strong> and point to the downloaded file.</p>

<p>You should be able to see a figure similar to the one below:</p>

<p><img alt="Mesh layer in QGIS" src="https://www.lutraconsulting.co.uk/img/posts/mdal_load.png" /></p>

<p>To view quantities within the mesh, you can open the <strong>Layer Styling Panel</strong>. Click on <img alt="symbology" src="https://www.lutraconsulting.co.uk/img/posts/mdal_symbology.png" /> Styling tab:</p>

<ul>
  <li>First select <img alt="symbology" src="https://raw.githubusercontent.com/qgis/QGIS/master/images/themes/default/propertyicons/meshframe.svg?sanitize=true" /> and deactivate <strong>Native Mesh Rendering</strong></li>
  <li>Click on <img alt="general" src="https://www.lutraconsulting.co.uk/img/posts/mdal_general.png" /> and under groups, towards the right of <strong>10 metre wind</strong> click on <img alt="contour" src="https://raw.githubusercontent.com/qgis/QGIS/master/images/themes/default/propertyicons/meshcontours.svg?sanitize=true" /> and <img alt="vector" src="https://raw.githubusercontent.com/qgis/QGIS/master/images/themes/default/propertyicons/meshvectors.svg?sanitize=true" /> to view the quantities.</li>
  <li>Below the <strong>Groups</strong>, you can move the slider to browse through time of the dateset(s).</li>
  <li>To change style of the contours and vectors you can click on <img alt="contour" src="https://raw.githubusercontent.com/qgis/QGIS/master/images/themes/default/propertyicons/meshcontours.svg?sanitize=true" /> and <img alt="vector" src="https://raw.githubusercontent.com/qgis/QGIS/master/images/themes/default/propertyicons/meshvectors.svg?sanitize=true" /> tabs and adjust the color ramps and vector sizes accordingly.</li>
</ul>

<p><img alt="Mesh layer in QGIS" src="https://www.lutraconsulting.co.uk/img/posts/mdal_contour.png" /></p>

<h1 id="what-happens-to-crayfish-plugin">What happens to Crayfish plugin?</h1>
<p>We have recently released a new version of <a href="https://github.com/lutraconsulting/qgis-crayfish-plugin">Crayfish plugin</a> to work directly with mesh layer in QGIS. Crayfish is now based on Python only and can be installed on all main platforms (including MacOS).</p>

<h1 id="future-developments">Future developments</h1>
<p>We are planning to add mesh calculator (either as a core QGIS feature or Crayfish/Processing plugin). There will be more formats in the pipeline to support in MDAL too.</p>

<p>If you’d like to add support for your mesh layer to MDAL, you can follow the examples on the <a href="https://github.com/lutraconsulting/MDAL">github repository</a>. We are always happy to help.</p>

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
