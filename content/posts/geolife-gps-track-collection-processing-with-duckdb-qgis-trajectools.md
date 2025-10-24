---
source: "blog"
title: "Wrangling hundreds of GPS files with DuckDB, QGIS & Trajectools"
date: "2025-10-12T19:21:53+0000"
link: "https://anitagraser.com/2025/10/12/geolife-gps-track-collection-processing-with-duckdb-qgis-trajectools/"
draft: "false"
showcase: "planet"
subscribers: ["anita_graser"]
author: "Anita Graser"
tags: ["big data", "data mining", "gis", "movement data in gis", "qgis", "spatio-temporal data", "trajectools", "duckdb", "etl", "movement data", "sql"]
languages: ["en_gb"]
available_languages: ["en_gb"]
---

<p>The last time I preprocessed the whole GeoLife dataset, I loaded it into PostGIS. Today, I want to share a new workflow that creates a (Geo)Parquet file and that is much faster. </p>
<h2 class="wp-block-heading">The dataset (GeoLife)</h2>
<blockquote class="wp-block-quote is-layout-flow wp-block-quote-is-layout-flow">
<p>“This GPS trajectory dataset was collected in (Microsoft Research Asia) Geolife project by 182 users in a period of over three years (from April 2007 to August 2012). A GPS trajectory of this dataset is represented by a sequence of time-stamped points, each of which contains the information of latitude, longitude and altitude. This dataset contains 17,621 trajectories with a total distance of about 1.2 million kilometers and a total duration of 48,000+ hours. These trajectories were recorded by different GPS loggers and GPS-phones, and have a variety of sampling rates. 91 percent of the trajectories are logged in a dense representation, e.g. every 1~5 seconds or every 5~10 meters per point.”</p>
</blockquote>
<p>The <a href="https://www.microsoft.com/en-us/download/details.aspx?id=52367">GeoLife GPS Trajectories</a> download contains 182 directories full of .plt files: </p>
<figure class="wp-block-image size-large"><img alt="" class="wp-image-9584" height="229" src="/img/subscribers/anita_graser/geolife-gps-track-collection-processing-with-duckdb-qgis-trajectools/image.webp" width="531"/></figure>
<p>Basically, CSV files  with a custom header: </p>
<figure class="wp-block-image size-large"><img alt="" class="wp-image-9585" height="251" src="/img/subscribers/anita_graser/geolife-gps-track-collection-processing-with-duckdb-qgis-trajectools/image-1.webp" width="541"/></figure>
<h2 class="wp-block-heading">Creating the (Geo)Parquet using DuckDB</h2>
<h3 class="wp-block-heading">DuckDB installation</h3>
<p>Following the <a href="https://duckdb.org/install/?platform=macos&amp;environment=cli">official instructions</a>, installation is straightforward:</p>
<div class="wp-block-syntaxhighlighter-code"><pre class="brush: bash; title: ; notranslate">
curl https://install.duckdb.org | sh
</pre></div>
<p>From there, I’ve been using the GUI which we can launch using:</p>
<div class="wp-block-syntaxhighlighter-code"><pre class="brush: bash; title: ; notranslate">
duckdb -ui
</pre></div>
<p>The <a href="https://duckdb.org/docs/stable/core_extensions/spatial/overview">spatial extension</a> is a DuckDB core extension, so it’s readily available. We can create a spatial db with:  </p>
<div class="wp-block-syntaxhighlighter-code"><pre class="brush: sql; title: ; notranslate">
ATTACH IF NOT EXISTS ':memory:' AS memory;
INSTALL spatial;
LOAD spatial;
</pre></div>
<figure class="wp-block-image size-large"><a href="https://anitagraser.com/wp-content/uploads/2025/10/image-2.png"><img alt="" class="wp-image-9592" height="278" src="/img/subscribers/anita_graser/geolife-gps-track-collection-processing-with-duckdb-qgis-trajectools/image-2.webp" width="733"/></a></figure>
<p>Reading a spatial file is as simple as:</p>
<div class="wp-block-syntaxhighlighter-code"><pre class="brush: sql; title: ; notranslate">
SELECT * 
FROM '/home/anita/Documents/Codeberg/trajectools/sample_data/geolife.gpkg'
</pre></div>
<p>thanks to the <a href="https://duckdb.org/docs/stable/core_extensions/spatial/gdal">GDAL integration</a>.</p>
<p>But today, we want to do to get a bit more involved …</p>
<h3 class="wp-block-heading">DuckDB SQL magic</h3>
<p>The issues we need to solve are:</p>
<ol class="wp-block-list">
<li>Read all CSV files from all subdirectories</li>
<li>Parse the CSV, ignoring the first couple of lines, while assigning proper column names</li>
<li>Assign the CSV file name as the trajectory ID (because there is no ID in the original files)</li>
<li>Create point geometries that will work with our GeoParquet file </li>
<li>Create proper datetimes from the separate date and time fields</li>
</ol>
<p>Luckily, DuckDB’s read_csv function comes with the necessary features built-in. Putting it all together: </p>
<div class="wp-block-syntaxhighlighter-code"><pre class="brush: sql; title: ; notranslate">
CREATE OR REPLACE TABLE geolife AS 
SELECT 
  parse_filename(filename, true) as vehicle_id, 
  strptime(date||' '||time, '%c') as t, 
  ST_Point(lon, lat) as geometry -- do NOT use ST_MakePoint
