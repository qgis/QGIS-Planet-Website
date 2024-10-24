---
source: "blog"
title: "QGIS Layer Tree API (Part 3)"
date: "2015-01-30T02:00:00-0600"
link: "https://lutraconsulting.co.uk/blog/2015/01/30/qgis-layer-tree-api-part-3/"
draft: "false"
showcase: "planet"
subscribers: ["lutragis"]
author: "Lutra Consulting"
tags: []
---

<p>In the two previous blog posts we have learned how to query a layer tree and how to modify it.
All these new APIs are available since QGIS 2.4 release.
Today we will look into how to make layer trees available in GUI and connect them with a map canvas.</p>

<!-- more -->

<h2 id="modelview-overview">Model/View Overview</h2>

<p>As we have seen earlier, a layer tree is a usual hierarchical data structure composed from nodes of two
types - layers and groups. They do not provide any GUI functionality as they live in the QGIS core library.
In order to visualize a layer tree, we will use Model/View approach from Qt framework. Readers not familiar
with those concepts are recommended to read the <a href="http://qt-project.org/doc/qt-4.8/qt4-interview.html">Qt Model/View overview</a> first.</p>

<p align="center"><img alt="Layer tree model/view" src="https://www.lutraconsulting.co.uk/img/posts/qgis_layer_tree_modelview.png" /></p>
<!--
Image generated with PlantUML: java -jar plantuml.jar qgis_layer_tree_modelview.txt
Content of the text file:

@startuml
class QTreeView #GreenYellow
class QAbstractItemModel #GreenYellow
QTreeView <|-- QgsLayerTreeView
QAbstractItemModel <|-- QgsLayerTreeModel
QgsLayerTreeView - QgsLayerTreeModel : shows >
QgsLayerTreeModel -- QgsLayerTreeGroup : uses\nlayer tree
hide circle
hide members
@enduml
-->

<p>There is <code class="highlighter-rouge">QgsLayerTreeModel</code> class (derived from <code class="highlighter-rouge">QAbstractItemModel</code>) which as you may have guessed provides
a model to access a layer tree. Instance of this class may be used in any <code class="highlighter-rouge">QTreeView</code> class, however
it is recommended to use it together with <code class="highlighter-rouge">QgsLayerTreeView</code> because of the extra convenience functionality
offerred by the custom view class.</p>

<p>Here is an example how to create another view of current project’s layer tree (try that in QGIS Python console):</p>

<div class="highlighter-rouge"><div class="highlight"><pre class="highlight"><code><span class="k">from</span> <span class="n">qgis</span><span class="p">.</span><span class="n">gui</span> <span class="n">import</span> <span class="p">*</span>

<span class="n">root</span> <span class="p">=</span> <span class="n">QgsProject</span><span class="p">.</span><span class="n">instance</span><span class="p">().</span><span class="n">layerTreeRoot</span><span class="p">()</span>
<span class="k">model</span> <span class="p">=</span> <span class="n">QgsLayerTreeModel</span><span class="p">(</span><span class="n">root</span><span class="p">)</span>
<span class="n">view</span> <span class="p">=</span> <span class="n">QgsLayerTreeView</span><span class="p">()</span>
<span class="n">view</span><span class="p">.</span><span class="n">setModel</span><span class="p">(</span><span class="k">model</span><span class="p">)</span>
<span class="n">view</span><span class="p">.</span><span class="n">show</span><span class="p">()</span>
</code></pre></div></div>

<p>Any changes that happen to the layer tree structure are automatically monitored by the model/view classes.
After running the example above, try changing a layer’s name or add/remove/reorder some layers - all
those actions will be immediately visible in all views.</p>

<p>As you can see, the layer tree view is just one way how to visualize the underlying layer tree - in the future
it may be possible to have different ways to show the layer tree, for example using Qt’s QML framework
(with all sorts of animated transitions known from mobile apps).</p>

<p>Plugin developers can access the layer tree view in the main window of QGIS through the following interface call:</p>

<div class="highlighter-rouge"><div class="highlight"><pre class="highlight"><code>view = iface.layerTreeView()
</code></pre></div></div>

<h2 id="more-about-the-model">More About the Model</h2>

<p>The model is meant to be flexible and it is possible to use it in various contexts. For example,
by default the model also provides legend for the layers in the tree. This however may not be wanted
in some cases. Similarly, sometimes the layer tree should be read-only while in other context it is
desired that the user can reorder layers or change their names. These preferences can be passed to
the model with flags:</p>

<div class="highlighter-rouge"><div class="highlight"><pre class="highlight"><code><span class="k">model</span> <span class="p">=</span> <span class="n">QgsLayerTreeModel</span><span class="p">(</span><span class="n">root</span><span class="p">)</span>
<span class="k">model</span><span class="p">.</span><span class="n">setFlag</span><span class="p">(</span><span class="n">QgsLayerTreeModel</span><span class="p">.</span><span class="n">AllowNodeReorder</span><span class="p">)</span>
<span class="k">model</span><span class="p">.</span><span class="n">setFlag</span><span class="p">(</span><span class="n">QgsLayerTreeModel</span><span class="p">.</span><span class="n">AllowNodeChangeVisibility</span><span class="p">)</span>
</code></pre></div></div>

<p>The <code class="highlighter-rouge">setFlag()</code> method has optional second parameter “enabled” (<code class="highlighter-rouge">True</code> by default). Flags can be also
set all at once with <code class="highlighter-rouge">setFlags()</code> method which expects a combination of flags joined by binary OR operator.
There are also <code class="highlighter-rouge">flags()</code> and <code class="highlighter-rouge">testFlag()</code> methods to query the current flags.</p>

