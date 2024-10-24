---
source: "blog"
title: "Getting Started Writing QGIS Python Plugins"
date: "2014-10-17T13:00:00-0500"
link: "https://lutraconsulting.co.uk/blog/2014/10/17/getting-started-writing-qgis-python-plugins/"
draft: "false"
showcase: "planet"
subscribers: ["lutragis"]
author: "Lutra Consulting"
tags: []
---

<p>This blog post is a QGIS plugin tutorial for beginners.  It was written to support a workshop we ran for the Scottish QGIS user group here in the UK and aims to be a simple step-by-step guide.</p>

<p>In this tutorial you will develop your first QGIS plugin - a Map Tool for selecting the closest feature within multiple loaded vector layers.  Knowledge of Python is recommended but not required.</p>

<!-- more -->

<h2 id="the-goal">The Goal</h2>

<p>Before we get started let’s look at where we’re going.</p>

<p>We will develop a plugin that implements a new QGIS Map Tool.  The <em>Identify Features</em> <img alt="QGIS Identify Tool" src="https://www.lutraconsulting.co.uk/img/posts/identify-tool-icon.png" /> and <em>Pan Map</em> <img alt="QGIS Pan Tool" src="https://www.lutraconsulting.co.uk/img/posts/pan-tool-icon.png" /> tools are both examples of QGIS Map Tools.  A Map Tool is a tool which performs an action when used with the map canvas.</p>

<p>We will create a new <em>Select Nearest Feature</em> Map Tool <img alt="Nearest Feature Tool" src="https://www.lutraconsulting.co.uk/img/posts/nearest-feature-icon.png" /> which will sit in the plugins toolbar.</p>

<p>Our <em>Select Nearest Feature</em> Map Tool will allow the user to select the feature nearest a mouse click on the canvas.  For example, clicking here:</p>

<p><img alt="Example Canvas Click" src="https://www.lutraconsulting.co.uk/img/posts/closest-plugin-click.png" /></p>

<p>would select the following polygon:</p>

<p><img alt="Example Polygon Selection" src="https://www.lutraconsulting.co.uk/img/posts/closest-plugin-select.png" /></p>

<h2 id="the-starting-point">The Starting Point</h2>

<p>Before getting started:</p>

<ul>
  <li>Install a text editor (e.g. <a href="http://www.geany.org/Download/Releases" rel="nofollow" target="_blank">Geany</a>)</li>
  <li>Download and extract <a href="https://www.lutraconsulting.co.uk/downloads/getting-started-writing-qgis-python-plugins-data.zip">this code and data</a></li>
  <li>Install QGIS &gt;= 2.4</li>
  <li>Install the <em>Plugin Reloader</em> plugin</li>
  <li>Open the <a href="http://qgis.org/api/2.4/annotated.html" rel="nofollow" target="_blank">QGIS API documentation</a></li>
</ul>

<p>The <em>QGIS Plugin Builder</em> plugin was used to create a base plugin which we’ll modify to fit our requirements.</p>

<p>This base plugin can be found in the zip file mentioned above under <em>code/01__Empty Plugin/NearestFeature</em></p>

<p><em>code/01__Empty Plugin</em> contains a batch file <em>install.bat</em> that can be used to copy the plugin into your QGIS plugins folder, making it available to QGIS.</p>

<p>Let’s now load and run this simple base plugin in QGIS.</p>

<ul>
  <li>Run install.bat</li>
  <li>Restart QGIS if already open</li>
  <li>Open the Plugin Manager: Plugins &gt; Manage and Install Plugins</li>
  <li>Enable the <em>Nearest Feature</em> plugin</li>
</ul>

<p>A new action <img alt="Nearest Feature Tool" src="https://www.lutraconsulting.co.uk/img/posts/nearest-feature-icon.png" /> should now be visible in the plugins toolbar which opens the following dialog:</p>

<p><img alt="Empty Dialog" src="https://www.lutraconsulting.co.uk/img/posts/nearest-feature-empty-dialog.png" /></p>

<h2 id="creating-a-basic-map-tool">Creating a Basic Map Tool</h2>

