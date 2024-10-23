---
source: "blog"
title: "FOSS4G Workshop: Working with mesh layer in QGIS"
date: "2019-08-26T19:00:01-0500"
link: "https://lutraconsulting.co.uk/blog/2019/08/26/foss4g-workshop/"
draft: "false"
showcase: "planet"
subscribers: ["lutragis"]
author: "Lutra Consulting"
tags: []
---

<p>We presented a workshop on Mesh layer in QGIS during FOSS4G in Bucharest. Below is step-by-step guide for those who’d like to know more about mesh layers in QGIS.</p>

<!-- more -->

<h2 id="introduction">Introduction</h2>

<p>Data for this tutorial can be found <a href="https://www.dropbox.com/s/ugvf9fbleo63gdj/Working%20with%20mesh%20layer.zip?dl=0">here</a>.</p>

<p>In this tutorial, we are going to work with a mesh layer in QGIS.
Throughout this tutorial you will learn to:</p>

<ul>
  <li>
    <p>Load a mesh layer</p>
  </li>
  <li>
    <p>Change symbology</p>
  </li>
  <li>
    <p>Working with time</p>
  </li>
  <li>
    <p>Creating time series/cross section plots</p>
  </li>
  <li>
    <p>Export mesh</p>
  </li>
  <li>
    <p>Creating animation</p>
  </li>
</ul>

<p>For the purpose of this tutorial, we are going to use the <a href="https://apps.ecmwf.int/datasets/">ERA5 dataset
from ECMWF</a>:</p>

<p>(the data in the first link should contain what you need to proceed with
this tutorial).</p>

<h2 id="loading-mesh-in-qgis">Loading mesh in QGIS</h2>

<p>Before loading the mesh layer in QGIS, we are going to add the world map
as a background layer.</p>

<p><strong>In QGIS, from the Browser panel, browse to the downloaded data &gt;
Working with mesh layer &gt; vector_data.gpkg and add world_map layer.</strong></p>

<p align="center">
    <img src="https://www.lutraconsulting.co.uk/img/posts/foss4g_mdal_01.png" />
  </p>

<p>You can change the project background layer to blue to have an image
similar to the one below:</p>

<p align="center">
  <img src="https://www.lutraconsulting.co.uk/img/posts/foss4g_mdal_02.png" />
</p>

<p>To add the mesh layer:</p>

<p><strong>In QGIS, from the Browser panel, browse to the downloaded data &gt;
Working with mesh layer and add Hurricane Michael data from Copernicus
ECMWF.nc as a mesh layer (not raster).</strong></p>

<p>Depending on your QGIS settings, the CRS setting window might appear.
Ensure you assign EPSG:4326 to the mesh layer.</p>

<p align="center">
  <img src="https://www.lutraconsulting.co.uk/img/posts/foss4g_mdal_03.png" />
</p>

<h3 id="mesh-layer-symbology-and-styling">Mesh layer symbology and styling</h3>

<p>To change the mesh layer style:</p>

<p><strong>In QGIS, from the layers panel, select the mesh layer and press F7</strong></p>

<p><strong>The layer styling panel will appear on the right of your QGIS window</strong></p>

<p align="center">
  <img src="https://www.lutraconsulting.co.uk/img/posts/foss4g_mdal_04.png" />
</p>

<p>Within this panel, you can switch on/off quantities, vectors, style the
layer and browse through time.</p>

<p>Below, we are going to switch on the wind data and style it:</p>

<p align="center">
  <img src="https://www.lutraconsulting.co.uk/img/posts/foss4g_mdal_05.png" />
</p>

<p><strong>On the Style panel, click on Symbology tab</strong></p>

<ul>
  <li>**Under Settings section, click on the icon in front of 10 metre
    <blockquote>
      <p>wind to switch on the quantity**</p>
    </blockquote>
  </li>
  <li>
    <p><strong>Under color ramp section:</strong></p>

    <ul>
      <li>
        <p><strong>Set Min to 0</strong></p>
      </li>
      <li>
        <p><strong>Set Max to 20</strong></p>
      </li>
      <li>
        <p><strong>Interpolation to Linear</strong></p>
      </li>
      <li>
        <p><strong>Color ramp to Blues (Inverted)</strong></p>
      </li>
      <li>
        <p><strong>Mode to Equal Interval</strong></p>
      </li>
      <li>
        <p><strong>Classes to 11</strong></p>
      </li>
    </ul>
  </li>
</ul>

<p>You can change the blending mode to Darken and you will see an image
similar to the one below:</p>

<p align="center">
  <img src="https://www.lutraconsulting.co.uk/img/posts/foss4g_mdal_06.png" />
</p>

<p>To style vector component of the wind data:</p>

<p align="center">
  <img src="https://www.lutraconsulting.co.uk/img/posts/foss4g_mdal_07.png" />
</p>

