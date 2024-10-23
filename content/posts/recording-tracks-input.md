---
source: "blog"
title: "Recording tracks using QGIS and Input app"
date: "2020-03-26T04:00:00-0500"
link: "https://lutraconsulting.co.uk/blog/2020/03/26/recording-tracks-input/"
draft: "false"
showcase: "planet"
subscribers: ["lutragis"]
author: "Lutra Consulting"
tags: []
---

<p>In this post, we will use <a href="https://merginmaps.com/">Input app</a> to record tracks. The first step is to set up a project in QGIS.</p>

<!-- more -->

<h2 id="quick-recap">Quick recap</h2>
<p>In the previous <a href="https://www.lutraconsulting.co.uk/blog/2020/02/14/survey-qgis-input/">tutorial</a>, we set up a simple QGIS project and transferred it to our devices using the <a href="https://merginmaps.com/">Mergin</a> service.</p>

<p>In this tutorial we are going to set up a new survey project with more advanced features:</p>

<ul>
  <li>Forms with more options</li>
  <li>Different background layers (aerial imagery and street map)</li>
  <li>Using different geometry type of survey layer</li>
  <li>Exploring other <a href="https://merginmaps.com/">Input app</a> functions</li>
</ul>

<h2 id="software-needed">Software needed</h2>
<p>To start with, you will need to install the following software applications:</p>
<ul>
  <li><a href="https://www.lutraconsulting.co.uk/blog/categories/qgis/www.qgis.org">QGIS</a> - for your PC/laptop: <a href="https://qgis.org/en/site/forusers/download.html">download</a> and install QGIS if you have not already done so</li>
  <li><a href="https://merginmaps.com/">Input app</a> - for your mobile table: you can download the app from <a href="https://play.google.com/store/apps/details?id=uk.co.lutraconsulting&amp;utm_source=lutra-atom&amp;utm_medium=lutra-blog&amp;utm_campaign=input">Google Play Store</a> or <a href="https://apps.apple.com/us/app/input/id1478603559?ls=1&amp;utm_source=lutra-atom&amp;utm_medium=lutra-blog&amp;utm_campaign=input">Apple’s App Store</a></li>
</ul>

<p>In addition, you will need to register with the <a href="https://merginmaps.com/">Mergin</a> service. The <a href="https://merginmaps.com/">Mergin</a> service allows you to transfer data between your PC/laptop and mobile/table via the cloud. Note that after signing up to the <a href="https://merginmaps.com/">Mergin</a> service, you have to activate the account by clicking on the link sent to your email.</p>

<h2 id="configuring-qgis-project">Configuring QGIS project</h2>

<p>Similar to the previous <a href="https://www.lutraconsulting.co.uk/blog/2020/02/14/survey-qgis-input/">tutorial</a>, we are going to start with a blank QGIS project. All the data and the project will be stored locally on a folder called <strong>recording tracks</strong>.</p>

<p>First, start a QGIS project and add the <strong>OpenStreetMap</strong> layer under <strong>XYZ Tiles</strong>. You can add also add <a href="https://gis.stackexchange.com/a/217670">aerial imagery</a> as an XYZ layer to your QGIS.</p>

<p><img alt="Project setup" src="https://www.lutraconsulting.co.uk/img/posts/track-qgis-project.png" /></p>

<p>Save your project as <strong>tracks</strong> in the <strong>recording tracks</strong> folder.</p>

<p>In addition, we need to create a <strong>Geopackage</strong> survey layer. Below are the attribute columns for your survey layer. Also note that need to select <strong>Line</strong> as geometry type.</p>

<p>To create a survey layer, in QGIS, from the main menu select <strong>Layer &gt; Create Layer &gt; New Geopackage Layer …</strong>. A new window will appear:</p>

<p>For <strong>Database</strong> click on <strong>…</strong> and select the <strong>recording tracks</strong> folder then type <strong>survey.gpkg</strong> for the name of your database.</p>

