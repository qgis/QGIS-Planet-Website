---
source: "blog"
title: "Trajectools tutorial: trajectory preprocessing"
date: "2024-09-21T14:34:18+0000"
link: "https://anitagraser.com/2024/09/21/trajectools-tutorial-trajectory-preprocessing/"
draft: "false"
showcase: "planet"
subscribers: ["anita_graser"]
author: "Anita Graser"
tags: ["gis", "movement data in gis", "movingpandas", "qgis", "spatio-temporal data", "movement data"]
languages: ["en_gb"]
available_languages: ["en_gb"]
---

<figure class="wp-block-image size-large"><img alt="" class="wp-image-9007" height="131" src="/img/subscribers/anita_graser/trajectools-tutorial-trajectory-preprocessing/trajectools2.webp" width="545"/></figure>
<p>Today marks the release of <a href="https://plugins.qgis.org/plugins/processing_trajectory/#plugin-versions">Trajectools 2.3</a> which brings a new set of algorithms, including trajectory generalizing, cleaning, and smoothing. </p>
<p>To give you a quick impression of what some of these algorithms would be useful for, this post introduces a trajectory preprocessing workflow that is quite general-purpose and can be adapted to many different datasets. </p>
<p>We start out with the Geolife sample dataset which you can find in the Trajectools plugin directory’s sample_data subdirectory. This small dataset includes 5908 points forming 5 trajectories, based on the trajectory_id field:</p>
<figure class="wp-block-image size-large"><a href="https://anitagraser.com/wp-content/uploads/2024/09/image-2.png"><img alt="" class="wp-image-9208" height="611" src="/img/subscribers/anita_graser/trajectools-tutorial-trajectory-preprocessing/image-2.webp" width="1024"/></a></figure>
<p>We first split our trajectories by observation gaps to ensure that there are no large gaps in our trajectories. Let’s make at cut at 15 minutes: </p>
<figure class="wp-block-image size-large is-resized"><a href="https://anitagraser.com/wp-content/uploads/2024/09/image-1.png"><img alt="" class="wp-image-9206" height="645" src="/img/subscribers/anita_graser/trajectools-tutorial-trajectory-preprocessing/image-1.webp" style="width: 840px; height: auto;" width="729"/></a></figure>
<p>This splits the original 5 trajectories into 11 trajectories: </p>
<figure class="wp-block-image size-large"><a href="https://anitagraser.com/wp-content/uploads/2024/09/image-3.png"><img alt="" class="wp-image-9209" height="611" src="/img/subscribers/anita_graser/trajectools-tutorial-trajectory-preprocessing/image-3.webp" width="1024"/></a></figure>
<p>When we zoom, for example, to the two trajectories in the north western corner, we can see that the trajectories are pretty noisy and there’s even a spike / outlier at the western end: </p>
<figure class="wp-block-image size-large"><a href="https://anitagraser.com/wp-content/uploads/2024/09/image-4.png"><img alt="" class="wp-image-9211" height="611" src="/img/subscribers/anita_graser/trajectools-tutorial-trajectory-preprocessing/image-4.webp" width="1024"/></a></figure>
<p>If we label the points with the corresponding speeds, we can see how unrealistic they are: over 300 km/h!</p>
<figure class="wp-block-image size-large"><a href="https://anitagraser.com/wp-content/uploads/2024/09/image-5.png"><img alt="" class="wp-image-9213" height="611" src="/img/subscribers/anita_graser/trajectools-tutorial-trajectory-preprocessing/image-5.webp" width="1024"/></a></figure>
<p>Let’s remove outliers over 50 km/h:</p>
<figure class="wp-block-image size-large"><a href="https://anitagraser.com/wp-content/uploads/2024/09/image-6.png"><img alt="" class="wp-image-9215" height="645" src="/img/subscribers/anita_graser/trajectools-tutorial-trajectory-preprocessing/image-6.webp" width="729"/></a></figure>
<p>Better but not perfect: </p>
<figure class="wp-block-image size-large"><a href="https://anitagraser.com/wp-content/uploads/2024/09/image-7.png"><img alt="" class="wp-image-9217" height="611" src="/img/subscribers/anita_graser/trajectools-tutorial-trajectory-preprocessing/image-7.webp" width="1024"/></a></figure>
<p>Let’s smooth the trajectories to get rid of more of the jittering. </p>
<p>(You’ll need to pip/mamba install the optional stonesoup library to get access to this algorithm.)</p>
<figure class="wp-block-image size-large"><a href="https://anitagraser.com/wp-content/uploads/2024/09/image-8.png"><img alt="" class="wp-image-9219" height="645" src="/img/subscribers/anita_graser/trajectools-tutorial-trajectory-preprocessing/image-8.webp" width="729"/></a></figure>
<p>Depending on the noise values we chose, we get more or less smoothing: </p>
<figure class="wp-block-image size-large is-resized"><a href="https://anitagraser.com/wp-content/uploads/2024/09/image-10.png"><img alt="" class="wp-image-9223" height="611" src="/img/subscribers/anita_graser/trajectools-tutorial-trajectory-preprocessing/image-10.webp" style="width: 840px; height: auto;" width="1024"/></a></figure>
<p>Let’s zoom out to see the whole trajectory again: </p>
<figure class="wp-block-image size-large"><a href="https://anitagraser.com/wp-content/uploads/2024/09/image-11.png"><img alt="" class="wp-image-9225" height="611" src="/img/subscribers/anita_graser/trajectools-tutorial-trajectory-preprocessing/image-11.webp" width="1024"/></a></figure>
<p>Feel free to pan around and check how our preprocessing affected the other trajectories, for example: </p>
<figure class="wp-block-image size-large"><a href="https://anitagraser.com/wp-content/uploads/2024/09/image-14.png"><img alt="" class="wp-image-9229" height="611" src="/img/subscribers/anita_graser/trajectools-tutorial-trajectory-preprocessing/image-14.webp" width="1024"/></a></figure>
<figure class="wp-block-image size-large"><a href="https://anitagraser.com/wp-content/uploads/2024/09/image-13.png"><img alt="" class="wp-image-9228" height="611" src="/img/subscribers/anita_graser/trajectools-tutorial-trajectory-preprocessing/image-13.webp" width="1024"/></a></figure>
