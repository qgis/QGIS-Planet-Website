---
source: "blog"
title: "FOSS4GUK Workshop: Collecting data with QGIS, Input and Mergin"
date: "2019-09-19T19:00:01-0500"
link: "https://lutraconsulting.co.uk/blog/2019/09/19/foss4guk/"
draft: "false"
showcase: "planet"
subscribers: ["lutragis"]
author: "Lutra Consulting"
tags: []
---

<p>During FOSS4GUK 2019 in Edinburgh we ran a workshop for collecting data using <a href="https://merginmaps.com">Input</a>. This is the content of the workshop with all the datasets.</p>

<!-- more -->

<h2 id="prerequisites">Prerequisites</h2>

<p>To be able to work with Input, you will need the following:</p>

<ul>
  <li><strong>QGIS</strong> <strong>Desktop</strong>: download the latest (LTR) version of QGIS for
your laptop here:
<a href="https://qgis.org/en/site/forusers/download.html"><em>https://qgis.org/en/site/forusers/download.html</em></a></li>
  <li><strong>The Input app</strong>: from your mobile/tablet, visit
<a href="https://merginmaps.com"><em>https://merginmaps.com</em></a> to install the app on
your device. If you are an iOS user, Input runs under TestFlight
which you will need to install first.</li>
  <li><strong>A Mergin account</strong>: visit
<a href="https://merginmaps.com/"><em>https://merginmaps.com/</em></a>
and sign up for a Mergin account.</li>
  <li><strong>QGIS Mergin Plugin</strong> (optional, covered later)</li>
</ul>

<h2 id="setting-up-the-survey-project">Setting up the survey project</h2>

<p>For the purpose of this workshop, we have prepared a QGIS project. Let’s
use that as a starting point:</p>

<ul>
  <li>Log into Mergin</li>
  <li>In the top-left, click on Projects and select Explore</li>
  <li>Find and click on saber/foss4guk</li>
  <li>In the top panel, click on the <img alt="mergin_clone" src="https://www.lutraconsulting.co.uk/img/posts/mergin_clone.png" /> icon to create a copy of the project under your own
Mergin account (foss4guk_YOURNAME)</li>
</ul>

<h2 id="exploring-the-project-in-qgis">Exploring the project in QGIS</h2>

<p>The project you have copied in Mergin, is a QGIS project with various
map layers. To see the content of the project in QGIS:</p>

<ul>
  <li>
    <p>In Mergin, in the top menu, select Projects &gt; My projects</p>
  </li>
  <li>
    <p>Select foss4guk_YOURUSERNAME (or the name you assigned when copying
the project).</p>
  </li>
  <li>
    <p>In the top menu, click on
the <img alt="mergin_download" src="https://www.lutraconsulting.co.uk/img/posts/mergin_download.png" /> icon to download the project</p>
  </li>
  <li>
    <p>Extract the content of the zip file</p>
  </li>
</ul>

<p>Alternatively:</p>

<p>The above process can be done through the Mergin plugin for QGIS. To do
that:</p>

<ul>
  <li>
    <p>Install the Mergin plugin in QGIS</p>
  </li>
  <li>
    <p>Restart QGIS</p>
  </li>
  <li>
    <p>In the QGIS Browser panel, right-click on Mergin and select Configure</p>
  </li>
  <li>
    <p>Enter your Mergin username and password</p>
  </li>
  <li>
    <p>Under My Project, right-click on foss4guk_YOURUSERNAME and select
Download</p>
  </li>
  <li>
    <p>Select a location under which the project will be downloaded to</p>
  </li>
  <li>
    <p>Once downloaded, select Open to open the project.</p>
  </li>
</ul>

<h2 id="layer-settings-and-forms">Layer settings and forms</h2>

<p>Input is based on QGIS, therefore, any layer symbology / styles you set
in QGIS, will be displayed in Input. If you are using SVGs (e.g. OS
MasterMap), you need to embed these in the QGIS project.</p>

<p>Input also supports most of the edit widgets from QGIS. Edit widgets
allow you to simplify filling-in forms with drop-down options,
TRUE/FALSE switches, sliders, calendar and time, default values,
attachments, value relations and more. To see some of those settings:</p>

<ul>
  <li>
    <p>From the Layers panel (in QGIS), right-click on the listed buildings
(points layer) and open the Properties window.</p>
  </li>
  <li>
    <p>From the left-hand panel, select Attributes Form. Explore the various
widgets assigned to different fields.</p>
  </li>
</ul>

<p>For this layer, we have set the <strong>Photo</strong> field to use an <strong>Attachment widget</strong>.
This will allow Input to make use of your mobile camera to attach photos
to features.</p>

<p>For the Surveyor field, we have linked it to an external CSV table, to
populate a drop-down option with the names of surveyors.</p>

<p>Input can also use a pop-up window (similar to Google Maps) to display
basic information about a single feature:</p>

<p align="center">
    <img src="https://www.lutraconsulting.co.uk/img/posts/input_edn_001.png" />
  </p>