<p>For <strong>Table name</strong>, type <strong>tracks</strong>.</p>

<p>For <strong>Geometry type</strong>, select <strong>Line</strong>.</p>

<p>You can select the option to <strong>Include Z dimension</strong>. The upcoming version of <a href="https://merginmaps.com/">Input app</a> supports capturing altitude from your device (or external GPS device tethered with your phone/tablet).</p>

<p>For Coordinate Reference System (CRS), select <strong>WGS 84 / Pseudo-Mercator EPSG:3857</strong>.</p>

<p>Add the following <strong>Fields</strong>. Note, different field types:</p>

<ul>
  <li><strong>Type</strong> field type as <strong>text</strong></li>
  <li><strong>Public</strong> field type as <strong>Boolean</strong> or bool</li>
  <li><strong>Photo</strong> field type as <strong>text</strong></li>
  <li><strong>Date</strong> field type as <strong>Date &amp; time</strong></li>
</ul>

<p><img alt="Geopackage survey layer" src="https://www.lutraconsulting.co.uk/img/posts/track-survey-layer.png" /></p>

<p>Click OK to create and add the layer to your QGIS session.</p>

<h2 id="styling-layers-and-setting-up-forms">Styling layers and setting up forms</h2>

<p>We are going to style the <strong>tracks</strong> layer based on <strong>Type</strong> field and use four categories:</p>
<ul>
  <li>Footpath</li>
  <li>Byway</li>
  <li>Cycle path</li>
  <li>Bridle way</li>
</ul>

<p>In the <strong>Layer Panels</strong> right-click on <strong>tracks</strong> layer and select <strong>Properties</strong>. A new window will appear. From the left panel, select <strong>Symbology</strong>. Change the styling from <strong>Single</strong> to <strong>Categorized</strong> on the top left section of the window. For the <strong>Value</strong>, select <strong>Type</strong> from the drop-down menu.</p>

<p>In the bottom-left section of the window, click on <strong>Classify</strong>. Then add 4 classes (by adding the green plus adjacent to <strong>Classify</strong>) for track types. In addition, we can add another class for <strong>Other</strong> types. Adjust the colours and line style accordingly:</p>

<p><img alt="Setting up style" src="https://www.lutraconsulting.co.uk/img/posts/track-style-layer.png" /></p>

<p>To set up the form, select <strong>Attribute forms</strong> from the left panel of the layer properties window. Adjust the <strong>Widget type</strong> as below:</p>

<ul>
  <li>For <strong>fid</strong>, select <strong>Hidden</strong></li>
  <li>For <strong>Type</strong>, select <strong>Value map</strong> and add the 5 categories (Footpath, Byway, Cycle path, Bridle way and Other) for <strong>Value</strong> and <strong>Description</strong> section (see image below)</li>
  <li>For <strong>Public</strong>, select <strong>Checkbox</strong></li>
  <li>For <strong>Photo</strong>, select <strong>Attachment</strong> and select the option for <strong>Relative path</strong></li>
  <li>For <strong>Date</strong>, select <strong>Date/Time</strong></li>
</ul>

<p><img alt="Setting up forms" src="https://www.lutraconsulting.co.uk/img/posts/track-forms-layer.png" /></p>

<p><a href="https://merginmaps.com/">Input app</a> allows you to have a custom pop-up drawer window when you tap on feature. To customise that, you can change the <strong>Display</strong> settings under the layer properties window. For <strong>Display name</strong> select <strong>Type</strong> and in the <strong>HTML Map Tip</strong> section type:</p>

<p><code class="highlighter-rouge"># image
file:///[%@project_folder%]/[% "Photo" %]</code></p>

<p><img alt="Custom pop-up" src="https://www.lutraconsulting.co.uk/img/posts/track-popup-layer.png" /></p>

