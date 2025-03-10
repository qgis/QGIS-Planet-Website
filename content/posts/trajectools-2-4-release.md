---
source: "blog"
title: "Trajectools 2.4 release"
date: "2025-01-11T20:04:27+0000"
link: "https://anitagraser.com/2025/01/11/trajectools-2-4-release/"
draft: "false"
showcase: "planet"
subscribers: ["anita_graser"]
author: "Anita Graser"
tags: ["gis", "movement data in gis", "movingpandas", "trajectools", "gtfs", "movement data", "public transport", "qgis"]
languages: ["en_gb"]
available_languages: ["en_gb"]
---

<figure class="wp-block-image size-large"><img alt="" class="wp-image-9007" height="131" src="/img/subscribers/anita_graser/trajectools-2-4-release/trajectools2.webp" width="545"/></figure>
<p>In this <a href="https://github.com/movingpandas/qgis-trajectools/releases/tag/v2.4">new release</a>, you will find new algorithms, default output styles, and other usability improvements, in particular for working with public transport schedules in GTFS format, including:</p>
<ul class="wp-block-list">
<li>Added GTFS algorithms for extracting stops, fixes <a href="https://github.com/movingpandas/qgis-trajectools/issues/43">#43</a></li>
<li>Added default output styles for GTFS stops and segments <a href="https://github.com/movingpandas/qgis-trajectools/commit/c6000600da91b616b474e0dd627bae26d93e874c">c600060</a></li>
<li>Added Trajectory splitting at field value changes <a href="https://github.com/movingpandas/qgis-trajectools/commit/286fdbdda5e39d00e257dfef53b32b4eddc408f7">286fdbd</a></li>
<li>Added option to add selected fields to output trajectories layer, fixes <a href="https://github.com/movingpandas/qgis-trajectools/issues/53">#53</a></li>
<li>Improved UI of the split by observation gap algorithm, fixes <a href="https://github.com/movingpandas/qgis-trajectools/issues/36">#36</a></li>
</ul>
<figure class="wp-block-image size-large"><a href="https://anitagraser.com/wp-content/uploads/2025/01/image-1.png"><img alt="" class="wp-image-9364" height="691" src="/img/subscribers/anita_graser/trajectools-2-4-release/image-1.webp" width="1024"/></a></figure>
<p><strong>Note:</strong> To use this new version of Trajectools, please upgrade your installation of <a href="https://github.com/movingpandas/movingpandas/releases">MovingPandas to &gt;= 0.21.2</a>, e.g. using</p>
<p>i<code>mport pip; pip.main(['install', '--upgrade', 'movingpandas'])</code></p>
<p>or</p>
<p><code>conda install movingpandas==0.21.2</code></p>
<p></p>
<figure class="wp-block-image size-large"><img alt="" class="wp-image-9358" height="614" src="/img/subscribers/anita_graser/trajectools-2-4-release/image.webp" width="399"/></figure>
