---
source: "blog"
title: "Editing raster cell values in QGIS using Serval plugin"
date: "2016-09-05T09:00:00-0500"
link: "https://lutraconsulting.co.uk/blog/2016/09/05/serval/"
draft: "false"
showcase: "planet"
subscribers: ["lutragis"]
author: "Lutra Consulting"
tags: []
---

<p>Users can directly edit raster cell values using Serval plugin in QGIS.</p>

<!-- more -->

<h2 id="how-to-use-serval">How to use Serval</h2>

<p>Serval is available from QGIS plugin repository. Note that you will need to restart QGIS if you upgrade Serval from an earlier version.</p>

<p>Once installed, Serval functions and settings will be available from the toolbar.</p>

<p><img alt="Serval Toolbar in QGIS" src="https://www.lutraconsulting.co.uk/img/posts/serval_toolbar.png" /></p>

<p>Serval supports Undo/Redo for editing values of raster. But it is recommended to make a copy of your raster.</p>

<p>Currently, the following functionalities are available:</p>

<ul>
  <li><img alt="Probe mode" src="https://www.lutraconsulting.co.uk/img/posts/serval_probe.png" /> Displays raster bands values in boxes.</li>
  <li><img alt="Draw mode" src="https://www.lutraconsulting.co.uk/img/posts/serval_draw.png" /> Draw/Edit mode: bands values can be modified in the boxes and written to the current raster cell by hitting the Enter key. In this mode the values will be also assigned to any other raster cell clicked by user.</li>
  <li><img alt="Write nodata" src="https://www.lutraconsulting.co.uk/img/posts/serval_write_nodata.png" /> To replace a cell value with the NODATA value.</li>
  <li><img alt="Define nodata" src="https://www.lutraconsulting.co.uk/img/posts/serval_define_nodata.png" /> To define or replace the NODATA value.</li>
  <li><img alt="Color picker" src="https://www.lutraconsulting.co.uk/img/posts/serval_color_picker.png" /> To pick a color using QGIS color picker (3-bands rasters only).</li>
  <li><img alt="Undo" src="https://www.lutraconsulting.co.uk/img/posts/serval_undo.png" /> <img alt="Redo" src="https://www.lutraconsulting.co.uk/img/posts/serval_redo.png" /> To Undo/Redo the cell edit. Edits history is saved separately for each raster, that is, undo/redo is always done for current raster layer.</li>
</ul>

<h2 id="future-developments">Future developments</h2>

<p>We’d like to add support to edit values using spatial and expression selection tools.</p>

<p>For any problems or feedback, please consider to file a ticket <a href="https://github.com/erpas/serval/issues" title="Serval issues">here</a>.</p>

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
