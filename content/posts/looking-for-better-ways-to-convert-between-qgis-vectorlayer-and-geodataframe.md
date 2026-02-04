---
source: "blog"
title: "Looking for better ways to convert between QGIS VectorLayer and (Geo)DataFrame"
date: "2025-10-26T21:34:54+0000"
link: "https://anitagraser.com/2025/10/26/looking-for-better-ways-to-convert-between-qgis-vectorlayer-and-geodataframe/"
draft: "false"
showcase: "planet"
subscribers: ["anita_graser"]
author: "Anita Graser"
tags: ["qgis", "arrow", "geopandas", "processing", "pyogrio", "pyqgis", "python"]
languages: ["en_gb"]
available_languages: ["en_gb"]
---

<p class="wp-block-paragraph">Plugin developers who want to use (Geo)Pandas-based functionality in their plugins regularly face the challenge of converting QGIS vector layers to (Geo)DataFrames. There is currently no built-in convenience function. </p>
<p class="wp-block-paragraph">In Trajectools, so far, I have been performing the conversion manually, looping through all features and taking care of tricky column types, such as datetimes and geometries: </p>
<div class="wp-block-syntaxhighlighter-code"><pre class="brush: python; title: ; notranslate">
def df_from_layer_trajectools(layer,time_field_name="t"):
    # Original Trajectools 2.7 version
    names = [field.name() for field in layer.fields()]
    data = []
    for feature in layer.getFeatures():
        my_dict = {}
        for i, a in enumerate(feature.attributes()):
            if names[i] == time_field_name and isinstance(a, QDateTime):
                a = a.toPyDateTime()
            my_dict[names[i]] = a
        pt = feature.geometry().asPoint()
        my_dict["geom_x"] = pt.x()
        my_dict["geom_y"] = pt.y()
        data.append(my_dict)
    df = pd.DataFrame(data)
    return df
</pre></div>
<p class="wp-block-paragraph">It works (<a href="https://codeberg.org/movingpandas/trajectools/issues/93">mostly</a>), but it’s far from fast. For the <a href="https://anitagraser.com/2025/10/12/geolife-gps-track-collection-processing-with-duckdb-qgis-trajectools/">25 million Geolife</a> points, it takes 4 minutes: </p>
<figure class="wp-block-image size-large"><img alt="" class="wp-image-9635" height="425" src="/img/subscribers/anita_graser/looking-for-better-ways-to-convert-between-qgis-vectorlayer-and-geodataframe/image-18.webp" width="563"/></figure>
<p class="wp-block-paragraph">In an <a href="https://codeberg.org/movingpandas/trajectools/issues/101">attempt to speed-up</a> (and make the conversion more robust, e.g. regarding datetime/timezone conversion and <a href="https://codeberg.org/movingpandas/trajectools/issues/93">null values</a>), I’ve spent some time at SDSL2025 with <a href="https://github.com/jorisvandenbossche">Joris Van den Bossche</a> trying a workaround that writes the QGIS layer to an Arrow file and then reads that file with pyogrio:</p>
<div class="wp-block-syntaxhighlighter-code"><pre class="brush: python; title: ; notranslate">
def gdf_from_layer_arrow(layer):
    # SDSL2025 version
    with tempfile.TemporaryDirectory() as tmpdirname:
        path = os.path.join(tmpdirname, "data.arrow")

        options = QgsVectorFileWriter.SaveVectorOptions()
        options.actionOnExistingFile = QgsVectorFileWriter.CreateOrOverwriteFile 
        options.layerName = 'data'
        options.driverName = "arrow"
        
        QgsVectorFileWriter.writeAsVectorFormatV3(
            layer, path, QgsProject.instance().transformContext(), options
        )
       
        meta, table = pyogrio.read_arrow(path)
        gdf = gpd.GeoDataFrame.from_arrow(table)

    return gdf
</pre></div>
<p class="wp-block-paragraph">Not only do we get a GeoDataFrame in return, this also runs in half the time, i.e. in 2 minutes instead of 4: </p>
<figure class="wp-block-image size-large"><img alt="" class="wp-image-9636" height="418" src="/img/subscribers/anita_graser/looking-for-better-ways-to-convert-between-qgis-vectorlayer-and-geodataframe/image-19.webp" width="568"/></figure>
<p class="wp-block-paragraph">Switching to this approach will require adding pyogrio to the plugin dependencies. Looks like it could be worth it.</p>
<p class="wp-block-paragraph">We also discussed another alternative: It would be faster to read the vector layer data source directly, in case it is a supported file format. However, this means we’d need separate handling for other input layers. </p>
<p class="wp-block-paragraph">There’s also the issue of supporting the Processing feature that allows users to run the algorithm only on the selected features because selected features are only exposed through QgsProcessingParameterFeatureSource (and not through QgsProcessingParameterVectorLayer). Maybe the Export Selected Features algorithm can cover this case but it will export an empty layer if there is no selection. </p>
<p class="wp-block-paragraph">Are you aware of any other / better ways to approach this issue? Any pointers are appreciated. </p>
<p class="wp-block-paragraph"></p>
