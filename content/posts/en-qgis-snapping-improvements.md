---
source: "blog"
title: "QGIS Snapping improvements"
date: "2020-01-10T09:39:10"
link: "https://oslandia.com/en/2020/01/10/en-qgis-snapping-improvements/"
draft: "false"
showcase: "planet"
subscribers: ["qgis_oslandia"]
author: "QGIS Oslandia"
tags: ["database", "gis", "qgis", "open source", "postgis", "snapping"]
---

<p>A few months ago, we proposed to the <a href="https://blog.qgis.org/2019/06/30/qgis-grant-programme-2019-results/">QGIS grant program</a> to make improvements to the snap cache in QGIS. The community vote selected our project which was funded by QGIS.org. Developments are now mostly finished.</p>
<p>In short, snapping is crucial for editing geospatial features. It is the only way to ensuring they are topologically related, ie, connected vertices have exactly the same coordinates even if manual digitizing on screen is imprecise by nature.  Snapping correctly supposes QGIS have in memory an indexed cache of the geometries to snap to. And maintainting this cache when data is modified, sometimes by another user or database logic, can be a real challenge. This it exactly what this work adresses.</p>
<p>The proposal was divided into two different tasks:</p>
<ul>
<li>Manage circular dependencies</li>
<li>Relax the snap cache index build</li>
</ul>
<h1>Manage cicular data dependencies</h1>
<h2>Data dependencies</h2>
<p>Data dependency is an existing feature that allows you to configure QGIS to reload layers (and their snapping cache) when a layer is modified.</p>
<p>It is useful when you store your data in a database and you set up triggers to maintain consistency between the different tables of your data model.</p>
<p>For instance, say you have topological informations containing lines and nodes. Nodes are part of lines and lines go through nodes. Then, you move a node in QGIS, and save your modifications to the database. In order to keep the data consistent, a trigger updates the geometry of the line going through the modified node.</p>
<p><img alt="" class="size-full wp-image-5322 aligncenter" height="154" src="https://oslandia.com/wp-content/uploads/2020/01/nodes.png" width="251" /></p>
<p style="text-align: center;">Node 2 is modified, Line 1 is updated accordingly</p>
<p>QGIS, as a database client, has no information that the line layer currently displayed in the canvas needs to be refreshed after the trigger. Although the map canvas will be up to date, because QGIS fetches data for display without any caching system, the snapping cache is not and you&#8217;ll end up with ghost snapping highlights issues.</p>
<p><img alt="" class=" wp-image-5341 aligncenter" height="182" src="https://oslandia.com/wp-content/uploads/2020/01/ghost.png" width="311" /></p>
<p style="text-align: center;">Snapping highlights (light red) differ from real line (orange)</p>
<p>Defining a dependency between nodes and lines layers tells QGIS that it has to refresh the line layer when a node is modified.</p>
<p style="text-align: center;"><img alt="" class="size-full wp-image-5353 aligncenter" height="515" src="https://oslandia.com/wp-content/uploads/2020/01/datadeps.png" width="953" />Dependencies configuration: Lines layer will be refreshed whenever Nodes layer is modified</p>
<p>It also have to work the other way, modifying a line should update the nodes to ensure they still are on the line.</p>
<h2>Circular data dependencies</h2>
<p>So here we are, lines depend on nodes which depend on lines which depend on nodes which&#8230;</p>
<p><img alt="" class="aligncenter size-medium wp-image-5358" height="300" src="https://oslandia.com/wp-content/uploads/2020/01/infinite_recursion-256x300.gif" width="256" /></p>
<p>That&#8217;s what circular dependencies is about. This specific behavior was previously forbidden and needed a special way to deal with it. Thanks to this <a href="https://github.com/qgis/QGIS/pull/30947">recent development</a>, it is now possible.</p>
<p>It&#8217;s also possible to add the layer itself as one of its own dependencies. It helps dealing with specific cases where one feature modification could lead to a modification of another feature in the same layer (to keep consistency on road networks for instance).</p>
<p><img alt="" class="size-full wp-image-5324 aligncenter" height="178" src="https://oslandia.com/wp-content/uploads/2020/01/roads.png" width="270" /></p>
<p style="text-align: center;">Road 2 is modified, Road 1 is updated accordingly</p>
<p>This feature is available in the next QGIS LTR version 3.10.</p>
<h1>Relax the snapping cache index build</h1>
<p>If you work in QGIS with huge projects displaying a lot of vector data, and you enable snapping while editing these data, you probably already met this dialog:</p>
<p style="text-align: center;"><img alt="" class="size-full wp-image-5318 aligncenter" height="243" src="https://oslandia.com/wp-content/uploads/2020/01/indexing.png" width="460" />Snap indexing dialog</p>
<p>This dialog informs you that data are currently being indexed so you can snap on them while you will edit feature geometry. And for big projects, this dialog can last for a really long time. Let&#8217;s work on speeding it up!</p>
<h2>What&#8217;s a snap index?</h2>
<p>Let&#8217;s say you want to move a line and snap it onto another one. While you drag your line with the mouse, QGIS will look for an existing geometry beneath the mouse cursor (with a certain pixel tolerance) every time you move your mouse. Without spatial index, QGIS will have to go through every geometry in your layer to check if the given geometry is beneath the cursor position. This would be <strong>very ineffective</strong>.</p>
<p>In order to prevent this, QGIS keeps an index where vector data are stored in a way that it can quickly find out what geometry is beneath the mouse cursor. The building of this data structure takes time and that is what the progress dialog is about.</p>
<h2>Firstly: Parallelize snap index build</h2>
<p>If you want to be able to snap on all layers in your project, then QGIS will have to build one snap index for each layer. This operation was made sequentially meaning that if you have for instance 20 layers and the index building last approximatively 3 seconds for each, then the whole index building will last 1 minute. We made modifications to QGIS so that index building could be done in parallel. As a result, the total index building time could theoretically be 3 seconds!</p>
<p style="text-align: center;"><img alt="" class="alignnone wp-image-5326 aligncenter" height="261" src="https://oslandia.com/wp-content/uploads/2020/01/parallelizeindex.png" width="598" />4 layers snap index being built in parallel</p>
<p>However, parallel operations are limited by the number of CPU cores of your machine, meaning that if you have 4 cores (core i7 for instance) then the total time will be up to 4 times faster than when the building is sequential (and last 15 seconds in our example).</p>
<h2>Secondly: relax the snap build</h2>
<p>For big projects, parallelizing index building is not enough and still takes too much time. Futhermore, to reduce snap index building, an existing optimisation was to build the spatial index for a specific area of interest (determined according to the displayed area and layer size). As a consequence, when you&#8217;ve done waiting for an index currently building and you move the map or zoom in/out, you could possibly trigger another snap index building and wait again.</p>
<p>So, the idea was to avoid waiting at all. Snap index is now built whenever it needs to (when you first enable snapping, when you move or zoom) but the <strong>user doesn&#8217;t have to wait for the build to be over</strong> and can continue what it was doing (creating feature, moving&#8230;). Snapping highlights will be missing when the index is currently being built and will appear gradually as soon as they finished. That&#8217;s what we call the <strong>relaxing mode</strong>.</p>
<p><img alt="" class="alignnone wp-image-5330 aligncenter" height="87" src="https://oslandia.com/wp-content/uploads/2020/01/63597696-590d1b00-c5be-11e9-8d60-5731fb5a9305.gif" width="173" /></p>
<p style="text-align: center;">No waiting dialog, snapping highlights appears as soon as snap index is ready</p>
<p>This feature has been merged into current QGIS master and will be present in future<strong> QGIS 3.12 release</strong>. We keep working on this feature in order to make it more stable and efficient.</p>
<h2>What&#8217;s next</h2>
<p>We&#8217;ll continue to improve this feature in the coming days, if you have the chance to test it and encounter issues please let us know on the <a href="https://github.com/qgis/QGIS/issues">QGIS tracker</a>. If you think about a missing feature or just want to know more about QGIS, feel free to contact us at <a href="mailto:infos+data@oslandia.com">infos+data@oslandia.com</a>. And please have a look at our <a href="https://qgis.oslandia.com">support offering for QGIS</a>.</p>
<p>Many thanks to QGIS grant program for funding these new features. Thanks also to all the people involved in reviewing the code and helping to better understand the existing mechanism.</p>
<p>&nbsp;</p>
