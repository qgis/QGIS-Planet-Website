---
source: "blog"
title: "Oceancolor Data Downloader v1.0 for QGIS"
date: "2015-02-12T03:05:20+0000"
link: "https://ieqgis.com/2015/02/12/oceancolor-data-downloader-v1-0-for-qgis/"
draft: "false"
showcase: "planet"
subscribers: ["ireland_qgis_user_group_blog"]
author: "Ireland QGIS User Group Blog"
tags: ["news", "plugin", "nasa", "qgis"]
---

<div class="wp-caption alignnone" id="attachment_702" style="width: 555px;"><a href="https://ieqgis.files.wordpress.com/2015/02/aqua-modis-sst-2015-01-13.png"><img alt="Aqua Modis SST 2015-01-13" class="wp-image-702 size-large" height="545" src="https://ieqgis.files.wordpress.com/2015/02/aqua-modis-sst-2015-01-13.png?w=545&#038;h=545" width="545" /></a><p class="wp-caption-text" id="caption-attachment-702">Sea Surface Temperature data downloaded by Oceancolor Data Downloader.</p></div>
<p><span style="color: #f7f9ff; text-decoration: underline;"><a href="https://github.com/antarctica/oceancolor_downloader">The Oceancolor Data Downloader</a></span> is a new plugin for QGIS from the <span style="color: #f7f9ff; text-decoration: underline;"><a href="http://www.antarctica.ac.uk//about_bas/our_organisation/eid/magic.php">Mapping and Geographic Information Centre</a></span> of the British Antarctic Survey that downloads Oceancolor and Sea Surface Temperature data from NASA&#8217;s <span style="color: #f7f9ff; text-decoration: underline;"><a href="http://oceancolor.gsfc.nasa.gov/">Oceancolor website</a></span>. The plugin currently downloads three datasets:</p>
<ul>
<li>MODIS AQUA chlorophyll concentration</li>
<li>SeaWiFS chlorophyll concentration</li>
<li>MODIS AQUA night time Sea Surface Temperatures</li>
</ul>
<p>The data accessed includes daily, 8 day, monthly and yearly composites, all of which can be saved to disk while downloading. Future plans for the plugin include additional access to other datasets such as ocean <span style="color: #f7f9ff; text-decoration: underline;"><a href="http://www.science.oregonstate.edu/ocean.productivity/">Net Primary Production</a></span>, selection by bounding box, the ability to save in other formats, a progress bar <em>etc</em>.</p>
<p>I used the plugin to download global Sea Surface Temperatures for the 13th Jan 2015. I then used shapefiles from <span style="color: #f7f9ff; text-decoration: underline;"><a href="http://www.naturalearthdata.com/">Natural Earth</a></span> to create a simple basemap. I finally chose the IBCAO Polar Stereographic projection (<span style="color: #f7f9ff; text-decoration: underline;"><a href="http://epsg.io/3996">EPSG: 3996</a></span>) to create a map centred on the North Pole.</p>
<p>If you use the plugin to produce published research, please cite:</p>
<p><a href="http://dx.doi.org/10.5281/zenodo.15018"><img alt="10.5281/zenodo.15018" src="https://zenodo.org/badge/doi/10.5281/zenodo.15018.svg" /></a></p>