<ul>
  <li>**Under Settings section, click on the arrow icon in front of 10
    <blockquote>
      <p>metre wind to switch on the vector**</p>
    </blockquote>
  </li>
  <li>
    <p><strong>Click on the vector settings section:</strong></p>

    <ul>
      <li>
        <p><strong>Enable the option for Display Vectors on User Grid</strong></p>

        <ul>
          <li>
            <p><strong>X Spacing: 10 px</strong></p>
          </li>
          <li>
            <p>**Y Spacing: 10 px **</p>
          </li>
        </ul>
      </li>
      <li>
        <p><strong>For Arrow Length, select Scaled to Magnitude</strong></p>

        <ul>
          <li><strong>Set the Scale by a Factor of 1</strong></li>
        </ul>
      </li>
    </ul>
  </li>
</ul>

<p align="center">
  <img src="https://www.lutraconsulting.co.uk/img/posts/foss4g_mdal_08.png" />
</p>

<h3 id="working-with-time">Working with time</h3>

<p>If your mesh layer has time dimension, you should be able to browse
through time using the slider provided under the settings tab:</p>

<p align="center">
  <img src="https://www.lutraconsulting.co.uk/img/posts/foss4g_mdal_09.png" />
</p>

<p>Note that the time reference does not always parse correctly. To change
the time (if you know the correct format and starting date/time):</p>

<p><strong>Click on the setting in front of time</strong></p>

<p><strong>In the new window:</strong></p>

<ul>
  <li>
    <p><strong>Use absolute time</strong></p>
  </li>
  <li>
    <p><strong>Reference date/time: 29.09.2018 04:00:00</strong></p>
  </li>
</ul>

<p align="center">
  <img src="https://www.lutraconsulting.co.uk/img/posts/foss4g_mdal_10.png" />
</p>

<h3 id="plotting-time-series-and-profiles">Plotting time series and profiles</h3>

<p>To plot time series, you will need to install Crayfish plugin from QGIS
plugin repository. Once the plugin is installed:</p>

<p><strong>In QGIS, from the main menu &gt; Mesh &gt; Crayfish &gt; Plot</strong></p>

<p>An empty plot appears at the bottom of your QGIS window. To generate
time series for multiple points on the map:</p>

<p><strong>Make sure you have the following settings</strong></p>

<p><strong>Layer: Hurricane Michale data from Copernicus ECMWF</strong></p>

<p><strong>Plot: Time series</strong></p>

<p><strong>Group: [current]</strong></p>

<p><strong>And then click on From Map: Point</strong></p>

<p><strong>Hold Ctrl key on your keyboard and click on the locations you want to
plot time series:</strong></p>

<p align="center">
  <img src="https://www.lutraconsulting.co.uk/img/posts/foss4g_mdal_11.png" />
</p>

<p>A series of graphs will be plotted for each point with matching colours.</p>

<p>You can also create long profile (including aggregated long plot) for a
specific time step.</p>

<h2 id="export-mesh-to-vector-or-raster">Export mesh to vector or raster</h2>

<p>To export mesh to a raster or vector, you can use the processing
toolbox:</p>

<p><strong>In QGIS, from the main menu &gt; Processing &gt; Toolbox</strong></p>

<p><strong>Under Crayfish algorithm, double click on Rasterize</strong></p>

<p><strong>A new window will appear:</strong></p>

<ul>
  <li>
    <p><strong>For Input mesh layer select Hurricane Michale data from Copernicus ECMWF</strong></p>
  </li>
  <li>
    <p><strong>For Minimum extent click on … and select Use Layer Extent. In the new pop-up, select Hurricane Michale data from Copernicus ECMWF</strong></p>
  </li>
  <li>
    <p><strong>For Map units per pixel, type: 0.500</strong></p>
  </li>
  <li>
    <p><strong>For Dataset group, select 2 metre temperature</strong></p>
  </li>
  <li>
    <p><strong>For Timestep, select 29 days, 6:00:00</strong></p>
  </li>
  <li>
    <p><strong>Click Run</strong></p>
  </li>
</ul>

<p align="center">
  <img src="https://www.lutraconsulting.co.uk/img/posts/foss4g_mdal_12.png" />
</p>

<p>Similarly, you can export your mesh to points or polygon for each time
step.</p>

<h3 id="export-to-animation">Export to animation</h3>

<p>To export to animation, you can set up a print layout template.</p>

<p><strong>Ensure you have selected 10 m wind quantity from the mesh layer
properties panel</strong></p>

<p><strong>Right-click on Hurricane Michael data from Copernicus ECMWF and select
Export to animation</strong></p>

<p><strong>Set the correct parameters for start time/end time</strong></p>

<p><strong>Set the values for time, legend, title, etc</strong></p>

<p><strong>Set the filename for the animation file</strong></p>

<h3 id="mesh-calculator">Mesh calculator</h3>

<p>Mesh calculator is similar to the Raster calculator with the following
added functionalities:</p>

<ul>
  <li>
    <p>Aggregate functions, e.g. calculate maximum values over time</p>
  </li>
  <li>
    <p>Time filter</p>
  </li>
</ul>

<p><strong>Try to calculate the maximum precipitation values for Hurricane
Michale data from Copernicus ECMWF dataset</strong></p>
