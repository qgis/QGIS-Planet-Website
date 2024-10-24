---
source: "blog"
title: "Google Summer of Code 2019 : QGIS 3D Improvements"
date: "2019-09-15T19:00:01-0500"
link: "https://lutraconsulting.co.uk/blog/2019/09/15/gsoc/"
draft: "false"
showcase: "planet"
subscribers: ["lutragis"]
author: "Lutra Consulting"
tags: []
---

<p>In this year Google Summer of Code (GSoC), there is a project involving QGIS 3D. <a href="https://ismailsunni.id">Ismail Sunni</a> as the student with Martin Dobias and Peter Petrik as the mentors
have implemented 3D On-Screen Navigation, 3D Measurement Tool and 3D Rendering Point Feature as A Billboard.</p>

<!-- more -->

<p>You can also learn more about this GSoC project <a href="https://ismailsunni.github.io/GSoC-2019/">here</a>.</p>

<h2 id="3d-on-screen-navigation">3D On-Screen Navigation</h2>

<p>Previously, user could already navigate the 3D world by using mouse and keyboard. Unfortunately, for a new user it is not easy
to start using them. 3D On-Screen Navigation will help navigating the 3D world. There are buttons to do zoom in/out, tilt up/down,
pan up/down/left/right, and rotate the 3D map view. This feature can be activated from the 3D map view toolbar. See how to use it
in this video:</p>

<center>
    
</center>

<h2 id="3d-measurement-tool">3D Measurement Tool</h2>

<p>Now you can measure distance in 3D map view with considering the z-value. This tool is available in the 3D map view toolbar.
It has the same UI as in 2D measurement tool with the same configuration (rubber band color, unit, decimal place,
and keeping the base unit). It also has the same behavior (left-click to add a new point, middle-click to delete
the last point, and right-click to restart the measurement). Now you can measure the distance between two building’s
top or length of a river in a mountain. See the 3D measurement tool in action:</p>

<center>
    
</center>

<h2 id="3d-point-feature-rendering-as-billboards">3D Point Feature Rendering As Billboards</h2>

<p>A new kind of rendering style has been added for point layers.
It allows you to show the point with QGIS symbol (e.g. marker, SVG, etc)
that always face to the user and always has the same size. You can see sample usage:</p>

<center>
  
</center>

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
