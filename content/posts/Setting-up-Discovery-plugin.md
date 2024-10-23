---
source: "blog"
title: "Setting up and Configuring Discovery plugin for QGIS"
date: "2016-04-25T09:00:00-0500"
link: "https://lutraconsulting.co.uk/blog/2016/04/25/Setting-up-Discovery-plugin/"
draft: "false"
showcase: "planet"
subscribers: ["lutragis"]
author: "Lutra Consulting"
tags: []
---

<p>As a part of migrating to Open Source GIS, the Newcastle City Council has commissioned us to create a user friendly gazetteer plugin.</p>

<p>In this post, we will import the OS Open Names and configure the Discovery plugin to use the data.</p>

<!-- more -->

<p>In the following sections, we are going to set up a PostGIS database and import the <a href="https://www.ordnancesurvey.co.uk/business-and-government/products/os-open-names.html" title="OS open data">OS Open Names</a>, freely available  from <a href="https://www.ordnancesurvey.co.uk/opendatadownload/products.html" title="OS download link">here</a>.</p>

<p>To use the data with the Discovery plugin, we need to first set up a PostGIS database and load the data inside the geo-databases.</p>

<p>If you have an existing Postgresql/PostGIS server, you can skip the next section.</p>

<h2 id="postgresqlpostgis-installation-and-configuration">Postgresql/PostGIS installation and configuration</h2>

<h3 id="installation">Installation</h3>
<p>For MS Windows users, download and install Postgresql from <a href="http://www.enterprisedb.com/postgresql-951-installers-win32?ls=Crossover&amp;type=Crossover">here (32-bit)</a> or  <a href="http://www.enterprisedb.com/postgresql-951-installers-win64?ls=Crossover&amp;type=Crossover">here (64-bit)</a> install the software.</p>

<p>During the installation, select the <strong>StackBuilder</strong> to install PostGIS, under <strong>Spatial Extensions</strong>.</p>

<p>If your StackBuilder fails to download PostGIS (in case your proxy server blocks it), you can <a href="http://download.osgeo.org/postgis/windows/pg95/" title="PostGIS">download</a> and install it manually.</p>

<h3 id="preparing-the-database">Preparing the database</h3>
<p>Now that installation is successful, create a new database as <strong>osdata</strong>. Make sure you add PostGIS extension to your database. You can do that by simply running the following command in the <strong>Query editor</strong>:</p>

<div class="highlighter-rouge"><div class="highlight"><pre class="highlight"><code>CREATE EXTENSION postgis;
</code></pre></div></div>

<p>Create <strong>osopennames</strong> as a new schema under <strong>osdata</strong>.</p>

<h2 id="preparing-data">Preparing data</h2>
<p>In this example, we are focusing on the OS Open Names comes (for Great Britain only) which comes in a zip file containing several CSV files.</p>

<p><strong>If you’d like to use address data for your part of the world, you can visit <a href="https://results.openaddresses.io/" title="openaddress">the OpenAddress website</a> for the global coverage. Note that the CSV files for this dataset come with the vrt files, so you can skip the vrt creation and directly use ogr2ogr.</strong></p>

<p>Once the zip file extracted, there are 2 folders, one containing the header file (<strong>DOC</strong>) and the other containing the csv files (<strong>DATA</strong>).</p>

<p>To be able to import all the csv files in PostGIS, we can merge all the files including the header file.</p>

<p>You can move the header file (<strong>OS_Open_Names_Header.csv</strong>) from the <strong>DOC</strong> folder. To ensure, the file will appear first during the merge process you can rename it to <strong>1_OS_Open_Names_Header.csv</strong>.</p>

<p>You can use Windows command prompt to merge the files. The following command merges all csv files to <strong>all_open_names.csv</strong>:</p>

<div class="highlighter-rouge"><div class="highlight"><pre class="highlight"><code> copy /b \*.csv all_open_names.csv
</code></pre></div></div>

<h2 id="loading-data-in-postgis">Loading data in PostGIS</h2>
<p>There are several methods to import <strong>all_open_names.csv</strong> in PostGIS:</p>

