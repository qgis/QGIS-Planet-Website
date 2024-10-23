---
source: "blog"
title: "Crayfish 2.3: New features"
date: "2016-07-15T09:00:00-0500"
link: "https://lutraconsulting.co.uk/blog/2016/07/15/crayfish-2-3/"
draft: "false"
showcase: "planet"
subscribers: ["lutragis"]
author: "Lutra Consulting"
tags: []
---

<p>Crayfish 2.3 is out with FLO-2D format support and automatic export of contours</p>

<!-- more -->

<h2 id="support-for-new-formats">Support for new formats</h2>

<p>We added support for <a href="http://www.flo-2d.com/" target="_blank">FLO-2D</a> result files.</p>

<p><img alt="FLO-2D format in Crayfish" src="https://www.lutraconsulting.co.uk/img/posts/flo2d_format.png" /></p>

<p><a href="http://www.wrf-model.org/index.php">Weather Research and Forecasting Model (WRF)</a> outputs are now fully supported in Crayfish.</p>

<h2 id="export-contours">Export contours</h2>
<p>Users can now directly generate vector contours from a Crayfish layer. The export-to-contour feature allows you to select type of contour (e.g. line or area contour) and contour intervals. A very handy option is that the current colour ramp can be also used for your contour intervals.</p>

<p><img alt="Exporting contours in Crayfish" src="https://www.lutraconsulting.co.uk/img/posts/export_contours.png" /></p>

<h2 id="processing-toolbox-crayfish-provider">Processing toolbox Crayfish provider</h2>

<p>We have incorporated many algorithms from Crayfish to processing toolbox (Export grid, Export mesh elements, …). To activate the Crayfish module, from the main menu, select <strong>Processing &gt; Options</strong> and in the new window, under <strong>Providers &gt; Crayfish algorithms</strong> select the option for <strong>Activate</strong>.</p>

<p><img alt="Exporting contours in Crayfish" src="https://www.lutraconsulting.co.uk/img/posts/crayfish_ptb.png" /></p>

<p>With the processing toolbox, user can create batch geo-processing algorithms to automate their work. For example, you can create a batch process using this module, to export several Crayfish grids to rasters.</p>

<p>Export to animation using the Processing Toolbox is not supported yet.</p>

<h2 id="future-developments">Future developments</h2>

<p>We’d like to add support for mesh generation and also mesh calculator. If these are something of you or your organisation interest and would like to contribute financially, feel free to get in touch.</p>

<p>For any problems or feedback, please consider to file a ticket <a href="https://github.com/lutraconsulting/qgis-crayfish-plugin/issues" title="Crayfish issues">here</a>.</p>

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
