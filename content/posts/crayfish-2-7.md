---
source: "blog"
title: "Crayfish new release and future plan"
date: "2017-10-23T04:00:00-0500"
link: "https://lutraconsulting.co.uk/blog/2017/10/23/crayfish-2-7/"
draft: "false"
showcase: "planet"
subscribers: ["lutragis"]
author: "Lutra Consulting"
tags: []
---

<p>Crayfish 2.7 is out with grid calculator, new formats and several enhancements. This will likely to be the last version of Crayfish for QGIS 2.x. We have started a crowd-funding campaign to port Crayfish to QGIS 3.</p>

<!-- more -->

<h2 id="crayfish-for-qgis-32">Crayfish for QGIS 3.2</h2>
<p>Crayfish has grown over the past few years and now handles several file formats. There are various functions within the plugin to analyse and process the data too. Instead of porting the plugin directly to QGIS 3, we decided to refactor the code with the possibility of incorporating the renderer directly in QGIS core. We have started a crowd-funding campaign and hoping the software vendors and organisations who are benefiting from the plugin will fund the effort:</p>

<p>https://www.lutraconsulting.co.uk/crowdfunding/qgis-crayfish-3/</p>

<h2 id="grid-calculator">Grid calculator</h2>

<p>We have implemented a new grid calculator for Crayfish layer. Users can now perform various operations on one or multiple layers. The output can be filtered by time or spatially. In addition, we have added logical and aggregating operators. The result is currently saved as a <a href="http://www.xmswiki.com/wiki/SMS:Binary_Dataset_Files_*.dat">binary XMS</a> file. Read <a href="https://www.lutraconsulting.co.uk/projects/crayfish/wiki">Crayfish wiki page</a> for more details.</p>

<p><img alt="Grid calculator" src="https://www.lutraconsulting.co.uk/img/posts/crayfish_grid_calculator.png" /></p>

<h2 id="enhancements">Enhancements</h2>
<p>Here is a list of enhancements for this release:</p>
<ul>
  <li>Better handling netcdf time</li>
  <li>Resolving rendering issues with some file formats</li>
  <li>Better support for Hydro_AS-2D files</li>
  <li>Smoother area contour export</li>
</ul>

<h2 id="sponsors">Sponsors</h2>
<p>This release was funded by <a href="https://www.bmlfuw.gv.at/">Austrian Ministry of Agriculture, Forestry, Environment and Water Management</a></p>

<h2 id="feedback-and-bug-report">Feedback and bug report</h2>
<p>If you have any problem with Crayfish, please do not email us directly and consider filing a bug here: https://github.com/lutraconsulting/qgis-crayfish-plugin/issues</p>

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
