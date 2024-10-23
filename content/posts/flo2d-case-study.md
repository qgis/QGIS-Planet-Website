---
source: "blog"
title: "Case Study: FLO-2D QGIS Plugin"
date: "2021-02-15T00:00:00-0600"
link: "https://lutraconsulting.co.uk/blog/2021/02/15/flo2d-case-study/"
draft: "false"
showcase: "planet"
subscribers: ["lutragis"]
author: "Lutra Consulting"
tags: []
---

<p>The case study presents the implementation of the QGIS FLO-2D Plugin project (5 minute read)</p>

<!-- more -->

<h2 id="introduction">Introduction</h2>
<p><a href="https://www.lutraconsulting.co.uk/blog/categories/qgis/www.flo-2d.com">FLO-2D</a> is one of the most widely used commercially available flood models. FLO-2D is capable of simulating urban flooding in high resolution including storm drain systems.</p>

<center>
<img alt="FLO-2D" src="https://www.lutraconsulting.co.uk/img/posts/logos/Flo2D_logo.jpg" title="FLO-2D" width="200" />
</center>

<p>In 2016 the FLO-2D team invited us to develop a set of tools for optimising the flood model build process in QGIS.  The resulting plugin allows hydraulic models to be built quickly by leveraging the wide range of tools available in the QGIS ecosystem.</p>

<p>The plugin can be downloaded by following the guidance in the plugin <a href="https://flo-2d.com/qgis-plugin/">documentation</a></p>

<p>As the use of open source GIS grows within the water engineering sector, Lutra Consulting develops and maintains <a href="https://www.lutraconsulting.co.uk/projects/mdal">MDAL</a> which makes the visualisation and post-processing of time-varying numerical model results possible in QGIS.</p>

<p>Contact us at <a href="mailto:info@lutraconsulting.co.uk">info@lutraconsulting.co.uk</a> if you’d like to discuss the benefits of integrating your flood modelling software more tightly with QGIS.</p>

<p><img alt="QGIS FLO-2D Plugin" src="https://www.lutraconsulting.co.uk/img/case-studies/flo2d-plugin/flo2dplugin1.png" /></p>

<h2 id="overview-of-previous-gui-tools-flo-2d-gds">Overview of Previous GUI tools: FLO-2D GDS</h2>
<p>FLO-2D’s focus on urban modeling requires large datasets that may include several million grid cells.  Each cell has between 4 and 10 attributes so datasets can often be in the range of several gigabytes.</p>

<p>Previously, Grid Developer System (GDS) was used to pre-process the spatial data used by FLO-2D. Being a 32-bit application, the GDS was only able to load up to 4 gigabytes of data and its programming framework was also no longer maintained by Microsoft.  Modellers could only be built on Windows PCs.</p>

<p>All development and maintenance of the GDS was carried out by the FLO-2D team.</p>

<h2 id="behind-the-implementation">Behind the Implementation</h2>

<h3 id="guiding-principles-behind-the-new-qgis-flo-2d-plugin">Guiding principles behind the new QGIS Flo-2D plugin</h3>

<p>We assessed the tools used at the time and in close collaboration with the FLO-2D team, optimised the workflow from the users’ point of view with emphasis on speed and simplicity.</p>

<p>To keep things simple for the users, we aimed to provide a level of abstraction so users would no longer need to be involved with the internal structure of FLO-2D solver input files.  They could instead focus on real-world aspects affecting their models.</p>

<p>Together with the FLO-2D team we designed a solution that was based on 3 core ideas:</p>

<ul>
  <li>Modellers will use native QGIS tools and point/line/polygon layers to define real-world objects (e.g. domain, boundary conditions, levees, …)</li>
  <li>These real-world objects will be converted automatically into the data structures required by the FLO-2D solver (although expert users can still modify these data structures if they so wish).</li>
  <li>Additional productivity tools will be provided to allow users to speed-up time consuming tasks</li>
</ul>

<h3 id="features-of-the-plugin">Features of the plugin</h3>
<p>Some of the key features of the solution are listed here:</p>

