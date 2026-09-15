---
source: "blog"
title: "Introducing the QCity Plugin"
date: "2026-07-09T04:15:53+0000"
link: "https://north-road.com/2026/07/09/introducing-the-qcity-plugin/"
draft: "false"
showcase: "planet"
subscribers: ["north_road"]
author: "North Road"
tags: ["modelling", "partners", "plugin", "qgis", "urban developemnt", "plugins", "qgis", "urban planning"]
languages: ["en_gb"]
available_languages: ["en_gb"]
---

<h2 style="text-align: center;">Urban Development Modelling in QGIS</h2>
<p><img alt="Qcity" class="aligncenter size-large wp-image-212972" height="576" src="/img/subscribers/north_road/introducing-the-qcity-plugin/QCity-Blog-banner-1024x576.webp" width="1024"/></p>
<h2 style="text-align: center;"></h2>
<p>Introducing <b>QCity</b>, a new plugin that brings advanced urban development modeling directly into QGIS. Developed in collaboration with the City of Canning (Perth, Western Australia), QCity enables urban planners to model project areas using predefined frameworks, providing visual 2D/3D insights and detailed statistical reports.</p>
<p>The plugin workflow begins in the “Project Setup” tab, where users either define a new Project Area boundary and input dwelling and parking (both car and bike) parameters, or load a previously saved site or QCity package:</p>
<p><img alt="" class="size-full wp-image-212974 aligncenter" height="883" src="/img/subscribers/north_road/introducing-the-qcity-plugin/qcity_002_project-setup.webp" width="506"/></p>
<p>Next, “Development Sites” are created within each Project Area. Development Sites options include:</p>
<ul>
<li>Setting the site’s status: constructed, proposed or modelled</li>
<li>Automatic calculation of the site’s floor space, car and bike parking (based on the specifications defined for the parent project area)</li>
<li>Setting the parameters for each Development Site</li>
</ul>
<p><img alt="" class="aligncenter size-full wp-image-212975" height="899" src="/img/subscribers/north_road/introducing-the-qcity-plugin/qcity_003_dev_sites.webp" width="510"/></p>
<p>Each Development Site can contain multiple Building Levels, which define the building floorplan and floors. Building Levels contain parameters to determine the composition of each level, such as:</p>
<ul>
<li>Usage: percent use for commercial, office and residential purposes</li>
<li>Residential: percent composition of 1-4+ bedroom dwellings</li>
<li>The building level height and height above ground</li>
<li>Based on the entered parameters, the area of Unallocated Residential Floorspace for each building level is automatically calculated</li>
</ul>
<p><img alt="" class="aligncenter size-full wp-image-212976" height="890" src="/img/subscribers/north_road/introducing-the-qcity-plugin/qcity_004_bldg_levels.webp" width="508"/></p>
<p>Finally, statistics are calculated for an entire Project Area, such as the total amount of commercial, office and residential floorspace, number of dwellings, and car and bicycle parking availability.</p>
<p><img alt="" class="aligncenter size-full wp-image-212977" height="891" src="/img/subscribers/north_road/introducing-the-qcity-plugin/qcity_005_statistics.webp" width="508"/></p>
<p>To see the workflow in action, watch the video below where a new project is created with development sites and building levels.</p>
<p></p>
<p>This is the first release of QCity, and accordingly it is currently available as an experimental plugin in the <a href="https://plugins.qgis.org/plugins/qcity/" rel="noopener" target="_blank">QGIS plugin repository</a>. This initial QCity version is designed for use in Australia only, however future development will enable its use in other parts of the world. On the <a href="https://github.com/north-road/QCity/issues" rel="noopener" target="_blank">QCity code repoistory</a> you can see some of the additional capabilities we are thinking of adding. QCity requires QGIS 4.0 or later.</p>
<p>For an in depth overview of the creation of QCity and a demonstration of its capabilities, please join us for the <a href="https://qgis-australia.org/2026/06/16/webinar-July.html" rel="noopener" target="_blank">QGIS Australia July webinar</a> where Gabriel Diosan, Senior Strategic Planning Spatial Analyst from the City of Canning will present <b><i>Urban Development Modelling in QGIS using QCity:</i></b></p>
<ul>
<li>1pm (AEST)Thursday 16th July (<a href="https://meet.google.com/fwi-wqyp-vic" rel="noopener" target="_blank">Meeting link</a>)</li>
<li>If you can’t make the webinar, subscribe to the <a href="https://www.youtube.com/@QGISAustralia" rel="noopener" target="_blank">QGIS Australia YouTube Channel</a> to watch it later.</li>
</ul>
<p>For more information:</p>
<ul>
<li><a href="https://north-road.github.io/QCity/" rel="noopener" target="_blank">QCity Documentation</a></li>
<li><a href="https://github.com/north-road/QCity" rel="noopener" target="_blank">QCity Homepage</a></li>
<li>Email us at <a href="mailto:info@north-road.com">info@north-road.com</a> if you have an idea to enhance QCity, or want to speed up any of its capabilities, or have another plugin or QGIS feature you wish for us to help you with.</li>
</ul>
