---
source: "blog"
title: "Create a QGIS vector data provider in Python is now possible"
date: "2018-06-06T12:24:41+0000"
link: "https://www.itopen.it/qgis-vector-data-provider-python/"
draft: "false"
showcase: "planet"
subscribers: ["itopen"]
author: "ItOpen"
tags: ["gis", "qgis"]
---

<p>&nbsp;</p>
<h2>Why python data providers?</h2>
<p>My main reasons for having Python data provider were:</p>
<ul>
	<li>quick prototyping</li>
	<li>web services</li>
	<li>why not?</li>
</ul>
<p>&nbsp;</p>
<p>This topic has been floating in my head for a while since I decided to give it a second look and I finally implemented it and merged for the next 3.2 release.</p>
<p>&nbsp;</p>
<h2>How it&#8217;s been done</h2>
<p>To make this possible I had to:</p>
<ul>
	<li>create a public API for registering the providers</li>
	<li>create the Python bindings (the hard part)</li>
	<li>create a sample Python vector data provider (the boring part)</li>
	<li>make all the tests pass</li>
</ul>
<p>&nbsp;</p>
<p>First, let me say that it wasn&#8217;t like a walk in the park: the Python bindings part is always like diving into woodoo and black magic recipes before I can get it to work properly.</p>
<p>For the Python provider sample implementation I decided to re-implement the memory (aka: scratch layers) provider because that&#8217;s one of the simplest providers and it does not depend on any external storage or backend.</p>
<p>&nbsp;</p>
<h2>How to and examples</h2>
<p>For now, the main source of information is the API and the tests:</p>
<ul>
	<li>
<ul>
	<li><a href="https://github.com/qgis/QGIS/blob/master/src/core/qgsproviderregistry.h#L188">https://github.com/qgis/QGIS/blob/master/src/core/qgsproviderregistry.h#L188</a></li>
	<li><a href="https://github.com/qgis/QGIS/blob/master/tests/src/python/provider_python.py">https://github.com/qgis/QGIS/blob/master/tests/src/python/provider_python.py</a></li>
	<li><a href="https://github.com/qgis/QGIS/blob/master/tests/src/python/test_provider_python.py">https://github.com/qgis/QGIS/blob/master/tests/src/python/test_provider_python.py</a></li>
</ul>
</li>
</ul>
<p>To register your own provider (<code>PyProvider</code> in the snippet below) these are the basic steps:</p>
<pre class="wp-code-highlight prettyprint">metadata = QgsProviderMetadata(PyProvider.providerKey(), PyProvider.description(), PyProvider.createProvider)
QgsProviderRegistry.instance().registerProvider(metadata)
</pre>
<p>To create your own provider you will need at least the following components:</p>
<ul>
	<li>the provider class itself (subclass of <code>QgsVectorDataProvider</code>)</li>
	<li>a feature source (subclass of <code>QgsAbstractFeatureSource</code>)</li>
	<li>a feature iterator (subclass of <code>QgsAbstractFeatureIterator</code>)</li>
</ul>
<p>Be aware that the implementation of a data provider is not easy and you will need to write a lot of code, but at least you could get some inspiration from the existing example.</p>
<p>&nbsp;</p>
<p>Enjoy wirting data providers in Python and please let me know if you&#8217;ve fond this implementation useful!</p><p>The post <a href="https://www.itopen.it/qgis-vector-data-provider-python/">Create a QGIS vector data provider in Python is now possible</a> first appeared on <a href="https://www.itopen.it">Open Web Solutions, GIS & Python Development</a>.</p>
