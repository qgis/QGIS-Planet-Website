---
source: "blog"
title: "Collecting data using QGIS and Input app"
date: "2020-02-14T02:00:00-0600"
link: "https://lutraconsulting.co.uk/blog/2020/02/14/survey-qgis-input/"
draft: "false"
showcase: "planet"
subscribers: ["lutragis"]
author: "Lutra Consulting"
tags: []
---

<p>In this post, we will walk you through basic steps to set up a survey project in QGIS desktop and using it in <a href="https://merginmaps.com/">Input app</a> to collect data in field using your Android or iPhone/iPad device.</p>

<!-- more -->

<h2 id="software-needed">Software needed</h2>
<p>To start with, you will need to install the following software applications:</p>
<ul>
  <li><a href="https://www.lutraconsulting.co.uk/blog/categories/qgis/www.qgis.org">QGIS</a> - for your PC/laptop: <a href="https://qgis.org/en/site/forusers/download.html">download</a> and install QGIS if you have not already done so</li>
  <li><a href="https://merginmaps.com/">Input app</a> - for your mobile table: you can download the app from <a href="https://play.google.com/store/apps/details?id=uk.co.lutraconsulting&amp;utm_source=lutra-atom&amp;utm_medium=lutra-blog&amp;utm_campaign=input">Google Play Store</a> or <a href="https://apps.apple.com/us/app/input/id1478603559?ls=1&amp;utm_source=lutra-atom&amp;utm_medium=lutra-blog&amp;utm_campaign=input">Apple’s App Store</a></li>
</ul>

<p>In addition, you will need to register with the <a href="https://merginmaps.com/">Mergin</a> service. The <a href="https://merginmaps.com/">Mergin</a> service allows you to transfer data between your PC/laptop and mobile/table via the cloud. Note that after signing up to the <a href="https://merginmaps.com/">Mergin</a> service, you have to activate the account by clicking on the link sent to your email.</p>

<h2 id="configuring-qgis-project">Configuring QGIS project</h2>

<p>To be able to survey data, we need to set up a project in QGIS. Usually, you will need some data for your background layer (so that you can locate yourself!). In addition, you need to set up a table (or layer), to store your survey information.</p>

<p>For background data, we are going to use Open Street Map. For survey table, we need to decide on a form structure and the type of feature you want to survey (e.g. point of interest, tracks or parcel of land). In this case, we want to survey potholes. Also, it would be good to attach some notes for each pothole, take a photo of it and add a date for survey. The GIS format best suited to store spatial information, is Geopackage.</p>

<p>Let’s start by opening QGIS and add the above layers to our project. To simplify things, we can create a folder on Desktop (referred to in this tutorial as <strong>data collection</strong> folder) and store everything there.</p>

<p>Open QGIS from your PC/laptop. From the <strong>Browser panel</strong> (usually located on the top left side), expand <strong>XYZ Tiles</strong> and double-click on <strong>OpenStreetMap</strong> to add it to QGIS:
<img alt="QGIS" src="https://www.lutraconsulting.co.uk/img/posts/input_basic_qgis.png" /></p>

<p><img alt="Browser panel in QGIS" src="https://www.lutraconsulting.co.uk/img/posts/input_basic_qgis_browser.png" /></p>

<p>You should see the OSM layer:</p>

<p><img alt="Adding OSM XYZ layer" src="https://www.lutraconsulting.co.uk/img/posts/input_basic_qgis_osm.png" /></p>

<p>Save your project as <strong>pothole survey</strong> in the <strong>data collection</strong> folder.</p>

<p>To create a survey layer, in QGIS, from the main menu select <strong>Layer &gt; Create Layer &gt; New Geopackage Layer …</strong>. Note that Geopackage is a file based database where you can store multiple tables (spatial or non-spatial). A new window will appear:</p>

<p><img alt="Creating a geodatabase" src="https://www.lutraconsulting.co.uk/img/posts/input_basic_gpkg-1.png" /></p>

<p>For <strong>Database</strong> click on <strong>…</strong> and select the <strong>data collection</strong> folder on your Desktop and then type <strong>survey-db.gpkg</strong> for the name of your database.</p>

<p>For <strong>Table name</strong>, type <strong>Potholes</strong>.</p>

<p>For <strong>Geometry type</strong>, select <strong>Point</strong>.</p>

<p>For Coordinate Reference System (CRS), click on the icon to the right of <strong>EPSG:4326 - WGS84</strong>. A new window will appear. Under <strong>Filter</strong> section on the top of the window, type: <strong>3857</strong> and under <strong>Predefined Coordinate Reference Systems</strong>, select <strong>WGS 84 / Pseudo-Mercator EPSG:3857</strong>. Then click OK.</p>

<p><img alt="Assigning CRS" src="https://www.lutraconsulting.co.uk/img/posts/input_basic_gpkg-2.png" /></p>

<p>We can now create the column headers for our table under <strong>New Field</strong> section. For this form, we want to create the following columns to store data: <strong>Date, Notes, Photo</strong></p>

