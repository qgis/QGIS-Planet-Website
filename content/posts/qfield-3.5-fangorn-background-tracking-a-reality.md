---
source: "blog"
title: "QField 3.5 “Fangorn”: Background tracking a reality!"
date: "2025-03-04T05:45:00+0000"
link: "https://qfield.org/blog/2025/03/04/qfield-3.5-fangorn-background-tracking-a-reality/"
draft: "false"
showcase: "planet"
subscribers: ["qfield"]
author: "QField"
tags: ["gis", "qfield", "highlights", "qgis.org"]
languages: ["en_gb"]
available_languages: ["en_gb"]
---

<p>Let’s not bury the lead here: the long-awaited capability to track position while QField is in the background or the device is locked has arrived in this brand-new version of QField. This feels like a magical moment, so we settled for a fantastical forest for our release name.</p>
<h2 id="main-highlights">Main highlights</h2>
<figure class="figure text-center mb-4"><img alt="" class="figure-img img-fluid gallery-img" height="736" src="/img/subscribers/qfield/qfield-3.5-fangorn-background-tracking-a-reality/splash_hu_91d75e230c707765.webp" width="1200"/></figure>
<p>As highlighted above, QField 3.5 has unlocked <strong>background position tracking</strong> on the Android platform. This allows users to keep track of their positions even as they put QField in the background to conduct other tasks on their devices. It also means that tracking has become far more battery efficient, as users can lock/suspend their phones and tablets for long periods while QField continues to collect and track positions. On top of it all, this will work out of the book with internal GNSS as well as external high-precision GNSS devices.</p>
<p>This is a long-requested functionality for QField, and we couldn’t be prouder to deliver it to our hundreds of thousands of Android users. Big thanks to <a href="https://www.groupementsforestiers.quebec/" rel="noopener" target="_blank">Groupements forestiers Québec</a>, <a href="https://www.biotope.fr/" rel="noopener" target="_blank">Biotope</a>, and <a href="https://www.terrexseismic.com/" rel="noopener" target="_blank">Terrex Seismic,</a> who jointly sponsored the development.</p>
<p>Moving on to the next major feature added to this new version. Users can now easily import folders from WebDAV services and subsequently upload and download content to that remote folder within QField itself. This functionality eases friction on Android and iOS platforms where storage access is heavily regulated. This implementation highlights our commitment to providing QField users with the freedom they need to build their workflows; thanks to <a href="https://www.prona-romandie.ch/" rel="noopener" target="_blank">Prona Romandie</a>, <a href="http://www.agaricig.com" rel="noopener" target="_blank">AgaricIG</a>, and <a href="https://oslandia.com/" rel="noopener" target="_blank">Oslandia</a> for commissioning this work.</p>
<p>It’s important to note that the WebDAV functionality does not provide data synchronization. The download and upload operations will overwrite datasets stored locally or remotely. <a href="https://qfield.cloud/" rel="noopener" target="_blank">For users in need of synchronization and smooth project distribution, QFieldCloud is the way to go</a>. With this new version of QField, downloading large datasets from QFieldCloud has become much more reliable, especially on devices with low memory.</p>
<p>Last but not least, QField has gained <strong>support</strong> <strong>for project-configured grid decoration</strong>. When activated, a grid is overlayed on top of the map canvas, which will dynamically render while panning and zooming around. The grid is configured and activated while setting up projects within QGIS itself.</p>
<figure class="figure text-center mb-4"><img alt="" class="figure-img img-fluid gallery-img" height="681" src="/img/subscribers/qfield/qfield-3.5-fangorn-background-tracking-a-reality/griddialog.webp" width="600"/></figure>
<p>Pro tip: this functionality can replace heavy grid datasets when covering a large dataset, something to consider when trying to optimize projects’ storage size. Big thanks to <a href="https://messtechnik.ch/" rel="noopener" target="_blank">Oester Messtechnik GmbH</a> for supporting the implementation of this fourth decoration following the arrival of title, copyright, and image decorations in earlier releases.</p>
<p>Other improvements in this release include <strong>“forward” angle snapping</strong> to digitize perfectly angled polygons, <strong>pinch gesture-driven feature rotation</strong>, and a new print template which unlocks printing of map canvas to PDF even when their projects have no layouts defined.</p>
<figure class="figure text-center mb-4"><img alt="" class="figure-img img-fluid gallery-img" height="560" src="/img/subscribers/qfield/qfield-3.5-fangorn-background-tracking-a-reality/alwayspdf.webp" width="764"/></figure>
<h2 id="plugin-specific-improvements"><strong>Plugin-specific improvements</strong></h2>
<p>One of the main additions to QField’s plugin framework is the <strong>capability to integrate custom results into the search bar</strong>. Thanks to Kanton Basel-Landschaft for supporting the development, users can enjoy OpenStreetMap Nominatim search result integration by <a href="https://github.com/opengisch/qfield-nominatim-locator" rel="noopener" target="_blank">installing this plugin</a> (instructions available on the repository). This integration also opens up many new possibilities, such as enabling plugins to send prompts to AI, just like <a href="https://github.com/mbernasocchi/qfield-ask-ai" rel="noopener" target="_blank">this plugin</a> does.</p>
<p>Other noteworthy improvements include shipping <strong>Quick3D QML modules, which allow authors to develop 3D overlays</strong>, a new API to customize QField’s colour appearance and a new mechanism for plugins to add a configuration button within the plugin manager.</p>
<figure class="figure text-center mb-4"><img alt="" class="figure-img img-fluid gallery-img" height="392" src="/img/subscribers/qfield/qfield-3.5-fangorn-background-tracking-a-reality/configuration.webp" width="800"/></figure>
<p>Users and plugin authors can expect an exciting year ahead as the QField plugin framework continues to grow with new functionalities and improvements. Watch this space!</p>
