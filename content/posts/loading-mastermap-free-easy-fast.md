---
source: "blog"
title: "Loading MasterMap: Free, Easy and Fast"
date: "2015-02-23T08:00:00-0600"
link: "https://lutraconsulting.co.uk/blog/2015/02/23/loading-mastermap-free-easy-fast/"
draft: "false"
showcase: "planet"
subscribers: ["lutragis"]
author: "Lutra Consulting"
tags: []
---

<p>We've developed a new graphical loading tool for OS MasterMap data focussing on usability and performance to make it easy to load national <a href="http://www.ordnancesurvey.co.uk/business-and-government/products/mastermap-products.html" rel="nofollow" target="_blank">Ordnance Survey MasterMap</a> datasets in a matter of hours.</p>

<p><img alt="OS Translator II - Load OS MasterMap into PostGIS quickly, easily and for free" src="https://www.lutraconsulting.co.uk/img/posts/os-translator-ii.png" /></p>

<!-- more -->

<p>The tool is <a href="https://www.lutraconsulting.co.uk/projects/ostranslator-ii/">OS Translator II</a> - it makes use of the excellent <a href="http://www.gdal.org/" rel="nofollow" target="_blank">GDAL library</a> and is available now in the <a href="http://plugins.qgis.org/plugins/OSTranslatorII/" target="_blank">official QGIS Plugins repository</a>.</p>

<p>This blog post talks about some simple benchmarks we've carried out.</p>

<p>If you are interested in using this tool and not familiar with Postgresql/PostGIS, you can sign up to one of our <a href="https://www.lutraconsulting.co.uk/support/">support packages</a> and we will be able to set you up and running within a couple of hours!</p>

<h2>Results</h2>

<p>National load times were as follows:</p>

<ul>
    <li><strong>MasterMap Topography (National)</strong> 20 hrs 21 mins <sup>1</sup></li>
    <li><strong>MasterMap ITN (National)</strong> &lt; 6 mins</li>
</ul>

<p>Installing PostgreSQL, PostGIS and QGIS took less than 10 minutes.</p>

<p><sup>1</sup> This is the most time-consuming test which filled the SSD on the first attempt. Importing to a tablespace on the main HDD completed after 20.3 hours but showed the import of tile 1592959-TR0585-5c3268.gz to have failed with <a href="https://github.com/lutraconsulting/ostranslator-ii/issues/6" rel="nofollow" target="_blank">this error</a>. Until this issue is resolved the tile would need to be loaded and de-duplicated manually (e.g. using ogr2ogr to import and a SQL query to de-duplicate) to complete the dataset. De-duplication removes duplicate features caused by the chunking / supply process.</p>

<h2>Comparison With Other Open Source Tools</h2>

<p>We were curious as to how OS Translator II load times compared with other open loading methods so we did some basic tests using the "SU" tile of MasterMap Topography and ITN datasets and compared it with the popular <a href="https://github.com/AstunTechnology/Loader" rel="nofollow" target="_blank">Loader</a> scripts. The results looked like this:</p>

<p><img alt="OS Translator II Benchmarks" src="https://www.lutraconsulting.co.uk/img/posts/os-translator-2-benchmarks.png" /></p>

<p>Please note that OS Translator II had an <em>unfair</em> advantage in these tests as it automatically takes advantage of multiple-CPU cores whereas Loader presently does not.</p>

<h2>Hardware and Software</h2>

<p>We used the following hardware and software configuration:</p>

<ul>
    <li><strong>CPU</strong> Intel Core i7 4790K (Haswell) @ 4GHz</li>
    <li><strong>Memory</strong> 32GB PC3-12800</li>
    <li><strong>Disk(s)</strong> Samsung 840 EVO 250GB SSD and Seagate Barracuda ST2000DM001 2TB HDD<sup>2</sup></li>
    <li><strong>OS</strong> Microsoft Windows 7 Professional (64-bit)</li>
    <li><strong>PostgreSQL</strong> 9.4.1 (x64)</li>
    <li><strong>PostGIS</strong> 2.1.5 (x64)</li>
    <li><strong>QGIS</strong> 2.6.1 (Brighton)</li>
    <li><strong>OS Translator II</strong> 1.0</li>
    <li><strong>Python</strong> 2.7.9 (win32)</li>
    <li><strong>lxml</strong> 3.2.3 (win32)</li>
    <li><strong>Loader</strong> Master (067a511313, 20<sup>th</sup> February 2014)</li>
</ul>

<p><sup>2</sup> Operating system and source gml.gz files located on the SSD and default PostgreSQL tablespace stored on secondary 2TB HDD.</p>

<h2>PostgreSQL Configuration</h2>

<p>The following changes were made to the default PostgreSQL configuration:</p>

<ul>
    <li><strong>shared_buffers</strong> 512MB</li>
    <li><strong>work_mem</strong> 16MB</li>
    <li><strong>maintenance_work_mem</strong> 128MB / 1024MB<sup>3</sup></li>
    <li><strong>checkpoint_segments</strong> 6</li>
    <li><strong>random_page_cost</strong> 2.0</li>
    <li><strong>fsync</strong> off</li>
</ul>

<p><sup>3</sup> maintenance_work_mem was set to 1024MB for the national load of MasterMap Topography layer only.</p>

<p><span><i class="fa fa-exclamation-triangle"></i></span> Turning fsync off is dangerous and can lead to data loss in the event of an unexpected power outage. Always switch fsync back on after loading and never use this option on a database containing critical data.</p>

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
