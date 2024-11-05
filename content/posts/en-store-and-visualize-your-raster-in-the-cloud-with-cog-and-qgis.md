---
source: "blog"
title: "Store and visualize your raster in the Cloud with COG and QGIS"
date: "2020-09-14T11:20:12"
link: "https://oslandia.com/en/2020/09/14/en-store-and-visualize-your-raster-in-the-cloud-with-cog-and-qgis/"
draft: "false"
showcase: "planet"
subscribers: ["qgis_oslandia"]
author: "QGIS Oslandia"
tags: ["gis", "non classé", "qgis", "sig", "", "cloud", "gdal"]
---

<p>We have recently been working for the French Space Agency ( <a href="https://www.cnes.fr/">CNES</a> ) who needed to store and visualize satellite rasters in a cloud platform. They want to access the image raw data, with no transformation, in order to fullfill deep analysis like instrument calibration. Using classic cartographic server standard like WMS or TMS is not an option because those services transform datasets in already rendered tiles.</p>
<p>We chose to use a quite recent format managed by GDAL, the <a href="https://www.cogeo.org/"><strong>COG (Cloud Optimize Geotiff) </strong></a>and target <a href="https://www.ovhcloud.com">OVH</a> cloud platform for it provides <a href="https://www.openstack.org/">OpenStack</a>, a open source cloud computing platform.</p>
<h2>How it works</h2>
<p>A COG file is a GEOTiff file which inner structure is tiled, meaning that the whole picture is divided in fixed size tile (256 x 256 pixels for instance) so you can efficiently retrieve parts of the raster. In addition to the HTTP/1.1 standard feature <em>range request, </em>it is possible to get specific tiles of an image <strong>through the network without downloading the entire raster</strong>.</p>
<p>We used a service provided by OpenStack, called <a href="https://en.wikipedia.org/wiki/Object_storage">Object Storage</a> to serve the COG imagery. Object storage allows to store and retrieve file as objects using HTTP GET/POST requests.</p>
<h5>Why not WCS ?</h5>
<p><a href="https://www.ogc.org/standards/wcs">Web Coverage Service</a> standard could have been an option. A WCS server can serve raw data according to a given geographic extent. It&#8217;s completely possible to deploy a container or a VPS (Virtual Private Server) running a WCS Server in a cloud plateform. The main advantages of the COG solution over WCS Server is that you don&#8217;t have to deal with the burden of deploying a server, like giving it ressources, configuring load balancing, handle updates, etc&#8230;</p>
<p>The beauty of COG solution is its simplicity. It is only HTTP requests, and everything else (rendering for instance) is done on the client side.</p>
<h2>Step by step</h2>
<p>Here are the different steps you&#8217;d have to go through if you&#8217;re willing to navigate in a big raster image directly from the cloud.</p>
<p>First, let&#8217;s generate a COG file</p>
<div class="code-embed-wrapper"> <pre class="language-bash code-embed-pre"><code class="language-bash code-embed-code">gdal_translate inputfile.tif cogfile.tif -co TILED=YES -co COPY_SRC_OVERVIEWS=YES -co COMPRESS=DEFLATE</code></pre> <div class="code-embed-infos"> </div> </div>
<p>Install your openstack-client, it can be achieved easily with Python pip install command line</p>
<div class="code-embed-wrapper"> <pre class="language-bash code-embed-pre"><code class="language-bash code-embed-code">$ pip install python-openstackclient</code></pre> <div class="code-embed-infos"> </div> </div>
<p>Next, configure your openstack client in order to generate an athentification token. To do so you need to <a href="https://help.dreamhost.com/hc/en-us/articles/228047207-How-to-download-your-DreamCompute-openrc-file">download your project specific openrc file</a> to setup your environment)</p>
<div class="code-embed-wrapper"> <pre class="language-bash code-embed-pre"><code class="language-bash code-embed-code">$ source myproject-openrc.sh
Please enter your OpenStack Password for project myproject as user myuser:
**********
$ openstack token issue                                 
+------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Field      | Value                                                                                                                                                                                   |
+------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| expires    | 2020-07-21T08:15:12+0000                                                                                                                                                                |
| id         | xxxx_my_token_xxxx
| project_id | 97e2e750f1904b41b76f80a50dabde0a                                                                                                                                                        |
| user_id    | 18f7ccaf1a2d4344a4e35f0d84eb065e                                                                                                                                                        |
+------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+</code></pre> <div class="code-embed-infos"> </div> </div>
<p>You are now good to push you COG file to the cloud instance</p>
<div class="code-embed-wrapper"> <pre class="language-bash code-embed-pre"><code class="language-bash code-embed-code">openstack object create MyContainer cogfile.tif --name cogfile.tif</code></pre> <div class="code-embed-infos"> </div> </div>
<p>Before starting QGIS, 2 environment variables need to be set.  (replace <em>xxxx_my_token_xxxx</em> with the token you&#8217;d just come to generate)</p>
<div class="code-embed-wrapper"> <pre class="language-bash code-embed-pre"><code class="language-bash code-embed-code">$ export SWIFT_AUTH_TOKEN=xxxx_my_token_xxxx
$ export SWIFT_STORAGE_URL=https://storage.sbg.cloud.ovh.net/v1/AUTH_$OS_PROJECT_ID</code></pre> <div class="code-embed-infos"> </div> </div>
<p>It can also be done directly from the QGIS Python console by setting those variable using the <a href="https://docs.python.org/3/library/os.html#os.environ"><em>os.environ.</em></a></p>
<p>Finally, add a cloud raster data source in in QGIS</p>
<p><img alt="" class="size-full wp-image-5822 aligncenter" height="373" src="https://oslandia.com/wp-content/uploads/2020/07/cog_source.png" width="882" /></p>
<p>You can now navigating into your image directly reading it from the cloud</p>
<div class="wp-caption aligncenter" id="attachment_5823" style="width: 1138px;"><img alt="" class="wp-image-5823 size-full" height="804" src="https://oslandia.com/wp-content/uploads/2020/07/democog.gif" width="1128" /><p class="wp-caption-text">© CNES 2018, Distribution Airbus DS</p></div>
<h2>Performances</h2>
<p>While panning in the map, QGIS will download only few tiles from the image in order to cover the view extent. The display latency that you could see in the video depends essentially on:</p>
<ul>
<li>The number of band of your image</li>
<li>The pixel size</li>
<li>Your internet connection (mine, the one use for the video, is not an awesome one)</li>
</ul>
<p>Note that the white flickering that you could see when you move in the map and the raster is refreshed should be removed in next version of QGIS according to this <a href="https://github.com/qgis/QGIS-Enhancement-Proposals/issues/181">QEP.</a></p>
<h2>What&#8217;s next ?</h2>
<p>Thanks so much to the <a href="https://gdal.org/">GDAL</a> and QGIS contributors for adding such a nice feature ! It brings lots of possibilities for organizations that have to deal with great number of big raster and just want to explore part of it.</p>
<p>We are already thinking about further improvments (ease authentification, better integration with processing&#8230;), so if you&#8217;re willing to fund them or just want to know more about QGIS, feel free to contact us at <a href="mailto:infos+data@oslandia.com">infos+data@oslandia.com</a>. And please have a look at our <a href="https://qgis.oslandia.com">support offering for QGIS</a>.</p>