<ol>
  <li>Adding it as a delimited text layer in QGIS and then load it in PostGIS</li>
  <li>Importing it in PostGIS as a CSV and then using PostGIS’ geometry  to create points</li>
  <li>Using virtual layer and OGR2OGR library</li>
</ol>

<p>In the example below, we explore the third option.</p>

<p>To create a virtual vector layer from your csv file, open a text editor, copy and paste the following lines and save it as  <strong>all_open_names.vrt</strong> under <strong>DATA</strong> folder along with your csv file.</p>

<div class="highlighter-rouge"><div class="highlight"><pre class="highlight"><code>
	&lt;OGRVRTDataSource&gt;
    	&lt;OGRVRTLayer name="all_open_names"&gt;
        	&lt;SrcDataSource relativeToVRT="1"&gt;all_open_names.csv&lt;/SrcDataSource&gt;
        	&lt;GeometryType&gt;wkbPoint&lt;/GeometryType&gt;
        	&lt;LayerSRS&gt;EPSG:27700&lt;/LayerSRS&gt;
        	&lt;GeometryField encoding="PointFromColumns" x="GEOMETRY_X" y="GEOMETRY_y"/&gt;
    	&lt;/OGRVRTLayer&gt;
	&lt;/OGRVRTDataSource&gt;
</code></pre></div></div>

<p>In fact, you can use the virtual vector layer to merge all your csv files and skip the previous section!</p>

<p>You can then use ogr2ogr command from the OSGeo4W shell to import it to your PostGIS:</p>

<div class="highlighter-rouge"><div class="highlight"><pre class="highlight"><code>    ogr2ogr -append  -a_srs EPSG:27700 -f "PostgreSQL" PG:"host=127.0.0.1 user=postgres dbname=osdata password=postgres active_schema=osopennames" -nln osnames all_open_names.vrt
</code></pre></div></div>

<p><strong>Note</strong>: if you are using the OpenAdress data make sure you assign the right EPSG (4326) in the above command.</p>

<h2 id="configuring-discovery-plugin">Configuring Discovery plugin</h2>
<p>First you need to install the plugin from the QGIS plugin repository.</p>

<p>Once the plugin installed, you should have a new toolbar. Click on <img alt="discovery" src="https://www.lutraconsulting.co.uk/img/posts/discovery_icon.png" /> from the toolbar to open the configuration:</p>

<ol>
  <li>For <strong>Connection</strong>, select <strong>OS Data</strong></li>
  <li>For <strong>Shema</strong>, select <strong>opennames</strong></li>
  <li>For <strong>Table</strong>, select <strong>osnames</strong></li>
  <li>For <strong>Search Column</strong>, select <strong>Name1</strong></li>
  <li>Select the option to <strong>Echo Search Column in Results</strong></li>
  <li>For <strong>Display Columns</strong> select the followings:
    <ol>
      <li><strong>Name2</strong></li>
      <li><strong>DISTRICT_BOROUGH</strong></li>
      <li><strong>POSTCODE_DISTRICT</strong></li>
      <li><strong>COUNTRY</strong></li>
    </ol>
  </li>
  <li>For <strong>Geometry Column</strong>, select <strong>geom</strong> (or other columns depending on your QGIS or OGR versions)</li>
  <li>For <strong>BBOX Expresssion</strong>, type the following:</li>
</ol>

<div class="highlighter-rouge"><div class="highlight"><pre class="highlight"><code>CASE
	WHEN "MBR_XMIN" IS NOT NULL
THEN
	MBR_XMIN || ',' ||
	MBR_YMIN || ',' ||
	MBR_XMAX || ',' ||
	MBR_YMAX
END
</code></pre></div></div>

<p>And you should be able to start using the gazetteer plugin after pressing <strong>OK</strong>.</p>

<p>For performance enhancement and other tips visit <a href="https://www.lutraconsulting.co.uk/projects/discovery/">this page</a>.</p>

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
