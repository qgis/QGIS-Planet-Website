---
source: "blog"
title: "Using Presets, multiple styles, Atlas with overview map"
date: "2015-11-15T10:00:00-0600"
link: "https://lutraconsulting.co.uk/blog/2015/11/15/print-composer-presets/"
draft: "false"
showcase: "planet"
subscribers: ["lutragis"]
author: "Lutra Consulting"
tags: []
---

<p>Our training courses are structured to give trainees step-by-step guide using the latest QGIS features. Here is an example of one our practicals for creating professional maps.</p>

<p>Trainees will learn how to</p>

<ul>
  <li>Assign multiple style to a layer</li>
  <li>Working with presets</li>
  <li>Working QGIS print composer</li>
  <li>Generating maps using Atlas</li>
</ul>

<!-- more -->

<h1 id="creating-professional-maps-with-the-print-composer">Creating professional maps with the Print Composer</h1>
<p>QGIS’ Print Composer allows users to create professional maps for
printing. It supports legends, frames, logos and all the other features
you’d expect to see in a print quality map.</p>

<p>In this example, we’ll use some of the most common features required to
generate a map for printing.</p>

<p>We’ll first load the electricity usage data created in
another tutorial, style it using a simple colour ramp, then
create a new map composer complete with title and legend.</p>

