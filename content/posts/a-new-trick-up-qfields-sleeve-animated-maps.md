---
source: "blog"
title: "A New Trick up QField’s Sleeve: Animated Maps"
date: "2022-08-16T04:58:00+0000"
link: "https://qfield.org/blog/2022/08/16/a-new-trick-up-qfields-sleeve-animated-maps/"
draft: "false"
showcase: "planet"
subscribers: ["qfield"]
author: "QField"
tags: ["qfield", "highlights", "qgis", "video", "qgis.org"]
languages: ["en_gb"]
available_languages: ["en_gb"]
---

<p><strong>Starting with QField 2.2, users can fully rely on animation capabilities that have made their way into QGIS during its last development cycle. This can be a powerful mean to highlight key elements on a map that require special user attention.</strong></p>
<p>The example below demonstrates a scenario where animated raster markers are used to highlight active fires within the visible map extent. Notice how the subtle fire animation helps draw viewers’ eyes to those important markers.</p>
<figure class="figure text-center mb-4"><img alt="" class="figure-img img-fluid gallery-img" height="464" src="/img/subscribers/qfield/a-new-trick-up-qfields-sleeve-animated-maps/Peek-2022-07-16-12-43.gif" width="799"/></figure>
<p><a href="https://www.qgis.org/en/site/forusers/visualchangelog326/index.html#feature-new-animated-marker-symbol-type" rel="noopener" target="_blank"><em>Animated raster markers</em> is a new symbol layer type in QGIS 3.26</a> that was developed by <a href="https://north-road.com/" rel="noopener" target="_blank">Nyall Dawson</a>. Supported image formats include GIF, WEBP, and APNG.</p>
<p>The second example below showcases more advanced animated symbology which relies on expressions to animate several symbol properties such as marker size, border width, and color opacity. While more complex than simply adding a GIF marker, the results achieved with data-defined properties animation can be very appealing and integrate perfectly with any type of project.</p>
<p><a href="https://player.vimeo.com/video/732691644" rel="noopener" target="_blank">https://player.vimeo.com/video/732691644</a></p>
<p>You’ll quickly notice how smooth the animation runs. That is thanks to OPENGIS.ch’s own ninjas having spent time improving the map canvas element’s handling of layers constantly refreshing. This includes automatic skipping of frames on older devices so the app remains responsive.</p>
<p>Oh, we couldn’t help ourselves but take the opportunity to demonstrate how nice the QField feature form layout is these days in the video above ? To know more about <a href="https://github.com/opengisch/QField/releases/tag/v2.2.0" rel="noopener" target="_blank">other new features in QField 2.2, go and read the release page</a>.</p>
<p>Happy field mapping to all!</p>
<p><em>The lovely animal markers used in the zoo example above were made by Serbian artist <a href="https://www.behance.net/gallery/38312723/Animals" rel="noopener" target="_blank">Arsenije Vujovic</a>.</em></p>
