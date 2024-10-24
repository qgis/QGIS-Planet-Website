---
source: "blog"
title: "Crayfish 2.2: New features"
date: "2016-04-14T09:00:00-0500"
link: "https://lutraconsulting.co.uk/blog/2016/04/14/crayfish-2-2/"
draft: "false"
showcase: "planet"
subscribers: ["lutragis"]
author: "Lutra Consulting"
tags: []
---

<p>Crayfish 2.2 is out with lots of new features and new formats.</p>

<!-- more -->

<h2 id="plotting-time-series-and-cross-sections">Plotting time series and cross sections</h2>

<p>Profile tool plugin deemed not to be suitable for plotting time series. It lacks several features for visualising plots over s specific grid and generally to user interface is not very intuitive.</p>

<p>With the new plot options, user can plot time series at a point from the map or using an existing layer to generate plots. The tool is very flexible and allows user to export the layer to another format. In addition to time series, you can also generate cross section plots. Video below demonstrates the new feature in action:</p>

<center>
  
</center>

<p>As you can see, in the above video, more points can be added to the plot. To do so, you need to hold down CTRL key.</p>

<h2 id="grib-and-netcdf-support">GRIB and NetCDF support</h2>

<p>We have decided to expand the user base for Crayfish and allow meteorologists and oceanographers to view their temporal unstructured GRIB or NetCDF directly in Crayfish. Examples of those datasets can be found <a href="http://apps.ecmwf.int/datasets/data/interim-full-daily/levtype=sfc/" title="GRIB format">here</a> and <a href="https://www.unidata.ucar.edu/" title="NetCDF">here</a></p>

<p><img alt="Visualising global temperature datasets (GRIB fromat) in Crayfish" src="https://www.lutraconsulting.co.uk/img/posts/globaltemperature_grib_data.gif" /></p>

<h2 id="support-for-telemac-and-hec-ras-2d">Support for TELEMAC and HEC RAS 2D</h2>

<p>We also added suppord for HEC RAS 2D and TELEMAC. Our initial benchmark shows that Crayfish is much faster than an other TELEMAC plugins we used. Plus, Crayfish is truly <a href="https://github.com/lutraconsulting/qgis-crayfish-plugin">open source</a>!</p>

<h2 id="more-vector-contour-and-mesh-options">More vector, contour and mesh options</h2>

<p>You can now filter vectors to display only values above/below a certain threshold.</p>

<p>Contour label and values in Crayfish are now similar to raster styling in QGIS. This will allow users to generate better legend directly from Crayfish for print or animation outputs.</p>

<p>For debugging, we have added option to allow users to label mesh and change symbology.</p>

<p><img alt="Mesh labels in Crayfish" src="https://www.lutraconsulting.co.uk/img/posts/crayfish_22_mesh_label.png" /></p>

<h2 id="sponsor">Sponsor</h2>

<p>We’d like to thank <a href="http://www.vaw.ethz.ch/index_EN" target="_blank">The Laboratory of Hydraulics, Hydrology and Glaciology (VAW) of ETH Zurich</a> for sponsoring plotting feature.</p>

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
