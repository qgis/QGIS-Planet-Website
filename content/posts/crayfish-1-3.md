---
source: "blog"
title: "Crayfish 1.3: What's new!"
date: "2015-03-12T09:00:00-0500"
link: "https://lutraconsulting.co.uk/blog/2015/03/12/crayfish-1-3/"
draft: "false"
showcase: "planet"
subscribers: ["lutragis"]
author: "Lutra Consulting"
tags: []
---

<p>Crayfish is becoming the must-have QGIS plugin for those working with the <a href="http://www.xmswiki.com/wiki/SMS:Binary_Dataset_Files_*.dat" rel="nofollow" target="_blank">binary</a> and <a href="http://www.xmswiki.com/wiki/SMS:ASCII_Dataset_Files_*.dat" rel="nofollow" target="_blank">ascii</a> DAT/.2dm formats. Recently we had some requests from <a href="http://www.basement.ethz.ch/about" rel="nofollow" target="_blank">BASEMENT</a> users to fully support the file format of their modelling package.</p>

<p>We have also been busy beta-testing our new illuvis flood risk communication service. Crayfish 1.3 integrates the illuvis client, allowing users to interact easily with this flood risk mapping service.</p>

<p>Read on for a look at some of the new features in more detail...</p>

<!-- more -->

<h2 id="advanced-styling">Advanced Styling</h2>

<p>You can now turn off values below or above certain thresholds. This feature is very useful when you work with rainfall-runoff models and want to turn off values below e.g. 2 cm.</p>

<p><span><img src="https://www.lutraconsulting.co.uk/img/posts/crayfish_1_3_all_values.png" /></span>
<p><span><img src="https://www.lutraconsulting.co.uk/img/posts/crayfish_1_3_above_2cm.png" /></span>

You can now set your colour ramps once, save them and apply them to other layers.


Export to Geo-TIFF
------------------

<p>You can now easily export outputs from Crayfish to Geo-TIFF (.tif) files. Simply select the Quantity and Output time in the Crayfish viewer then right-click on the Crayfish layer in the QGIS Layers panel and select Export to grid...</p>

<center>
  
</center>

Export to illuvis
-----------------
<p>For those users who have been using illuvis, you can now upload crayfish layers directly to the flood map publishing web service rather than first having to convert results to Geo-TIFF. If you would like to become an illuvis beta-tester, please contact us.</p>


Support for BASEMENT
--------------------

Users can now view outputs from the BASEMENT modelling package.
<p><span><img src="https://www.lutraconsulting.co.uk/img/posts/crayfish_1_3_basement_support.png" /></span>


Binary package for Ubuntu
-------------------------
<p>We love Linux and have finally managed to prepare crayfish binaries for Ubuntu 14.04. If you are using other distros, the compilation should be straight-forward using guide in the <a href="https://github.com/lutraconsulting/qgis-crayfish-plugin/blob/master/README.md" rel="nofollow" target="_blank">README file.</a></p>


Problems
--------
If you have some feedback or come across a bug, feel free to file a ticket on the <a href="https://github.com/lutraconsulting/qgis-crayfish-plugin/issues" rel="nofollow" target="_blank">issues page</a> of the Crayfish github repository.


Sponsors
--------
We'd like to thank <a href="http://www.vaw.ethz.ch/index_EN" rel="nofollow" target="_blank">The Laboratory of Hydraulics, Hydrology and Glaciology (VAW) of ETH Zurich</a> for sponsoring some of the great features in this release.
 
</p></p></p>
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
