---
source: "blog"
title: "Capturing geotagged photos with Input app"
date: "2021-04-20T04:00:00-0500"
link: "https://lutraconsulting.co.uk/blog/2021/04/20/photo-exif-input/"
draft: "false"
showcase: "planet"
subscribers: ["lutragis"]
author: "Lutra Consulting"
tags: []
---

<p>In this post, we will explore the new feature in the <a href="https://merginmaps.com/">Input app</a> which allows you to record and display photo’s geotag information (e.g. direction, longitude and latitude).</p>

<!-- more -->

<h2 id="photos-metadata">Photos’ metadata</h2>
<p>When users take photos in the field, they often would like to record extra information which can help convey a better understanding and awareness of the surroundings. Recent mobile devices allow users to record photo direction, location, time stamp, camera settings, etc when taking photos. This information is often optional or restricted by default (due to privacy) within the mobile settings.</p>

<p>For surveying and data collection, this information can add extra dimension and context. For example, if you are surveying a bat nesting, it is useful to know the directions of the photos you have taken. This will help identifying the site easily in the subsequent site visit.</p>

<p>Geotag information is also useful metadata to have attached to your photos. There are other GIS or non-GIS applications which can read and interoperate the information.</p>

<p>In the recent version of the <a href="https://merginmaps.com/">Input app</a>, we have added a feature which allows you record and display the geotag information. Combined with QGIS styling, you can create a very informative symbology to display the information while you are capturing it in the field.</p>

<h2 id="before-you-start">Before you start</h2>
<p>To be able to capture geotag information, you need to enable your <strong>Camera app</strong> to use location. For that:</p>

<ul>
  <li>
    <p>in Android, from <strong>Settings</strong> &gt; <strong>Apps and notifications</strong> &gt; (see all) <strong>Camera</strong> and under <strong>Permission</strong> ensure you allow <strong>Location</strong></p>

    <p><img alt="" src="https://www.lutraconsulting.co.uk/img/posts/exif_camera_android.png" /></p>
  </li>
  <li>
    <p>in iOS, from <strong>Settings</strong> &gt; <strong>Privacy</strong> &gt; <strong>Location Services</strong> &gt; <strong>Camera</strong> and the <strong>Precise Location</strong> is enabled.</p>

    <p><img alt="" src="https://www.lutraconsulting.co.uk/img/posts/exif_camera_iphone.png" /></p>
  </li>
</ul>

<h2 id="quick-start">Quick start</h2>
<p>If you want to record photos with directions as shown below, you can follow the following steps:</p>

<p><img alt="" src="https://www.lutraconsulting.co.uk/img/posts/exif_example_project.png" /></p>

<ul>
  <li>Log into <a href="https://merginmaps.com/">Mergin</a> (or <a href="https://merginmaps.com/">sign up</a> if you have not yet registered)</li>
  <li>Brows to <a href="https://merginmaps.com/projects/lutraconsulting/photo_survey/tree">photo survey project</a></li>
  <li>On the top right-click on <strong>Clone</strong> to make a copy of your project in your account. You can choose a different project name:</li>
</ul>

<p><img alt="" src="https://www.lutraconsulting.co.uk/img/posts/exif_clone_project_in_mergin.png" /></p>

<ul>
  <li>
    <p>Download and install the <a href="https://merginmaps.com/">Input app</a></p>
  </li>
  <li>
    <p>Select <strong>My projects</strong> and log in using your Mergin credentials</p>
  </li>
  <li>
    <p>Download the newly created project from the earlier step</p>
  </li>
  <li>
    <p>Start recording points and add photos, you should see photo direction</p>
  </li>
</ul>

<h2 id="more-details">More details</h2>

<p>The project configuration is done in QGIS. The form has been set up to allow you take photos using Attachment widget. To learn more about different form edit tools in Input app and how to set the up in QGIS, see the <a href="https://merginmaps.com/docs/howto/project/settingup_forms">Input app help pages</a>.</p>

<p>There are multiple fields to extract geotag information from the photo, as soon as you add the photo either using the camera or the gallery:</p>

<ul>
  <li>Direction: <code class="highlighter-rouge">read_exif_img_direction(@project_home + '/' + "photo")</code></li>
  <li>Latitude: <code class="highlighter-rouge">read_exif_latitude(@project_home + '/' + "photo")</code></li>
  <li>Longitude: <code class="highlighter-rouge">read_exif_longitude(@project_home + '/' + "photo")</code></li>
</ul>

<p>As noted, all the above functions take the path to the photo (<code class="highlighter-rouge">@project_home + '/' + "photo"</code>) and return different metadata related to the image.</p>

<p>In addition to the form, the layer styling has been modified to resemble the direction of the camera and field of view.</p>

<p>To set the camera icon and direction of the camera:</p>

<ul>
  <li>For the point styling, select <strong>SVG Marker</strong></li>
  <li>From the list of SVGs, select the camera icon. (ensure to embed the SVG to the project, otherwise it will appear as a question mark in the Input app.)</li>
  <li>For the <strong>Rotation</strong>, select <strong>direction</strong> field</li>
</ul>

<p>To add field of view:</p>

<ul>
  <li>Add another symbol layer to your point</li>
  <li>For <strong>Symbol layer type</strong> select <strong>Geometry Generator</strong></li>
  <li>For <strong>Geometry type</strong> select <strong>Polygon / MultiPolygon</strong></li>
  <li>For the expression, type:
<code class="highlighter-rouge">wedge_buffer(center:=$geometry,azimuth:= "direction",width:=45,outer_radius:=0.0008)</code></li>
  <li>For <strong>Symbol layer type</strong>, select <strong>Shapeburst Fill</strong></li>
</ul>

<p><img alt="" src="https://www.lutraconsulting.co.uk/img/posts/exif_layer_styling.png" /></p>

<h2 id="feedback-and-suggestions">Feedback and suggestions</h2>

<p><a href="https://merginmaps.com">Input, a field data collection app based on QGIS</a>. Input makes field work easy with its simple interface and cloud-based sync. Available on Android and iOS.</p>

<p><img alt="Screenshots of the Input App for Field Data Collection" src="https://www.lutraconsulting.co.uk/img/posts/input_app_for_field_data_collection.jpg" /></p>

<p><a href="https://play.google.com/store/apps/details?id=uk.co.lutraconsulting&amp;utm_source=lutra-atom&amp;utm_medium=lutra-blog&amp;utm_campaign=input"><img alt="Get it on Google Play" src="https://play.google.com/intl/en_us/badges/images/generic/en_badge_web_generic.png" width="180px" /></a><a href="https://apps.apple.com/us/app/input/id1478603559?ls=1&amp;utm_source=lutra-atom&amp;utm_medium=lutra-blog&amp;utm_campaign=input"><img alt="Get it on Apple store" src="https://www.lutraconsulting.co.uk/img/posts/App_Store.svg" style="padding-top: 0px;" width="144px" /></a></p>

<p>If you would like to add a new feature  or suggestions to improve the app, do not hesitate to contact us on info@lutraconsulting.co.uk</p>
