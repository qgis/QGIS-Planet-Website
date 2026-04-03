---
source: "blog"
title: "Powerful and gentle QField 1.8 Selma sneaked in"
date: "2021-02-24T06:31:00+0000"
link: "https://qfield.org/blog/2021/02/24/powerful-and-gentle-qfield-1.8-selma-sneaked-in/"
draft: "false"
showcase: "planet"
subscribers: ["qfield"]
author: "QField"
tags: ["android-qgis", "featured", "gis", "qfield", "highlights", "qgis.org"]
languages: ["en_gb"]
available_languages: ["en_gb"]
---

<p><strong>Get fieldwork smoothly and nimbly done despite the ice and snow outside. Collect accurate data with freehand digitizing and improved form widgets, use the data from your external GNSS receivers without any third-party apps and enjoy the pleasant usability of QField 1.8 Selma.</strong></p>
<p>This year started off hi-speed for us. There’s been already a lot of coding, designing and teaching, and we’ve thrown ourselves into these things we love to do. And we published another QField release last week that I completely forgot to announce in this blog. But here it is. It’s QField 1.8, Selma. And it’s packed with cool features.</p>
<p>Let’s have a look.</p>
<h2 id="freehand-drawing">Freehand drawing</h2>
<p>This might be a feature that brings a lot of fun and professionalism to your work. The freehand digitizing mode allows the user to “draw” lines and polygons with the stylus pen. The mode is available for adding line/polygon features as well as for the ring tool of the geometry editor.</p>
<figure class="figure text-center mb-4"><img alt="" class="figure-img img-fluid gallery-img" height="804" src="/img/subscribers/qfield/powerful-and-gentle-qfield-1.8-selma-sneaked-in/freehand_hu_abc12d029e3b948b.webp" width="1200"/></figure>
<p>Together with the powerful options in the topological editing where you can snap to existing features and avoid overlaps, it’s very convenient to digitize complex shapes.</p>
<h2 id="zoom-in-and-out">Zoom in and out</h2>
<p>Speaking of fun. One day, a guy from the QGIS community asked us if we could implement the functionality to zoom in and zoom out like he is able to do with an app called Maps from a company named Google. I didn’t know what he meant, but he explained: Single finger double tap-and-hold zoom gesture (which allows you to zoom smoothly from anywhere on the screen). Wow! Didn’t know it before, but it’s super neat! So we made it available in QField as well.</p>
<figure class="figure text-center mb-4"><img alt="" class="figure-img img-fluid gallery-img" height="618" src="/img/subscribers/qfield/powerful-and-gentle-qfield-1.8-selma-sneaked-in/zoom2-1.gif" width="1195"/></figure>
<p>If you are used to it, it’s quite easy. But for beginners it can be a bit difficult. So for people who are not that deft - and to keep the UX self-explanatory and simple - we also added two buttons + / - to zoom in and zoom out with just one finger. So now even a clumsy pirate with a hook instead of a hand can collect data with QField :-)</p>
<h2 id="powerful-relation-reference-widget">Powerful Relation Reference Widget</h2>
<p>Let’s be a little bit more serious and talk about how powerful the relation reference widget has become.</p>
<h3 id="view-and-edit-selected-feature">View and Edit selected feature</h3>
<p>The intuitive eye icon next to the widget lets you open the form of the referenced parent feature to view and edit it.</p>
<h3 id="autocomplete-mode">Autocomplete mode</h3>
<p>When auto-complete is enabled, you can easily perform a search in all available parent features.</p>
<figure class="figure text-center mb-4"><img alt="autocomplete" class="figure-img img-fluid gallery-img" src="/img/subscribers/qfield/powerful-and-gentle-qfield-1.8-selma-sneaked-in/102783259-f2a73100-439a-11eb-88e2-d979ea263da5.webp"/>
<figcaption class="figure-caption text-center">autocomplete</figcaption></figure>
<p>With space-separated input, you can search for the beginning of multiple words in the display name of the parent features. So in this example searching for “Ma” will find the name “Mae” and “Marie” and using the second word “buck” it finds the Buckfast bees - so the entries containing both values will be listed on top.</p>
<h2 id="integration-of-external-gnss-receivers">Integration of external GNSS receivers</h2>
<p>In case you wondered, why we did not release 1.8 Selma earlier? Because we wanted to have it feature loaded and rocket proof. And one of this cool feature is the integration of external GNSS receivers.</p>
<p>QField can receive and decode NMEA sentences received via Bluetooth from an external GNSS receiver (such as an EMLID Reach RS2) without the need for any third party app.</p>
<figure class="figure text-center mb-4"><img alt="nmea" class="figure-img img-fluid gallery-img" src="/img/subscribers/qfield/powerful-and-gentle-qfield-1.8-selma-sneaked-in/102783305-ff2b8980-439a-11eb-8907-cd9c447a87df.webp"/>
<figcaption class="figure-caption text-center">nmea</figcaption></figure>
<p>Search for paired Bluetooth devices in the device settings, connect to the external device and receive the GNSS information.</p>
<h2 id="select-vertical-grid-shift-files">Select vertical grid shift files</h2>
<p>In the QField settings, you can select a grid file on your mobile device by placing it in a directory named <code>QField/proj</code> in the main folder of the internal storage to increase the vertical location accuracy.</p>
<h2 id="postgres-config-file">Postgres Config File</h2>
<p>If you once started using PostgreSQL configuration files, you don’t want to live without them anymore. And when you use it on your PC, I’m sure you want to use it on your mobile device as well.</p>
<p>Define Postgresql services in a pg_service.conf file and use it on QField by placing it directly in a directory named <code>QField</code> in the main folder of the internal storage.</p>
<h2 id="add-reload-data-button">Add reload data button</h2>
<p>The layer properties have been polished and in addition, you will find a button to reload the layer data. This is especially useful if you use WFS layers from which you need to get updates.</p>
<figure class="figure text-center mb-4"><img alt="nmea" class="figure-img img-fluid gallery-img" src="/img/subscribers/qfield/powerful-and-gentle-qfield-1.8-selma-sneaked-in/102783341-0e123c00-439b-11eb-9d54-e360f08a7749.webp"/>
<figcaption class="figure-caption text-center">nmea</figcaption></figure>
<h2 id="register-extra-fonts">Register extra fonts</h2>
<p>Also, you can add <code>TTF</code> and <code>OTF</code> font files into a directory named <code>QField/fonts</code> at the main folder of the internal storage to use the nice fonts you like.</p>
<figure class="figure text-center mb-4"><img alt="fonts" class="figure-img img-fluid gallery-img" src="/img/subscribers/qfield/powerful-and-gentle-qfield-1.8-selma-sneaked-in/102783368-18343a80-439b-11eb-842d-a2d9bb144d5b.webp"/>
<figcaption class="figure-caption text-center">fonts</figcaption></figure>
<p>How beautiful is that!</p>
<h2 id="support-of-new-raster-file-formats">Support of new raster file formats</h2>
<p>By the way: Many new raster file formats are supported - most notably <a href="https://www.cogeo.org/" rel="noopener" target="_blank">COG</a>. While not yet supported as remote format streamed directly from the web, it is also a high performance format if used locally</p>
<h2 id="what-about-the-cloud">What about the cloud?</h2>
<p>You might be one of these people eagerly waiting and always receiving the same message: Keep calm, it’s coming soon. Sorry for that. But when we do something, we do it right. And we prefer to have a stable solution than to publish half baked stuff. We are still highly busy coding, testing and promoting <a href="https://qfield.cloud/" rel="noopener" target="_blank">QFieldCloud</a>. It’s announced for this spring / early summer.</p>
<p>Also, keep an eye on the <a href="https://twitter.com/qfieldforqgis" rel="noopener" target="_blank">@QFieldForQgis</a> and <a href="https://twitter.com/qfieldcloud" rel="noopener" target="_blank">@QFieldCloud</a> twitter accounts to stay updated.</p>
<h2 id="we--our-beta-testers">We ♥ our Beta Testers</h2>
<p>The Beta Testers are our secret heroes. They report bugs and inconveniences before the normal users are bothered with them. Thanks to the Beta Testers QField is so stable. And at this point we would like to say: Thank you, test heroes!</p>
<p>And what do the beta testers get in return? Well, they can be the very first to try out the great new features. This is exciting and fun. So don’t hesitate. Join the beta.</p>
<figure class="figure text-center mb-4"><img alt="" class="figure-img img-fluid gallery-img" height="511" src="/img/subscribers/qfield/powerful-and-gentle-qfield-1.8-selma-sneaked-in/WhatsApp-Image-2021-02-21-at-21.54.31.webp" width="1080"/></figure>
<p>In the Play Store you should find this section under the “QField for QGIS” app listing. Enjoy the feature frenzy and report the problems at <a href="https://qfield.org/issues" rel="noopener" target="_blank">qfield.org/issues</a></p>
<h2 id="and-if-you-wondered">And if you wondered…</h2>
<p>… why this release is called “Selma”. It’s of course because of the Mount Selma in Australia… And because it’s the name of my beloved cat. That’s her - Selma Eulenkopf - staring at me while I’m coding QField.</p>
<figure class="figure text-center mb-4"><img alt="" class="figure-img img-fluid gallery-img" height="685" src="/img/subscribers/qfield/powerful-and-gentle-qfield-1.8-selma-sneaked-in/selm_office_hu_28e262b3140d4f78.webp" width="1200"/></figure>
