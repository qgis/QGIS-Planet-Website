---
source: "blog"
title: "New version of Serval QGIS plugin"
date: "2020-12-21T03:00:00-0600"
link: "https://lutraconsulting.co.uk/blog/2020/12/21/new_serval_version_310/"
draft: "false"
showcase: "planet"
subscribers: ["lutragis"]
author: "Lutra Consulting"
tags: []
---

<p>Raster selection tools and editing with QGIS expressions.</p>

<!-- more -->

<h2 id="whats-new">What’s new?</h2>
<p>In the <a href="https://www.lutraconsulting.co.uk/blog/2016/09/05/serval/">previous version</a> Serval allowed for setting a constant value to a single raster cell at a time.
The latest version brings in new <strong>raster cells selection tools</strong> and new ways of <strong>manipulating cells value</strong>:</p>

<ul>
  <li>QGIS expressions and</li>
  <li>3x3 low-pass filter.</li>
</ul>

<p>Multi-bands rasters are fully supported - each band can be edited separately.
Serval is meant to provide a convenient way to modify <strong>selected parts</strong> of a raster layer.
It is not optimized to process entire images - use <a href="https://docs.qgis.org/latest/en/docs/user_manual/working_with_raster/raster_analysis.html#raster-calculator">Raster Calculator</a> for that.</p>

<h2 id="raster-selection-tools">Raster selection tools</h2>
<p>In order to modify raster cells values users need to select them first with a <strong>line</strong> or <strong>polygon selection tool</strong>. 
The line selection tool has a configurable width and unit. 
Selections can also be easily imported/exported from/to a vector map layer.</p>

<p>Multiple selections are allowed and users can add or remove from existing selection using CTRL and SHIFT keys modifiers, respectively.</p>

<p><img alt="Selecting raster cells" src="https://www.lutraconsulting.co.uk/img/posts/serval_310_selection_tools.gif" /></p>

<h2 id="modifying-rasters-with-qgis-expressions">Modifying rasters with QGIS expressions</h2>

<p>In addition to setting a constant value, new cells value might be evaluated using QGIS expressions.
Users can build their expressions using cells’ <code class="highlighter-rouge">row</code> and <code class="highlighter-rouge">column</code> variables, or <code class="highlighter-rouge">x</code> and <code class="highlighter-rouge">y</code> of cell center point.</p>

<p>In the <code class="highlighter-rouge">Serval</code> group of the builder users will find several expression functions for:</p>

<ul>
  <li>interpolating raster value from a mesh layer,</li>
  <li>averaging attribute values from vector layer features intersecting the cell,</li>
  <li>getting the nearest vector layer feature attribute,</li>
  <li>interpolating z-value from the nearest 3D linestring feature.</li>
</ul>

<h3 id="interpolation-on-a-mesh-layer">Interpolation on a mesh layer</h3>

<p>With the recent QGIS additions it is very easy to create mesh layers. Users can use a mesh layer for raster cell value interpolation.
For example, <code class="highlighter-rouge">interpolate_from_mesh()</code> function will identify mesh dataset value and return it as a new raster value, optionally only when the value is higher than existing cell value.
It is a convenient way for finding an embankment shape on a raster DTM - see pictures below.</p>

<p><img alt="Serval QGIS expression builder" src="https://www.lutraconsulting.co.uk/img/posts/serval_310_expression_builder.png" /></p>

<p><img alt="Raster values interpolated on a mesh layer" src="https://www.lutraconsulting.co.uk/img/posts/serval_310_mesh_interp_3d.png" /></p>

<h3 id="interpolation-on-3d-linestrings">Interpolation on 3D linestrings</h3>

<p>Another useful function finds the nearest point on a 3D line feature and interpolate its z-value. 
It could be used for fine-tuning terrain elevation from a 3D profile line.</p>

<p>For example, if the existing embankment crown needs to be raised by an amount at one of its ends, a 
user could create a profile line, adjust the vertex elevation in the Vertex Editor and use it for the interpolation.</p>

<p><img alt="Raising embankment elevation based on 3D profile line" src="https://www.lutraconsulting.co.uk/img/posts/serval_310_interp_on_3d_line.png" /></p>

<h3 id="creating-custom-expression-functions">Creating custom expression functions</h3>

<p>In the Expression builder users can define their own functions using other types of vector and raster layers.</p>

<h2 id="applying-3x3-low-pass-filter">Applying 3x3 low-pass filter</h2>

<p>For eliminating peak values or local cell values averaging, users can use 3x3 low-pass filter.</p>

<p><img alt="Applying low-pass filter" src="https://www.lutraconsulting.co.uk/img/posts/serval_310_low_pass_filter.gif" /></p>

<p>For more details and examples, refer to the <a href="https://github.com/lutraconsulting/serval/blob/master/Serval/docs/user_manual.md">plugin’s Manual</a>.</p>

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
