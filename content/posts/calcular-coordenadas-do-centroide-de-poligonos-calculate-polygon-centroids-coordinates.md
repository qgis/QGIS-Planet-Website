---
source: "blog"
title: "Calculate polygon centroid’s coordinates"
date: "2015-02-10T23:34:49+0000"
link: "https://gisunchained.wordpress.com/2015/02/10/calcular-coordenadas-do-centroide-de-poligonos-calculate-polygon-centroids-coordinates/"
draft: "false"
showcase: "planet"
subscribers: ["alexandre_netos_blog"]
author: "Alexandre Neto's blog"
tags: ["uncategorized", "hint", "qgis"]
---

<p style="text-align: left;">EN | <span style="color: #808080;"><a href="https://sigsemgrilhetas.wordpress.com/2015/02/10/calcular-coordenadas-do-centroide-de-poligonos-calculate-polygon-centroids-coordinates/">PT</a></span></p>
<p>I had the need to add columns with the coordinates of polygons centroids. I came up with the following expressions to calculate X e Y, respectively:</p>
<pre class="brush: plain; title: ; notranslate">
xmin(centroid($geometry))
ymin(centroid($geometry))
</pre>
<p>The expression seems quite simple, but it toke me some time before I realize that, not having a x(geometry) and y(geometry) functions, I could use the xmin() and ymin() to get the coordinates of the polygons centroids. Since this wasn&#8217;t the first time I had to use this expressions, this post will work as a reminder for the future.</p>
