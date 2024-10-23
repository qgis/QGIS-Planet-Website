---
source: "blog"
title: "Crayfish 2.0: What's new!"
date: "2015-04-08T09:00:00-0500"
link: "https://lutraconsulting.co.uk/blog/2015/04/08/crayfish-2-0/"
draft: "false"
showcase: "planet"
subscribers: ["lutragis"]
author: "Lutra Consulting"
tags: []
---

<p>After listening to user feedback we decided to do some major work on Crayfish. The changes include code refactoring, changes to the user interface, support for an additional file format, adding a vector and contour overlay, and a shiny new logo! </p>

<center>
	<img alt="Crayfish 2.0" src="https://www.lutraconsulting.co.uk/img/posts/crayfish logo_2_0.png" />
</center>

<!-- more -->

<h2 id="time-control">Time control</h2>

<p>In the new version of Crayfish a time slider allows users to quickly browse through time. A drop-down menu allows the selection of an exact time.</p>

<center>
  
</center>

<h2 id="vector-and-contour-overlay">Vector and contour overlay</h2>

<p>In previous versions of Crayfish it was only possible to load contours and vectors from the same dataset. For example, it was not possible to show velocity vectors on top of depth contours. With the new Crayfish you can "unlock" the legend and choose different vectors or contours to be displayed. The video below demonstrates this in action.</p>

<center>
  
</center>

<h2 id="special-times">Special times</h2>

<p>Some datasets contain a special time-step outside the outputted time range. For example, Maximums and Minimums are stored at time 99999 in TUFLOW modelling package. Within the layer tree, additional time-steps items will now be shown if they exist within the dataset.</p>

<h2 id="additional-file-formats">Additional file formats</h2>

<p>We have added support for the <a href="http://en.wikipedia.org/wiki/XMDF" rel="nofollow" target="\_blank">XMDF</a> file format.
In addition, <a href="http://www2.hydrotec.de/vertrieb/hydro_as_2d" rel="nofollow" target="\_blank">Hydro_AS 2D</a> users should be able to open their files in the latest Crayfish.</p>

<h2 id="new-python-module">New Python Module</h2>

<p>We've refactored lots of code in the Crayfish library which makes it much easier to add support for further file formats and additional functionality. The Crayfish library now comes with a new Python module that allows easy manipulation with the mesh and results data - either in your custom scripts or within the QGIS Python console. For example, printing the coordinates of the nodes of a mesh together with their elevation takes just few lines of code:</p>

<div class="highlighter-rouge"><div class="highlight"><pre class="highlight"><code>import crayfish

m = crayfish.Mesh("/data/my_mesh.2dm")
o = m.dataset(0).output(0) # bed elevation data

for index, node in enumerate(m.nodes()):
print "Node XYZ: ", node.x, node.y, o.value(index)
</code></pre></div></div>

<h2 id="new-profile-tool-plugin">New Profile tool plugin</h2>

<p>If you use Profile tool plugin in QGIS, you can create a profile from the Crayfish layer and browse through the time. The profile gets updated as you change the output time. </p>

<h2 id="problems">Problems</h2>
<p>If you have some feedback on our changes, suggestions for new functionality, or come across a bug, feel free to file a ticket on the <a href="https://github.com/lutraconsulting/qgis-crayfish-plugin/issues" rel="nofollow" target="\_blank">issues page</a> of the Crayfish github repository.</p>

<h2 id="sponsors">Sponsors</h2>

<p>We’d like to thank <a href="http://www.maroondah.vic.gov.au" rel="nofollow" target="\_blank">Maroondah City Council </a> for sponsoring some of the great features in this release.</p>

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