<h2 id="setting-up-map-themes">Setting up map themes</h2>
<p>We can set up two different map themes: one with aerial imagery and one with street map. To do that, ensure you have only the following layers are set to visible in your layer panel:</p>
<ul>
  <li>tracks</li>
  <li>Aerial images</li>
</ul>

<p><img alt="Layer visibility" src="https://www.lutraconsulting.co.uk/img/posts/track-theme-ap1.png" /></p>

<p>On top of the layers panel, select <strong>Manage Map Themes</strong> &gt; <strong>Add Theme …</strong></p>

<p><img alt="Creating a new theme" src="https://www.lutraconsulting.co.uk/img/posts/track-theme-ap2.png" /></p>

<p>A new window will appear. Type <strong>Aerial photo</strong> for the name of your map theme and press OK.</p>

<p>Now, turn off your <strong>Aerial images</strong> layer in the layer panel and turn on the <strong>OpenStreetMap</strong> layer:</p>

<p><img alt="OSM theme in QGIS" src="https://www.lutraconsulting.co.uk/img/posts/track-theme-osm.png" /></p>

<p>You can now add a new map theme and call it <strong>Street map</strong>.</p>

<p>Save your project and transfer your data and project to your phone through the <a href="https://merginmaps.com/">Mergin</a> service as described in the previous <a href="https://www.lutraconsulting.co.uk/blog/2020/02/14/survey-qgis-input/">tutorial</a>.</p>

<p>If you missed a step, you can see the final version of the project <a href="https://merginmaps.com/projects/saber/Tracks/tree">here</a>. You can also skip the above section by cloning the project in the above link.</p>

<h2 id="recording-tracks-using-input-app">Recording tracks using Input app</h2>
<p>In <a href="https://merginmaps.com/">Input app</a>, download and open <strong>Tracks</strong> project.</p>

<p><img alt="Downloading a project" src="https://www.lutraconsulting.co.uk/img/posts/tracks-input-project.png" /></p>

<p><img alt="Map view in Input" src="https://www.lutraconsulting.co.uk/img/posts/tracks-input-map.png" /></p>

<p>You can easily change between different map themes in Input, by going to <strong>(… More) &gt; Map Themes</strong>:</p>

<p><img alt="Selecting theme in Input" src="https://www.lutraconsulting.co.uk/img/posts/tracks-input-themes.png" /></p>

<p><img alt="OSM map theme" src="https://www.lutraconsulting.co.uk/img/posts/tracks-input-osm.png" /></p>

<p>To capture tracks, press <strong>Record</strong> button in the lower panel in Input. A green cross will appear, centred on your GPS location. You can capture a line in two different methods:</p>

<ul>
  <li>Adding points to form the line by moving the map and pressing <strong>Add Point</strong></li>
  <li>Streaming GPS location while moving to form a line. To do that, press and hold <strong>GPS</strong> icon on the bottom left of your screen (see image below)</li>
</ul>

<p><img alt="Streaming GPS" src="https://www.lutraconsulting.co.uk/img/posts/tracks-input-stream.png" /></p>

<p>You can change the frequency of adding points when streaming GPS location, under <strong>Settings</strong> in Input. Also note that the GPS streaming can be done for polygon survey layer.</p>

<p>Once you finished capturing the track, press <strong>Done</strong> and you will be presented with a form:</p>

<p><img alt="Forms" src="https://www.lutraconsulting.co.uk/img/posts/tracks-input-form.png" /></p>

<p>You can easily fill the form using the drop-down menu for <strong>Type</strong> and checkbox option for <strong>Public</strong>.</p>

<p>By tapping on tracks on the map, you will should be able to see a small preview window presenting <strong>Type</strong> and <strong>Photo</strong>:</p>

<p><img alt="Preview panel" src="https://www.lutraconsulting.co.uk/img/posts/tracks-input-preview.png" /></p>

<p>After completion of the survey, you can synchronise your data back through the <a href="https://merginmaps.com/">Mergin</a> and see the results in QGIS desktop.</p>
