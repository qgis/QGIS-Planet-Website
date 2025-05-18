---
source: "blog"
title: "Speed up your analytics with the new MovingPandas 0.22 and Trajectools 2.6"
date: "2025-05-17T17:35:41+0000"
link: "https://anitagraser.com/2025/05/17/speed-up-your-analytics-with-the-new-movingpandas-0-22-and-trajectools-2-6/"
draft: "false"
showcase: "planet"
subscribers: ["anita_graser"]
author: "Anita Graser"
tags: ["gis", "mobility data science", "movement data in gis", "movingpandas", "qgis", "trajectools", "movement data", "python", "spatio-temporal data", "trajectories"]
languages: ["en_gb"]
available_languages: ["en_gb"]
---

<p>The latest releases of <a href="https://movingpandas.org/">MovingPandas</a> and <a href="https://plugins.qgis.org/plugins/processing_trajectory/#plugin-versions">Trajectools</a> come with many “under the hood” changes that aim to make your movement analytics faster:</p>
<ol class="wp-block-list">
<li>Instead of immediately creating a GeoPandas GeoDataFrame and populating the geometry column with Point objects, MovingPandas now has <strong>“lazy geometry column creation”</strong> that holds off on this operation until / if the geometries are actually needed. This way, for many operations, no geometry objects have to be generated at all.</li>
<li>MovingPandas TrajectorySplitters now support <strong>parallel processing</strong> and Trajectools uses parallel processing whenever available (e.g. for adding speed &amp; direction metrics, detecting stops, splitting trajectories).</li>
<li>When a minimum length is specified for trajectories, MovingPandas now avoids computing the total trajectory length and, instead, immediately stops once the threshold value has been reached (<strong>“early skip”</strong>). </li>
<li>Trajectools now offers the option to <strong>skip computation of movement metrics</strong> (speed &amp; direction). This way, we can skip unnecessary computations and leverage the lazy geometry column creation, wherever applicable. </li>
</ol>
<p>Let’s have a look at some example performance measurements!</p>
<h2 class="wp-block-heading">Example 1: MovingPandas ValueChangeSplitter</h2>
<p><em>The ValueChangeSplitter splits trajectories when it detects a value change in the specified column. This is useful, for example, to split up public trajectories that contain a “next_stop” column. </em></p>
<p>The following graph shows ValueChangeSplitter runtimes for different minimum trajectory length settings (from 0 to 1km, 100km, and 10,000km): </p>
<figure class="wp-block-image size-large"><a href="https://anitagraser.com/wp-content/uploads/2025/05/mpd0.22_performance1.png"><img alt="" class="wp-image-9516" height="490" src="/img/subscribers/anita_graser/speed-up-your-analytics-with-the-new-movingpandas-0-22-and-trajectools-2-6/mpd0.22_performance1.webp" width="989"/></a></figure>
<p>We see that the new, lazy geometry column initialization outperforms the old original code in all cases (e.g.<strong> 57%</strong> runtime reduction for 1km), except for the  worst-case scenario, when the original implementation discards all trajectories as too short right from the start. <em>(For most use cases, min_length will be set to rather small values to avoid creation of undesired short trajectory fragments, similar to sliver polygons in classic geometry operations.)</em></p>
<p>Additionally, we can engage multiprocessing by setting the <code>n_processes</code> parameter, e.g. to the number of CPUs to achieve further speedup: </p>
<figure class="wp-block-image size-large"><a href="https://anitagraser.com/wp-content/uploads/2025/05/mpd0.22_performance2.png"><img alt="" class="wp-image-9517" height="324" src="/img/subscribers/anita_graser/speed-up-your-analytics-with-the-new-movingpandas-0-22-and-trajectools-2-6/mpd0.22_performance2.webp" width="545"/></a></figure>
<h2 class="wp-block-heading">Example 2: Trajectools</h2>
<p>By applying all above-mentioned speedup techniques, Trajectools is now considerably faster. For example, the following runtime reductions can be achieved by deactivating the “Add movement metrics (speed, direction)” option in the algorithm dialog: </p>
<ul class="wp-block-list">
<li>Create trajectories: <strong>62%</strong> </li>
<li>Spatiotemporal generalization (TDTR): <strong>78%</strong></li>
<li>Temporal generalization: <strong>81%</strong> </li>
<li>Split trajectories at stops: <strong>53%</strong></li>
</ul>
<figure class="wp-block-image size-large"><a href="https://anitagraser.com/wp-content/uploads/2025/05/image-2.png"><img alt="" class="wp-image-9525" height="734" src="/img/subscribers/anita_graser/speed-up-your-analytics-with-the-new-movingpandas-0-22-and-trajectools-2-6/image-2.webp" width="700"/></a></figure>
<p>I have also updated the default trajectory points output style. It now uses a graduated renderer to visualize the speed values (if they have been calculated) instead of the previously used data-defined override. This makes the style faster to customize and provides a user-friendly legend: </p>
<figure class="wp-block-image size-large"><a href="https://anitagraser.com/wp-content/uploads/2025/05/image-3.png"><img alt="" class="wp-image-9527" height="385" src="/img/subscribers/anita_graser/speed-up-your-analytics-with-the-new-movingpandas-0-22-and-trajectools-2-6/image-3.webp" width="1024"/></a></figure>
<p>For more infos, have a look at: </p>
<ul class="wp-block-list">
<li><a href="https://github.com/movingpandas/movingpandas/releases/tag/v0.22" rel="noreferrer noopener" target="_blank">MovingPandas 0.22 release notes</a></li>
<li><a href="https://codeberg.org/movingpandas/trajectools/releases/tag/v2.6" rel="noreferrer noopener" target="_blank">Trajectools 2.6 release notes</a></li>
</ul>
<p>Enjoy the latest performance increases!</p>
