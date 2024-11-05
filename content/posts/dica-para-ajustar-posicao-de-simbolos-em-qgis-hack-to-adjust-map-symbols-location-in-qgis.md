---
source: "blog"
title: "Hack to adjust map symbols location in QGIS"
date: "2015-02-23T23:44:33+0000"
link: "https://gisunchained.wordpress.com/2015/02/23/dica-para-ajustar-posicao-de-simbolos-em-qgis-hack-to-adjust-map-symbols-location-in-qgis/"
draft: "false"
showcase: "planet"
subscribers: ["alexandre_netos_blog"]
author: "Alexandre Neto's blog"
tags: ["uncategorized", "cartography", "hint", "qgis"]
---

<p style="text-align: left;">EN | <span style="color: #808080;"><a href="https://sigsemgrilhetas.wordpress.com/2015/02/23/dica-para-ajustar-posicao-de-simbolos-em-qgis-hack-to-adjust-map-symbols-location-in-qgis/" target="_blank">PT</a></span></p>
<p>Now and then I get too many map symbols (points) in the same place, and I thought how nice it would be if we could drag n&#8217; drop them around without messing with their geometries position, just like we do with labels. That thought gave me an idea for a cool hack.</p>
<p>Choose your point layer and start by creating two new fields called symbX and symbY (Type: Decimal number; Size: 20; Precision: 5). Now go the layer properties and in the Style tab edit your symbol. <strong>For each level of your symbol</strong> select &#8220;map units&#8221; as the offset units, and set the following expression in the offset data define properties option:</p>
<pre class="brush: plain; title: ; notranslate">

CASE WHEN symbX IS NOT NULL AND symbY IS NOT NULL THEN
    tostring($x - symbX) + ',' + tostring($y - symbY)
ELSE
    '0,0'
END

</pre>
<p><a href="https://gisunchained.files.wordpress.com/2015/02/screenshot-from-2015-02-22-181843.png"><img alt="Screenshot from 2015-02-22 18:18:43" class="wp-image-572 size-full aligncenter" height="247" src="https://gisunchained.files.wordpress.com/2015/02/screenshot-from-2015-02-22-181843.png" width="439" /></a></p>
<p>Be aware that, if your coordinates have negative values, you need to adapt the code. E.g., If you have negative values in X you should use &#8220;tostring(symbX -$x)&#8221; instead.</p>
<p>Now, temporarly  label your layer with a small convenient text (I used a centered &#8216;+&#8217; (plus sign) with a white buffer) and set its coordinates to data defined using the symbX and symbY Fields.</p>
<p><a href="https://gisunchained.files.wordpress.com/2015/02/screenshot-from-2015-02-22-224207.png"><img alt="Screenshot from 2015-02-22 22:42:07" class="size-large wp-image-575 aligncenter" height="595" src="https://gisunchained.files.wordpress.com/2015/02/screenshot-from-2015-02-22-224207.png?w=660" width="660" /></a></p>
<p>From this point on, when you use the move label tool, not only the label position change but also the actual symbol! Pretty cool, isn&#8217;t it?</p>
<p><a href="https://gisunchained.files.wordpress.com/2015/02/anim.gif"><img alt="anim" class="size-full wp-image-576 aligncenter" height="347" src="https://gisunchained.files.wordpress.com/2015/02/anim.gif" width="500" /></a></p>
<p>Notice that the features geometries are not changed during the process. Also, remember that in this case you can also <a href="https://sigsemgrilhetas.wordpress.com/2015/01/12/etiquetas-com-guias-em-qgis-e-postgis-labels-leading-lines-with-qgis-and-postgis/">add leading lines</a> to connect the symbols to the original position of the points.</p>
