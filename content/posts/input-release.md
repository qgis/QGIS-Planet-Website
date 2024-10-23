---
source: "blog"
title: "Input: a mobile app for surveying"
date: "2019-03-25T19:00:00-0500"
link: "https://lutraconsulting.co.uk/blog/2019/03/25/input-release/"
draft: "false"
showcase: "planet"
subscribers: ["lutragis"]
author: "Lutra Consulting"
tags: []
---

<p>We are pleased to announce the first public release of <a href="https://merginmaps.com/">Input</a>. Input is a <a href="https://github.com/lutraconsulting/input">Free and Open Source</a> mobile application built on top of QGIS.</p>

<p><a href="https://play.google.com/store/apps/details?id=uk.co.lutraconsulting&amp;utm_source=lutra-atom&amp;utm_medium=lutra-blog&amp;utm_campaign=input"><img alt="Get it on Google Play" src="https://play.google.com/intl/en_us/badges/images/generic/en_badge_web_generic.png" width="170" /></a></p>

<!-- more -->

<h2 id="why-input">Why Input?</h2>

<p><img alt="Input in action" src="https://www.lutraconsulting.co.uk/img/posts/input_capturing_points.png" /></p>

<p>Collecting data is often an essential part of a geo-data management workflow. The problems we have tried to resolve with <a href="https://merginmaps.com/">Input</a>:</p>

<ul>
  <li>
    <p>A mobile app: to collect the data. The app has an intuitive interface. Similar to Google Maps, you don’t need to read a whole bunch of documentation to be able to use the app.</p>
  </li>
  <li>
    <p>Data synchronisation: a collaborative way of managing the data. We provide <a href="https://merginmaps.com/">Mergin</a>, a central storage, where data administrators can upload their data/projects for their users to change in the field. Changes made to the data through <a href="https://merginmaps.com/">Input</a> will be tracked and can be uploaded to <a href="https://merginmaps.com/">Mergin</a>. Likewise, data administrators can propagate changes to their users by updating the files on <a href="https://merginmaps.com/">Mergin</a>.</p>
  </li>
</ul>

<h2 id="how-to-use-input">How to use Input?</h2>

<p>You can set up your projects in <a href="https://qgis.org">QGIS</a>. <a href="https://merginmaps.com/">Input</a> is based on QGIS, so it can read all data and services (e.g. Shapefile, Geopackage, TIF, WMS, XYZ tiles, WFS, etc) available in QGIS.</p>

<p>You can customise your forms and identify panel for the layers to be surveyed. <a href="https://merginmaps.com/">Input</a> uses <strong>Display</strong> tags and <strong>Map Themes</strong> to better view the data. For more information, see <a href="https://github.com/lutraconsulting/input/blob/master/docs/users/project_config.md">QGIS project configuration</a> of the user documentations.</p>

<p><img alt="Input in action" src="https://www.lutraconsulting.co.uk/img/posts/input_identify_path.png" /></p>

<p>You can then upload your data and projects to <a href="https://merginmaps.com/">Mergin</a> and share them with your users. Permissions to users to read/write the project can be granted through Mergin.</p>

<p>Input can be installed from <a href="https://play.google.com/store/apps/details?id=uk.co.lutraconsulting&amp;utm_source=lutra-atom&amp;utm_medium=lutra-blog&amp;utm_campaign=input">Google Play Store</a>. Users will be able to log in to the their <a href="https://merginmaps.com/">Mergin</a> account and download the projects.</p>

<p>Within the app, users can capture geometries (e.g. points, lines and polygons). Capturing of data can be free-hand, or it can be achieved by streaming the GPS locations and generating vertices.</p>

<p>Forms can be easily edited based on the widgets users have set up in the QGIS project. For example, you can add photos, notes, dates, etc to the digitised features.</p>

<p>Input keeps track of changes and you can upload the changes back to Mergin from within the app.</p>

<h2 id="feedback">Feedback</h2>

<p>If you’d like to use Input and Mergin within your enterprise environment, please contact us so that we can provide you with a dedicated hosting and no data limit.</p>
