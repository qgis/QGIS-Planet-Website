---
source: "blog"
title: "How to use Function Editor in QGIS Field calculator"
date: "2015-06-05T09:00:00-0500"
link: "https://lutraconsulting.co.uk/blog/2015/06/05/qgis-function-editor/"
draft: "false"
showcase: "planet"
subscribers: ["lutragis"]
author: "Lutra Consulting"
tags: []
---

<p>In QGIS 2.8, there is a new option for users to add their own python function in the Field calculator. This is an extremely useful feature enabling users to populate data within the attribute table using customised python function.</p>

<!-- more -->

<p>Nathan wrote a <a href="http://nathanw.net/2015/01/19/function-editor-for-qgis-expressions/" target="_blank">blog post</a> about the feature and how to write a python with arguments. But in QGIS 2.8, the function editor does not correctly support functions without arguments.</p>

<p>In the example below, we are going to calculate proportion of area for each SAC (Special Areas of Conservation) in Great Britain to the total area of the <a href="http://jncc.defra.gov.uk/protectedsites/SACselection/gis_data/terms_conditions.asp" target="_blank">layer</a>.</p>

<p>Add <strong>GB_SAC_20130918_Dissolved.shp</strong> layer to QGIS, right-click on the layer and open attribute table. Make the layer editable and click on the Field calculator.
We are now going to create a new column (propArea) and populate proportionate area of each SAC to the total area of the layer.</p>

<p>Under <strong>Function Editor</strong> tab, click on <strong>New file</strong> and type <strong>area</strong> for the name and save the file. For the content, copy and paste the following lines:</p>

<div class="highlighter-rouge"><div class="highlight"><pre class="highlight"><code>"""
A custom function to calculate total area of the GIS layer.
This function has no arguments.
"""

from qgis.core import *
from qgis.gui import *
from qgis.utils import iface

@qgsfunction(args='auto', group='Custom')
def total_area(x, feature, parent):
	return sum( f.geometry().area() for f in iface.activeLayer().getFeatures() )
</code></pre></div></div>

<p>Click on <strong>Run Script</strong> to add <strong>total_area</strong> function to your <strong>Custom</strong> function list.</p>

<p>Now, click on <strong>Expression</strong> tab and type:</p>

<div class="highlighter-rouge"><div class="highlight"><pre class="highlight"><code>$area / total_area(0)
</code></pre></div></div>

<p>As you can see, we have passed 0 as an argument. If you click OK, your QGIS will freeze! As there are many features in the layer, the expression, calculates total area for each row.</p>

<p>Lets make the script a bit more elegant. Firstly, we need to add caching, so that area will be calculated only once and cached for the rest of operation. Secondly, we can make the script a bit more generic, so that we can use it to get the area of other loaded layers in QGIS:</p>

<div class="highlighter-rouge"><div class="highlight"><pre class="highlight"><code>from qgis.core import *
from qgis.gui import *
from qgis.utils import iface

cache = {}
def _layer_area(layer):
	""" Internal method """
	if layer.name() not in cache:
		area = sum( f.geometry().area() for f in layer.getFeatures() )
		cache[layer.name()] = area
	return cache[layer.name()]

@qgsfunction(args='auto', group='Custom')
def total_area(layer_name, feature, parent):
	for layer in iface.mapCanvas().layers():
		if layer.name() == layer_name:
			return _layer_area(layer)
	return 0
</code></pre></div></div>

<p>Now, click on <strong>Expression</strong> tab and type:</p>

<div class="highlighter-rouge"><div class="highlight"><pre class="highlight"><code>$area / total_area('GB_SAC_20130918_Dissolved')
</code></pre></div></div>

<p>This time, it should be quicker!</p>
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
