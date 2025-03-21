---
source: "blog"
title: "New release for QField : 3.3 &#8220;Darién&#8221;"
date: "2024-06-14T13:10:36"
link: "https://oslandia.com/en/2024/06/14/sortie-de-qfield-3-3-darien/"
draft: "false"
showcase: "planet"
subscribers: ["qgis_oslandia"]
author: "QGIS Oslandia"
tags: ["gis", "news", "newsfr", "open source", "qgis", "sig", "android", "annonce", "apple", "mobile", "opengis.ch", "qfield", "survey", "terrain"]
languages: ["en_gb"]
available_languages: ["en_gb"]
---

<p>Oslandia is the main partner of <a href="https://opengis.ch">OPENGIS.ch</a> around <a href="https://qfield.org">QField</a>. We are proud today to forward the announcement of the new QField release 3.3 “Darién”. This release introduces a brand new plugin framework that empowers users to customize and add completely new functionalities to their favourite field application.</p>
<p>The plugin framework comes with other new features and improvements for this release, detailed below.</p>
<h2 class="wp-block-heading">Main highlights</h2>
<figure class="wp-block-image size-full"><img alt="" class="wp-image-14432" height="467" src="/img/subscribers/qgis_oslandia/sortie-de-qfield-3-3-darien/33splash.webp" width="750"/></figure>
<p>One of the biggest feature additions of this version is a<strong> brand new drawing tool</strong> that allows users to sketch out important details over captured photos or annotate drawing templates. This was a highly requested feature, which is brought to all supported platforms (Android, iOS, Windows, macOS, and, of course, Linux) with the financial support of the <a href="http://qgis.ch">Swiss QGIS user group</a>.</p>
<p>Also landing in this version is support for <strong>copying and pasting vector features into and from the clipboard</strong>. This comes in handy in multiple ways, from providing a quick and easy way to transfer attributes from one feature to another through matching field names to pasting the details of a captured feature in the field into a third-party messenger, word editing, or email application. Copying and pasting features can be done through the feature form’s menu as well as long pressed over the map canvas. Moreover, a new feature-to-feature attributes transfer shortcut has also been added to the feature form’s menu. Appreciation to <a href="https://uwe.lu.ch/" rel="noreferrer noopener" target="_blank">Switzerland, Canton of Lucerne, Environment and Energy</a> for providing the funds for this feature.</p>
<figure class="wp-block-gallery has-nested-images columns-default is-cropped wp-block-gallery-1 is-layout-flex wp-block-gallery-is-layout-flex">
<figure class="wp-block-image size-large"><img alt="" class="wp-image-14433" height="386" src="/img/subscribers/qgis_oslandia/sortie-de-qfield-3-3-darien/transfer_attributes.webp" width="750"/></figure>
</figure>
<p>The feature form continues to gain more functionalities; in this version, the feature form’s value map editor widget has gained a <strong>new toggle button interface</strong> that can help fasten data entry. The interface replaces the traditional combo box with a series of toggle buttons, lowering the number of taps required to pick a value. The <a href="https://www.kulturgutretter.org/en/home-2/">German Archaeological Institut – KulturGutRetter</a> sponsored this feature.</p>
<p>Other improvements in the feature form include support for <strong>value relation item grouping</strong> and respect for<strong> the vector layer attributes’ « reuse last entered value » setting</strong>.</p>
<figure class="wp-block-gallery has-nested-images columns-default is-cropped wp-block-gallery-2 is-layout-flex wp-block-gallery-is-layout-flex">
<figure class="wp-block-image size-large"><img alt="" class="wp-image-14434" height="386" src="/img/subscribers/qgis_oslandia/sortie-de-qfield-3-3-darien/value_map_buttons.webp" width="750"/></figure>
</figure>
<p>Finally, additional features include support for <strong>image decoration overlay</strong>, a new interface to <strong>hop through cameras </strong>(front, back, and external devices) for the ‘non-native’ camera<strong>, </strong>the possibility to<strong> disable the 3-finger map rotation gesture</strong>, <a href="https://github.com/opengisch/QField/releases/tag/v3.3.0">and much more</a>.</p>
<h2 class="wp-block-heading"><strong>User experience improvements</strong></h2>
<p>Long-time users of QField will notice the new version <strong>restyling of the information panels such as GNSS positioning, navigation, elevation profile, and sensor data</strong>. The information is now presented as an overlay sitting on top of the map canvas, which increases the map canvas’ visibility while also achieving better focus and clarity on the provided details. With this new version, all details, including altitude and distance to destination, respect user-configured project distance unit type.</p>
<p>The dashboard’s legend has also received some attention. You can now <strong>toggle the visibility of any layer via a quick tap on a new eye icon sitting in the legend tree</strong> itself. Similarly, legend groups can be expanded and collapsed directly for the tree. This also permits you to show or hide layers while digitizing a feature, something which was not possible until now. The development of these improvements was supported by <a href="https://www.gispo.fi/en">Gispo</a> and sponsored by the <a href="https://www.maanmittauslaitos.fi/en">National Land Survey of Finland</a>.</p>
<h2 class="wp-block-heading"><strong>Plugin framework</strong></h2>
<p>QField 3.3 introduces a brand new plugin framework using Qt’s powerful QML and JavaScript engine. With a few lines of code, plugins can be written to tweak QField’s behaviour and add new capabilities. Two types of plugins are possible: app-wide plugins as well as project-scoped plugins. To ensure maximum ease of deployment, plugin distribution has been made possible  through <a href="https://qfield.cloud" rel="noreferrer noopener" target="_blank">QFieldCloud</a>! <a href="https://www.amsa.it/en/cittadini" rel="noreferrer noopener" target="_blank">Amsa</a> provided the financial contribution that brought this project to life.</p>
<figure class="wp-block-image size-large"><img alt="" class="wp-image-14443" height="350" src="/img/subscribers/qgis_oslandia/sortie-de-qfield-3-3-darien/WhatsApp-Image-2024-06-10-at-14.52.50.webp" width="750"/></figure>
<p>Our partner OPENGIS.ch will soon offer a webinar to discover how QField plugins can help your field (and business) workflows by allowing you to be even more efficient in the field.</p>
<p>Users interested in authoring plugins or better understanding the framework, can already visit the <a href="https://docs.qfield.org/how-to/plugins/" rel="noreferrer noopener" target="_blank">dedicated documentation page</a> and a <a href="https://github.com/opengisch/qfield-weather-forecast">sample plugin implementation</a> sporting a weather forecast integration.</p>
<p>A question concerning QField ? Interested in QField deployment ? Do not hesitate to <a href="mailto://infos+qfield@oslandia.com">contact Oslandia to discuss your project</a> !</p>
<p> </p>