<p>To customise this pop window’s content:</p>

<ul>
  <li>
    <p>Open the properties table, and select the Display tab</p>
  </li>
  <li>
    <p>You can see the title is set to <strong>ENT_TITLE</strong> and there is an image tag
referencing the Photo field:</p>
    <div class="highlighter-rouge"><div class="highlight"><pre class="highlight"><code>  # image
  file:///[%@project_folder%]/[% "Photo" %]
</code></pre></div>    </div>
  </li>
</ul>

<h2 id="map-themes">Map themes</h2>

<p>To simplify handling layer visibility, Input makes use of map themes
defined in your QGIS project. In this project, there is a map theme for
aerial photo (using a Bing aerial layer) and OpenStreetMap (geopackage).</p>

<p>[]{#anchor-5}Survey layer</p>

<p>In Input, any vector layer (point, line, polygon) can be edited (as long
as editing that format is supported in QGIS). This could be very
confusing when dealing with large numbers of vector layers in a single
project (trying to figure out which one to edit).</p>

<p>Luckily you can set background layers (or those you don’t want to be
editable in Input) to read-only:</p>

<ul>
  <li>
    <p>In QGIS, from the main menu, select Project &gt; Properties</p>
  </li>
  <li>
    <p>In the new window, select the Data Sources tab from the left-hand
panel</p>
  </li>
</ul>

<p>Below is the list of layers and their capability settings for the
project. Layers <strong>not marked as read-only</strong> will be shown as survey
layers (editable) in Input.</p>

<p align="center">
  <img src="https://www.lutraconsulting.co.uk/img/posts/qgis_project_properties.png" />
</p>

<p>By default, the file paths to layers are relative. You can change that
under the General tab of this window.</p>

<h2 id="using-input">Using Input</h2>

<p>To use Input, open the app on your device. On its first run, Input will
show the Projects page.</p>

<ul>
  <li>Under Projects, select My projects</li>
  <li>From the list, find YOUR_Mergin_USERNAME/foss4guk_YOURUSERNAME
(e.g. saber/foss4guk_saber)</li>
  <li>Tap the download icon on the right-hand side of the project to
download the project (warning: if you are not connected to WiFi, this
will use some of your mobile data allowance)</li>
  <li>After downloading, tap Home</li>
  <li>Select your downloaded project</li>
</ul>

<p align="center">
  <img src="https://www.lutraconsulting.co.uk/img/posts/input_edn_002.png" />
</p>

<p>When you open the project, you may not see all layers. This is because
some of the layers have zoom-dependant visibility settings (again
configured in QGIS).</p>

<h2 id="exploring-the-project">Exploring the project</h2>

<p>To switch map themes:</p>

<ul>
  <li>
    <p>Tap More on the bottom-right side of the screen</p>
  </li>
  <li>
    <p>Tap Map themes &gt; aerial photo</p>
  </li>
</ul>

<p align="center">
  <img src="https://www.lutraconsulting.co.uk/img/posts/input_edn_003.png" />
</p>

<p>You can also display feature details simply by tapping on them.</p>

<ul>
  <li>Tap on the point representing Queensberry House:</li>
</ul>

<p align="center">
  <img src="https://www.lutraconsulting.co.uk/img/posts/input_edn_004.png" />
</p>

<h2 id="capturing-data">Capturing data</h2>

<p>To capture data:</p>

<ul>
  <li>
    <p>Tap <strong>Record</strong></p>
  </li>
  <li>
    <p>You can then choose the layer in which you want to record your
feature, by tapping on the light green band, in the lower part of the
screen, above the Input menu.</p>
  </li>
  <li>
    <p>If you are capturing a point, by default, the suggested point to
capture will be on your GPS location. You can drag the map to adjust the
location of the new point. To switch back to the current GPS location,
tap the GPS icon on the bottom-left of your screen.</p>
  </li>
  <li>
    <p>After adding a point, you will be prompted to fill-in the form.</p>
  </li>
</ul>

<p>If you are recording a line or a polygon, you can either add points to define
the shape of your feature or <strong>press and hold the GPS icon when in
Record mode</strong> to generate a shape from your GPS track.</p>

<h2 id="editing-data">Editing data</h2>

<p>You can edit the existing features on your map. For point layers, you
can edit geometry and form data. For lines and polygons, you can edit
only the form data.</p>

<h2 id="try-it">Try it!</h2>

<p>Let’s get out and capture some data for the Path layer!</p>

<h2 id="uploading-your-changes">Uploading your changes</h2>

<p>Once you have made changes to your data, you can upload them back to
Mergin:</p>

<ul>
  <li>
    <p>In Input, tap Projects</p>
  </li>
  <li>
    <p>Select My projects</p>
  </li>
  <li>
    <p>Click on the sync/refresh icon to the right of your project</p>
  </li>
</ul>

<p>You can now download the project again to your desktop and see the
changes in QGIS. Alternatively, you can synchronise the changes you made
back to QGIS by using the Mergin plugin for QGIS (described earlier).</p>
