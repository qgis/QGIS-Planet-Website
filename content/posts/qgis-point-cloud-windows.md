---
source: "blog"
title: "Test QGIS with Point Clouds on Windows"
date: "2021-02-15T18:00:01-0600"
link: "https://lutraconsulting.co.uk/blog/2021/02/15/qgis-point-cloud-windows/"
draft: "false"
showcase: "planet"
subscribers: ["lutragis"]
author: "Lutra Consulting"
tags: []
---

<p>In the past months, we have been busy adding support for point cloud data in QGIS (3.18). Read more on how to install and test this feature under MS Windows.</p>

<h2 id="installation">Installation</h2>
<p>To be able to use this feature, you need extra packages and also the latest OSGeo4W installer.</p>

<h2 id="update">Update</h2>

<p>Since the original post, Jürgen Fischer has created a stand-alone MSI installer. You can download the new installer from the <a href="https://qgis.org/downloads/QGIS-OSGeo4W-3.18.0-1.msi">QGIS website</a>. The installer is only for 64-bit platforms and does not support MS Windows 7.</p>

<p>Note that there have been several regressions and bugs with the first release of QGIS 3.18.0. The issues are being addressed and soon there will be an updated version available. The above link is only for those who are eager to test the point cloud data in QGIS.</p>

<h2 id="installation-1">Installation</h2>
<p>To be able to use this feature, you need extra packages and also the latest OSGeo4W installer.</p>

<p><strong>Note</strong>: This is a completely revamped and different packaging system than the current OSGeo4W installer. To avoid any clash with your current installation, it is recommended to use different paths for temporary download files and installation of the new packages. The new packaging only supports 64-bit platform.</p>

<p>1- Download and run the <strong>NEW</strong> <a href="http://download.osgeo.org/osgeo4w/testing/osgeo4w-setup.exe">OSGeo4W installer</a></p>

<p>2- Select the <strong>Advanced install</strong> and pick <strong>qgis-dev</strong> from the list of packages</p>

<p>Special thanks to Jürgen Fischer for his hard work on preparing the new packages for Windows.</p>

<h2 id="testing">Testing</h2>
<p>Once installation is completed, try to run QGIS from the installation path (e.g. C:\OSGeo4W64\bin\qgis-dev.bat). You should be able to load LAS\LAZ file to your map from the Browser panel or the Data Source Manager.</p>

<p>The point cloud data can be visualised in 2D and 3D map canvas.</p>

<p><img alt="Point Clouds in QGIS under Windows" src="https://www.lutraconsulting.co.uk/img/posts/windows_point_clouds.png" /></p>

<p>Please test and let us know if you encounter any problems when loading, viewing or styling point cloud data. The best way to do that is to create a new issue on GitHub: https://github.com/qgis/QGIS/issues</p>

<p>QGIS 3.18 will be released later this week (February 19), so grab your copy of QGIS today and give it a try, so that we can fix any remaining issues before the release!</p>

<h2 id="troubleshooting">Troubleshooting</h2>

<p><strong>Problem</strong>: I am unable to add any LAS/LAZ point cloud file</p>

<p><strong>Solution</strong>: Ensure you have used the correct installer linked above. Development builds of QGIS in the ordinary OSGeo4W installer DO NOT include support for point clouds.</p>

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