<ul>
  <li>Easy creation and handling of new models (all model data sits in a single GeoPackage file)</li>
  <li>User friendly and intuitive digitizing and manipulation of model components (through simple GIS layers and dedicated tools) including:
    <ul>
      <li>1D domain</li>
      <li>Boundary and initial conditions</li>
      <li>1D channels and cross-sections</li>
      <li>Levees</li>
      <li>Rainfall</li>
      <li>Infiltration areas</li>
      <li>Storm drains</li>
    </ul>
  </li>
  <li>Various options for obtaining grid data such as elevation, roughness, reduction factors etc. from different sources (raster layers, external vector layers etc.)</li>
  <li>Plotting profiles and editing time series data</li>
  <li>Automated tools for schematizing input layers into the GDS format</li>
  <li>Importing basic data from HEC-RAS models</li>
  <li>Import / export functionality between GeoPackage and GDS format (*.DAT files)</li>
  <li>Running external FLO-2D tools (FLO-2D Pro engine etc.) directly from QGIS</li>
</ul>

<p><img alt="QGIS FLO-2D Plugin" src="https://www.lutraconsulting.co.uk/img/case-studies/flo2d-plugin/flo2dplugin2.png" /></p>

<h2 id="benefits-for-the-flo-2d-developers">Benefits for the FLO-2D developers:</h2>
<p>Benefits for the developers of FLO-2D include:</p>

<ul>
  <li>Reduced development and maintenance costs, since much of the heavy lifting of the FLO-2D plugin is done by QGIS itself</li>
  <li>By being part of the QGIS ecosystem, gaining opportunities to approach QGIS users in the flood risk industry to use FLO-2D software</li>
  <li>The FLO-2D plugin is developed on GitHub, allowing the latest development technologies such as continuous integration, automatic testing and issue tracking to be used</li>
  <li>Ability to solve upstream bugs in QGIS or <a href="https://www.lutraconsulting.co.uk/projects/mdal">MDAL</a> due to the open-source nature of the projects</li>
</ul>

<center>
<img alt="QGIS3" src="https://www.lutraconsulting.co.uk/img/posts/qgis3_logo.png" title="FLO-2D" width="400" />
</center>

<h2 id="benefits-for-flo-2d-users">Benefits for FLO-2D users:</h2>
<p>Some of the benefits realised by FLO-2D customers include:</p>

<ul>
  <li>Being able to work with their FLO-2D models using open source GIS on all major operating systems</li>
  <li>A full GIS application to support their data pre-processing</li>
  <li>Logical and intuitive workflows</li>
  <li>FLO-2D results can now be visualised and post-processed natively in QGIS via mesh layer</li>
  <li>Ability to use all native QGIS support and development channels in addition to FLO-2D support</li>
  <li>Integration of internal workflows with powerful native QGIS features including projection support, GDAL/OGR integrations, background maps support (e.g. vector tiles), printed flood maps, etc.</li>
  <li>Ability analyze results via QGIS’ Crayfish plugin and produce graphs and outputs</li>
</ul>

<h2 id="the-plugin-in-action">The plugin in action!</h2>

<center>

</center>

<h2 id="further-reading">Further Reading</h2>
<ul>
  <li><a href="https://flo-2d.com">FLO-2D webpage</a></li>
  <li><a href="https://www.lutraconsulting.co.uk/projects/mdal">MDAL and Mesh Layer</a></li>
</ul>

<p>Do you have any questions or would like to see demo of QGIS Mesh Layer? Contact us at <a href="mailto:info@lutraconsulting.co.uk">info@lutraconsulting.co.uk</a>
or schedule a demo call <a href="https://calendly.com/saber-razmjooei/15min">calendly.com/saber-razmjooei/15min</a></p>

<h2 id="key-words">Key words</h2>
<p>QGIS, plugin, python, migration, optimised, speed up, fast, hydraulic modelling, water, 2D, open-source, cost reduction, software development</p>

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