FROM read_csv('/home/anita/Documents/Geodata/Geolife/Geolife Trajectories 1.3/Data/*/*/*.plt',
    skip=6,
    filename = true, 
    columns = {
        'lat': 'DOUBLE', 
        'lon': 'DOUBLE', 
        'ignore': 'INT', 
        'alt': 'DOUBLE', 
        'epoch': 'DOUBLE', 
        'date': 'VARCHAR',
        'time': 'VARCHAR'
    });
</pre></div>
<p>It’s blazingly fast: </p>
<figure class="wp-block-image size-large is-resized"><a href="https://anitagraser.com/wp-content/uploads/2025/10/image-3.png"><img alt="" class="wp-image-9598" height="794" src="/img/subscribers/anita_graser/geolife-gps-track-collection-processing-with-duckdb-qgis-trajectools/image-3.webp" style="width: 824px; height: auto;" width="824"/></a></figure>
<p><em>I haven’t tested reading directly from ZIP archives yet, but there seems to be a <a href="https://duckdb.org/community_extensions/extensions/zipfs.html">community extension (zipfs)</a> for this exact purpose. </em></p>
<h2 class="wp-block-heading">Ready to QGIS</h2>
<p>GeoParquet files can be drag-n-dropped into QGIS:</p>
<figure class="wp-block-image size-large"><a href="https://anitagraser.com/wp-content/uploads/2025/10/image-4.png"><img alt="" class="wp-image-9601" height="348" src="/img/subscribers/anita_graser/geolife-gps-track-collection-processing-with-duckdb-qgis-trajectools/image-4.webp" width="1024"/></a></figure>
<p><em>I’m running QGIS 3.42.1-Münster from conda-forge on Linux Mint.</em></p>
<p>Yes, it takes a while to render all 25 million points … But you know what? It get’s really snappy once we zoom in closer, e.g. to the situation in Germany: </p>
<figure class="wp-block-image size-large"><a href="https://anitagraser.com/wp-content/uploads/2025/10/image-5.png"><img alt="" class="wp-image-9603" height="504" src="/img/subscribers/anita_graser/geolife-gps-track-collection-processing-with-duckdb-qgis-trajectools/image-5.webp" width="889"/></a></figure>
<p>Let’s have a closer look at what’s going on here. </p>
<h3 class="wp-block-heading">Trajectools time</h3>
<p>Selecting the 9,438 points in this extent, let’s compute movement metrics (speed &amp; direction) and create trajectory lines: </p>
<figure class="wp-block-image size-large"><a href="https://anitagraser.com/wp-content/uploads/2025/10/image-8.png"><img alt="" class="wp-image-9608" height="1004" src="/img/subscribers/anita_graser/geolife-gps-track-collection-processing-with-duckdb-qgis-trajectools/image-8.webp" width="928"/></a></figure>
<p>Looks like we have some high-speed sections in there (with those red &gt; 100 km/h streaks): </p>
<figure class="wp-block-image size-large"><a href="https://anitagraser.com/wp-content/uploads/2025/10/image-9.png"><img alt="" class="wp-image-9610" height="422" src="/img/subscribers/anita_graser/geolife-gps-track-collection-processing-with-duckdb-qgis-trajectools/image-9.webp" width="808"/></a></figure>
<p>When we zoom in to Darmstadt and enable the trajectories layer, we can see each individual trip. Looks like car trips on the highway and walks through the city: </p>
<figure class="wp-block-image size-large"><a href="https://anitagraser.com/wp-content/uploads/2025/10/image-10.png"><img alt="" class="wp-image-9612" height="607" src="/img/subscribers/anita_graser/geolife-gps-track-collection-processing-with-duckdb-qgis-trajectools/image-10.webp" width="833"/></a></figure>
<p>That looks like quite the long round trip: </p>
<figure class="wp-block-image size-large"><a href="https://anitagraser.com/wp-content/uploads/2025/10/image-11.png"><img alt="" class="wp-image-9614" height="456" src="/img/subscribers/anita_graser/geolife-gps-track-collection-processing-with-duckdb-qgis-trajectools/image-11.webp" width="1024"/></a></figure>
<p>Let’s see where they might have stopped to have a break: </p>
<figure class="wp-block-image size-large"><a href="https://anitagraser.com/wp-content/uploads/2025/10/image-13.png"><img alt="" class="wp-image-9617" height="1003" src="/img/subscribers/anita_graser/geolife-gps-track-collection-processing-with-duckdb-qgis-trajectools/image-13.webp" width="997"/></a></figure>
<p>If I had to guess, I’d say they stayed at the Best Western: </p>
<figure class="wp-block-image size-large"><a href="https://anitagraser.com/wp-content/uploads/2025/10/image-15.png"><img alt="" class="wp-image-9621" height="333" src="/img/subscribers/anita_graser/geolife-gps-track-collection-processing-with-duckdb-qgis-trajectools/image-15.webp" width="1024"/></a></figure>
<h2 class="wp-block-heading">Conclusion</h2>
<p>DuckDB has been great for this ETL workflow. I didn’t use much of its geospatial capabilities here but I was pleasantly surprised how smooth the GeoParquet creation process has been. Geometries are handled without any special magic and are recognized by QGIS. Same with the timestamps. All ready for more heavy spatiotemporal analysis with <a href="https://plugins.qgis.org/plugins/processing_trajectory/#plugin-versions">Trajectools</a>. </p>
<p>If you haven’t tried DuckDB or GeoParquet yet, give it a try, particularly if you’re collaborating with data scientists from other domains and want to exchange data. </p>
<p></p>
