---
source: "blog"
title: "Offline WMS - Benchmarking raster formats for QField"
date: "2020-06-09T05:03:00+0000"
link: "https://qfield.org/blog/2020/06/09/offline-wms-benchmarking-raster-formats-for-qfield/"
draft: "false"
showcase: "planet"
subscribers: ["qfield"]
author: "QField"
tags: ["processing", "qfield", "qgis", "scripts", "qgis.org"]
languages: ["en_gb"]
available_languages: ["en_gb"]
---

<h2 id="what-are-we-looking-for">What are we looking for?</h2>
<p>We would like to use WMS offline on QField. For that, we need to figure out what is the best way to get a raster from a WMS and which format is the most efficient (size and performance).</p>
<p>In this post we’ll show you is how to generate the ideal raster file from a WMS and the results of our efficiency tests for the the different raster formats.</p>
<h2 id="wms-to-gpkg">WMS to GPKG</h2>
<h3 id="the-simple-way">The simple way</h3>
<p>If there is no limitation on the WMS or you need only a small region, here is the easiest process.</p>
<ol>
<li>Request the WMS and store a <a href="https://gdal.org/drivers/raster/wms.html#xml-description-file" rel="noopener" target="_blank">description file in XML</a>:</li>
</ol>
<pre tabindex="0"><code>gdal_translate "WMS:url" file.xml -of WMS
</code></pre><ol>
<li>Create a Geopackage from the information in the description file.</li>
</ol>
<pre tabindex="0"><code>gdal_translate -of GPKG file.xml file.gpkg -co TILE_FORMAT=JPEG
</code></pre><p>That was quite simple, right?</p>
<h3 id="the-larger-datasets-way">The larger datasets way</h3>
<p>If the command takes too much time, it means that it is trying to download too much data and could be caused by downloading higher resolution data than required.<br/>
The command might even completely fail if it contains a request for bigger data blocks thant the server allows.</p>
<p>Here is the process to get larger datasets in a simple way. Let’s use a real example:</p>
<ol>
<li>Use <code>gdal_translate "WMS:https://www.gebco.net/data_and_products/gebco_web_services/web_map_service/mapserv?request=getmap&amp;service=wms&amp;crs=EPSG:4326&amp;format=image/jpeg&amp;layers=gebco_latest&amp;version=1.1.0" test.xml -of WMS</code></li>
<li>Open the test.xml file for editing, here you’ll find the parameters of the WMS. We change the “SizeX” to 3600 and “SizeY” to 1800. By changing these parameters we lower the resolution. It is important to keep proportionality.</li>
<li>Another thing we need to change are “BlockSizeX” and “BlockSizeY” that define the size of the tiles. We change both to 2048.</li>
<li>Finally, use <code>gdal_translate -of GPKG test.xml test.gpkg -co TILE_FORMAT=JPEG</code></li>
<li>To make a Geopackage pyramid use <code>gdaladdo GPKG:test.gpkg:gebco_latest</code>. It will <strong>replace</strong> the Geopackage, if you want to keep the original one, you need to copy it first.</li>
</ol>
<p>Now you have a raster Geopackage that you can use in QField.</p>
<h2 id="testing-raster-formats">Testing raster formats</h2>
<h3 id="preparing-the-files">Preparing the files</h3>
<p>As first step we exported our test orthophoto WMS to a plain GeoTIFF using QGIS’ default behaviour.</p>
<figure class="figure text-center mb-4"><img alt="" class="figure-img img-fluid gallery-img" src=""/></figure>
<p>Formatgdal_translategdaladdogpkg JPEGgdal_translate -of GPKG “C:\test\ortho_test.tif” “C:\test\test_JPEG.gpkg” -co TILE_FORMAT=JPEG
gpkg PNGgdal_translate -of GPKG “C:\test\ortho_test.tif” “C:\test\test_PNG.gpkg” -co TILE_FORMAT=PNGgpkg PNG_JPEGgdal_translate -of GPKG “C:\test\ortho_test.tif” “C:\test\test_PNG_JPEG.gpkg” -co TILE_FORMAT=PNG_JPEGgpkg PNG8gdal_translate -of GPKG “C:\test\ortho_test.tif” “C:\test\test_PNG8.gpkg” -co TILE_FORMAT=PNG8gpkg WEBPgdal_translate -of GPKG “C:\test\ortho_test.tif” “C:\test\test_WEBP.gpkg” -co TILE_FORMAT=WEBPgpkg pyramid_JPEGgdal_translate -of GPKG “C:\test\ortho_test.tif” “C:\test\test_JPEG.gpkg” -co TILE_FORMAT=JPEGgdaladdo GPKG:C:\test\test_JPEG.gpkg:test_gpkg_JPEG gpkg pyramid_PNGgdal_translate -of GPKG “C:\test\ortho_test.tif” “C:\test\test_PNG.gpkg” -co TILE_FORMAT=PNGgdaladdo GPKG:C:\test\test_PNG.gpkg:test_gpkg_PNGgpkg pyramid_PNG_JPEGgdal_translate -of GPKG “C:\test\ortho_test.tif” “C:\test\test_PNG_JPEG.gpkg” -co TILE_FORMAT=PNG_JPEGgdaladdo GPKG:C:\test\test_PNG_JPEG.gpkg:test_gpkg_PNG_JPEGgpkg pyramid_PNG8gdal_translate -of GPKG “C:\test\ortho_test.tif” “C:\test\test_PNG8.gpkg” -co TILE_FORMAT=PNG8gdaladdo GPKG:C:\test\test_PNG8.gpkg:test_gpkg_PNG8gpkg pyramid_WEBPgdal_translate -of GPKG “C:\test\ortho_test.tif” “C:\test\test_WEBP.gpkg” -co TILE_FORMAT=WEBPgdaladdo GPKG:C:\test\test_WEBP.gpkg:test_gpkg_WEBPJPEG2000gdal_translate -of JP2OpenJPEG “C:\test\ortho_test.tif” “C:\test\test_jpeg_2000.jpg"COG DEFLATEgdal_translate “C:\test\ortho_test.tif” “C:\test\test_cog.tif” -co TILED=YES -co COPY_SRC_OVERVIEWS=YES -co COMPRESS=DEFLATECOG_JPEGgdal_translate “C:\test\ortho_test.tif” “C:\test\test_cog_JPEG.tif” -co TILED=YES -co COPY_SRC_OVERVIEWS=YES -co COMPRESS=JPEGtifIn QGIS right click on the layer &gt; export &gt; save as &gt; (see the details in the picture under the table)MBTgdal_translate -of MBTILES “C:\test\ortho_test.tif” “C:\test\test_mbt.mbtiles"Creation commands for all the tested formats</p>
<h3 id="rendering-test-results">Rendering test results</h3>
<p>We have tested many formats, here is a table with the results of the size and rendering speed in QGIS and QField.<br/>
To analyze the speed we used <code>qgis_bench.exe -i 10 -p "C:\test\test.qgs" &gt;&gt; "C:\test\test.log</code>.<br/>
Qgis_bench is a tool that renders a QGIS project a number of times to get performance measurements. The parameter -i is to define the iterations and -p is the project used which contains only the generated raster.</p>
<p>FormatExtent [m]File size [GB]Total_avgTotal_maxdevTotal_minTotal_stdevgpkg JPEG52'880/29'2300.4250.242255.7815.539244.984gpkg PNG52'880/29'2302.9412.002490.328152.142259.859gpkg PNG_JPEG52'880/29'2300.4250.125256.8756.750245.172gpkg PNG852'880/29'2301.4283.875296.40612.625271.250gpkg WEBP52'880/29'2300.3330.238348.10973.534256.703gpkg pyramid_JPEG52'880/29'2300.51.0093.4062.3970.688gpkg pyramid_PNG52'880/29'2303.01.2083.2812.0730.688gpkg pyramid_PNG_JPEG52'880/29'2300.61.4914.3442.8531.016gpkg pyramid_PNG852'880/29'2301.61.5084.3752.8670.969gpkg pyramid_WEBP52'880/29'2300.41.3334.9063.5730.766JPEG200052'880/29'2301.113.888136.109122.2220.219COG DEFLATE52'880/29'2303.6264.427273.09425.411239.016COG_JPEG52'880/29'2301.014.778131.172116.3941.734tif52'880/29'2306.42.3676.7344.3671.672MBT52'880/29'2304.40.4694.6414.1710Comparison of file size and rendering speed of different raster formats. “Total” columns are rendering times in [s]. Lower file size is more storage friendly, lower Total_avg is more performant.</p>
<h2 id="analysis">Analysis</h2>
<h3 id="file-size">File size</h3>
<p>The Geopackage WEBP (with and without pyramid) has the best result for file size, but it is not _yet_supported by QField (from 1.6) and is only slightly smaller than the JPEG variant.</p>
<p>Plain GeoTiff, MBTiles, Cloud Optimized GeoTIFF (COG - DEFLATE mode) and Geopackages with PNG generate by far the largest file sizes (up to 20x larger) and are thus not recommended.</p>
<h3 id="rendering-speed">Rendering speed</h3>
<p>MBTiles are on average double as fast as JPEG Geopackages with pyramids which in turn are more than double as fast as GeoTIFF and 15x faster than COG.<br/>
Geopackages without pyramids are 200 to 400 times slower.</p>
<h2 id="conclusion">Conclusion</h2>
<p>Even though MBTiles render faster than the Geopackage pyramid JPEG, they come with an almost 10x bigger storage requirement which makes us say that the best offline raster format supported by QField is <strong>Geopackage pyramid JPEG</strong> or if you need transparency and slightly smaller files <strong>Geopackage pyramid WebP</strong>.</p>
<p>If you need transparency before QField 1.6, the best results are achieved with Geopackage pyramid PNG_JPEG.</p>
