---
source: "blog"
title: "Getting started with QGIS"
date: "2014-06-06T13:00:00-0500"
link: "https://lutraconsulting.co.uk/blog/2014/06/06/getting-started-with-qgis/"
draft: "false"
showcase: "planet"
subscribers: ["lutragis"]
author: "Lutra Consulting"
tags: []
---

<p>QGIS is a Free and Open Source Software, developed by a growing community of individuals and organisations.</p>

<ul><li><a href="https://www.lutraconsulting.co.uk/blog/categories/qgis/atom.xml#installation">Installation</a></li>
	<li><a href="https://www.lutraconsulting.co.uk/blog/categories/qgis/atom.xml#starting">Starting QGIS</a>
		<ul class="l2"><li><a href="https://www.lutraconsulting.co.uk/blog/categories/qgis/atom.xml#arrange">Arranging tool-bars</a></li>
		<li><a href="https://www.lutraconsulting.co.uk/blog/categories/qgis/atom.xml#crs">Setting the Coordinate Reference System (CRS)</a></li>
        </ul>
	</li>
	<li><a href="https://www.lutraconsulting.co.uk/blog/categories/qgis/atom.xml#data">Adding data</a>
		<ul class="l2"><li><a href="https://www.lutraconsulting.co.uk/blog/categories/qgis/atom.xml#raster">Raster</a></li>
		<li><a href="https://www.lutraconsulting.co.uk/blog/categories/qgis/atom.xml#vector">Vector</a></li>
		<li><a href="https://www.lutraconsulting.co.uk/blog/categories/qgis/atom.xml#otherdata">Other Data</a></li>
		</ul>
	</li>
	<li><a href="https://www.lutraconsulting.co.uk/blog/categories/qgis/atom.xml#plugins">Plugins</a>
		<ul class="l2"><li><a href="https://www.lutraconsulting.co.uk/blog/categories/qgis/atom.xml#core">Core plugins</a></li></ul>
	</li>
	<li><a href="https://www.lutraconsulting.co.uk/blog/categories/qgis/atom.xml#moreinfo">Further information</a></li>
	<li><a href="https://www.lutraconsulting.co.uk/blog/categories/qgis/atom.xml#troubleshooting">Troubleshooting</a>
		<ul class="l2">
		<li><a href="https://www.lutraconsulting.co.uk/blog/categories/qgis/atom.xml#ts_openlayers">Missing OpenLayers Plugin</a></li>
		<li><a href="https://www.lutraconsulting.co.uk/blog/categories/qgis/atom.xml#ts_installation" title="Installation in Windows">Windows installation</a></li>
		<li><a href="https://www.lutraconsulting.co.uk/blog/categories/qgis/atom.xml#core">Proxy settings</a></li>
		</ul>
	</li>
</ul>

<!-- more -->

