---
source: "blog"
title: "QGIS Layer Tree API (Part 1)"
date: "2014-07-06T13:00:00-0500"
link: "https://lutraconsulting.co.uk/blog/2014/07/06/qgis-layer-tree-api-part-1/"
draft: "false"
showcase: "planet"
subscribers: ["lutragis"]
author: "Lutra Consulting"
tags: []
---

<p>This blog post will be about the QGIS component responsible for showing the list of layers.
In the QGIS project we typically call this component the “legend widget”. People used to other GIS software
may also use other names such as “table of contents (ToC)”.</p>

<p>Layers in the legend widget can be organised into groups. This grouping allows easier manipulation
of layers. For example it is possible to toggle the visibility of all layers at once. In addition to
layers, groups can also contain other groups, effectively creating a hierarchy of groups and layers.
From now on, we will refer to this hierarchy as the <em>layer tree</em>.</p>

<!-- more -->

<p>The legend widget might look like this:</p>

<p align="center"><img alt="QGIS Legend Widget" src="https://www.lutraconsulting.co.uk/img/posts/qgis_legend_widget.png" /></p>

<p>Until QGIS 2.4, there has been only limited support for interacting with the legend widget using the QGIS API.
There is a <code class="highlighter-rouge">QgsLegendInterface</code> class (which can be obtained with <code class="highlighter-rouge">iface.legendInterface()</code>) available for
plugins. The legend interface has emerged in an ad-hoc way, leading to various issues when used in plugins.
It is also worth noting that third-party applications based on QGIS have no access to the legend
interface.</p>

<h2 id="layer-tree-api">Layer Tree API</h2>

<p>The layer tree API has been introduced in QGIS 2.4 to overcome these existing problems and add even
more flexibility to the way the layer tree can be queried or modified.</p>

<p>The layer tree is a classical tree structure built of nodes. There are currently two types
of nodes: group nodes and layer nodes. Group nodes can contain other (child) nodes, while layer nodes
are ‘leaves’ of the tree, without any child nodes. The layer tree for the legend widget shown
in the picture above looks like this:</p>

<p align="center"><img alt="Layer Tree Structure" src="https://www.lutraconsulting.co.uk/img/posts/qgis_layer_tree_structure.png" /></p>

<p>The green nodes are group nodes (<code class="highlighter-rouge">QgsLayerTreeGroup</code> class) and the yellow nodes
are layer nodes (<code class="highlighter-rouge">QgsLayerTreeLayer</code> class).</p>

<p>The legend widget also displays items using symbols, making it look like a real legend. The symbology
is not part of the layer tree and will be discussed in an upcoming post.</p>

<p>To start working with the layer tree, we first need a reference to its root node.
The project’s layer tree can be accessed easily:</p>

<div class="highlighter-rouge"><div class="highlight"><pre class="highlight"><code>root = QgsProject.instance().layerTreeRoot()
</code></pre></div></div>

<p>The root node is a group node - its children are shown as top-level items in the legend widget.</p>

<div class="highlighter-rouge"><div class="highlight"><pre class="highlight"><code>print root
print root.children()
</code></pre></div></div>

<p>This returns a list of the children of a node. The list includes only direct children - children of sub-groups
need to be queried directly from those sub-groups.</p>

<p>Now let’s try to access the first child node in the tree and do a little bit of introspection:</p>

<div class="highlighter-rouge"><div class="highlight"><pre class="highlight"><code>child0 = root.children()[0]
print child0
print type(child0)
print isinstance(child0, QgsLayerTreeLayer)
print child0.parent()
</code></pre></div></div>

<p>With the <code class="highlighter-rouge">children()</code> and <code class="highlighter-rouge">parent()</code> methods it is possible to traverse the layer tree. A node is the root node
of a tree if it has no parent:</p>

<div class="highlighter-rouge"><div class="highlight"><pre class="highlight"><code>print root.parent()
</code></pre></div></div>

<p>The following example shows how to list top-level items of the layer tree. For group nodes it will
print the group name, for layer nodes it will print the layer name and ID.</p>

<div class="highlighter-rouge"><div class="highlight"><pre class="highlight"><code>for child in root.children():
  if isinstance(child, QgsLayerTreeGroup):
    print "- group: " + child.name()
  elif isinstance(child, QgsLayerTreeLayer):
    print "- layer: " child.layerName() + "  ID: " + child.layerId()
</code></pre></div></div>

<p>In order to traverse the full layer tree, it would be necessary to recursively call the same code for sub-groups.</p>

<p>There are some helper routines for common tasks like finding nodes representing layers in the tree.
These take into account all descendants, not just top-level nodes.</p>

<div class="highlighter-rouge"><div class="highlight"><pre class="highlight"><code>ids = root.findLayerIds()
print ids
print root.findLayers()
print root.findLayer(ids[0])
</code></pre></div></div>

<p>It is assumed that a single layer is represented in a layer tree only once. There may however be temporary situations
when a layer is represented by more than one node, for example when moving nodes (a new node is created before
the old one is removed shortly after).</p>

<p>Similarly it is possible to search for group nodes by name:</p>

<div class="highlighter-rouge"><div class="highlight"><pre class="highlight"><code>print root.findGroup("POI")
</code></pre></div></div>

<p>Group names are not necessarily unique - if there are multiple groups with the same name, the first
encountered during tree traversal will be returned.</p>

<h2 id="summary">Summary</h2>

<p>In this blog post we have shown how to query the project’s layer tree. Upcoming blog entries will
focus on modifying the layer tree and interacting with other parts of QGIS.</p>

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