<p>The <code class="highlighter-rouge">QgsLayerTreeModel</code> class also provides routines for conversion between <code class="highlighter-rouge">QgsLayerTreeNode</code> instances
and corresponding <code class="highlighter-rouge">QModelIndex</code> objects used by Qt Model/View framework - <code class="highlighter-rouge">index2node()</code> and <code class="highlighter-rouge">node2index()</code>
may come handy especially when working with views.</p>

<p>There is also some functionality related to legend display - it has been greatly extended in QGIS 2.6 release
and we will try to cover that in a future blog post.</p>

<h2 id="more-about-the-view">More About the View</h2>

<p>As mentioned earlier, it is possible to use any <code class="highlighter-rouge">QTreeView</code> instance in combination with <code class="highlighter-rouge">QgsLayerTreeModel</code>
to show the layer tree, but it is highly recommended to use <code class="highlighter-rouge">QgsLayerTreeView</code> class (a subclass of <code class="highlighter-rouge">QTreeView</code>)
because of the additional functionality it provides (and more may be added in the future):</p>

<ul>
  <li>
    <p>Easier handling of selection. Normally one needs to work with selection through view’s selection model.
The <code class="highlighter-rouge">QgsLayerTreeView</code> class adds higher level methods that operate with <code class="highlighter-rouge">QgsLayerTreeNode</code> objects
like <code class="highlighter-rouge">currentNode()</code> or with <code class="highlighter-rouge">QgsMapLayer</code> objects
like <code class="highlighter-rouge">currentLayer()</code>.</p>

    <div class="highlighter-rouge"><div class="highlight"><pre class="highlight"><code>def onChange(layer):
  QMessageBox.information(None, "Change", "Current Layer: "+str(layer))

# connect to the signal
view.currentLayerChanged.connect(onChange)
# change selection to the top-most layer (onChange will be also called)
view.setCurrentLayer( iface.mapCanvas().layers()[0] )
</code></pre></div>    </div>
  </li>
  <li>
    <p>Display of context menu. It is possible to assign a menu provider to the view
(subclass of <code class="highlighter-rouge">QgsLayerTreeViewMenuProvider</code>) - its <code class="highlighter-rouge">createContextMenu()</code> implementation will return
a <code class="highlighter-rouge">QMenu</code> object with custom actions whenever user right-clicks in the view. Additionally, there is a factory
class <code class="highlighter-rouge">QgsLayerTreeViewDefaultActions</code> that can create commonly use actions for use in the menu,
such as “Add Group”, “Remove” or “Zoom to Layer”. The following example shows how to create a provider
with one action that shows the current layer’s extent:</p>

    <div class="highlighter-rouge"><div class="highlight"><pre class="highlight"><code>class MyMenuProvider(QgsLayerTreeViewMenuProvider):
  def __init__(self, view):
    QgsLayerTreeViewMenuProvider.__init__(self)
    self.view = view

  def createContextMenu(self):
    if not self.view.currentLayer():
      return None
    m = QMenu()
    m.addAction("Show Extent", self.showExtent)
    return m

  def showExtent(self):
    r = self.view.currentLayer().extent()
    QMessageBox.information(None, "Extent", r.toString())

provider = MyMenuProvider(view)
view.setMenuProvider(provider)
</code></pre></div>    </div>
  </li>
</ul>

<h2 id="interaction-with-canvas">Interaction with Canvas</h2>

<p>The layer tree classes and map canvas class are separate components that are not dependent on each other.
This is a good thing and a great step forward, because until QGIS 2.2 there was big internal monolithic
<code class="highlighter-rouge">QgsLegend</code> view class that handled everything and it was directly connected to map canvas and various other
components, making it impossible to reuse it elsewhere. With the new layer tree API this has been solved,
now it is possible use map canvas without an associated layer tree view or vice versa - to use a
layer tree view without map canvas. It is even possible to get creative and use one layer tree with several
map canvas instances at once.</p>

<p>Layer tree and map canvas can be connected via <code class="highlighter-rouge">QgsLayerTreeMapCanvasBridge</code> class. It listens to signals
from the given layer tree hierarchy and updates canvas accordingly. Let’s see how we could create a new
map canvas that would show the same layers as the main canvas does:</p>

<div class="highlighter-rouge"><div class="highlight"><pre class="highlight"><code>canvas = QgsMapCanvas()
root = QgsProject.instance().layerTreeRoot()
bridge = QgsLayerTreeMapCanvasBridge(root, canvas)
canvas.zoomToFullExtent()
canvas.show()
</code></pre></div></div>

<p>That’s it! We have tied the new canvas with project’s layer tree. So any actions you do in the layer tree view
(for example, add or remove layers, enable or disable layers) are automatically passed to the new canvas.
And of course this does not work just with project’s layer tree - you could use any custom layer tree
in your layer tree model/view or canvas.</p>

<p>The bridge class has advanced functionality worth mentioning. By default the ordering of layers in canvas
is according to the order in the layer tree (with first layer in the tree being at the top), though
there are API methods to override the default order.</p>

<p>For convenience, the bridge by default also configures some settings of the canvas (this can be disabled if necessary):</p>

<ul>
  <li>enable on-the-fly reprojections if layers have different coordinate reference system (CRS)</li>
  <li>setup destination CRS and map units when first layers are added</li>
  <li>zoom to full extent when first layers are added</li>
</ul>

<h2 id="summary">Summary</h2>

<p>I hope you have enjoyed the three blog posts introducing QGIS layer tree API. They should cover
everything you need to know in order to start using the new functionality. In a future post we will
have a look at the new legend API that nicely complements the layer tree API - stay tuned!</p>

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
