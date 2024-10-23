---
source: "blog"
title: "Visualising dam breach in QGIS"
date: "2016-03-06T10:00:00-0600"
link: "https://lutraconsulting.co.uk/blog/2016/03/06/visualising-dam-breach-in-qgis/"
draft: "false"
showcase: "planet"
subscribers: ["lutragis"]
author: "Lutra Consulting"
tags: []
---

<p>Recently, I have <a href="http://foreignpolicy.com/2016/02/03/will-italy-be-able-to-fix-the-worlds-most-dangerous-dam/">come across</a> the <a href="http://www.theguardian.com/world/2016/mar/02/mosul-dam-engineers-warn-it-could-fail-at-any-time-killing-1m-people">news</a> about extent of damage and human loss, in case of <a href="http://www.scienpress.com/Upload/GEO/Vol%205_3_8.pdf">the Mosul dam breach in Iraq</a>.</p>

<p>Having all the tools, some freely available data and a free weekend, I have decided to carry out my own analysis.</p>

<!-- more -->

<h1 id="data">Data</h1>

<p>For the Digital Elevation Model (DEM), I used the data from <a href="http://www.eorc.jaxa.jp/en/">JAXA Earth Observation Center (EORC)</a>.</p>

<p>The resolution of the DEM is approximately 30 metres. For more detailed analysis, a better dataset (e.g. LIDAR) would be ideal.</p>

<h1 id="methodology">Methodology</h1>

<p>I set up a 2-dimensional model with the following assumptions and parameters:</p>

<ul>
  <li>A square cell size (70 metres)</li>
  <li>The dam was assumed to be full</li>
  <li>Simulation time of 24 hours</li>
  <li>The breach would occur after the first hour (1:00 hour in to the model run)</li>
  <li>The dam would be completely breached after 1 hour (between 1:00 - 2:00 hour during the model run)</li>
</ul>

<h1 id="results">Results</h1>
<p>Using <a href="https://www.lutraconsulting.co.uk/projects/crayfish">Crayfish</a> plugin for QGIS, the results can be animated to see the on-set of the flooding.</p>

<center>
		
</center>

<p>Note, that the first hour of the model run was used to initialise the water level within the dam. Hence, for the actual flood travel time, one hour should be deducted from the timing shown towards the bottom right corner of the video.</p>

<p>Below, you can see the flood extent generated based on my calculations and the extent shown <a href="http://foreignpolicy.com/2016/02/03/will-italy-be-able-to-fix-the-worlds-most-dangerous-dam/">here</a> (red line in the main map) for Mosul.</p>

<center>
<a href="https://www.lutraconsulting.co.uk/img/posts/dam_breach_osm.png" rel="lightbox"><img src="https://www.lutraconsulting.co.uk/img/posts/dam_breach_osm_499.png" title="Example of label rules (Click to enlarge)" /></a>
<p class="caption">Maximum flood extent due to the breach of the upstream dam in Mosul. (Click to enlarge)</p>
</center>

<p><strong>Disclaimer</strong>: The calculation carried out for this demo was very approximate. Despite obtaining very similar results for Mosul compared to the original study, further checks and revisions are required.</p>

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