<p>When activated, our plugin currently shows a simple dialog (functionality provided by the <em>Plugin Builder</em> plugin.  We’re going to adapt it to instead activate a Map Tool.</p>

<p>A basic Map Tool is included within the zip file mentioned above.  It can be found in <em>nearest_feature_map_tool.py</em> in the <em>Additional Files</em> folder.</p>

<ul>
  <li>Copy <em>nearest_feature_map_tool.py</em> into the <em>NearestFeature</em> folder and open it in an editor.</li>
  <li>Note that many of the code segments (highlighted in <code class="highlighter-rouge">gray</code>) below link to relevant parts of the API docs.  Those links will open in a dedicated browser tab.</li>
</ul>

<p><em>nearest_feature_tool.py</em> defines a new <code class="highlighter-rouge">NearestFeatureMapTool</code> class (line 28) which inherits (is based on) <a href="http://qgis.org/api/2.4/classQgsMapTool.html" rel="nofollow" target="_api"><code class="highlighter-rouge">QgsMapTool</code></a>, the QGIS Map Tool class.  Its <code class="highlighter-rouge">__init__()</code> method expects to be passed a reference to a <a href="http://qgis.org/api/2.4/classQgsMapCanvas.html" rel="nofollow" target="_api"><code class="highlighter-rouge">QgsMapCanvas</code></a>.  This canvas reference is passed to the constructor of the underlying <a href="http://qgis.org/api/2.4/classQgsMapTool.html" rel="nofollow" target="_api"><code class="highlighter-rouge">QgsMapTool</code></a> class on line 32 and then stored on line 33 for later use.  The <a href="http://qgis.org/api/2.4/classQgsMapTool.html" rel="nofollow" target="_api">QGIS API documentation</a> describes the functionality made available by <a href="http://qgis.org/api/2.4/classQgsMapTool.html" rel="nofollow" target="_api"><code class="highlighter-rouge">QgsMapTool</code></a>.</p>

<p>On line 34 we define a simple, different-looking cursor (a <a href="http://qt-project.org/doc/qt-4.8/qcursor.html" rel="nofollow" target="_api"><code class="highlighter-rouge">QCursor</code></a> based on <code class="highlighter-rouge">Qt.CrossCursor</code>) later used to indicate that the Map Tool is active.</p>

<p>Our class definition features a method called <a href="http://qgis.org/api/2.4/classQgsMapTool.html#ae43d0b80202ae4c9706c6154ae04b525" rel="nofollow" target="_api"><code class="highlighter-rouge">activate()</code></a>. Notice the API documentation for <a href="http://qgis.org/api/2.4/classQgsMapTool.html" rel="nofollow" target="_api"><code class="highlighter-rouge">QgsMapTool</code></a> already defines a method with the same name.  Any methods defined as <em>virtual</em> methods in the API documentation can be overwritten or redefined as they have been within this file.  Here we have overwritten the default implementation of <a href="http://qgis.org/api/2.4/classQgsMapTool.html#ae43d0b80202ae4c9706c6154ae04b525" rel="nofollow" target="_api"><code class="highlighter-rouge">activate()</code></a>.</p>

<p>The <a href="http://qgis.org/api/2.4/classQgsMapTool.html#ae43d0b80202ae4c9706c6154ae04b525" rel="nofollow" target="_api"><code class="highlighter-rouge">activate()</code></a> method is called when the tool is activated.  The new cursor based on <code class="highlighter-rouge">Qt.CrossCursor</code> defined above is set with a call to <a href="http://qgis.org/api/2.4/classQgsMapTool.html#a7e7c23ef178baef9884d874620ea6968" rel="nofollow" target="_api"><code class="highlighter-rouge">QgsMapCanvas.setCursor()</code></a>.</p>

<p>For the moment, when activated, our Map Tool would simply change the cursor style - that’s all.</p>

<p>Great - next we’ll get our plugin to use the new Map Tool.</p>

<h2 id="connecting-the-basic-map-tool">Connecting the Basic Map Tool</h2>

<p>In this section we will modify the plugin to make use of our new Map Tool.</p>

<ul>
  <li>Open nearest_feature.py in a text editor.</li>
</ul>

<p>We need to first import the <code class="highlighter-rouge">NearestFeatureMapTool</code> class before we can use it.</p>

<ul>
  <li>Add the following code towards the top of the file just before <code class="highlighter-rouge">os.path</code> is imported:</li>
</ul>

<div class="highlighter-rouge"><div class="highlight"><pre class="highlight"><code>from nearest_feature_map_tool import NearestFeatureMapTool
</code></pre></div></div>

<p>Next we will create a new instance of the <code class="highlighter-rouge">NearestFeatureMapTool</code> class and store a reference to it in <code class="highlighter-rouge">self.nearestFeatureMapTool</code>.</p>

<ul>
  <li>Add the following code to the <code class="highlighter-rouge">initGui()</code> method just before the call to <code class="highlighter-rouge">self.add_action()</code> taking care to ensure the indentation is correct:</li>
</ul>

<div class="highlighter-rouge"><div class="highlight"><pre class="highlight"><code># Create a new NearestFeatureMapTool and keep reference
self.nearestFeatureMapTool = NearestFeatureMapTool(self.iface.mapCanvas())
</code></pre></div></div>

<p>Notice that a reference to the map canvas has been passed when creating the new NearestFeatureMapTool instance.</p>

<p>The <code class="highlighter-rouge">run()</code> method is called when our plugin is called by the user.  It’s currently used to show the dialog we saw previously.  Let’s overwrite its current implementation with the following:</p>

<div class="highlighter-rouge"><div class="highlight"><pre class="highlight"><code># Simply activate our tool
self.iface.mapCanvas().setMapTool(self.nearestFeatureMapTool)
</code></pre></div></div>

<p>The QGIS map canvas (<a href="http://qgis.org/api/2.4/classQgsMapCanvas.html" rel="nofollow" target="_api"><code class="highlighter-rouge">QgsMapCanvas</code></a> class) provides the <a href="http://qgis.org/api/2.4/classQgsMapCanvas.html#a56daede1f52bfdade5064a61e9d9a8ce" rel="nofollow" target="_api"><code class="highlighter-rouge">setMapTool()</code></a> method for setting map tools.  This method takes a reference to the new map tool, in this case a reference to a <code class="highlighter-rouge">NearestFeatureMapTool</code>.</p>

<p>To ensure that we leave things in a clean state when the plugin is unloaded (or reloaded) we should also ensure the Map Tool is unset when the plugin’s <code class="highlighter-rouge">unload()</code> method is called.</p>

<ul>
  <li>Add the following code to the end of the <code class="highlighter-rouge">unload()</code> method:</li>
</ul>

<div class="highlighter-rouge"><div class="highlight"><pre class="highlight"><code># Unset the map tool in case it's set
self.iface.mapCanvas().unsetMapTool(self.nearestFeatureMapTool)
</code></pre></div></div>

<p>Now let’s see the new map tool in action.</p>

<ul>
  <li>Save your files</li>
  <li>Run install.bat to copy the updated files to the QGIS plugin folder</li>
  <li>Configure the <em>Plugin Reloader</em> plugin to reload the NearestFeature plugin using its configure button, <img alt="Configure Plugin Reloader Tool" src="https://www.lutraconsulting.co.uk/img/posts/configure-reload-plugin-icon.png" /></li>
</ul>

<p><img alt="Configure Plugin Reloader Dialog" src="https://www.lutraconsulting.co.uk/img/posts/configure-reload-plugin.png" /></p>

<ul>
  <li>Reload the Nearest Feature plugin using the <img alt="Reload Plugin Tool" src="https://www.lutraconsulting.co.uk/img/posts/reload-plugin-icon.png" /> button.</li>
  <li>Click the <img alt="Nearest Feature Tool" src="https://www.lutraconsulting.co.uk/img/posts/nearest-feature-icon.png" /> button</li>
</ul>

<p>When passing the mouse over the map canvas the cursor should now be shown as a simple cursor resembling a <em>plus sign</em>.  Congratulations - the Map Tool is being activated.</p>

<h2 id="map-tool-state">Map Tool State</h2>

<p>When you use the <em>Identify Features</em> Map Tool you’ll notice that its button remains depressed when the tool is in use. The button for our map tool does not yet act in this way.  Let’s fix that.</p>

<p>The <em>action</em> (<a href="http://qt-project.org/doc/qt-4.8/qaction.html" rel="nofollow" target="_api"><code class="highlighter-rouge">QAction</code></a>) associated with our plugin is defined in the <code class="highlighter-rouge">initGui()</code> method with a call to <code class="highlighter-rouge">self.add_action()</code>.</p>

<p><code class="highlighter-rouge">self.add_action()</code> actually returns a reference to the new action that’s been added.   We’ll make use of this behaviour to make the action / button associated with our Map Tool toggleable (checkable).</p>

<ul>
  <li>Modify the call to <code class="highlighter-rouge">add_action()</code> as follows:</li>
</ul>

<div class="highlighter-rouge"><div class="highlight"><pre class="highlight"><code>action = self.add_action(
            icon_path,
            text=self.tr(u'Select nearest feature.'),
            callback=self.run,
            parent=self.iface.mainWindow())

action.setCheckable(True)
</code></pre></div></div>

<p>We now use the reference to the new action to make it checkable.</p>

<p>The <a href="http://qgis.org/api/2.4/classQgsMapTool.html" rel="nofollow" target="_api"><code class="highlighter-rouge">QgsMapTool</code></a> class has a <a href="http://qgis.org/api/2.4/classQgsMapTool.html#a861b5670efeb10e9356fea9dbac57641" rel="nofollow" target="_api"><code class="highlighter-rouge">setAction()</code></a> method which can be used to associate a <a href="http://qt-project.org/doc/qt-4.8/qaction.html" rel="nofollow" target="_api"><code class="highlighter-rouge">QAction</code></a> with the Map Tool.  This allows the Map Tool to handle making the associated button look pressed.</p>

<ul>
  <li>Add the following line to the end of <code class="highlighter-rouge">initGui()</code>:</li>
</ul>

<div class="highlighter-rouge"><div class="highlight"><pre class="highlight"><code>self.nearestFeatureMapTool.setAction(action)
</code></pre></div></div>

<ul>
  <li>Save your files and run install.bat</li>
  <li>Reload the Nearest Feature plugin using the <img alt="Reload Plugin" src="https://www.lutraconsulting.co.uk/img/posts/reload-plugin-icon.png" /> button</li>
  <li>Click the <img alt="Nearest Feature Tool" src="https://www.lutraconsulting.co.uk/img/posts/nearest-feature-icon.png" /> button</li>
</ul>

<p>The button should now remain pressed, indicating that the tool is in use.</p>

<ul>
  <li>Activate the <em>Identify Features</em> <img alt="Identify Features Tool" src="https://www.lutraconsulting.co.uk/img/posts/identify-tool-icon.png" /> tool</li>
</ul>

<p>The Nearest Feature button should now appear unpressed.</p>

<h2 id="handling-mouse-clicks">Handling Mouse Clicks</h2>

<p>The <a href="http://qgis.org/api/2.4/classQgsMapTool.html" rel="nofollow" target="_api"><code class="highlighter-rouge">QgsMapTool</code></a> class has a number of methods for handling user events such as mouse clicks and movement.  We will override the <a href="http://qgis.org/api/2.4/classQgsMapTool.html#acbe6dac923ba3e27635decd42a30bc12" rel="nofollow" target="_api"><code class="highlighter-rouge">canvasReleaseEvent()</code></a> method to implement the search for the closest feature.  <a href="http://qgis.org/api/2.4/classQgsMapTool.html#acbe6dac923ba3e27635decd42a30bc12" rel="nofollow" target="_api"><code class="highlighter-rouge">canvasReleaseEvent()</code></a> is called whenever the user clicks on the map canvas and is passed a <a href="http://qt-project.org/doc/qt-4.8/qmouseevent.html" rel="nofollow" target="_api"><code class="highlighter-rouge">QMouseEvent</code></a> as an argument.</p>

<p>We will now write some functionality which:</p>

<ol>
  <li>Loops through all visible vector layers and for each:
    <ul>
      <li>Deselects all features</li>
      <li>Loops through all features and for each:
        <ul>
          <li>Determines their distance from the mouse click</li>
          <li>Keeps track of the closest feature and its distance</li>
        </ul>
      </li>
    </ul>
  </li>
  <li>Determines the closest feature from all layers</li>
  <li>Selects that feature</li>
</ol>

<p> </p>

<ul>
  <li>Add the following method to the NearestFeatureMapTool class:</li>
</ul>

<div class="highlighter-rouge"><div class="highlight"><pre class="highlight"><code>def canvasReleaseEvent(self, mouseEvent):
    """
    Each time the mouse is clicked on the map canvas, perform
    the following tasks:
        Loop through all visible vector layers and for each:
            Ensure no features are selected
            Determine the distance of the closes feature in the layer to the mouse click
            Keep track of the layer id and id of the closest feature
        Select the id of the closes feature
    """

    layerData = []

    for layer in self.canvas.layers():

        if layer.type() != QgsMapLayer.VectorLayer:
            # Ignore this layer as it's not a vector
            continue

        if layer.featureCount() == 0:
            # There are no features - skip
            continue

        layer.removeSelection()
</code></pre></div></div>

<p>The <a href="http://qgis.org/api/2.4/classQgsMapCanvas.html#a43c643d06e315b90c25e10d8a4644f4e" rel="nofollow" target="_api"><code class="highlighter-rouge">layers()</code></a> method of <a href="http://qgis.org/api/2.4/classQgsMapCanvas.html" rel="nofollow" target="_api"><code class="highlighter-rouge">QgsMapCanvas</code></a> (stored earlier in <code class="highlighter-rouge">self.canvas</code>) returns a list of <a href="http://qgis.org/api/2.4/classQgsMapLayer.html" rel="nofollow" target="_api"><code class="highlighter-rouge">QgsMapLayer</code></a>. These are references to all visible layers and could represent vector layers, raster layers or even plugin layers.</p>

<p>We use the <a href="http://qgis.org/api/2.4/classQgsMapLayer.html#a209afd81e5d57a7d909acab01ed608e0" rel="nofollow" target="_api"><code class="highlighter-rouge">type()</code></a> and <a href="http://qgis.org/api/2.4/classQgsVectorLayer.html#a65286a9f1c393269cc392fbe539b37b0" rel="nofollow" target="_api"><code class="highlighter-rouge">featureCount()</code></a> methods to skip non-vector layers and empty vector layers.</p>

<p>Finally we use the layer’s <a href="http://qgis.org/api/2.4/classQgsVectorLayer.html#acedacb37761e05ab82e068d693959c86" rel="nofollow" target="_api"><code class="highlighter-rouge">removeSelection()</code></a> method to clear any existing selection.  <code class="highlighter-rouge">layerData</code> is a list that we’ll use in a moment.</p>

<p>Our plugin now clears the selection in all visible vector layers.</p>

<ul>
  <li>Open the Shapefiles included in the Data folder.</li>
  <li>Make a selection of one or more layers.</li>
  <li>Reload the plugin and ensure it is working as expected (removing any selection).</li>
</ul>

<h2 id="accessing-features-and-geometry">Accessing Features and Geometry</h2>

<p>We now need access to each feature and its geometry to determine its distance from the mouse click.</p>

<ul>
  <li>Add the following code to <code class="highlighter-rouge">canvasReleaseEvent()</code> within the loop over layers:</li>
</ul>

<div class="highlighter-rouge"><div class="highlight"><pre class="highlight"><code># Determine the location of the click in real-world coords
layerPoint = self.toLayerCoordinates( layer, mouseEvent.pos() )

shortestDistance = float("inf")
closestFeatureId = -1

# Loop through all features in the layer
for f in layer.getFeatures():
    dist = f.geometry().distance( QgsGeometry.fromPoint( layerPoint) )
    if dist &lt; shortestDistance:
        shortestDistance = dist
        closestFeatureId = f.id()

info = (layer, closestFeatureId, shortestDistance)
layerData.append(info)
</code></pre></div></div>

<p>The mouse click event (a <a href="http://qt-project.org/doc/qt-4.8/qmouseevent.html" rel="nofollow" target="_api"><code class="highlighter-rouge">QMouseEvent</code></a>) is stored in <code class="highlighter-rouge">mouseEvent</code>. Its <a href="http://qt-project.org/doc/qt-4.8/qmouseevent.html#pos" rel="nofollow" target="_api"><code class="highlighter-rouge">pos()</code></a> method returns a <a href="http://qt-project.org/doc/qt-4.8/qpoint.html" rel="nofollow" target="_api"><code class="highlighter-rouge">QPoint</code></a> describing the position of the mouse click relative to the map canvas (x and y pixel coordinates).  To calculate its distance to each feature we’ll need to first convert the mouse click position into real world (layer) coordinates.  This can be done using a call to <a href="http://qgis.org/api/2.2/classQgsMapTool.html#a4f7916307e7098786bdb3994d358922e" rel="nofollow" target="_api"><code class="highlighter-rouge">QgsMapTool.toLayerCoordinates()</code></a> which automatically deals with on-the-fly projection and returns a <a href="http://qgis.org/api/2.2/classQgsPoint.html" rel="nofollow" target="_api"><code class="highlighter-rouge">QPoint</code></a> in layer coordinates.</p>

<p>The features of a vector layer can be accessed using the layer’s <a href="http://qgis.org/api/2.4/classQgsVectorLayer.html#a412ac9a3563e542485927bde03397962" rel="nofollow" target="_api"><code class="highlighter-rouge">getFeatures()</code></a> method which returns (by default) a list of all <a href="http://qgis.org/api/2.4/classQgsFeature.html" rel="nofollow" target="_api"><code class="highlighter-rouge">QgsFeature</code></a> in the layer that we can iterate over using a simple loop.</p>

<p>With access to features we can easily gain access to geometry using <a href="http://qgis.org/api/2.4/classQgsFeature.html#a2593e515a73b8bc33d80abbb1bc69354" rel="nofollow" target="_api"><code class="highlighter-rouge">QgsFeature.geometry()</code></a>.  The <a href="http://qgis.org/api/2.4/classQgsGeometry.html" rel="nofollow" target="_api"><code class="highlighter-rouge">QgsGeometry</code></a> class has a number of spatial relationship methods including <a href="http://qgis.org/api/2.4/classQgsGeometry.html#a9971f1e9c56cdf57c06017ec64e70151" rel="nofollow" target="_api"><code class="highlighter-rouge">distance()</code></a> which returns the distance to a second <a href="http://qgis.org/api/2.4/classQgsGeometry.html" rel="nofollow" target="_api"><code class="highlighter-rouge">QgsGeometry</code></a> passed as an argument.</p>

<p>In the code above we loop over all features, keeping track of the feature id of the closest feature using <a href="http://qgis.org/api/2.2/classQgsFeature.html#ab16e0aa72ae9904e5260f29816ac4fac" rel="nofollow" target="_api"><code class="highlighter-rouge">QgsFeature.id()</code></a>.  The shortest distance and closest feature id are stored in <code class="highlighter-rouge">shortestDistance</code> and <code class="highlighter-rouge">closestFeature</code>.  When we are finished iterating through all the features in this layer, we store a note of the layer, its closest feature id and associated distance into <code class="highlighter-rouge">layerData</code>.</p>

<p>Note that we convert <code class="highlighter-rouge">layerPoint</code> (a <a href="http://qgis.org/api/2.4/classQgsPoint.html" rel="nofollow" target="_api"><code class="highlighter-rouge">QgsPoint</code></a>) into a <a href="http://qgis.org/api/2.4/classQgsGeometry.html" rel="nofollow" target="_api"><code class="highlighter-rouge">QgsGeometry</code></a> so we can use it directly in spatial relationship operations such as <a href="http://qgis.org/api/2.4/classQgsGeometry.html#a9971f1e9c56cdf57c06017ec64e70151" rel="nofollow" target="_api"><code class="highlighter-rouge">QgsGeometry.distance()</code></a>.</p>

<h2 id="completing-canvasreleaseevent">Completing canvasReleaseEvent</h2>

<p>We’re almost done.  At this point <code class="highlighter-rouge">layerData</code> is a list of tuples, one for each vector layer containing:</p>

<ol>
  <li>A reference to the layer</li>
  <li>The id of the closest feature within that layer</li>
  <li>The distance of that closest feature from the mouse click</li>
</ol>

<p>Now we can simply sort <code class="highlighter-rouge">layerData</code> by distance (its 3rd <em>column</em>) and make a selection based on the layer and feature in the first row of <code class="highlighter-rouge">layerData</code>.</p>

<ul>
  <li>Add the following code to <code class="highlighter-rouge">canvasReleaseEvent()</code> outside the outer <em>for</em> loop:</li>
</ul>

<div class="highlighter-rouge"><div class="highlight"><pre class="highlight"><code>if not len(layerData) &gt; 0:
    # Looks like no vector layers were found - do nothing
    return

# Sort the layer information by shortest distance
layerData.sort( key=lambda element: element[2] )

# Select the closest feature
layerWithClosestFeature, closestFeatureId, shortestDistance = layerData[0]
layerWithClosestFeature.select( closestFeatureId )
</code></pre></div></div>

<p>The code above returns early if no workable vector layers were found.  It sorts <code class="highlighter-rouge">layerData</code> (the list of tuples) by the 3rd element (the distance).</p>

<p>The code then calls <a href="http://qgis.org/api/2.4/classQgsVectorLayer.html#accc4ac76dc76a279a33a934749daa2d5" rel="nofollow" target="_api"><code class="highlighter-rouge">QgsVectorLayer.select()</code></a> to select the closest feature by its feature id.</p>

<p>The plugin should now be finished.</p>

<ul>
  <li>Reload the plugin</li>
  <li>Ensure it works as expected.</li>
</ul>

<h2 id="summary">Summary</h2>

<p>Within this tutorial we’ve worked briefly with the following parts of the QGIS API:</p>

<ul>
  <li>Map Tools</li>
  <li>Map Canvas</li>
  <li>Vector Layers</li>
  <li>Features</li>
  <li>Geometry</li>
</ul>

<p>Hopefully this has been a useful tutorial.  Please feel free to <a href="mailto:info@lutraconsulting.co.uk">contact us</a> with any specific questions.</p>

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
