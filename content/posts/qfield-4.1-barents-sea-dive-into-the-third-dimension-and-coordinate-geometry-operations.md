---
source: "blog"
title: "QField 4.1 \"Barents Sea\": Dive into the third dimension and coordinate geometry operations!"
date: "2026-03-23T00:05:00+0000"
link: "https://qfield.org/blog/2026/03/23/qfield-4.1-barents-sea-dive-into-the-third-dimension-and-coordinate-geometry-operations/"
draft: "false"
showcase: "planet"
subscribers: ["qfield"]
author: "QField"
tags: ["releases", "highlights", "qfield", "qgis.org"]
languages: ["en_gb"]
available_languages: ["en_gb"]
---

<p>QField’s first release of the year comes packed with new features as well as a bundle of improvements and polishing. Let’s jump right into it.</p>
<h2 id="main-highlights">Main highlights</h2>
<p><img alt="" src="/img/subscribers/qfield/qfield-4.1-barents-sea-dive-into-the-third-dimension-and-coordinate-geometry-operations/splash41.webp"/></p>
<h3 id="3d">3D</h3>
<p>This new version of QField comes with a <strong>shiny 3D map view</strong>, giving users the ability to render their map content on top of a three-dimensional terrain.</p>
<p>Users can rotate the terrain geometry to get a better understanding of elevation profiles, while also adjusting the plane’s extent by panning and zooming with drag and pinch gestures. When the GNSS positioning service is enabled, the <strong>user’s current position, as well as ongoing tracking sessions, will be overlaid on top of the 3D terrain geometry</strong>.</p>
<p><a href="https://qfield.org/tags/qgis.org/3d.webm" target="_blank">Watch Video</a></p>
<p>By default, QField relies on Mapzen Global Terrain tiles to determine terrain elevation. As its name indicates, this is a 30-meter digital elevation model covering the globe and hosted online, which allows QField to render 3D views without any user configuration. But it does not stop there. QField <strong>supports additional elevation sources, such as disk-based GeoTIFFs, to work in offline areas</strong>. This can be configured when setting up a project by changing the terrain type in QGIS.</p>
<h3 id="cogo-operations">COGO operations</h3>
<p>Moving on to the next major functionality introduced in this new version: a <strong>COGO (Coordinate Geometry) framework to support fieldwork</strong> through a set of parameter-driven operations to generate vertices. This has been one of the most requested features by professional land surveyors, so we couldn’t be more excited to deliver it and hear back from our community.</p>
<p><img alt="" src="/img/subscribers/qfield/qfield-4.1-barents-sea-dive-into-the-third-dimension-and-coordinate-geometry-operations/cogotools.webp"/></p>
<p>QField 4.1 ships with three COGO tools:</p>
<ul>
<li>The <strong>XYZ parameters</strong> operation generates vertices based on a manually entered pair of X and Y coordinates as well as an optional Z value;</li>
<li>The <strong>distance/angle from point</strong> operation generates vertices based on distance and angle values from a given point; and</li>
<li>The <strong>circles’ intersection</strong> operation generates vertices at the intersection of two circles, each defined by a point and a radius.</li>
</ul>
<p>Leveraging QField’s capabilities, a COGO operation’s point parameter can be defined in multiple ways: users can enter values manually or automatically fill in the parameter using either the current GNSS position, the geometry of a pre-existing feature within a point layer, or the coordinate cursor’s location. The latter is super useful when coupled with project snapping.</p>
<h3 id="theres-more">There’s more</h3>
<p>Beyond these two flagship features, this new version contains tons of improvements.</p>
<p>We’re happy to report that <strong>the background tracking functionality introduced for Android last year is now available on iOS</strong>. Users can now save battery by locking their phone while QField continues to track positions. Upon reopening QField, the collected positions will be written into your project. No Apple will be left behind.</p>
<p>The feature form continued to receive improvements during this development cycle. Starting with this version, Remember Last Value pins are hidden by default. Moving away from an always-shown interface, <strong>remember last value pin visibility can now be configured per field</strong>. Using the latest QGIS (4.0 and above), users can configure the presence of the pin and whether remembrance should be active by default in the vector layer properties’ attribute form panel.</p>
<p>Position tracking has received a lot of attention during this development cycle focused on optimizations. <strong>Tracking is now friendlier to your device battery</strong> while user interface responsiveness has been improved when tracking sessions are ongoing. We’ve also spent some time making Bluetooth connections to external GNSS devices even more reliable. If this was an issue for you in the past, give this version a try again.</p>
<p>Finally, something to please our advanced users: QField now offers the <strong>ability to tunnel network traffic through a proxy</strong> that can be enabled and configured in the settings panel.</p>
<h2 id="barents-sea-release-name">‘Barents Sea’ release name</h2>
<p>The Barents Sea, a marginal sea of the Arctic Ocean bordered by Norway and Russia, is one of the most ecologically and geopolitically significant water bodies on the planet. Home to some of the world’s largest cod and haddock fisheries, it sustains both marine ecosystems and the livelihoods of coastal communities across the high north. Its waters are a barometer for our changing climate: the Barents Sea is the fastest-warming part of the Arctic, making it a critical area of scientific observation and environmental monitoring. The <a href="https://arvenetternansen.com/" rel="noopener" target="_blank">Nansen Legacy project</a> has been tracking these changes closely (<a href="https://arvenetternansen.com/wp-content/uploads/2024/04/The-future-Barents-Sea-fact-sheet-AeN-2024.pdf" rel="noopener" target="_blank">factsheet</a>).
<figure class="figure text-center mb-4"><img alt="Sea ice in the Barents Sea" class="figure-img img-fluid gallery-img" height="685" src="/img/subscribers/qfield/qfield-4.1-barents-sea-dive-into-the-third-dimension-and-coordinate-geometry-operations/ice.webp" width="1023"/>
<figcaption class="figure-caption text-center">Sea ice in the Barents Sea, Peter Prokosch <a href="https://www.grida.no/resources/3636" rel="noopener" target="_blank">https://www.grida.no/resources/3636</a></figcaption></figure></p>
<p>At OPENGIS.ch, we see the Barents Sea as a powerful symbol of why field data collection matters. Understanding and protecting remote, extreme environments like the Arctic requires tools that are reliable, offline-capable, and built for real-world conditions. That is precisely what QField is designed to deliver.</p>
<p>With QField 4.1 ‘Barents Sea’, we continue building on that mission, bringing new capabilities to field workers, researchers, and environmental stewards wherever their work takes them.</p>
<p>Happy field mapping!</p>
