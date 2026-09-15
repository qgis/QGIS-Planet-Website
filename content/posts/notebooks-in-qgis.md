---
source: "blog"
title: "Notebooks in QGIS"
date: "2026-01-10T22:03:44+0000"
link: "https://anitagraser.com/2026/01/10/notebooks-in-qgis/"
draft: "false"
showcase: "planet"
subscribers: ["anita_graser"]
author: "Anita Graser"
tags: ["gis", "qgis", "jupyter"]
languages: ["en_gb"]
available_languages: ["en_gb"]
---

<p class="wp-block-paragraph">Finally it’s here: Jupyter notebooks inside QGIS. I don’t know about you but I’ve been hoping for someone to get around to doing this for quite a while. </p>
<p class="wp-block-paragraph"><a href="https://wetlands.io">Qiusheng Wu</a> published the first version of the <a href="https://plugins.qgis.org/plugins/qgis_notebook/#plugin-versions">Notebook plugin</a> on 26 Dec 2025. Late Christmas present?! </p>
<p class="wp-block-paragraph">For the setup, there’s a handy <a href="https://courses.gisopencourseware.org/mod/book/view.php?id=1455&amp;chapterid=3672#mod_book-chapter">tutorial by Hans van der Kwast</a> and, additionally, Qiusheng published an intro video: </p>
<figure class="wp-block-embed is-type-video is-provider-youtube wp-block-embed-youtube wp-embed-aspect-16-9 wp-has-aspect-ratio"><div class="wp-block-embed__wrapper">
</div></figure>
<p class="wp-block-paragraph">Development is going fast (version 0.3.0 at the time of writing) so there will be new features when you install / update the plugin compared to both the tutorial and the video. </p>
<p class="wp-block-paragraph">The user interface is pretty stripped down with just a few buttons to add new code or markdown cells and to run them. And there is a neat drop-down menu with all kinds of ready-made code snippets to get you started: </p>
<figure class="wp-block-image size-large"><img alt="" class="wp-image-9681" height="690" src="/img/subscribers/anita_graser/notebooks-in-qgis/image.webp" width="1024"/></figure>
<p class="wp-block-paragraph">For other functionalities, for example, to delete cells, you need to right-click on the cell to access the function through the context menu. And, as far as I can tell, there is currently no way to rearrange cells (moving them up or down). </p>
<p class="wp-block-paragraph">I also haven’t quite understood yet what kinds of outputs are displayed and which are not because – quite often – the cell output just stays empty, even though the same code generates output on the console: </p>
<figure class="wp-block-image size-large"><img alt="" class="wp-image-9685" height="650" src="/img/subscribers/anita_graser/notebooks-in-qgis/image-1.webp" width="1024"/></figure>
<p class="wp-block-paragraph">Some of the plugin settings I would have liked to experiment with, such as adjusting the font size or enabling line numbers, don’t seem to work yet. So a little more patience seems to be necessary. </p>
<p class="wp-block-paragraph">I’ll definitely keep an eye on this one :)</p>
<p class="wp-block-paragraph"></p>
