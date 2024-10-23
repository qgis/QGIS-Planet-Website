---
source: "blog"
title: "Case Study: QGIS Core Development for TUFLOW"
date: "2021-08-18T01:00:00-0500"
link: "https://lutraconsulting.co.uk/blog/2021/08/18/tuflow-case-study/"
draft: "false"
showcase: "planet"
subscribers: ["lutragis"]
author: "Lutra Consulting"
tags: []
---

<p>The case study presents the C++ development of QGIS Desktop to support rendering of 3D results produced by TUFLOW’s 3D capable solver: TUFLOW FV (10 minute read)</p>

<!-- more -->

<h2 id="introduction">Introduction</h2>
<p><a href="https://www.tuflow.com">TUFLOW</a> is a suite of advanced 1D/2D/3D computer simulation software for flooding, urban drainage, coastal hydraulics, sediment transport, particle tracking and water quality. With over 30 years of continuous development, TUFLOW is internationally recognised as one of the industry leaders for hydraulic modelling accuracy, speed and workflow efficiency.</p>

<p>Lutra Consulting Ltd is a leader in software development for pre- and post-processing of hydraulic and meteorological results in open-source QGIS. We also work on mobile data collection <a href="https://merginmaps.com/en/">Input App</a> and GIS data synchronization service <a href="https://merginmaps.com">Mergin</a></p>

<center>
<img alt="TUFLOW" src="https://lutraconsulting.co.uk/img/posts/logos/TUFLOW_RGB.png" title="TUFLOW" width="200" />
</center>

<p>In 2019 the TUFLOW team commissioned us to develop post-processing support for their <a href="https://www.tuflow.com/products/tuflow-fv/">TUFLOW Flexible Mesh</a> format for QGIS 3.12. The format is 3D stacked mesh, which consists of multiple stacked 2D unstructured meshes each extruded in the vertical direction (levels) by means of a vertical coordinate.</p>

<center>
<img alt="TUFLOW" src="https://lutraconsulting.co.uk/img/case-studies/tuflow/stackedmesh.png" title="TUFLOW" width="600" />
</center>

<p>At that time QGIS only supported 2D meshes that defined results on vertices and faces. We had been keen to extend the capabilities of the software stack to support 3D mesh data for a long time so this was an exciting opportunity. Part of the task was also to include rendering support for TUFLOW model results on the QGIS 3D view. The delivery of the project was within one QGIS release cycle (less than 6 months time for users to use it on their projects!)</p>

<p>
<center>
<figure><img alt="Flooding simulation simulated as a mesh layer in QGIS 3D" src="https://lutraconsulting.co.uk/img/posts/mesh_flooding_3d.gif" title="Mesh 3D" /></figure>
</center></p>

<p>Contact us at <a href="mailto:info@lutraconsulting.co.uk">info@lutraconsulting.co.uk</a> if you’d like to discuss the benefits of integrating your flood modelling software more tightly with QGIS or you have some custom QGIS development in mind.</p>

<h1 id="c-development-process-from-requirement-to-delivery">C++ Development Process: From requirement to delivery</h1>

<h2 id="communicate-project-with-the-community-first">Communicate project with the community first</h2>

<p>When doing a substantial change in the QGIS codebase, the developer needs to write a technical specification of the QGIS changes for community discussion. QGIS Core Developers (which Lutra is a part of) can give valuable feedback to the overall technical approach and the wider community can raise some usability issues or enhancement proposals. Most importantly, each part of the QGIS code has its lead maintainers, for example Martin Dobias, our CTO, is the maintainer of QGIS 3D code and Peter Petrik is the maintainer of the Mesh layer code. It is a good practice to address the maintainers’, users’ and other developers’ concerns and feedback to ensure the feature can be implemented in QGIS.</p>

<p>So after a thorough discussion about the requirements with the TUFLOW team and analysis of the existing tools for post-processing and display of the TUFLOW FV format we came up with the <a href="https://github.com/qgis/QGIS-Enhancement-Proposals/issues/158">QGIS Enhancement: Support of 3D layered meshes</a></p>

<p>The community reaction was very positive and supportive. Time to start coding!</p>

<h3 id="mdal-to-support-tuflow-fv-netcdf-format">MDAL to support TUFLOW FV NetCDF format</h3>

<p>Mesh Data Abstraction Library <a href="https://www.mdal.xyz">MDAL</a> is a C++ library for handling unstructured mesh data. It provides a single data model for multiple supported data formats. MDAL is used by QGIS for data access for mesh layers. If you want QGIS to support your data format, you need to have a driver in MDAL that implements it.</p>

<center>
<img alt="MDAL" src="https://lutraconsulting.co.uk/img/OS_projects/mdal_logo_small.png" title="MDAL" width="200" />
</center>

<p>We added support for 3D stacked meshes and the TUFLOW FV format in <a href="https://github.com/lutraconsulting/MDAL/commit/6c39e40bf5047b53b4633a5cb611c9e7d6ce9098">MDAL</a>. When we develop features in MDAL, we focus on quality code, so</p>
<ul>
  <li>all changes have a proper code review,</li>
  <li>all code has fully automated tests with more than 90% coverage target</li>
  <li>the documentation and manual testing is done after coding</li>
</ul>

<p>To implement the TUFLOW FV driver for 3D stacked meshes, we added a new API/interface in MDAL, so we needed to follow up with the QGIS changes in <code class="highlighter-rouge">QgsMeshLayer</code> and MDAL data-provider.</p>

