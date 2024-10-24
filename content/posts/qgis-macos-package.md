---
source: "blog"
title: "QGIS 3.16 package on macOS"
date: "2020-10-01T19:00:01-0500"
link: "https://lutraconsulting.co.uk/blog/2020/10/01/qgis-macos-package/"
draft: "false"
showcase: "planet"
subscribers: ["lutragis"]
author: "Lutra Consulting"
tags: []
---

<p>QGIS 3.16 on macOS coming with Proj6, GDAL3 and major fixes!
macOS packaging mechanism is completely reworked for QGIS 3.16. 
This will bring QGIS on macOS on par with other platforms that already benefit from the new versions of 
PROJ and GDAL libraries - especially the greatly improved reprojection support.</p>

<!-- more -->

<h2 id="qgis-nightly-and-qgis-316">QGIS nightly and QGIS 3.16</h2>

<p><img alt="QGIS3.16" src="https://www.lutraconsulting.co.uk/img/posts/qgis315_deps.png" /></p>

<p>If you want to try the new packages, download and install the QGIS from <a href="https://qgis.org/downloads/macos/nightly/">nightly builds</a>.
There are still few weeks before QGIS 3.16 release for testing and bug-fixing, so make sure you <a href="https://github.com/qgis/QGIS/issues">report</a> all your issues before the 
23rd October 2020. Multiple packages now can be installed side-by-side, just rename or move the installed QGIS.app!</p>

<p>The earlier packages were based on Homebrew, but we didn’t have control over the versions of dependencies. 
We switched to the new system where we have full control, which is important for good quality releases.</p>

<p>The package/installer is not yet notarized by Apple, so you need to right-click on the QGIS.app icon and open it to overcome the security control of 
your macOS (only for 10.15+).</p>

<p>If you want to join the effort in testing and/or development of macOS packages, please drop me a mail on <a href="mailto:peter.petrik@lutraconsulting.co.uk">peter.petrik@lutraconsulting.co.uk</a>
We have a dedicated Slack channel to discuss the maintenance of the macOS packages.</p>

<h2 id="what-is-in-the-all-in-one-bundle">What is in the all-in-one bundle?</h2>

<p>The goal is to have all advanced functionality of QGIS prepared and ready to use after simple one-click installation.</p>

<h3 id="qgis-and-utilities">QGIS and utilities</h3>

<p>QGIS Desktop, of course, but also</p>
<ul>
  <li>QGIS server (try with <code class="highlighter-rouge">/Applications/QGIS.app/Contents/MacOS/bin/qgis_mapserver</code>)</li>
  <li>QGIS process (try with <code class="highlighter-rouge">/Applications/QGIS.app/Contents/MacOS/bin/qgis_process</code>)</li>
  <li>QtDesigner for custom forms (<code class="highlighter-rouge">/Applications/QGIS.app/Contents/MacOS/bin/designer</code>)</li>
  <li>ogr2ogr and various other gdal utilities</li>
</ul>

<h3 id="foss4g-libraries">FOSS4G libraries</h3>

<ul>
  <li>Geos 3.8.1</li>
  <li>Proj 6.3.2</li>
  <li>GDAL 3.1.2</li>
  <li>GRASS 7.8.3</li>
  <li>SAGA 7.3.0</li>
</ul>

<h3 id="python-37">Python 3.7</h3>
<p>with pip, so you can install the missing packages with command 
  <code class="highlighter-rouge">/Applications/QGIS.app/Contents/MacOS/bin/pip3 install &lt;your package&gt;</code></p>

<p>but, many packages are already preinstalled for you!</p>
<ul>
  <li>pipenv</li>
  <li>requests</li>
  <li>plotly</li>
  <li>matplotlib</li>
  <li>scipy</li>
  <li>numpy</li>
  <li>shapely</li>
  <li>geopandas</li>
  <li>gdal</li>
  <li>h5py</li>
  <li>pyproj</li>
  <li>pillow</li>
</ul>

<h3 id="qgis-processing">QGIS Processing</h3>

<ul>
  <li>GRASS processing tools</li>
  <li>GDAL processing tools</li>
  <li>SAGA processing tools</li>
  <li>OTB processing tools (needs external <a href="https://www.orfeo-toolbox.org/CookBook/QGISInterface.html#the-qgis-otb-plugin-requires-qgis-3-2">installation</a> of OTB)</li>
</ul>

<h3 id="data-providers">Data Providers</h3>

<p>All basic providers</p>
<ul>
  <li>GeoPackage</li>
  <li>Spatialite</li>
  <li>DB2</li>
  <li>WCS/WFS/OWS/WMS/WMTS</li>
  <li>Vector Tiles</li>
  <li>XYZ Tiles</li>
  <li>OGR/GDAL</li>
  <li>PostgreSQL</li>
  <li>MDAL</li>
</ul>

<p>But also:</p>

<ul>
  <li>ECW</li>
  <li>MrSID</li>
  <li>MSSQL</li>
  <li>OracleDB</li>
</ul>

<h2 id="acknowledgments">Acknowledgments</h2>
<p>In Spring <a href="https://www.lutraconsulting.co.uk/blog/2020/04/22/qgis-macos-development/">2020</a>, we prototyped the building of FOSS macOS libraries in completely controlled environment. 
Few weeks ago we have successfully finished the <a href="https://github.com/qgis/QGIS-Enhancement-Proposals/issues/177">QGIS 2020 Grant “QGIS macOS Package Improvements”</a>. 
This wouldn’t be possible without support from QGIS.org and its sponsors. And without proper testing and reporting of issues from our macOS power-users.</p>

<h2 id="qgis-for-ios">QGIS for iOS</h2>
<p>Do you want to see your QGIS projects and data from your iPhone and iPad? Check <a href="https://www.lutraconsulting.co.uk/blog/categories/qgis/merginmaps.com">InputApp</a></p>
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