<!-- [Click here](https://www.lutraconsulting.co.uk/downloads/PrintComposer_Tutorial_data.zip) to download the tutorial data. After downloading, ensure to extract the file. -->

<h2 id="loading-data-in-qgis">Loading data in QGIS</h2>

<p>The styling of a vector layer can be performed using a single style, or
a varying style, based on the value of one or more attributes. We are
going to first load the London energy usage layer prepared in
an another tutorial by joining electricity usage with the LSOAs vector layer.</p>

<div class="highlighter-rouge"><div class="highlight"><pre class="highlight"><code>Start a new QGIS project

Add the MSOA_GL_ElecUsage.shp layer under extracted
downloaded folder
</code></pre></div></div>

<p>The vector layer should now look like the figure below.</p>

<p><img alt="Energy consumption in London" src="https://www.lutraconsulting.co.uk/img/posts/PrintComposerEnergyStyled_499.png" />
<em>Energy consumption in London</em></p>

<p>Next, we are going to add a shapefile of London Boroughs to identify
areas of high and low usage.</p>

<div class="highlighter-rouge"><div class="highlight"><pre class="highlight"><code>Add London_boroughs.shp from extracted downloaded
folder

Open layer properties and under Style:

Set the style of the polygons to "No Brush" with a
"Dash Line".
</code></pre></div></div>

<p><a href="https://www.lutraconsulting.co.uk/img/posts/PrintComposerLondonProps.png" rel="lightbox"><img src="https://www.lutraconsulting.co.uk/img/posts/PrintComposerLondonProps_499.png" title="Styles for London Boroughs vector layer (Click to enlarge)" /></a></p>
<p class="caption">Styles for London Boroughs vector layer (Click to enlarge)</p>

<p>Your map now should look like the figure below:</p>

<p><img alt="Energy consumption in London" src="https://www.lutraconsulting.co.uk/img/posts/PrintComposerEnergyLondonStyled_499.png" />
<em>Energy consumption in London</em></p>

<p>In QGIS, you can apply multiple styles to a single layer. Using this
method, we do not need to load the same layer multiple times. In this
case, we need two styles for London boroughs layer:</p>

<ol>
  <li>
    <p>Without labels (as created above); to be used as an overview map</p>
  </li>
  <li>
    <p>With labels (next section); for the main map</p>
  </li>
</ol>

<p>We can save the current style (without label):</p>

<div class="highlighter-rouge"><div class="highlight"><pre class="highlight"><code>Right-click on London_boroughs layer from the layer
tree and select Styles &gt; Add

For the new style, type 'no label' and click OK
</code></pre></div></div>

<p>We can save the new styles (with labels) for the layer:</p>

<div class="highlighter-rouge"><div class="highlight"><pre class="highlight"><code>Right-click on London_boroughs layer from the layer
tree and select Styles &gt; Add

For the new style, type 'with label' and click OK
</code></pre></div></div>

<p>Changes in the next section (adding label) will be saved in <strong>with
label</strong> style.</p>

<h2 id="labels">Labels</h2>

<p>We’ll now add labels to each of the boroughs. The name of each borough
is stored as the value of the NAME attribute.</p>

<div class="highlighter-rouge"><div class="highlight"><pre class="highlight"><code>Click on the London_boroughs layer in the ToC

Form the main menu, select Layer &gt; Labelling
</code></pre></div></div>

<p>This window will allow us the set an attribute for label and also change font, size, rotation, buffer, etc.</p>

<p><img alt="Setting up labels on the London boroughs layer" src="https://www.lutraconsulting.co.uk/img/posts/PrintComposerLabel1_499.png" />
<em>Setting up labels on the London boroughs layer</em></p>

<div class="highlighter-rouge"><div class="highlight"><pre class="highlight"><code>Enable the Label this layer with option

Set Field with labels to NAME

Under Text section, set the font to 7 pt

Under Buffer section:

  Enable Draw text buffer

  Set the Size to 0.5 mm

Click OK
</code></pre></div></div>

<p>You should now be able to see a label for each borough.</p>

<p><img alt="London boroughs with labels" src="https://www.lutraconsulting.co.uk/img/posts/PrintComposerEnergyLondonStyledLabel_499.png" />
<em>London boroughs with labels</em></p>

<h2 id="presets">Presets</h2>

<p>In QGIS, you can create presets for layer visibility and styles. In this
example we are going to create the following presets:</p>

<ul>
  <li>
    <p>Map of LSOAs with the energy usage and borough boundaries</p>
  </li>
  <li>
    <p>A separate preset for the London boroughs (without labels) which
will be used as an “overview” for the print composer</p>
  </li>
</ul>

<p>To create the first preset:</p>

<div class="highlighter-rouge"><div class="highlight"><pre class="highlight"><code>Ensure both layers are visible

Right-click on London_boroughs and select
Style &gt; with label
</code></pre></div></div>

<p>On top of the legend tree in QGIS,  you can see the icon for <strong>Manage
Layer Visibility</strong>
<img alt="image" src="https://www.lutraconsulting.co.uk/img/posts/mActionShowAllLayers.png" /></p>

<div class="highlighter-rouge"><div class="highlight"><pre class="highlight"><code>Click on the Manage Layer Visibility icon

From the drop-down menu, select Add preset...

For the Name of the new preset insert Energy map

Click OK
</code></pre></div></div>

<p>To ensure the preset has been correctly set, you can change the
visibility of the layer, or change the style, and select the preset from
the <strong>Manage Layer Visibility</strong> menu.</p>

<p>To create the second preset:</p>

<div class="highlighter-rouge"><div class="highlight"><pre class="highlight"><code>Hide All Layers from Manage Layer Visibility or simply
press Ctrl+Shift+H

Turn on the visibility for London_boroughs

Right-click on London_boroughs and select
Style &gt; no label

On top of the legend tree in QGIS, click on
Manage Layer Visibility

From the drop-down menu, select Add preset...

For the Name of the new preset insert overview map
</code></pre></div></div>

<p><img alt="London boroughs - without labels" src="https://www.lutraconsulting.co.uk/img/posts/PrintComposerOverViewStyle_499.png" />
<em>London boroughs</em></p>

<p>Now you should be able to switch between those two presets, and later
use them as print composer frames.</p>

<h2 id="print-composer">Print Composer</h2>

<h3 id="creating-layout">Creating layout</h3>

<p>The map is almost ready to be printed. Before printing, we’ll need to
add a border, logos, legends, scale, etc.</p>

<p>There are quite a few steps involved in configuring the print composer
so it’s recommended to regularly save your progress by saving the QGIS
project.</p>

<div class="highlighter-rouge"><div class="highlight"><pre class="highlight"><code>From the main menu, select File &gt; New Print Composer

A new window will appear for Composer title

Type Energy usage in London
</code></pre></div></div>

<p><img alt="The print composer title window" src="https://www.lutraconsulting.co.uk/img/posts/PrintComposerTitle.png" />
<em>The print composer title window</em></p>

<p>The print composer will appear. See <a href="https://www.lutraconsulting.co.uk/blog/categories/qgis/atom.xml#PrintComposerWindowEmpty">Figure</a>.</p>

<p><img alt="PrintComposerWindowEmpty" src="https://www.lutraconsulting.co.uk/img/posts/PrintComposerWindowEmpty_499.png" />
<em>The print composer window</em></p>

<p>The print composer is split into two sections. Section 1 shows the map
to be outputted and section 2 shows the settings for selected items in
section 1.</p>

<p>The map we are going to produce is an A4 landscape PNG file.</p>

<div class="highlighter-rouge"><div class="highlight"><pre class="highlight"><code>In section 2, under Composition, for Presets, select
A4(210 x 297 mm)
</code></pre></div></div>

<p>Now we need to add frames for the map extent and legend sections. You can add a rectangular shape by clicking on <img alt="image" src="https://www.lutraconsulting.co.uk/img/posts/PrintComposerAddRect.png" /> from the main toolbar.</p>

<div class="highlighter-rouge"><div class="highlight"><pre class="highlight"><code>From the main toolbar, add a new rectangle

Click and drag a shape in section 1
</code></pre></div></div>

<p>Now let’s change the position and size of the rectangle:</p>

<div class="highlighter-rouge"><div class="highlight"><pre class="highlight"><code>Ensure the rectangle shape is selected in section 1

Click on Item properties in section 2

Under Shape, select Position and size

Set the option as shown in Figure
</code></pre></div></div>

<p><img alt="Shape options" src="https://www.lutraconsulting.co.uk/img/posts/PrintComposerRect1.png" />
<em>Shape options</em></p>

<div class="highlighter-rouge"><div class="highlight"><pre class="highlight"><code>Add second, third and fourth rectangles with the
following information

Rectangle 2:

  X: 270

  Y: 145

  Width: 43.5

  Height: 60

  Reference Point: Centre

Rectangle 3:

  X: 270

  Y: 95

  Width: 43.5

  Height: 60

  Reference Point: Centre

Rectangle 4:

  X: 270

  Y: 105

  Width: 43.5

  Height: 200

  Reference Point: Centre

Lock the position of each window by right-clicking
on each of them
</code></pre></div></div>

<p>Section 1 of the print composer should look like this:</p>

<p><img alt="The print composer with placeholders layout" src="https://www.lutraconsulting.co.uk/img/posts/PrintComposerRects_499.png" />
<em>The print composer with placeholders layout</em></p>

<h3 id="adding-image">Adding image</h3>

<p>Let’s add the logos.</p>

<div class="highlighter-rouge"><div class="highlight"><pre class="highlight"><code>From the main menu, select Layout &gt; Add Image

Click within the middle rectangle on the right

An empty box will appear

In the right-hand panel (section 2), under the
Item properties tab,

	click on Main properties button

For Path, click on ... and browse to the folder where
your images are located.

Select an image
</code></pre></div></div>

<p>You should now see something similar to the image below.</p>

<p><img alt="Logos added to the composer" src="https://www.lutraconsulting.co.uk/img/posts/PrintComposerLogosAdded.png" />
<em>Logos added to the composer</em></p>

<h3 id="adding-text">Adding text</h3>

<p>Now we’ll add some text in the rectangle below the logos:</p>

<div class="highlighter-rouge"><div class="highlight"><pre class="highlight"><code>From the main menu, select Layout &gt; Add Label  

Click somewhere within the lower right-hand box  
</code></pre></div></div>

<p>A new text box will appear, reading <strong>QGIS</strong>.</p>

<div class="highlighter-rouge"><div class="highlight"><pre class="highlight"><code>From the right-hand panel, click on Item properties

In Main properties, change the text to refer to the
source of the data and copyright notices.
</code></pre></div></div>

<p><img alt="Copyright notices" src="https://www.lutraconsulting.co.uk/img/posts/PrintComposerCopyright.png" />
<em>Copyright notices</em></p>

<h3 id="adding-map">Adding map</h3>

<p>Now we’ll add the map from the QGIS canvas.</p>

<div class="highlighter-rouge"><div class="highlight"><pre class="highlight"><code>From the main menu, select Layout &gt; Add map

Drag a box in the main window
</code></pre></div></div>

<p>A map similar to the image below should now appear in the
print composer.</p>

<p>To finalise the main map window, a few more changes will need to be
made.</p>

<p><img alt="Adding map to the print composer" src="https://www.lutraconsulting.co.uk/img/posts/PrintComposerAddMap_499.png" />
<em>Adding map to the print composer</em></p>

<div class="highlighter-rouge"><div class="highlight"><pre class="highlight"><code>From the right panel, click on the Item properties tab

  Under the Main properties, set the following values:

    Tick the box for Lock layers for map item see
image below

  Under Extents:

    Tick the box for Controlled by atlas
</code></pre></div></div>

<p><img alt="Adding a preset for map view" src="https://www.lutraconsulting.co.uk/img/posts/PrintComposerAddPresetView.png" />
<em>Adding a preset for map view</em></p>

<h3 id="add-scalebar">Add scalebar</h3>

<p>To add a scalebar:</p>

<div class="highlighter-rouge"><div class="highlight"><pre class="highlight"><code>From the main menu, select Layout &gt; Add Scalebar
</code></pre></div></div>

<p><img alt="Adding a scalebar to the map" src="https://www.lutraconsulting.co.uk/img/posts/PrintComposerAddScalebar.png" />
<em>Adding a scalebar to the map</em></p>

<p>A scalebar with default settings should appear on the map. See Figure
[PrintComposerAddScalebar]. To change the scalebar:</p>

<div class="highlighter-rouge"><div class="highlight"><pre class="highlight"><code>Select the scalebar from the map

Click on Item Properties from the left-hand panel

Under Segments

   Set left 0 and right 2

   Set Size to 1000

   Set Height to 2 mm  
</code></pre></div></div>

<h3 id="adding-legend">Adding legend</h3>

<p>Next, we’ll add a legend:</p>

<div class="highlighter-rouge"><div class="highlight"><pre class="highlight"><code>From the main menu, select Layout &gt; Add Legend

Click somewhere within the upper right-hand box
</code></pre></div></div>

<p>QGIS will automatically add a legend for all the layers loaded in the
canvas. We can edit the legend’s settings and remove the legend entries
that we do not want to show. Manual edits of the legend text can also be
performed to make it more readable.</p>

<p>To be able to edit the legend items, you first need to untick the box for <strong>Auto update</strong>. Use icons under the <strong>Legend items</strong> to edit or change the order of the items.</p>

<p><img alt="The default legend" src="https://www.lutraconsulting.co.uk/img/posts/PrintComposerDefaultLegend.png" />
<em>The default legend</em></p>

<div class="highlighter-rouge"><div class="highlight"><pre class="highlight"><code>From the right-hand panel, click on the Item properties

  Under Legend items:

    Select London_boroughs and then click on the red
    minus sign


    Select MSOA_GL_ElecUsage and click on the edit
    sign, a new window will appear.

    Change the content of Item text to Electricity
	Usage

    Click on the first value 2576.2400 – 3000.0000
	and select edit sign to change the range to
	2000 – 3000   

    Repeat for the rest of the values to round them
	and remove any unwanted zeros.   
</code></pre></div></div>

<p><img alt="Editing legend values" src="https://www.lutraconsulting.co.uk/img/posts/PrintComposerLegendItemBeautify.png" />
<em>Editing legend values</em></p>

<p><img alt="Map with legend" src="https://www.lutraconsulting.co.uk/img/posts/PrintComposerAddLegend_499.png" />
<em>Map with legend</em></p>

<h3 id="add-overview">Add overview</h3>

<p>To add an overview:</p>

<div class="highlighter-rouge"><div class="highlight"><pre class="highlight"><code>Add a new map (Map 1) to the place-holder between
the map legend and the logos

For Map 1, from the Item properties,

Under Main properties

   Select Lock layers for map item

   From the visibility preset, select overview map

Under Overviews tab  

   Click on the plus sign,
	Overview 1 should be added to the overview list

   Ensure Draw "Overview 1" overview is selected

   For Map frame, select Map 0
</code></pre></div></div>

<p><img alt="Setting the preset view for the overview map" src="https://www.lutraconsulting.co.uk/img/posts/PrintComposerAddOverviewPreset.png" />
<em>Setting the preset view for the overview map</em></p>

<p>The map is now almost ready. You can export it as PNG or a PDF. Or you can keep reading for
even more excitement!</p>

<p><img alt="The completed map" src="https://www.lutraconsulting.co.uk/img/posts/PrintComposerCompletedMap_499.png" />
<em>The completed map</em></p>

<h3 id="atlas-generation">Atlas generation</h3>

<p>The map is now ready to be printed or outputted as an image. But, we are
going to use this layout as a template and auto-generate energy
consumption for each borough.</p>

<p>To set the coverage (this is already set, but make sure the option is
enabled):</p>

<div class="highlighter-rouge"><div class="highlight"><pre class="highlight"><code>While Map 0 (the main map) item is selected, click on
Item properties from the right-hand panel

Select the option for Controlled by atlas generation
</code></pre></div></div>

<p>You can change the <strong>Margin around feature</strong> if you like, but we can
keep at 10%. Further settings are also required:</p>

<div class="highlighter-rouge"><div class="highlight"><pre class="highlight"><code>Click on Atlas generation tab from the right-hand panel

Tick the box for Generate an atlas

Under Configuration, for Coverage layer select
	London_boroughs

Under Output, for Output filename expression type:
	'energy_'|| "NAME"  
</code></pre></div></div>

<p>The expression for output will set the name of each output file. In this
example we are going to have a name with <strong>‘energy_‘</strong> combined with
the value of <strong>NAME</strong> column (what do you think this value is?)</p>

<p>To generate the maps:</p>

<div class="highlighter-rouge"><div class="highlight"><pre class="highlight"><code>In the print composer, from the main menu, select
Atlas &gt; Export Atlas as Images...

Select a folder to output maps and press Choose
</code></pre></div></div>

<p>The process may take a while but you will eventually have 33 maps of the
energy consumption for each borough. Note the overview for the maps and
also the naming of the output files. See
Figure beloq as an example of the maps created.</p>

<p><img alt="Final energy map for Kingston upon Thames generated by the Atlas" src="https://www.lutraconsulting.co.uk/img/posts/energy_KingstonUponThames_499.jpg" />
<em>Final energy map for Kingston upon Thames generated by the Atlas</em></p>

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
