---
source: "blog"
title: "Google Summer of Code 2021 : Virtual Raster Provider for QGIS"
date: "2021-09-12T19:00:01-0500"
link: "https://lutraconsulting.co.uk/blog/2021/09/12/qgis-gsoc-2021/"
draft: "false"
showcase: "planet"
subscribers: ["lutragis"]
author: "Lutra Consulting"
tags: []
---

<p>Read the guest post and congratulate Francesco Bursi, who successfully completed GSOC 2021 project to add
virtual raster provider for QGIS with help of mentors Martin Dobias and Peter Petrik.</p>

<!-- more -->

<hr />

<p>In this year’s <a href="https://wiki.osgeo.org/wiki/Google_Summer_of_Code_2021_Results">Google Summer of Code (GSoC)</a>, I decided to work on the native QGIS raster calculator. Martin Dobias and Peter Petrik volunteered to mentor my work. I’ve been studying Civil Engineering and GeoInformatics at the University of Padua; here I had the opportunity to work both with a lot of GIS software including QGIS. I enjoyed working with <a href="https://qgis.org/en/site/">QGIS</a> almost immediately because of the possibility to perform complex analysis with a few clicks or with few python commands. Being passionate about programming and enthusiastic about Open Source, I realized that having the possibility to work together with some experienced developers and with an active community was really a great and unique opportunity, so I decided to apply to the GSoC.</p>

<center>
<img alt="GSOC &amp; OSGeo" src="https://lutraconsulting.co.uk/img/posts/gsoc_2021/gsoc_logo.png" title="GSOC &amp; OSGeo" width="600" />
</center>

<h1 id="virtual-raster-provider">Virtual Raster Provider</h1>

<p>The existing raster calculator is a powerful tool to perform map algebra that outputs a raster layer, before this work it was possible to take advantage of this tool only by saving the output of this operation as a file. The aim of this year GSoC was to allow users to perform their analysis without creating a new derived raster and taking up  disk space and therefore have the result as an  on-the-fly computational layer.</p>

<p>Let’s jump to an example and let’s say I want to compute the <a href="https://opentopography.org/news/opentopography-releases-canopy-height-model-tool">Chanopy Height Model (CHM)</a>, subtracting the Digital Terrain Model (DTM) from the Digital Surface Model (DSM).</p>

<p>I also want to perform some other analysis on the DTM since I want to compute the ideal elevation value for a particular tree planting (disclaimer: the elevation value used is example purposes only, moreover when planting trees you should take into account a lot of factors like slope, aspect, latitude. QGIS, by the way, can really be helpful in this kind of analysis). To do so I will start from the same data and I will create different on-the-fly layers for each calculation, in order to avoid the creation of different files I can take advantage of the new checkbox added to the raster calculator dialog.
The computation of CHM is performed in the next screencast and the output layer  name is, of course, CHM.</p>

<center>
<img alt="computation of CHM" src="https://lutraconsulting.co.uk/img/posts/gsoc_2021/image1.gif" title="computation of CHM" width="600" />
</center>

<p>I’ll end up with a new raster layer (CHM) that can be styled as a normal raster and that is not written as an output file to the disk.
For some further analysis, from the DTM, I want to obtain the portion of the area with an elevation between 150 and 350 metres above the datum. By applying the following expression to DTM I’ll end up with a raster that has a value of 1 where conditions specified by the expression is <code class="highlighter-rouge">TRUE</code> and it will have value of 0 otherwise.</p>

<div class="highlighter-rouge"><div class="highlight"><pre class="highlight"><code>("dtm@1" &gt; 150) AND ("dtm@1" &lt; 350)
</code></pre></div></div>

<p>I did not select the output layer name intentionally. The resulting layer will be named after the expression used to generate the layer.</p>

<center>
<img alt="generation of CHM layer" src="https://lutraconsulting.co.uk/img/posts/gsoc_2021/image2.gif" title="generation of CHM layer" width="600" />
</center>

<h1 id="conditional-statement">Conditional Statement</h1>

<p>I also had the opportunity to improve the raster calculator capabilities by adding the possibility to write expressions that involve conditional statements. Taking the already used example, let’s imagine I want to compute the CHM only for the areas of the DTM that are between 150 and 350 metres above the datum. It’s now possible to write an expression as the following one:</p>

<div class="highlighter-rouge"><div class="highlight"><pre class="highlight"><code>if ( ("dtm@1" &gt; 150) AND ("dtm@1" &lt; 350), CHM, -10)
</code></pre></div></div>

<p>This expression will output a raster with values of the CHM where the conditions are met and value of -10 if the conditions are not met. Since this is a final result of our analysis I’ll store this output as a file to the disk in the form of a GeoTIFF. I’d like to outline that the CHM used in the expression above and in the next screencast is an onn-the-fly computed raster, so it is possible to:</p>
<ul>
  <li>Take advantage of the virtual raster provider (on-the-fly computed raster) in other analysis with the raster calculator (and with other analysis tools);</li>
  <li>Store the on-the-fly computed raster as a file.</li>
</ul>

<center>
<img alt="" src="https://lutraconsulting.co.uk/img/posts/gsoc_2021/image3.gif" title="" width="600" />
</center>

<h1 id="conclusion">Conclusion</h1>
<p>I had fun and I struggled working with QGIS, but I learned a lot of new and interesting things.
My pull requests were met with several constructive comments, suggestions and feedback.
Some suggestions can be a starting point for future improvements.</p>
<ul>
  <li>An enhancement for the feature I’ve developed can be the possibility to take advantage of OpenCL acceleration as it has also been suggested in the dev mailing list;</li>
  <li>Another enhancement that concerns the raster calculator and only partially the virtual raster provider would be the possibility to support the creation of output raster with multiple bands with the declaration of multiple formulas.
I hope to continue to contribute to the QGIS project in the future.</li>
</ul>
