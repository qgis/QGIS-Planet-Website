---
source: "blog"
title: "Labels leading lines with QGIS and Postgis"
date: "2015-01-12T08:00:41+0000"
link: "https://gisunchained.wordpress.com/2015/01/12/etiquetas-com-guias-em-qgis-e-postgis-labels-leading-lines-with-qgis-and-postgis/"
draft: "false"
showcase: "planet"
subscribers: ["alexandre_netos_blog"]
author: "Alexandre Neto's blog"
tags: ["uncategorized", "cartography", "hint", "postgis", "qgis"]
---

<p style="text-align: left;">EN | <span style="color: #808080;"><a href="https://sigsemgrilhetas.wordpress.com/2015/01/12/etiquetas-com-guias-em-qgis-e-postgis-labels-leading-lines-with-qgis-and-postgis/">PT</a></span></p>
<p>Recently I had the need to add labels to features with very close geometries, resulting in their collision.</p>
<p><img alt="Capturar_3" class="size-large wp-image-550 aligncenter" height="436" src="https://gisunchained.files.wordpress.com/2015/01/capturar_3-e1420735767497.png?w=584" width="584" /></p>
<p>Using data-defined override for label&#8217;s position (I have used<a href="https://plugins.qgis.org/plugins/toLabeledLayer/"> layer to labeled layer</a> plugin to set this really fast) and the QGIS tool to move labels, it was quite easy to relocate them to better places. However, in same cases, it was difficult to understand to which geometry they belonged.</p>
<p><img alt="Capturar_2" class="size-large wp-image-549 aligncenter" height="436" src="https://gisunchained.files.wordpress.com/2015/01/capturar_2-e1420735797114.png?w=584" width="584" /></p>
<p>I needed some kind of leading lines to connect, whenever necessary, label and feature. I knew another great plugin called &#8220;<a href="https://plugins.qgis.org/plugins/EasyCustomLabeling/">Easy Custom Labeling</a>&#8220;, by <a href="https://plugins.qgis.org/plugins/author/Regis%2520Haubourg%2520%2528Agence%2520de%2520l%2527eau%2520Adour%2520Garonne%2529/" title="Plugins by Regis Haubourg (Agence de l'eau Adour Garonne)">Regis Haubourg</a>, that did what I needed, but it would create a memory duplicate of the original layer, wish meant that any edition on the original layer wouldn&#8217;t be updated in the labels.</p>
<p>Since the data were stored in a PostgreSQL/Postgis database, I have decided to create a query that would return a layer with leading lines. I used the following query in DB manager:</p>
<pre class="brush: sql; title: ; notranslate">
SELECT
  gid,
  label,
  ST_Makeline(St_setSRID(ST_PointOnSurface(geom),27493), St_setSRID(St_Point(x_label::numeric, y_label::numeric),27493))
FROM
  epvu.sgev
WHERE
  x_label IS NOT NULL AND
  y_label IS NOT NULL AND
  NOT ST_Within(ST_Makeline(St_setSRID(ST_PointOnSurface(geom),27493), St_setSRID(St_Point(x_label::numeric, y_label::numeric),27493)),geom))</pre>
<p>This query creates a line by using the feature centroid as starting point and the label coordinate as end point. The last condition on the WHERE statement assures that the lines are only created for labels outside the feature.</p>
<p><a href="https://gisunchained.files.wordpress.com/2015/01/capturar_1-e1420735837615.png"><img alt="Capturar_1" class="size-large wp-image-548 aligncenter" height="436" src="https://gisunchained.files.wordpress.com/2015/01/capturar_1-e1420735837615.png?w=584" width="584" /></a></p>
<p>With the resulting layer loaded in my project, all I need is to move my labels and save the edition (and press refresh) to show a nice leading line.</p>
<p><a href="https://gisunchained.files.wordpress.com/2015/01/guidelines1.gif"><img alt="guidelines" class="wp-image-554 size-full aligncenter" height="436" src="https://gisunchained.files.wordpress.com/2015/01/guidelines1.gif" width="584" /></a></p>
