---
source: "blog"
title: "Crayfish 2.5: New features"
date: "2017-04-03T04:00:00-0500"
link: "https://lutraconsulting.co.uk/blog/2017/04/03/crayfish-2-5/"
draft: "false"
showcase: "planet"
subscribers: ["lutragis"]
author: "Lutra Consulting"
tags: []
---

<p>A new release of Crayfish is now available from QGIS plugin repo.</p>

<p>Here are the new features in more detail…</p>

<!-- more -->

<h2 id="trace-animation">Trace animation</h2>
<p>We have added support for live trace animation on QGIS canvas:</p>

<center>
  
</center>

<p>Please note that export to trace animation (as an avi file) is not supported yet. To change vector style to traces, please refer to the Crayfish manual.</p>

<h2 id="support-for-ugrid">Support for UGRID</h2>

<p><a href="https://github.com/ugrid-conventions/ugrid-conventions">UGRID</a> format for <a href="https://www.deltares.nl/en/">Deltares</a> modelling packages are now supported in Crayfish. In addition to 2D mesh, UGRID also supports 1D mesh. Support for 1D mesh is experimental in this release.</p>

<h2 id="flo-2d-hdf-format">FLO-2D HDF format</h2>
<p>In addition to ASCII FLO-2D files, Crayfish can handle binary HDF output from <a href="https://www.flo-2d.com/">FLO-2D</a>. Several bugs related to FLO-2D file format were also resolved.</p>

<h2 id="xdmf-format">XDMF format</h2>
<p>We are pleased to merge changes from <a href="https://www.fugro.com/">Furgo GeoConsulting</a> to support <a href="http://www.xdmf.org/index.php/Main_Page">XDMF</a> format. The new format supports on-the-fly loading of the data.</p>

<h2 id="sponsors">Sponsors</h2>
<p>The new and improved support for file formats for HDF5 and UGRID have been kindly sponsored by <a href="https://www.flo-2d.com/">FLO-2D</a> and <a href="https://www.deltares.nl/en/">Deltares</a>. We developed trace animation for fun.</p>

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
