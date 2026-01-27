---
source: "blog"
title: "New map coloring algorithms in QGIS 3.0"
date: "2017-02-22T06:17:02+0000"
link: "https://nyalldawson.net/2017/02/new-map-coloring-algorithms-in-qgis-3-0/"
draft: "false"
showcase: "planet"
subscribers: ["nyalldawson_net"]
author: "nyalldawson.net"
tags: ["qgis", "3.0", "cartography", "colour", "osgeo", "processing", "qgis"]
languages: ["en_gb"]
available_languages: ["en_gb"]
---

<p>It’s been a long time since I last blogged here. Let’s just blame that on the amount of changes going into QGIS 3.0 and move on…</p>
<p>One new feature which landed in QGIS 3.0 today is a processing algorithm for automatic coloring of a map in such a way that adjoining polygons are all assigned different color indexes. Astute readers may be aware that this was possible in earlier versions of QGIS through the use of either the (QGIS 1.x only!) <em>Topocolor</em> plugin, or the <em>Coloring a map</em> plugin (2.x).</p>
<p>What’s interesting about this new processing algorithm is that it introduces several refinements for cartographically optimising the coloring. The earlier plugins both operated by pure “graph” coloring techniques. What this means is that first a graph consisting of each set of adjoining features is generated. Then, based purely on this abstract graph, the coloring algorithms are applied to optimise the solution so that connected graph nodes are assigned different colors, whilst keeping the total number of colors required minimised.</p>
<p>The new QGIS algorithm works in a different way. Whilst the first step is still calculating the graph of adjoining features (now super-fast due to use of spatial indexes and prepared geometry intersection tests!), the colors for the graph are assigned while considering the <strong>spatial</strong> arrangement of all features. It’s gone from a purely abstract mathematical solution to a context-sensitive cartographic solution.</p>
<div class="wp-caption aligncenter" id="attachment_710" style="width: 763px;"><img class="wp-image-710 size-full" height="546" src="/img/subscribers/nyalldawson_net/new-map-coloring-algorithms-in-qgis-3-0/Screenshot-from-2017-02-22-15-45-07.webp" width="753"/><p class="wp-caption-text" id="caption-attachment-710">The “Topological coloring” processing algorithm</p></div>
<p>Let’s explore the differences. First up, the algorithm has an option for the “minimum distance between features”. It’s often the case that features aren’t really touching, but are instead just very close to each other. Even though they aren’t touching, we still don’t want these features to be assigned the same color. This option allows you to control the minimum distance which two features can be to each other before they can be assigned the same color.</p>
<p>The biggest change comes in the “balancing” techniques available in the new algorithm. By default, the algorithm now tries to assign colors in such a way that the total number of features assigned each color is equalised. This avoids having a color which is only assigned to a couple of features in a large dataset, resulting in an odd looking map coloration.</p>
<div class="wp-caption aligncenter" id="attachment_712" style="width: 786px;"><img class="wp-image-712 size-full" height="288" src="/img/subscribers/nyalldawson_net/new-map-coloring-algorithms-in-qgis-3-0/balance_classes-1.webp" width="776"/><p class="wp-caption-text" id="caption-attachment-712">Balancing color assignment by count – notice how each class has a (almost!) equal count</p></div>
<p>Another available balancing technique is to balance the color assignment by total area. This technique assigns colors so that the total <strong>area</strong> of the features assigned to each color is balanced. This mode can be useful to help avoid large features resulting in one of the colors appearing more dominant on a colored map.</p>
<div class="wp-caption aligncenter" id="attachment_713" style="width: 786px;"><img alt="" class="size-full wp-image-713" height="288" src="/img/subscribers/nyalldawson_net/new-map-coloring-algorithms-in-qgis-3-0/balance_by_area.webp" width="776"/><p class="wp-caption-text" id="caption-attachment-713">Balancing assignment by area – note how only one large feature is assigned the red color</p></div>
<p>The final technique, and my personal preference, is to balance colors by distance between colors. This mode will assign colors in order to <strong>maximize</strong> the <strong>distance</strong> between features of the same color. Maximising the distance helps to create a more uniform distribution of colors across a map, and avoids certain colors clustering in a particular area of the map. It’s my preference as it creates a really nice balanced map – at a glance the colors look “randomly” assigned with no discernible pattern to the arrangement.</p>
<div class="wp-caption aligncenter" id="attachment_714" style="width: 786px;"><img alt="" class="size-full wp-image-714" height="288" src="/img/subscribers/nyalldawson_net/new-map-coloring-algorithms-in-qgis-3-0/balance_by_distance.webp" width="776"/><p class="wp-caption-text" id="caption-attachment-714">Balancing colors by distance</p></div>
<p>As these examples show, considering the geographic arrangement of features while coloring allows us to optimise the assigned colors for cartographic output.</p>
<p>The other nice thing about having this feature implemented as a processing algorithm is that unlike standalone plugins, processing algorithms can be incorporated as just one step of a larger model (and also reused by other plugins!).</p>
<p>QGIS 3.0 has tons of great new features, speed boosts and stability bumps. This is just a tiny taste of the handy new features which will be available when 3.0 is released!</p>
