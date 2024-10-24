---
source: "blog"
title: "Working with climate data in QGIS"
date: "2017-11-02T04:00:00-0500"
link: "https://lutraconsulting.co.uk/blog/2017/11/02/working-with-climate-data-in-qgis/"
draft: "false"
showcase: "planet"
subscribers: ["lutragis"]
author: "Lutra Consulting"
tags: []
---

<p>In this tutorial, we are going to explore methods of visualising climate data within QGIS using Crayfish plugin. We are going to use September 2017 datasets from NASA which will include Hurricane Irma.</p>

<!-- more -->

<h2 id="downloading-data">Downloading data</h2>
<p><strong>Note</strong>: You can download the processed data <a href="https://dl.dropboxusercontent.com/s/uq4hvn919359b9w/september_prec_wind_temp.grb.zip">here</a>. and skip to <strong>Viewing data in QGIS</strong>.</p>

<p>There are several resources available to obtain climate data. Due to the large volume of data and number of variables, the providers usually offer APIs to interact with dataset repository. But, you can download some datasets directly from their websites.</p>

<p><a href="http://apps.ecmwf.int/datasets/data/interim-full-daily/levtype=sfc/">ECMWF</a> and <a href="https://disc.gsfc.nasa.gov/mirador-guide">NASA</a> data portals offering such services.</p>

<p>In this tutorial, we are using <a href="https://disc.gsfc.nasa.gov/mirador-guide">NASA</a> portal to download NLDAS Secondary Forcing data for September 2017. Follow the instructions to batch download all the GRIB files using the script provided on their website.</p>

<h2 id="manipulating-data">Manipulating data</h2>
<p>Each grb file downloaded in the previous step is only for one time step containing multiple variables. You can extract certain variable and also merge the files using <a href="https://code.mpimet.mpg.de/projects/cdo/">Climate Data Operators</a>:</p>

<p><code class="highlighter-rouge">cdo mergetime *.grb september.grb</code></p>

<p><code class="highlighter-rouge">cdo select,name=var61,var33,var34,var11 september.grb september_prec_wind_temp.grb</code></p>

<p>The first command will merge all the times and generates a single GRIB file containing all the time step. The second command, extracts temperature, precipitation and wind data.</p>

<h2 id="viewing-data-in-qgis">Viewing data in QGIS</h2>
<p>To view the data, you will need <a href="https://www.lutraconsulting.co.uk/projects/crayfish">Crayfish plugin</a>. Download and install the plugin from the QGIS plugin repository.</p>

<p>Add the GRIB file as a Crayfish layer (under Plugins &gt; Crayfish &gt; Add Crayfish Layer). You should be able to see precipitation, temperature and wind data from the Crayfish panel. Note that the wind data contains vector in addition to grid.</p>

<p>You can use the slider to move the time. Read more on how to use <a href="https://www.lutraconsulting.co.uk/projects/crayfish/wiki">Crayfish plugin</a>.</p>

<p>To view wind data as trace animation, move the slider time to 12.09.2017 07:00 (or 319:00:16.04 if your time is set to relative) and select Vector Options. Set the parameters according to the dialog window below:</p>

<p><img alt="Vector Options" src="https://www.lutraconsulting.co.uk/img/posts/crayfish_irma_vector_option.png" /></p>

<p>You should now be able to see live traces of the wind from your QGIS canvas:</p>

<p><img alt="GIF animation of Irma" src="https://www.lutraconsulting.co.uk/img/posts/crayfish_irma.gif" /></p>

<p>You can plot the time series by clicking on the plot tool <img src="https://www.lutraconsulting.co.uk/img/posts/crayfish_wiki_gui_plot.png" /> from Crayfish panel:</p>

<center>
  
</center>

<p>To generate an animation of precipitation and wind, you need to first click on <img src="https://www.lutraconsulting.co.uk/img/posts/crayfish_wiki_gui_lock.png" /> from Crayfish panel and then enable wind vectors and precipitation grid. From Plugins &gt; Crayfish &gt; Export to animation you can generate animation of your time series.</p>

<center>
  
</center>

<h2 id="support-funding-crayfish-port-to-qgis-3">Support funding Crayfish port to QGIS 3</h2>
<p>If you are interested in using Crayfish in QGIS 3, help with <a href="https://www.lutraconsulting.co.uk/crowdfunding/qgis-crayfish-3/">this crowd-funding</a>.</p>

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
