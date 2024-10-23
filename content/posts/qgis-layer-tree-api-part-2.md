---
source: "blog"
title: "QGIS Layer Tree API (Part 2)"
date: "2014-07-25T13:00:00-0500"
link: "https://lutraconsulting.co.uk/blog/2014/07/25/qgis-layer-tree-api-part-2/"
draft: "false"
showcase: "planet"
subscribers: ["lutragis"]
author: "Lutra Consulting"
tags: []
---

<p>In <a href="https://www.lutraconsulting.co.uk/blog/2014/07/06/qgis-layer-tree-api-part-1/">part 1</a> we covered how to access the project’s layer tree
and read its data. Now let’s focus on building and manipulating layer trees.
We’ll also look at how to receive updates about changes within a layer tree.</p>

<!-- more -->

<p>Starting with an empty project, first we will get access to the layer tree and create some memory
layers for testing:</p>

<div class="highlighter-rouge"><div class="highlight"><pre class="highlight"><code>root = QgsProject.instance().layerTreeRoot()

layer1 = QgsVectorLayer("Point", "Layer 1", "memory")
layer2 = QgsVectorLayer("Polygon", "Layer 2", "memory")
</code></pre></div></div>

<h2 id="adding-nodes">Adding Nodes</h2>

<p>Now let’s add some layers to the project’s layer tree. There are two ways of doing that:</p>

<ol>
  <li>
    <p>Explicit addition. This is done with the <code class="highlighter-rouge">addLayer()</code> or <code class="highlighter-rouge">insertLayer()</code> call of the <code class="highlighter-rouge">QgsLayerTreeGroup</code> class.
The former appends to the group node, while the latter allows you to specify the index at which the layer
should be added.</p>

    <div class="highlighter-rouge"><div class="highlight"><pre class="highlight"><code># step 1: add the layer to the registry, False indicates not to add to the layer tree
QgsMapLayerRegistry.instance().addMapLayer(layer1, False)
# step 2: append layer to the root group node
node_layer1 = root.addLayer(layer1)
</code></pre></div>    </div>
  </li>
  <li>
    <p>Implicit addition. The project’s layer tree is connected to the layer registry and listens
for the addition and removal of layers. When a layer is added to the registry, it will
be automatically added to the layer tree. It is therefore enough to simply add a layer to the map
layer registry (leaving the second argument of addMapLayer() with its default value of <code class="highlighter-rouge">True</code>):</p>

    <div class="highlighter-rouge"><div class="highlight"><pre class="highlight"><code>QgsMapLayerRegistry.instance().addMapLayer(layer1)
</code></pre></div>    </div>

    <p>This behaviour is facilitated by the <code class="highlighter-rouge">QgsLayerTreeRegistryBridge</code> class. By default it inserts layers
at the first position of the root node. The insertion point for new layers can be changed -
within the QGIS application the insertion point is updated whenever the current selection in the layer tree
view changes.</p>
  </li>
</ol>

<p>Groups can be added using the <code class="highlighter-rouge">addGroup()</code> or <code class="highlighter-rouge">insertGroup()</code> calls of the <code class="highlighter-rouge">QgsLayerTreeGroup</code> class:</p>

<div class="highlighter-rouge"><div class="highlight"><pre class="highlight"><code>node_group1 = root.insertGroup(0, "Group 1")
# add another sub-group to group1
node_subgroup1 = node_group1.addGroup("Sub-group 1")
</code></pre></div></div>

<p>There are also the general <code class="highlighter-rouge">addChildNode()</code>, <code class="highlighter-rouge">insertChildNode()</code> and <code class="highlighter-rouge">insertChildNodes()</code> calls
that allow the addition of existing nodes:</p>

<div class="highlighter-rouge"><div class="highlight"><pre class="highlight"><code>QgsMapLayerRegistry.instance().addMapLayer(layer2, False)

node_layer2 = QgsLayerTreeLayer(layer2)
root.insertChildNode(0, node_layer2)

node_group2 = QgsLayerTreeGroup("Group 2")
root.addChildNode(node_group2)
</code></pre></div></div>

<p>Nodes that are being added must not have any parent yet (i.e. being part of some layer tree).
On the other hand, the nodes that get inserted may already have children, so it is possible
to create a whole sub-tree and then add it in one operation to the project’s layer tree.</p>

<h2 id="removing-nodes">Removing Nodes</h2>

<p>The removal of nodes from a layer tree is always done from the parent group node. For example, nodes displayed
as top-level items need to be removed from the root node. There are several ways of removing them.
The most general form is to use the <code class="highlighter-rouge">removeChildren()</code> method that takes two arguments: the index of the first
child node to be removed and how many child nodes to remove. Removal of a group node will also remove all
of its children.</p>

<p>There are several convenience methods for removal:</p>

<div class="highlighter-rouge"><div class="highlight"><pre class="highlight"><code>root.removeChildNode(node_group2)

root.removeLayer(layer1)
</code></pre></div></div>

<p>There is one more way to remove layers from the project’s layer tree:</p>

<div class="highlighter-rouge"><div class="highlight"><pre class="highlight"><code>QgsMapLayerRegistry.instance().addMapLayer(layer1)
</code></pre></div></div>

<p>The project’s layer tree is notified when any map layers are being removed from the map layer registry
and the layer nodes representing affected layers will be automatically removed from the layer tree.
This is handled by the <code class="highlighter-rouge">QgsLayerTreeRegistryBridge</code> class mentioned earlier.</p>

<h2 id="moving-nodes">Moving Nodes</h2>