<p>For <strong>Name</strong>, type <strong>Date</strong></p>

<p>For <strong>Type</strong>, select <strong>Date</strong></p>

<p>Click on <strong>Add to Field lists</strong> to add your column.</p>

<p>Repeat the same process for <strong>Notes</strong> and <strong>Photos</strong> columns, <strong>but</strong> make sure to change the <strong>Type</strong> for those columns to <strong>Text</strong>. At this stage, you should see an image similar to the one below:</p>

<p><img alt="Sharing projects through Mergin" src="https://www.lutraconsulting.co.uk/img/posts/input_basic_gpkg-3.png" /></p>

<p>Go ahead and click OK to create the layer and add it to QGIS.</p>

<h2 id="styling-layers-and-setting-up-forms">Styling layers and setting up forms</h2>

<p>The default style applied to <strong>Potholes</strong> layer is not very visible probably. To change it:</p>

<p>In the <strong>Layer Panels</strong> right-click on <strong>Potholes</strong> layer and select <strong>Properties</strong>. A new window will appear. From the left panel, select <strong>Symbology</strong>. Try to change the style to something shown in the image below:</p>

<p><img alt="Sharing projects through Mergin" src="https://www.lutraconsulting.co.uk/img/posts/input_basic_style.png" /></p>

<p>Click on <strong>Apply</strong>.</p>

<p>We can also change the way user fills in the form. By default, you have to type in the values. But by using different <strong>widgets</strong>, we can simplify filling the form in the field.</p>

<p>In the <strong>Properties</strong> window, from the left panel, select <strong>Attribute forms</strong>.</p>

<p><img alt="Sharing projects through Mergin" src="https://www.lutraconsulting.co.uk/img/posts/input_basic_forms.png" /></p>

<p>We are going to change the <strong>Widget Type</strong> for each of the <strong>Fields</strong>.</p>

<p><strong>fid</strong> is an auto-increment field and we can keep it hidden from users. So, highlight the <strong>fid</strong> field under <strong>Field</strong> section and then from the <strong>Widget Type</strong> select <strong>Hidden</strong></p>

<p>For <strong>Data</strong>, it should have automatically selected the correct widget type:</p>

<p><img alt="Sharing projects through Mergin" src="https://www.lutraconsulting.co.uk/img/posts/input_basic_widget-1.png" /></p>

<p>For <strong>Notes</strong>, you can also leave the <strong>Widget Type</strong> as <strong>Text Edit</strong>.</p>

<p>For <strong>Photos</strong>, we need to change the <strong>Widget Type</strong> to <strong>Attachment</strong>. Also make sure to select the option for <strong>Relative paths</strong>. This will allow us to attach photos using mobile camera or gallery folder to the pothole point.</p>

<p><strong>Tip</strong>: You can scroll further down and under <strong>Integrated Document Viewer</strong> and select <strong>Type</strong> as <strong>Image</strong>. This will show the image in QGIS forms too.</p>

<p><img alt="Sharing projects through Mergin" src="https://www.lutraconsulting.co.uk/img/posts/input_basic_widget-2.png" /></p>

<p>Project set up is completed and we can save the project.</p>

<h2 id="transferring-data-to-mobile-devices">Transferring data to mobile devices</h2>

<p>You have 2 options to transfer your data to the mobile through the Mergin service: through website or through Mergin plugin in QGIS. In this tutorial we are going to use the plugin from within QGIS.</p>

<p>In QGIS, from the main menu, select <strong>Plugins &gt; Manage and Install Plugins …</strong>. A new window will appear. From the left panel, select <strong>All</strong> and then in the search section (on the top) search for <strong>Mergin</strong>. Select the plugin from the list and click on <strong>Install plugin</strong>. After installation, you need to <strong>restart your QGIS</strong>.</p>

<p>After the restart, you should be able to see the Mergin icon in your <strong>Browser Panel</strong>:</p>

<p><img alt="Sharing projects through Mergin" src="https://www.lutraconsulting.co.uk/img/posts/input_basic_mergin-1.png" /></p>

<p>In the <strong>Browser Panel</strong>, right click on the <strong>Mergin</strong> and select <strong>Configure</strong>. Type in your username (or email address) and password that you have registered with the Mergin service.</p>

<p><img alt="Sharing projects through Mergin" src="https://www.lutraconsulting.co.uk/img/posts/input_basic_mergin-2.png" /></p>

<p>Click on <strong>Test Connection</strong> and you should see a green OK.</p>

<p>If you have selected to <strong>Save credentials</strong> (so you do not need to type in the username and password again) and you have not configured QGIS password manager, you will be prompted to set a password for your QGIS password manager.</p>

<p>After clicking OK, you should see a list of folders on your Mergin connection in your browser panel:</p>

<p><img alt="Sharing projects through Mergin" src="https://www.lutraconsulting.co.uk/img/posts/input_basic_mergin-3.png" /></p>

