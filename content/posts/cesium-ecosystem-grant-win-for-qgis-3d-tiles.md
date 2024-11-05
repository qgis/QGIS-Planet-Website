---
source: "blog"
title: "Cesium Ecosystem Grant Win for QGIS 3D Tiles!"
date: "2023-06-01T03:23:23+0000"
link: "https://north-road.com/2023/06/01/cesium-ecosystem-grant-win-for-qgis-3d-tiles/"
draft: "false"
showcase: "planet"
subscribers: ["north_road"]
author: "North Road"
tags: ["3d tiles", "core feature development", "integrations", "partners", "qgis"]
---

<div class="ql-block">Success! <a class="ql-link" href="https://www.lutraconsulting.co.uk/" rel="noopener noreferrer" target="_blank">Lutra </a>and North Road have been rewarded a Cesium Ecosystem Grant to provide access to 3D tiles within QGIS. We will be creating the ability for users to visualise 3D Tiles in QGIS alongside other standard geospatial sources in both 3D and 2D map views.</div>
<figure class="wp-caption aligncenter" id="attachment_212525" style="width: 680px;"><img alt="3D Tiles Cesium integration ecosystem diagram" class=" wp-image-212525" height="641" src="https://north-road.com/wp-content/uploads/2023/05/Cesium-integration-ecosystem-diagram_QGISv2-1024x964.png" width="680" /><figcaption class="wp-caption-text" id="caption-attachment-212525">3D Tiles Cesium integration ecosystem</figcaption></figure>
<div></div>
<div class="ql-block">We are very excited about it, but to be included in the first cohort of awardees is also an added honour! We share this distinction with 3 other recipients:</div>
<ul>
<li class="ql-block"><a class="ql-link" href="https://www.linkedin.com/in/ACoAAA1MAWYBhe7u7Uc40tXIg_s6awS97NHgGYs" rel="noopener noreferrer" target="_blank">Peter Kimberley</a>, <a class="ql-link" href="https://www.linkedin.com/company/gradata-systems/" rel="noopener noreferrer" target="_blank">Gradata Systems Pty Ltd</a>, Canberra, Australia Vietnam War Missing in Action (MIA) Support</li>
<li class="ql-block"><a class="ql-link" href="https://www.linkedin.com/in/ACoAADsgMRwBYuXpHANwZ5tTIbjtE4OP7Ky2UTQ" rel="noopener noreferrer" target="_blank">HIdenori Watanave</a>, <a class="ql-link" href="https://www.linkedin.com/company/university-of-tokyo/" rel="noopener noreferrer" target="_blank">The University of Tokyo</a>, Tokyo, Japan, Digital Archives of War and Disasters</li>
<li class="ql-block"><a class="ql-link" href="https://www.linkedin.com/in/ACoAAB8in-kBGeFovnyDWRugvSvMD-y0dYpVZAE" rel="noopener noreferrer" target="_blank">Ethan Berg</a>, <a class="ql-link" href="https://www.linkedin.com/company/agoraworld-io/" rel="noopener noreferrer" target="_blank">Agora World</a>, Philadelphia, PA, USA, GeoForAll: Simplifying 3D Geospatial Metaverse Creation</li>
</ul>
<div class="ql-block">The opportunity was brought to our attention by our friends over at <a class="ql-link" href="https://www.nearmap.com/au/en" rel="noopener noreferrer" target="_blank">Nearmap</a>, which, along with the existence of this grant, shows how the geospatial community is working together by evolving the Open Source Economy. A movement close to our hearts and our core business. Working between commercial software and open-source, Cesium&#8217;s <a class="ql-link" href="https://cesium.com/why-cesium/open-ecosystem/cesium-business-model/" rel="noopener noreferrer" target="_blank">business model</a> recognises the legitimacy of Open Source Software for use as a geospatial standard operating procedure by promoting openness and interoperability.</div>
<div class="ql-block"></div>
<div class="ql-block">Our team of <a class="ql-link" href="https://www.linkedin.com/in/nyall-dawson-18b6016a/" rel="noopener noreferrer" target="_blank">Nyall Dawson</a> and <a class="ql-link" href="https://www.linkedin.com/in/martin-dobias-92590339/" rel="noopener noreferrer" target="_blank">Martin Dobias</a> will create a new layer type, QgsTiledMeshLayer, allowing for direct access to Cesium 3D tile sources alongside the other supported geospatial layer types within QGIS. This will include visualisation of the tile data in both 3D and 2D map views (feature footprints). It will fulfill a critical need for QGIS users, permitting access to 3d data provided by their respective government agencies to work alongside all their other standard geospatial layers (vector, raster, point clouds). By making 3D Tiles a first class citizen in QGIS we help strengthen the case that those agencies should be providing their data in the Cesium format (as opposed to any proprietary alternatives).</div>
<div class="ql-block">
<figure class="wp-caption aligncenter" id="attachment_212532" style="width: 1024px;"><img alt="Proposed Technical Architecture Cesium QGIS" class="size-full wp-image-212532" height="593" src="https://north-road.com/wp-content/uploads/2023/05/Proposed-Technical-Architecture-Cesium-QGIS-v2-e1684390715529.png" width="1024" /><figcaption class="wp-caption-text" id="caption-attachment-212532">Proposed Technical Architecture for Cesium 3D Tiles in QGIS</figcaption></figure>
</div>
<div class="ql-block"></div>
<div>
<div class="ql-block">Here&#8217;s a breakdown of what we will be doing:</div>
<ul>
<li>Develop a new QGIS layer type “QgsTiledMeshLayer”</li>
<li>Develop a parser for 3D Tiles format, supporting Batched 3D Model (with a reasonable set of glTF 2.0 features)</li>
<li>Develop a 3D renderer which dynamically loads and displays features from 3D Tiles based on appropriate 3D view level of detail. (A similar approach has already been implemented in QGIS for optimised viewing of point cloud data).</li>
<li>Develop a 2D renderer for 3D Tiles, which will display the footprints of 3D tile features in 2D QGIS map views. Just like the 3D renderer, the 2D renderer will utilise map scale information to dynamically load 3D tiles and display a suitable level of detail for the footprints.</li>
<li>Users will have full control over the appearance of the 2D footprints, with support for all of QGIS’ extensive polygon symbology options.</li>
<li>By permitting users to view the 2D footprints of features, we will promote use of Cesium 3D Tiles as a suitable source of cartographic data, eg display of authoritative building footprints supplied by government agencies in the Cesium 3D Tile format.</li>
</ul>
<p>Through past partnerships, North Road and Lutra Consulting have developed and extended the 3D mapping functionality of QGIS. To date, all the framework for mature, performant 3D scenes including vector, mesh, raster and point cloud sources are in place. We are now ready to extend the existing functionality with Cesium 3D tiles support as QGIS 3D engine already implements most of the required concepts, such as out of core rendering and hierarchical level of detail (tested with point clouds with billions of points).</p>
</div>
<p>So there we go! Working together collaboratively with Lutra Consulting on another great addition to QGIS 3D Functionality thanks to Cesium Ecosystem Grants. Stay tuned on our social channels to find out when it will be released in QGIS.</p>
<p><img alt="Cesium Ecosystem grant Badge" class="wp-image-212524 aligncenter" height="250" src="https://north-road.com/wp-content/uploads/2023/05/73304078772281.png" width="250" /></p>
<p>&nbsp;</p>
<div class="supsystic-social-sharing supsystic-social-sharing-package-flat supsystic-social-sharing-hide-on-homepage supsystic-social-sharing-spacing supsystic-social-sharing-content supsystic-social-sharing-content-align-left" style="font-size: 0.7em!important; display: none;"><a class="social-sharing-button sharer-flat sharer-flat-1 counter-standard without-counter twitter" href="https://twitter.com/share?url=https%3A%2F%2Fnorth-road.com%2F2023%2F06%2F01%2Fcesium-ecosystem-grant-win-for-qgis-3d-tiles%2F&amp;text=Cesium+Ecosystem+Grant+Win+for+QGIS+3D+Tiles%21" rel="nofollow" target="_blank" title="Twitter"><i class="fa-ssbs fa-ssbs-fw fa-ssbs-twitter"></i><div class="counter-wrap standard"><span class="counter">0</span></div></a><a class="social-sharing-button sharer-flat sharer-flat-1 counter-standard without-counter linkedin" href="https://www.linkedin.com/shareArticle?mini=true&amp;title=Cesium+Ecosystem+Grant+Win+for+QGIS+3D+Tiles%21&amp;url=https%3A%2F%2Fnorth-road.com%2F2023%2F06%2F01%2Fcesium-ecosystem-grant-win-for-qgis-3d-tiles%2F" rel="nofollow" target="_blank" title="Linkedin"><i class="fa-ssbs fa-ssbs-fw fa-ssbs-linkedin"></i><div class="counter-wrap standard"><span class="counter">0</span></div></a><a class="social-sharing-button sharer-flat sharer-flat-1 counter-standard without-counter facebook" href="http://www.facebook.com/sharer.php?u=https%3A%2F%2Fnorth-road.com%2F2023%2F06%2F01%2Fcesium-ecosystem-grant-win-for-qgis-3d-tiles%2F" rel="nofollow" target="_blank" title="Facebook"><i class="fa-ssbs fa-ssbs-fw fa-ssbs-facebook"></i><div class="counter-wrap standard"><span class="counter">0</span></div></a></div>