<p>When managing the layer tree, it is often necessary to move some nodes to a different position - 
within the same parent node or to a different parent node (group). Moving a node is done in three
steps: 1. clone the existing node, 2. add the cloned node to the desired place in layer tree, 3. remove
the original node. The following code assumes that the existing node we move is a child of the root node:</p>

<div class="highlighter-rouge"><div class="highlight"><pre class="highlight"><code>cloned_group1 = node_group1.clone()
root.insertChildNode(0, cloned_group1)
root.removeChildNode(node_group1)
</code></pre></div></div>

<h2 id="modifying-nodes">Modifying Nodes</h2>

<p>There are a number of operations one can do with nodes:</p>

<ol>
  <li>
    <p><strong>Rename.</strong> Both group and layer nodes can be renamed. For layer nodes this will modify the name
directly inside the map layers.</p>

    <div class="highlighter-rouge"><div class="highlight"><pre class="highlight"><code>node_group1.setName("Group X")
node_layer2.setLayerName("Layer X")
</code></pre></div>    </div>
  </li>
  <li>
    <p><strong>Change visibility.</strong> This is actually a check state (checked or unchecked, for group nodes also
partially checked) that is associated with the node and normally related to the visibility of
layers and groups in the map canvas. In the GUI, the layer tree view is capable of showing a check box
for changing the state.</p>

    <div class="highlighter-rouge"><div class="highlight"><pre class="highlight"><code>print node_group1.isVisible()
node_group1.setVisible(Qt.Checked)
node_layer2.setVisible(Qt.Unchecked)
</code></pre></div>    </div>
  </li>
  <li>
    <p><strong>Change expanded state.</strong> The boolean expanded/collapsed state refers to how the node should
be shown in layer tree view in the GUI - whether its children should be shown or hidden.</p>

    <div class="highlighter-rouge"><div class="highlight"><pre class="highlight"><code>print node_group1.isExpanded()
node_group1.setExpanded(False)
</code></pre></div>    </div>
  </li>
  <li>
    <p><strong>Change custom properties.</strong> Each node may have some associated custom properties. The
properties are key-value pairs, keys being strings, values being of variant type (QVariant). They
can be used by other components of QGIS or plugins to store additional data. Custom properties
are preserved when a layer tree is saved and loaded.</p>

    <p>Use the <code class="highlighter-rouge">customProperties()</code> call to get a list of keys of custom properties, then the <code class="highlighter-rouge">customProperty()</code>
method for getting the value of a particular key. To modify properties, there is
a <code class="highlighter-rouge">setCustomProperty()</code> method which sets a key-value pair and a <code class="highlighter-rouge">removeCustomProperty()</code> method to remove a pair.</p>

    <div class="highlighter-rouge"><div class="highlight"><pre class="highlight"><code>node_group1.setCustomProperty("test_key", "test_value")
print node_group1.customProperties()
print node_group1.customProperty("test_key")
node_group1.removeCustomProperty("test_key")
print node_group1.customProperties()
</code></pre></div>    </div>
  </li>
</ol>

<h2 id="signals-from-nodes">Signals from Nodes</h2>

<p>There are various signals emitted by nodes which may be used by client code to follow changes to the layer tree.
Signals from children are automatically propagated to their parent node, so it is enough to connect
to the root node to listen for changes from any level of the tree.</p>

<h4 id="modification-of-the-layer-tree-structure">Modification of the Layer Tree Structure</h4>

<p>The addition of new nodes always emits a pair of signals - before and after the actual addition.
Signals pass information about which node is the parent node and the range of child indices:</p>

<ul>
  <li><code class="highlighter-rouge">willAddChildren(node, indexFrom, indexTo)</code></li>
  <li><code class="highlighter-rouge">addedChildren(node, indexFrom, indexTo)</code></li>
</ul>

<p>In order to access the newly added nodes, it is necessary to use the <code class="highlighter-rouge">addedChildren</code> signal.</p>

<p>The following code sample illustrates how to connect to signals emitted from the layer tree. When the last line is executed, two lines from the newly defined methods should be printed to the console:</p>

<div class="highlighter-rouge"><div class="highlight"><pre class="highlight"><code>def onWillAddChildren(node, indexFrom, indexTo):
  print "WILL ADD", node, indexFrom, indexTo
def onAddedChildren(node, indexFrom, indexTo):
  print "ADDED", node, indexFrom, indexTo

root.willAddChildren.connect(onWillAddChildren)
root.addedChildren.connect(onAddedChildren)

g = root.addGroup("My Group")
</code></pre></div></div>

<p>Removal of nodes is handled in a very similar manner to the addition - there is also a pair of signals:</p>

<ul>
  <li><code class="highlighter-rouge">willRemoveChildren(node, indexFrom, indexTo)</code></li>
  <li><code class="highlighter-rouge">removedChildren(node, indexFrom, indexTo)</code></li>
</ul>

<p>This time in order to access nodes being removed it is necessary to connect to the <code class="highlighter-rouge">willRemoveChildren</code> signal.</p>

<h4 id="modification-of-tree-nodes">Modification of Tree Nodes</h4>

<p>There are a few more signals that allow monitoring of internal changes to nodes:</p>

<ul>
  <li>a node is checked or unchecked: <code class="highlighter-rouge">visibilityChanged(node, state)</code></li>
  <li>a node’s custom property is defined or removed: <code class="highlighter-rouge">customPropertyChanged(node, key)</code></li>
  <li>a node gets expanded or collapsed: <code class="highlighter-rouge">expandedChanged(node, expanded)</code></li>
</ul>

<h2 id="summary">Summary</h2>

<p>We have covered how to make changes to a layer tree structure and how to listen for changes
possibly made by other pieces of code. In a future post we look at GUI components
for displaying and modifying the layer tree and the connection between map canvas and layer tree.</p>

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
