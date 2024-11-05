---
source: "blog"
title: "Speeding up your PyQGIS scripts"
date: "2016-10-17T04:07:25+0000"
link: "http://nyalldawson.net/2016/10/speeding-up-your-pyqgis-scripts/"
draft: "false"
showcase: "planet"
subscribers: ["nyalldawson_net"]
author: "nyalldawson.net"
tags: ["qgis", "geospatial", "osgeo", "pyqgis", "python", "qgis"]
---

<p>I&#8217;ve recently spent some time optimising the performance of various QGIS plugins and algorithms, and I&#8217;ve noticed that there&#8217;s a few common performance traps which developers fall into when fetching features from a vector layer. In this post I&#8217;m going to explore these traps, what makes them slow, and how to avoid them.</p>
<p>As a bit of background, features are fetched from a vector layer in QGIS using a <a href="https://qgis.org/api/classQgsFeatureRequest.html">QgsFeatureRequest</a> object. Common use is something like this:</p>
<pre class="brush: python; title: ; notranslate">
request = QgsFeatureRequest()
for feature in vector_layer.getFeatures(request):
    # do something
</pre>
<p>This code would iterate over all the features in layer. Filtering the features is done by tweaking the QgsFeatureRequest, such as:</p>
<pre class="brush: python; title: ; notranslate">
request = QgsFeatureRequest().setFilterFid(1001)
feature_1001 = next(vector_layer.getFeatures(request))
</pre>
<p>In this case calling getFeatures(request) just returns the single feature with an ID of 1001 (which is why we shortcut and use next(&#8230;) here instead of iterating over the results).</p>
<p>Now, here&#8217;s the trap: calling getFeatures is expensive. If you call it on a vector layer, QGIS will be required to setup an new connection to the data store (the layer provider), create some query to return data, and parse each result as it is returned from the provider. This can be slow, especially if you&#8217;re working with some type of remote layer, such as a PostGIS table over a VPN connection. This brings us to our first trap:</p>
<h2>Trap #1: Minimise the calls to getFeatures()</h2>
<p>A common task in PyQGIS code is to take a list of feature IDs and then request those features from the layer. A see a lot of older code which does this using something like:</p>
<pre class="brush: python; title: ; notranslate">
for id in some_list_of_feature_ids:
    request = QgsFeatureRequest().setFilterFid(id)
    feature = next(vector_layer.getFeatures(request))
    # do something with the feature
</pre>
<p>Why is this a bad idea? Well, remember that every time you call getFeatures() QGIS needs to do a whole bunch of things before it can start giving you the matching features. In this case, the code is calling getFeatures() once for every feature ID in the list. So if the list had 100 features, that means QGIS is having to create a connection to the data source, set up and prepare a query to match a single feature, wait for the provider to process that, and then finally parse the single feature result. That&#8217;s a lot of wasted processing!</p>
<p>If the code is rewritten to take the call to getFeatures() outside of the loop, then the result is:</p>
<pre class="brush: python; title: ; notranslate">
request = QgsFeatureRequest().setFilterFids(some_list_of_feature_ids)
for feature in vector_layer.getFeatures(request):
    # do something with the feature
</pre>
<p>Now there&#8217;s just a single call to getFeatures() here. QGIS optimises this request by using a single connection to the data source, preparing the query just once, and fetching the results in appropriately sized batches. The difference is huge, especially if you&#8217;re dealing with a large number of features.</p>
<h2>Trap #2: Use QgsFeatureRequest filters appropriately</h2>
<p>Here&#8217;s another common mistake I see in PyQGIS code. I often see this one when an author is trying to do something with all the selected features in a layer:</p>
<pre class="brush: python; title: ; notranslate">
for feature in vector_layer.getFeatures():
    if not feature.id() in vector_layer.selectedFeaturesIds():
        continue

    # do something with the feature
</pre>
<p>What&#8217;s happening here is that the code is iterating over all the features in the layer, and then skipping over any which aren&#8217;t in the list of selected features. See the problem here? This code iterates over EVERY feature in the layer. If you&#8217;re layer has 10 million features, we are fetching every one of these from the data source, going through all the work of parsing it into a QGIS feature, and then promptly discarding it if it&#8217;s not in our list of selected features. It&#8217;s very inefficient, especially if fetching features is slow (such as when connecting to a remote database source).</p>
<p>Instead, this code should use the <a href="https://qgis.org/api/classQgsFeatureRequest.html#a59955b7d1e3d23b32020465ce41e2da1">setFilterFids</a>() method for QgsFeatureRequest:</p>
<pre class="brush: python; title: ; notranslate">
request = QgsFeatureRequest().setFilterFids(vector_layer.selectedFeaturesIds())
for feature in vector_layer.getFeatures(request):
    # do something with the feature
</pre>
<p>Now, QGIS will only fetch features from the provider with matching feature IDs from the list. Instead of fetching and processing every feature in the layer, only the actual selected features will be fetched. It&#8217;s not uncommon to see operations which previously took many minutes (or hours!) drop down to a few seconds after applying this fix.</p>
<p>Another variant of this trap uses expressions to test the returned features:</p>
<pre class="brush: python; title: ; notranslate">
filter_expression = QgsExpression('my_field &amp;gt; 20')
for feature in vector_layer.getFeatures():
    if not filter_expression.evaluate(feature):
        continue

    # do something with the feature
</pre>
<p>Again, this code is fetching every single feature from the layer and then discarding it if it doesn&#8217;t match the &#8220;my_field &gt; 20&#8221; filter expression. By rewriting this to:</p>
<pre class="brush: python; title: ; notranslate">
request = QgsFeatureRequest().setFilterExpression('my_field &amp;gt; 20')
for feature in vector_layer.getFeatures(request):
    # do something with the feature
</pre>
<p>we hand over the bulk of the filtering to the data source itself. Recent QGIS versions intelligently translate the filter into a format which can be applied directly at the provider, meaning that any relevant indexes and other optimisations can be applied by the provider itself. In this case the rewritten code means that ONLY the features matching the &#8216;my_field &gt; 20&#8217; criteria are fetched from the provider &#8211; there&#8217;s no time wasted messing around with features we don&#8217;t need.</p>
<p>&nbsp;</p>
<h2>Trap #3: Only request values you need</h2>
<p>The last trap I often see is that more values are requested from the layer then are actually required. Let&#8217;s take the code:</p>
<pre class="brush: python; title: ; notranslate">
my_sum = 0
for feature in vector_layer.getFeatures(request):
    my_sum += feature['value']
</pre>
<p>In this case there&#8217;s no way we can optimise the filters applied, since we need to process every feature in the layer. But &#8211; this code is still inefficient. By default QGIS will fetch all the details for a feature from the provider. This includes all attribute values and the feature&#8217;s geometry. That&#8217;s a lot of processing &#8211; QGIS needs to transform the values from their original format into a format usable by QGIS, and the feature&#8217;s geometry needs to be parsed from it&#8217;s original type and rebuilt as a QgsGeometry object. In our sample code above we aren&#8217;t doing anything with the geometry, and we are only using a single attribute from the layer. By calling <a href="https://qgis.org/api/classQgsFeatureRequest.html#a57064dfedab31e466f9660f36dc6f6cf">setFlags</a>( QgsFeatureRequest.NoGeometry ) and <a href="https://qgis.org/api/classQgsFeatureRequest.html#a85f831f339a9882822d5d5cf19b29fdf">setSubsetOfAttributes</a>() we can tell QGIS that we don&#8217;t need the geometry, and we only require a single attribute&#8217;s value:</p>
<pre class="brush: python; title: ; notranslate">
my_sum = 0
request = QgsFeatureRequest().setFlags(QgsFeatureRequest.NoGeometry).setSubsetOfAttributes(['value'], vector_layer.fields() )
for feature in vector_layer.getFeatures(request):
    my_sum += feature['value']
</pre>
<p>None of the unnecessary geometry parsing will occur, and only the &#8216;value&#8217; attribute will be fetched and populated in the features. This cuts down both on the processing required AND the amount of data transfer between the layer&#8217;s provider and QGIS. It&#8217;s a significant improvement if you&#8217;re dealing with larger layers.</p>
<h2>Conclusion</h2>
<p>Optimising your feature requests is one of the easiest ways to speed up your PyQGIS script! It&#8217;s worth spending some time looking over all your uses of getFeatures() to see whether you can cut down on what you&#8217;re requesting &#8211; the results can often be mind blowing!</p>