<h2 id="qgis-c-development-to-support-stacked-meshes-and-visualization-in-3d">QGIS C++ Development to support stacked meshes and visualization in 3D</h2>

<p>The implementation of large feature changes is best to split into smaller but self-consistent parts. For example the first <a href="https://github.com/qgis/QGIS/pull/33153">pull request</a> added the basic support for the new 3D stacked meshes. Each pull request we do has a screenshot or gif/video with the new functionality preview, follows <a href="https://docs.qgis.org/3.16/en/docs/developers_guide/codingstandards.html">QGIS Coding Standards</a>, has unit tests where necessary and includes the documentation for the functions/classes added in the public interface. Once the request is merged, the features are next day available in nightly builds on all platforms for testing!</p>

<center>
<img alt="3D Terrain in QGIS3" src="https://lutraconsulting.co.uk/img/case-studies/tuflow/terrain3dmesh.gif" title="3D Terrain in QGIS3" width="400" />
</center>

<h2 id="final-steps-feedback-testing-documentation-and-presentation">Final Steps: feedback, testing, documentation and presentation</h2>

<p>When all the features were in QGIS master, the TUFLOW team used windows <a href="https://qgis.org/en/site/forusers/alldownloads.html?highlight=nightly#windows">nightly builds</a> to test the new features and provide feedback. After a small number of iterations, all issues were resolved and implementation signed.</p>

<p>Shortly the new official QGIS <a href="https://www.qgis.org/en/site/getinvolved/development/roadmap.html#release-schedule">release</a> was published and we started promotion of the new features on our social media channels. Also, the features developed under this contract were promoted in the visual QGIS changelog.</p>

<ul>
  <li><a href="https://www.qgis.org/en/site/forusers/visualchangelog312/index.html#feature-3d-mesh-layer-terrain-renderer">Mesh Layer in 3D</a></li>
  <li><a href="https://www.qgis.org/en/site/forusers/visualchangelog312/index.html#feature-support-for-mesh-reference-time">Mesh Reference Time</a></li>
  <li><a href="https://www.qgis.org/en/site/forusers/visualchangelog312/index.html#feature-vector-trace-animation-and-streamlines-for-mesh-layer">Mesh Vector Streamlines</a></li>
</ul>

<center>
<img alt="Streamlines in QGIS3" src="https://lutraconsulting.co.uk/img/case-studies/tuflow/streamlines.png" title="Streamlines in QGIS3" width="400" />
</center>

<h1 id="benefits-for-tuflow-to-support-qgis-core-c-development">Benefits for TUFLOW to support QGIS Core C++ Development:</h1>

<ul>
  <li>Reduced development and maintenance costs for tools such as the <a href="https://wiki.tuflow.com/index.php?title=TUFLOW_Viewer">TUFLOW Viewer QGIS Plugin</a> since the new features are part of the QGIS core</li>
  <li>By being part of the QGIS ecosystem it provides opportunities to approach QGIS users in the flooding and coastal modeling industry to use TUFLOW software</li>
  <li>As a project sponsor, the requirements of the new features meet the present and future needs of the TUFLOW user base.</li>
  <li>At the beginning of the project Lutra showed all the current relevant capabilities of QGIS ecosystem, allowing TUFLOW to be aware of the latest and greatest features</li>
  <li>Allowed TUFLOW to solve upstream bugs in QGIS or <a href="https://www.lutraconsulting.co.uk/projects/mdal">MDAL</a> due to the open-source nature of the projects</li>
</ul>

<center>
<img alt="QGIS3" src="https://lutraconsulting.co.uk/img/posts/qgis3_logo.png" title="QGIS3 Logo" width="400" />
</center>

<h2 id="benefits-for-tuflow-users">Benefits for TUFLOW users:</h2>
<p>Key benefits made available to TUFLOW users include:</p>

<ul>
  <li>Being able to work with TUFLOW models using open source GIS on all major operating systems</li>
  <li>A full GIS application to support their data pre-processing</li>
  <li>Logical and intuitive workflows</li>
  <li>Visualisation and post-processing of TUFLOW results natively in QGIS via mesh layer</li>
  <li>The development allows interactive plotting features for 3D results, such as 3D profiles and curtains that can be easily extracted, providing an improved user experience</li>
  <li>Ability to use all native QGIS support and development channels in addition to TUFLOW support</li>
  <li>Integration of internal workflows with powerful native QGIS features including projection support, GDAL/OGR integrations, background maps support (e.g. vector tiles) and printed flood maps.</li>
</ul>

<h2 id="further-reading">Further Reading</h2>
<ul>
  <li><a href="https://www.tuflow.com">TUFLOW webpage</a></li>
  <li><a href="https://www.lutraconsulting.co.uk/projects/mdal">MDAL and Mesh Layer</a></li>
  <li><a href="https://wiki.tuflow.com/index.php?title=TUFLOW_Viewer">TUFLOW Viewer QGIS Plugin</a></li>
</ul>

<p>Do you have any questions or would like to see a demo of the QGIS Mesh Layer? Contact us at <a href="mailto:info@lutraconsulting.co.uk">info@lutraconsulting.co.uk</a> or schedule a demo call <a href="https://calendly.com/saber-razmjooei/15min">calendly.com/saber-razmjooei/15min</a></p>

<h2 id="key-words">Key words</h2>
<p>QGIS, migration, optimised, speed up, fast, hydraulic modelling, water, 2D, 3D, open-source, cost reduction, software development,  TUFLOW, TUFLOW FV</p>

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
