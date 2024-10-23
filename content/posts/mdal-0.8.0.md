---
source: "blog"
title: "Overview of QGIS 3.16 LTR and QGIS 3.18 Mesh Features"
date: "2021-01-20T19:00:00-0600"
link: "https://lutraconsulting.co.uk/blog/2021/01/20/mdal-0.8.0/"
draft: "false"
showcase: "planet"
subscribers: ["lutragis"]
author: "Lutra Consulting"
tags: []
---

<p>QGIS Mesh Layer now support DHI dfsu and HECRAS 6.0 format.</p>

<!-- more -->

<p>The releases of QGIS 3.16 LTR/QGIS 3.18, MDAL 0.8.0 and Crayfish 3.5.0 are planned for 19 February 2021.
We are delighted to present the following improvements for the upcoming releases:</p>
<ul>
  <li>In-memory mesh datasets with persistence</li>
  <li>Multi identify tool for mesh</li>
  <li>Virtual dataset groups for mesh layer</li>
  <li>3D Mesh Layer Bug Fixes and speed optimizations</li>
  <li><a href="https://www.youtube.com/watch?v=E8o00xfH8CM&amp;feature=youtu.be">DHI’s dfsu</a> format support (QGIS 3.18 only)</li>
  <li><a href="https://www.hec.usace.army.mil/software/hec-ras/">HECRAS 6.0</a> format support</li>
</ul>

<p>If you’d like try the latest features, you can always install QGIS nightlies/master, which comes with all the latest features described in this blog post.</p>

<p>If you want to learn more about Mesh Layer in QGIS, <a href="https://www.lutraconsulting.co.uk/projects/mdal/">read more here…</a></p>

<h2 id="mesh-calculator-and-layer-improvements">Mesh Calculator and Layer Improvements</h2>

<p>The <a href="https://www.qgis.org/en/site/forusers/visualchangelog316/index.html#virtual-dataset-groups-for-mesh-layer">Virtual dataset groups for mesh layer</a> and 
<a href="https://www.qgis.org/en/site/forusers/visualchangelog316/index.html#in-memory-mesh-datasets-with-persistence">In-memory mesh datasets with persistence</a> 
improvements greatly improves the workflows when using the Mesh Calculator in QGIS. Users can store the 
intermediate results into virtual layers that are recalculated on the fly (similarly to QGIS expressions for 
vector layers). The layers can be later persisted to any supported MDAL formats with write capabilities.</p>

<p><a href="https://www.qgis.org/en/site/forusers/visualchangelog316/index.html#multi-identify-for-mesh-layer">Multi identify tool for mesh</a>
feature allows to browse the temporal mesh data in more intuitive way and includes the extra information 
about the Mesh datasets loaded.</p>

<p>These features were sponsored by <a href="https://www.arteliagroup.com/en">Artelia Group</a>.</p>

<h2 id="dhis-dfsu-format-support">DHI’s dfsu format support</h2>

<p>MDAL 0.8.0 supports loading of the external drivers. 
A first driver, available on Windows QGIS 3.18 only, is popular DFSU format by DHI, which is used to store MIKE 21 output results.</p>

<p>You can see how to configure and use QGIS to work with DFSU format on the <a href="https://www.youtube.com/watch?v=E8o00xfH8CM&amp;feature=youtu.be">DHI’s YouTube channel</a></p>

<p>Special thanks to the sponsor <a href="https://www.dhigroup.com">DHI</a> this feature.</p>

<h3 id="qgis">QGIS</h3>
<p>We have added the following new features to QGIS to convert between mesh and vector/raster:</p>
<ul>
  <li><a href="https://www.qgis.org/en/site/forusers/visualchangelog316/index.html#tin-mesh-creation">TIN Mesh creation</a></li>
  <li>Ported most of the processing algorithms from Crayfish to QGIS core</li>
  <li>3D rendering improvements</li>
  <li>Many Mesh Layer bugfixes</li>
</ul>

<h3 id="mdal">MDAL</h3>
<ul>
  <li>Support for external drivers.</li>
  <li>Fixed HECRAS vector datasets support</li>
  <li>Packaging in <a href="https://anaconda.org/conda-forge/mdal">conda</a></li>
</ul>

<h3 id="crayfish">Crayfish</h3>
<ul>
  <li>Fixed SAGA flow direction support</li>
  <li>Fixed FFMPEG download link</li>
  <li>Ported most of the processing algorithms from Crayfish to QGIS core</li>
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