<p>We can know upload the data:</p>

<p>Right click on the <strong>Mergin</strong> and select <strong>Create new project</strong>. A new window will appear:</p>

<p>For <strong>Project name</strong> type <strong>Potholes survey</strong></p>

<p>Select <strong>Initialize from local drive</strong></p>

<p>Click on … and and select <strong>data collection</strong> folder</p>

<p><img alt="Sharing projects through Mergin" src="https://www.lutraconsulting.co.uk/img/posts/input_basic_mergin-4.png" /></p>

<p>Once click OK, the project will be created and content of the <strong>data collection</strong> folder will be uploaded there.</p>

<p>The project is now ready to be downloaded on your mobile device.</p>

<h2 id="collecting-data-using-input-app">Collecting data using Input app</h2>

<p>The project can now be accessed from Input app. Open your Input app and for the first time you should see a screen similar to the image below:</p>

<p><img alt="Sharing projects through Mergin" src="https://www.lutraconsulting.co.uk/img/posts/input_basic_input-1.png" /></p>

<p>To log in to the Mergin service, you can select <strong>My projects</strong> or the green and white icon on the top right.</p>

<p><img alt="Sharing projects through Mergin" src="https://www.lutraconsulting.co.uk/img/posts/input_basic_input-2.png" /></p>

<p>Type your Mergin username (or email address) and password and then select <strong>Sign in</strong>.</p>

<p>Once signed in, select <strong>My projects</strong> and you will see <strong>Potholes survey</strong> project in the lists</p>

<p><img alt="Sharing projects through Mergin" src="https://www.lutraconsulting.co.uk/img/posts/input_basic_input-3.png" /></p>

<p>Select the download icon on the right side of <strong>Potholes survey</strong> to download your project on the phone and make it ready for survey.</p>

<p>After downloading is completed, select <strong>Home</strong> and you should be able to see <strong>Potholes survey</strong>.</p>

<p><img alt="Sharing projects through Mergin" src="https://www.lutraconsulting.co.uk/img/posts/input_basic_input-4.png" /></p>

<p>Select <strong>Potholes survey</strong> and it will open the map:</p>

<p><img alt="Sharing projects through Mergin" src="https://www.lutraconsulting.co.uk/img/posts/input_basic_input-5.png" /></p>

<p>To record a feature, select <strong>Record</strong> button and the pointer changes to a cross-hair.</p>

<p><img alt="Sharing projects through Mergin" src="https://www.lutraconsulting.co.uk/img/posts/input_basic_input-6.png" /></p>

<p>By default, the cross-hair centres to your location (the orange point) on the map. You can move the map and adjust the location. To recentre the map to your location, you can select <strong>GPS</strong> button. Once you are happy with the location, you can select <strong>Add point</strong> and the form for your point will appear:</p>

<p><img alt="Sharing projects through Mergin" src="https://www.lutraconsulting.co.uk/img/posts/input_basic_input-7.png" /></p>

<p>Fill in the form and press <strong>Save</strong>. You should see the map with the newly captured pothole:</p>

<p><img alt="Sharing projects through Mergin" src="https://www.lutraconsulting.co.uk/img/posts/input_basic_input-8.png" /></p>

<h2 id="synchronising-data">Synchronising data</h2>
<p>The data you have captured on your phone can be synchronised through the Mergin service.</p>

<p>In Input app, select <strong>Projects</strong> and then <strong>My projects</strong>. You should see a double arrow on the right side of the <strong>Potholes survey</strong>.</p>

<p><img alt="Sharing projects through Mergin" src="https://www.lutraconsulting.co.uk/img/posts/input_basic_input-9.png" /></p>

<p>Select the double arrow to sync your project. You can also open QGIS from your PC/laptop and synchronise changes back to your desktop:</p>

<p>In QGIS, from the <strong>Browser Panel</strong> under <strong>Mergin &gt; My projects</strong> right-click on <strong>Potholes survey</strong> and select <strong>Synchronize</strong></p>

<p><img alt="Sharing projects through Mergin" src="https://www.lutraconsulting.co.uk/img/posts/input_basic_mergin-5.png" /></p>

<p>After synchronising is completed, you should be able to see the point and its associated form on your QGIS.</p>

<p><img alt="Sharing projects through Mergin" src="https://www.lutraconsulting.co.uk/img/posts/input_basic_mergin-6.png" /></p>

<h2 id="further-reading">Further reading</h2>

<p>Input app’s manual can be found <a href="https://github.com/lutraconsulting/input#documentation">here</a>.</p>

<p>With the <a href="https://merginmaps.com/">Mergin</a> service, multiple users can collect data on the same project. For more information, see this the <a href="https://www.lutraconsulting.co.uk/blog/2019/11/23/input-geodiff/">blog post</a>.</p>

<p>For more information on how to set up complex forms and map themes see <a href="https://www.qgis.org/en/docs/index.html">QGIS documentation</a>.</p>