<h2><a id="installation" name="installation"></a>Installation</h2>
<p>You can download the latest version of QGIS from <a href="http://qgis.org/en/site/forusers/download.html" rel="nofollow" target="_blank" title="QGIS download page">here</a>. On that page, you can find the appropriate QGIS installation package for your operating system. </p>
<p>If you are a MS Windows user, you have 2 options: the standalone installer or the OSGeo4W installer, each of which has its own strengths:</p>
<ul><li><strong>OSGeo4W Installer Strengths</strong>
	<ul><li>Access to the "master" (development) version of QGIS which means you can make use of the latest (yesterday's) cutting-edge features</li>
	<li>Access to QGIS-Server (which allows you to publish your maps through a Web Mapping Service)</li>
	</ul></li>
	</ul>
<ul><li><strong>Standalone Installer Strengths</strong>
	<ul><li>Simplest method of installation</li>
	</ul></li>
</ul>

<h2><a id="starting" name="starting"></a>Starting QGIS</h2>
<p>Once you finish installing QGIS, you can find its icon on your desktop and/or Start menu. <strong>Launch QGIS</strong> and wait for the application to start. If you're a MS Windows user, QGIS might take some time to start up for the first time but subsequent loads will be much faster.</p>
<p><img alt="QGIS Start page" height="440" src="https://www.lutraconsulting.co.uk/img/posts/qgisintor_qgis.png" title="QGIS Start page" width="600" /></p>

<h3><a id="arrange" name="arrange"></a>Arranging tool-bars</h3>
<p>QGIS features a number of tool-bars. You can move them around by clicking and dragging the vertical or horizontal dotted bars separating the tool-bars (for example, the bar to the left of the help tool's icon in the image above).</p>

<h3><a id="crs" name="crs"></a>Setting the Coordinate Reference System (CRS)</h3>
<p>It is recommended to set the Coordinate Reference System (CRS) for your project before adding any data. CRS or SRS <a href="http://en.wikipedia.org/wiki/Spatial_reference_system" rel="nofollow" target="_blank" title="CRS">is a coordinate-based local, regional or global system used to locate geographical entities</a>. Many CRSs are available and each is suited to a particular area of the globe. There is a comprehensive list of CRS codes available <a href="http://spatialreference.org/" rel="nofollow" target="_blank" title="spatialref">here</a>. In this example, we will set the CRS to match the British National Grid coordinate reference system. The easiest way to search for a specific CRS is using its unique EPSG code. The EPSG code for British National Grid is 27700.</p>

<p>To set the CRS for your projects in QGIS, from the main menu, select <strong>Settings &gt; Options</strong>. A new window will appear. Select  <strong>CRS</strong> tab.  </p>

<p><img alt="QGIS Options" height="361" src="https://www.lutraconsulting.co.uk/img/posts/qgisintro_Options.png" title="QGIS Options" width="600" /></p>

<p><img alt="CRS list" height="474" src="https://www.lutraconsulting.co.uk/img/posts/qgisintro_pr.png" title="CRS list" width="433" /></p>

<p>In the Search section, set <em>Authority </em>to <strong>"EPSG"</strong> and <em>Search for</em> to <strong>"ID"</strong>. Type <strong>27700</strong> into the search box and <strong>click Find</strong>. Highlight the correct row in Coordinate Reference System section and click <strong>OK</strong>.</p>
<h2><a id="data" name="data"></a>Adding data</h2>
<p>GIS data is usually in either <a href="http://en.wikipedia.org/wiki/GIS_data#Raster" rel="nofollow" target="_blank" title="raster data">raster</a> or <a href="http://en.wikipedia.org/wiki/GIS_data#Vector" rel="nofollow" target="_blank" title="vector data">vector</a> format. QGIS supports a large number of GIS data formats through the GDAL/OGR library and other plugins. In the example below we will download and add some OS OpenData™ raster and vector datasets into QGIS.</p>
<h3><a id="raster" name="raster"></a>Raster</h3>
<p>Ordnance Survey released a number of OS OpenData raster datasets to the public under a very <a href="http://www.nationalarchives.gov.uk/doc/open-government-licence/version/3/" rel="nofollow" target="_blank" title="Open Government License">permissive license</a>. You can download the data from <a href="https://www.ordnancesurvey.co.uk/opendatadownload/products.html" rel="nofollow" target="_blank" title="opendata">here</a>. </p>
<p>For this particular example, follow <a href="https://www.ordnancesurvey.co.uk/opendatadownload/products.html" rel="nofollow" target="_blank" title="opendata">this link</a> and browse to <strong>OS Street View<sup>&reg;</sup></strong>. Select <strong>SX</strong> from the map. Move towards the bottom of the page and click <strong>next</strong>. Fill in the required information and click <strong>continue</strong>. You should receive an email with a link to download <em>osstvw_sx.zip</em> (note: it is a 383.9 MB file - you can order a DVD instead if you have a slow internet connection). Once the download has finished, <strong>unzip the file</strong>. You should now have a new folder called <em>OS Street View SX</em> which contains 2 subfolders and a readme file.</p>
<p>Browse to <em>Street View SX &gt; data &gt; georeferencing files &gt; tfw. </em>Select all the TFW files and move them to the <em>Street View SX &gt; data &gt; sx </em>folder. The TFW files contain georeferencing information describing the location of each TIF file.</p>
<p>In QGIS, from the main menu, select<strong> Layer &gt; Add Raster Layer...</strong> and browse to the <em>Street View SX &gt; data &gt; sx </em>folder<em>. </em><strong>Select <em>sx99nw.tif, sx99ne</em><em>.tif</em><em>, sx99sw</em><em>.tif</em><em> </em></strong>and <strong><em>sx99se</em><em>.tif</em></strong>. Click <strong>Open</strong>. You should now be able to see the raster tiles in the QGIS canvas and the Layers panel at the left side of the screen. </p>
<p>Raster files do not always contain CRS information. We can easily organise the layers and assign the correct CRS (EPSG:27700) with the help of <em>groups</em>. Create a new group by right-clicking on the blank space (not on the sx99 layers) in the Layers panel and selecting <strong>Add group</strong>. Set the name of the group to <em>OS Street View</em>. Next, move the sx99 layers into the new group by selecting them all and dragging them into the OS Street View group. Once all the sx99 layers are inside the OS Street View group, right-click on the group and select <strong>Set group CRS</strong>. A new dialog, similar to that seen in the <a href="https://www.lutraconsulting.co.uk/blog/categories/qgis/atom.xml#crs" title="Setting the CRS">Setting the CRS</a> chapter will appear. Assign the British National Grid CRS (EPSG:27700) and click <strong>OK</strong>. </p>
<p><img alt="QGIS raster" height="382" src="https://www.lutraconsulting.co.uk/img/posts/qgisintro_raster.png" title="QGIS raster" width="600" /></p>
<h3><a id="vector" name="vector"></a>Vector</h3>
<p>Next, we'll bring some vector data into QGIS. Go to the <a href="https://www.ordnancesurvey.co.uk/opendatadownload/products.html" rel="nofollow" target="_blank">OS OpenData Supply</a> page and browse to <strong>OS VectorMap&#8482; District </strong><span style="color: red;">(there are two OS VectorMap datasets on this page, for this example, ensure you select the <strong>vector</strong> version and not the raster version)</span> and select SX from the map. Scroll to the bottom of the page and click <strong>next</strong>. Fill in the required information and click <strong>continue</strong>. Download <em>vmdvec_sx.zip</em> from the link you'll receive by email. Extract the contents of the ZIP file.</p>
<p>In QGIS, from the main menu, select<strong> Layer &gt; Add Vector Layer...</strong> and browse to the <em>OS VectorMap District (Vector) SX &gt; data &gt; SX. </em>Select <em>SX_Airport.shp, SX_RailwayTrack.shp </em>and <em>SX_Road.shp.</em> Click <strong>Open</strong>. Click <strong>Open</strong> again. </p>
<p>To change the style of a vector layer, right-click on the layer in the Layers panel and select Properties. In the Style tab of the Layer Properties dialog, you can define exactly how the layer should look. <em><br /></em></p>
<p><img alt="QGIS vector" height="382" src="https://www.lutraconsulting.co.uk/img/posts/qgisintro_vector.png" title="QGIS vector" width="600" /></p>
<h3><a id="otherdata" name="otherdata"></a>Other Data</h3>
<p>Internet based mapping can also be brought into QGIS, for example, a plugin exists that allows OpenStreetMap, Google, Bing and Yahoo maps to be added to QGIS. </p>
<p>Web map services (<a href="http://en.wikipedia.org/wiki/Web_Map_Service" rel="nofollow" target="_blank" title="wms">WMS</a>) are another source of mapping data. In the next we'll add a WMS layer provided by <a href="http://www.bgs.ac.uk/home.html" rel="nofollow" target="_blank" title="bgs">British Geological Survey</a> to our map. Please read the <a href="http://www.bgs.ac.uk/data/services/digmap50wms.html" rel="nofollow" target="_blank">BGS WMS Terms of use</a>. Another example of WMS is Ordnance Survey's <strong><a href="http://www.ordnancesurvey.co.uk/oswebsite/web-services/os-ondemand/index.html" rel="nofollow" target="_blank" title="OS OnDemand link 1">OS OnDemand</a></strong> service. If you have <a href="http://www.ordnancesurvey.co.uk/oswebsite/web-services/os-ondemand/index.html" rel="nofollow" target="_blank" title="OS OnDemand link"><strong>OS OnDemand</strong></a> license, you can follow the instructions on Ordnance Survey's website (sorry, link no longer works) to add other useful WMS layers.</p>
<p>To add the BGS WMS, select <strong>Layer &gt; Add WMS Layer...</strong> from the main menu. The <em>Add Layer(s) from a Server</em> dialog will appear. Click <strong>New</strong>.<em><br /></em></p>
<p><img alt="wms add" height="446" src="https://www.lutraconsulting.co.uk/img/posts/qgisintro_wmsAdd.png" title="wms add" width="600" /></p>
<p>Set the name to <strong><em>BGS</em></strong> and set the URL to the following:</p>
<p><a href="http://maps.bgs.ac.uk/ArcGIS/services/BGS_Detailed_Geology/MapServer/WMSServer" rel="nofollow" target="_blank">http://maps.bgs.ac.uk/ArcGIS/services/BGS_Detailed_Geology/MapServer/WMS...</a></p>
<p>Click <strong>OK</strong>, and in the <em>Add Layer(s) from a Server dialog</em>, click <strong>Connect</strong>. </p>
<p><img alt="wms add layer" height="446" src="https://www.lutraconsulting.co.uk/img/posts/qgisintro_wmsAddLayer.png" title="wms add layer" width="600" /></p>
<p><strong>Select all the layers</strong> and click <strong>Add</strong>. <strong>Close</strong> the <em>Add Layer(s) from a Server</em> dialog. The BGS layer should become visible as you<strong> zoom-in to a scale of 1:50000</strong> or closer. Alternatively, you can manually set the Scale in the status bar to 1:50000 and the BGS layer will appear. </p>
<p><img alt="wms BGS" height="382" src="https://www.lutraconsulting.co.uk/img/posts/qgisintro_wmsBGS.png" title="wms BGS" width="600" /></p>
<h2><a id="plugins" name="plugins"></a>Plugins</h2>
<p>QGIS is written in a manner that makes it possible for anyone it extend its functionality through the use of plugins. As a result, there are many plugins available to the user, making QGIS highly modular and flexible. </p>
<h3><a id="core" name="core"></a>Core plugins</h3>
<p>Core plugins are plugins that are shipped with QGIS and can be optionally enabled through the <em>QGIS Plugin Manager</em>.&nbsp; To access the <em>QGIS Plugin Manager</em>, from the main menu, Select <strong>Plugins &gt; Manage Plugins... </strong></p>
<p><img alt="qgis core plugins" height="284" src="https://www.lutraconsulting.co.uk/img/posts/qgisintro_coreplugins.png" title="QGIS Plugins" width="600" /></p>

<p>Select the <strong>All tab</strong> and type <em>OpenLayers Plugin</em> into the Filter box. Select the plugin and click <strong>Install plugin</strong>. You should now be able to add OpenStreetMap, Google, Bing and Yahoo maps to your canvas using the <strong>Web &gt; OpenLayers plugin</strong> menu.</p>
<p><img alt="qgis and OpenLayers" height="382" src="https://www.lutraconsulting.co.uk/img/posts/qgisintro_openlayers.png" title="QGIS and OpenLayers" width="600" /></p>
<h2><a id="moreinfo" name="moreinfo"></a>Further information</h2>
<p>For further help using QGIS, you can always check the manual, <a href="http://lists.osgeo.org/mailman/listinfo/qgis-user" rel="nofollow" target="_blank" title="userML">user</a> or <a href="http://lists.osgeo.org/mailman/listinfo/qgis-developer" rel="nofollow" target="_blank" title="dev_ML">developer</a> mailing lists or <a href="http://forum.qgis.org/index.php" rel="nofollow" target="_blank" title="forum">QGIS forum</a>. </p>
<p>If you'd like to master QGIS as quickly as possible, why not attend one of our <a href="https://www.lutraconsulting.co.uk/training/">training courses</a>.</p>
<h2><a id="troubleshooting" name="troubleshooting"></a>Troubleshooting</h2>
<h3><a id="ts_openlayers" name="ts_openlayers"></a>Installing OpenLayers Plugin</h3>
<p>To install OpenLayers plugin, from the main menu, click <strong>Plugins &gt; Manage and Install Plugins...</strong>. A new window will appear.
<p>You should be able to search and install the OpenLayers plugin within your list.</p>
<h3><a id="ts_installation" name="ts_installation"></a>Windows Installation</h3>
<p>Although you can have different version of QGIS installed under Windows, it's recommended to uninstall old versions before attempting to install new versions. </p>
<p>On rare occasions, some anti-virus software has been known to remove the qgis.exe and python.exe files from the installation folder. If you're having problems running the QGIS shortcut, please ensure those 2 files exist in the installation folder.</p>
<p>If QGIS cannot find your Python folder, you may need to set the PYTHONPATH environment variable to your QGIS folder (<em>\QGIS\apps\python</em>).</p>
<h3><a id="ts_access" name="ts_access"></a>Access to internet</h3>
<p>To be able to access WMS, WFS and 3<sup>rd</sup> party plugins, you'll need to have  internet access. In the event that you're behind a proxy server, you can enter the proxy server details in <strong>Settings &gt; Options &gt; Network</strong>:</p>
<p><img alt="qgis proxy" height="467" src="https://www.lutraconsulting.co.uk/img/posts/qgisintro_proxy.png" title="QGIS Proxy Settings" width="600" /></p>
 
</p>
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
