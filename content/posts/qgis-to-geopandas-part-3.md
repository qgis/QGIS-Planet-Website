---
source: "blog"
title: "QGIS to (Geo)Pandas – part 3"
date: "2025-12-03T20:33:38+0000"
link: "https://anitagraser.com/2025/12/03/qgis-to-geopandas-part-3/"
draft: "false"
showcase: "planet"
subscribers: ["anita_graser"]
author: "Anita Graser"
tags: ["gis", "qgis", "geopandas", "pyqgis", "python"]
languages: ["en_gb"]
available_languages: ["en_gb"]
---

<p class="wp-block-paragraph">The journey continues: <a href="https://github.com/qgis/QGIS/pull/63749">QgsArrowIterator is now merged</a>! This makes it possible to iterate over <code>QgsFeature</code>s as Arrow batches. </p>
<p class="wp-block-paragraph">This is where we are now, quoting <a href="https://github.com/qgis/QGIS/pull/63749#issuecomment-3475806601">Dewey Dunnington</a>: </p>
<div class="wp-block-syntaxhighlighter-code"><pre class="brush: python; title: ; notranslate">
import geopandas
from nanoarrow.c_array import allocate_c_array
import qgis
from qgis.core import QgsVectorLayer

# Create a vector layer
layer = QgsVectorLayer("tests/testdata/zonalstatistics/polys.shp", "layer_name", "ogr")
schema = qgis.core.QgsArrowIterator.inferSchema(layer)

it = qgis.core.QgsArrowIterator(layer.getFeatures())
it.setSchema(schema, 1)

c_array = allocate_c_array()
schema.exportToAddress(c_array.schema._addr())
it.nextFeatures(5, c_array._addr())

print(geopandas.GeoDataFrame.from_arrow(c_array))
#&gt; lev3_name                                           geometry
#&gt; 0    poly_1  MULTIPOLYGON (((100.37934 -0.96049, 100.37934 ...
#&gt; 1    poly_2  MULTIPOLYGON (((100.37944 -0.96044, 100.37955 ...
#&gt; 2    poly_3  MULTIPOLYGON (((100.37938 -0.96049, 100.37949 ...

print(geopandas.read_file("tests/testdata/zonalstatistics/polys.shp"))
#&gt; lev3_name                                           geometry
#&gt; 0    poly_1  POLYGON ((100.37934 -0.96049, 100.37934 -0.960...
#&gt; 1    poly_2  POLYGON ((100.37944 -0.96044, 100.37955 -0.960...
#&gt; 2    poly_3  POLYGON ((100.37938 -0.96049, 100.37949 -0.960...
</pre></div>
<p class="wp-block-paragraph"><a href="https://github.com/qgis/QGIS/issues/64110">Further improvements are already being planned</a>. To quote from the ticket:</p>
<p class="wp-block-paragraph">“The final state after this improvement would be a compact way for Arrow Python consumers like GeoPandas to ergonomically consume a layer. Maybe:</p>
<div class="wp-block-syntaxhighlighter-code"><pre class="brush: python; title: ; notranslate">
geopandas.GeoDataFrame.from_arrow(qgis_layer_object)
</pre></div>
<p class="wp-block-paragraph">Or maybe:</p>
<div class="wp-block-syntaxhighlighter-code"><pre class="brush: python; title: ; notranslate">
geopandas.GeoDataFrame.from_arrow(qgis_layer_object.getArrowStream())
</pre></div>
<p class="wp-block-paragraph">Looking forward to seeing this develop further. </p>
