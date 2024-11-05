---
source: "blog"
title: "Identify feature on map"
date: "2013-02-14T10:48:58+0000"
link: "https://3nids.wordpress.com/2013/02/14/identify-feature-on-map/"
draft: "false"
showcase: "planet"
subscribers: ["qgis_tips"]
author: "QGIS Tips"
tags: ["map tools", "plugins"]
---

<p>A very awaited feature is now available in the master version of QGIS: identifying features in the map!</p>
<p>You can define the class of the map tool as follows:</p>
<pre class="brush: python; title: ; wrap-lines: false; notranslate">
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from qgis.core import *
from qgis.gui import *

class IdentifyGeometry(QgsMapToolIdentify):
 def __init__(self, canvas):
  self.canvas = canvas
  QgsMapToolIdentify.__init__(self, canvas)

 def canvasReleaseEvent(self, mouseEvent):
  results = self.identify(mouseEvent.x(),mouseEvent.y(), self.TopDownStopAtFirst, self.VectorLayer)
  if len(results) &gt; 0:
   self.emit( SIGNAL( &quot;geomIdentified&quot; ), results[0].mLayer, results[0].mFeature)
</pre>
<p>This class will try to identify a feature of any visible vector layer and returning the first found feature (using layer order). Then, it will emit the signal with the layer and the feature identified.<br />
To customize this, you can use the identify method with different arguments:</p>
<ul>
<li>type of layer</li>
<li>type of identification (current layer, top-down, top-down stop at first or the QGIS setting)</li>
<li>list of layers</li>
</ul>
<p>There is two ways of calling the identify methods:</p>
<ul>
<li><span style="line-height: 13px;">identify (x, y, layerList=[], IdentifyMode mode=self.DefaultQgsSetting)</span></li>
<li>identify (x, y, identifyMode, layerType=AllLayers)</li>
</ul>
<p>Identify mode and layer types are defined <a href="http://www.qgis.org/api/classQgsMapToolIdentify.html#pub-types" target="_blank" title="API reference">here</a>. Mainly the options can be:</p>
<ul>
<li>Identify mode: self.DefaultQgsSetting, self.ActiveLayer, self.TopDownStopAtFirst, self.TopDownAll</li>
<li>Layer type: self.AllLayers, self.VectorLayer, self.RasterLayer</li>
</ul>
<p>Both methods return a structure IdentifyResult defined in the <a href="http://www.qgis.org/api/structQgsMapToolIdentify_1_1IdentifyResult.html" target="_blank" title="API reference">API</a>. Mainly, it contains:</p>
<ul>
<li><span style="line-height: 13px;">the feature (mFeature) if the identified layer is a vector layer</span></li>
<li>the corresponding layer (mLayer)</li>
<li>the derived attributes (mDerivedAttributes): the raster value for raster layers</li>
</ul>
<p>In your plugin main code, you can define a toolbox button to enable your map tool:</p>
<pre class="brush: python; title: ; wrap-lines: false; notranslate">
class myPlugin():
 def initGui(self):
  self.mapToolAction = QAction(QIcon(&quot;:/plugins/myPlugin/icons/myIcon.png&quot;), &quot;My Plugin&quot;, self.iface.mainWindow())
  self.mapToolAction.setCheckable(True)
  QObject.connect(self.mapToolAction, SIGNAL(&quot;triggered()&quot;), self.mapToolInit)
  self.iface.addToolBarIcon(self.mapToolAction)
  self.iface.addPluginToMenu(&quot;&amp;My Plugin&quot;, self.mapToolAction)

 def mapToolInit(self):
  canvas = self.iface.mapCanvas()
  if self.mapToolAction.isChecked() is False:
   canvas.unsetMapTool(self.mapTool)
   return
  self.mapToolAction.setChecked( True )
  self.mapTool = IdentifyGeometry(canvas)
  QObject.connect(self.mapTool , SIGNAL(&quot;geomIdentified&quot;) , self.doSometing )
  canvas.setMapTool(self.mapTool)
  QObject.connect( canvas, SIGNAL( &quot;mapToolSet(QgsMapTool *)&quot; ), self.mapToolChanged)&lt;/em&gt;

 def doSomething(self, layer, feature):
  # do something
</pre>
<p>If you want your plugin to be back compatible with version before 1.9, you can select the features at the clicked point using a given tolerance and using the current layer:</p>
<pre class="brush: python; title: ; wrap-lines: false; notranslate">
try:
 from qgis.gui import QgsMapToolIdentify
except:
 from qgis.gui import QgsMapTool as QgsMapToolIdentify

class IdentifyGeometry(QgsMapToolIdentify):
 def __init__(self, canvas):
  self.canvas = canvas
  QgsMapToolIdentify.__init__(self, canvas)

 def canvasReleaseEvent(self, mouseEvent):
  try:
  results = self.identify(mouseEvent.x(),mouseEvent.y(), self.TopDownStopAtFirst, self.VectorLayer)
  if len(results) &gt; 0:
   self.emit( SIGNAL( &quot;geomIdentified&quot; ), results[0].mLayer, results[0].mFeature)
  except: # qgis &lt;1.9
   point = self.toMapCoordinates( mouseEvent.pos() )
   layer = self.canvas.currentLayer()
   if layer == None:
    return
   if layer.type() != QgsMapLayer.VectorLayer:
    return
   point = self.canvas.mapRenderer().mapToLayerCoordinates(layer, point)
   pixTolerance = 6
   mapTolerance = pixTolerance * self.canvas.mapUnitsPerPixel()
   rect = QgsRectangle(point.x()-mapTolerance,point.y()-mapTolerance,point.x()+mapTolerance,point.y()+mapTolerance)
   provider = layer.dataProvider()
   provider.select([], rect, True, True)
   subset = []
   f = QgsFeature()
   while (provider.nextFeature(f)):
    subset.append(f)
    if len(subset) == 0:
     return
    if len(subset) &gt; 1:
     idx = QgsSpatialIndex()
    for f in subset:
     idx.insertFeature(f)
     nearest = idx.nearestNeighbor( point, 1 )
     layer.featureAtId(nearest[0],f, True, False)
    self.emit( SIGNAL( &quot;geomIdentified&quot; ), layer, f)
</pre>
<p>Note, that this last code (for version &lt;1.9) does not consider scale dependent visibility and can therefore return a feature which is not visible in the map!</p>
