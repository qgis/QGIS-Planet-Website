---
source: "blog"
title: "QField 4.2 \"Coral Sea\": Reaching sub-centimeter accuracy out of the box"
date: "2026-06-09T00:02:00+0000"
link: "https://qfield.org/blog/2026/06/09/qfield-4.2-coral-sea-reaching-sub-centimeter-accuracy-out-of-the-box/"
draft: "false"
showcase: "planet"
subscribers: ["qfield"]
author: "QField"
tags: ["releases", "highlights", "qfield", "qgis.org"]
languages: ["en_gb"]
available_languages: ["en_gb"]
---

<p>Here’s another QField release, packed with the features that have been at the top of professional surveyors’ wish list! (hint: it’s in the title) — plus improvements across the board for our wide range of users.</p>
<h2 id="main-highlights">Main highlights</h2>
<p><img alt="" src="/img/subscribers/qfield/qfield-4.2-coral-sea-reaching-sub-centimeter-accuracy-out-of-the-box/splash42.webp"/></p>
<h3 id="ntrip--bluetooth-low-energy">NTRIP &amp; Bluetooth Low Energy</h3>
<p>First up, NTRIP support has been added in QField <strong>unlocking sub-centimeter accuracy position readings without the need for any third-party app</strong>. This has long been requested by cadastral surveyors and other professional field workers in need of highly accurate data where being a few centimeters off can have real consequences.</p>
<p>To configure an NTRIP connection, simply connect to an RTK capable GNSS device via Bluetooth, BLE or TCP from the QField settings positioning panel. Once connected, the NTRIP user interface will be visible just below the positioning devices combo box in the same panel.</p>
<p>From there, users can enter their NTRIP caster details and enable the connection. An NTRIP visual indicator has been added at the top of the map canvas positioning information panel overlay to reflect the status of the connection. A blue dot means everything’s working, a glowing orange dot means the connection has stopped receiving correction data, and a gray dot means the connection has turned off.</p>
<p><img alt="" src="/img/subscribers/qfield/qfield-4.2-coral-sea-reaching-sub-centimeter-accuracy-out-of-the-box/ntrip.webp"/></p>
<p>Moving onto another functionality that walks hand in hand with NTRIP: QField now <strong>supports connecting to external GNSS devices via Bluetooth Low Energy (BLE)</strong>. This means a whole array of GNSS devices can now talk directly to QField on iOS as well, simplifying workflows for field surveyors working on this platform. While the benefit is most visible on iOS as QField previously lacked the ability to talk through Bluetooth altogether on that platform, BLE connections are also available on Android, Windows, and Linux. In many cases, it can offer a more stable connection.</p>
<p>The <strong>development of these fantastic features was supported by two QField hardware partners: HappySurvey and ArduSimple</strong>. Their support meant we were able to focus on getting the best possible experience running on their devices. Other hardware will definitively work out of the box too, and we’d love to hear about your experiences. However, since we are dealing with functionalities that are often driven by vendor-specific commands and UUIDs, there’s plenty of room to grow when it comes to compatibility. So if you’re a hardware vendor, feel free to reach out, <a href="https://qfield.org/hardware/" rel="noopener" target="_blank">join our certified hardware program</a>
 and support QField’s growth! :)</p>
<p>Moving on to another noteworthy newly-added functionalities.</p>
<h3 id="feature-form-improvements">Feature form improvements</h3>
<p>Starting with QField 4.2, the feature form includes a <strong>new gallery editor which shows previews of image, video, and audio content</strong> from relationships where the child layer has one or more attachment attributes. It will turn itself on automatically whenever QField detects this setup. The gallery editor also offers a quick snap button allowing for a much faster workflow around photo and video capture. And yes, we’ve updated our notes layer to support this when creating projects using QField.</p>
<p>Another feature form improvement is a <strong>wizard mode, which turns a complex set of tabs into a simple, linear flow guided by next and previous buttons that respond to constraints.</strong> driven by an easy to use pair of next and previous buttons that are reacting to constraints. The wizard mode is a per-project setting that can be enabled when setting up projects in QGIS. Simply make sure QFieldSync is installed to see the configuration panel in the project properties dialog.</p>
<p style="text-align: center;"><a href="https://qfield.org/tags/qgis.org/wizard.webm" target="_blank">Watch Video</a></p>
<h3 id="feature-identification-in-3d-and-more">Feature identification in 3D, and more</h3>
<p>Users enjoying QField’s recent addition of 3D views will be delighted by what’s coming next. <strong>Feature identification by tapping on the terrain in 3D map views</strong> is now possible. This removes the need to switch back and forth between 2D and 3D to do attribute editing or getting more information on a nearby point of interest during 3D-enhanced hikes through your favorite national park.</p>
<p>There are countless more improvements that would transform this announcement into a full on essay ;) to highlight a few more:</p>
<ul>
<li>
<p>A new <strong>project information popup</strong> accessible via the side dashboard <strong>displays crucial project metadata such as the title, the abstract description, and the author(s)</strong>.</p>
</li>
<li>
<p>The <strong>features list now reflects attribute table’s row conditional styling</strong> configured in QGIS, providing a nice way to add visual hints to make features in need of attention pop out in the list;</p>
</li>
<li>
<p><strong>Audio attachments now show a level preview</strong> that helps identify key parts of a clip during playback.</p>
</li>
<li>
<p>Lines and polygons digitized using a stylus in freehand mode are now smoother with cleaner geometries containing fewer redundant vertices; and</p>
</li>
</ul>
<p>As always, the full changelog is available over here for even more goodies.</p>
<h2 id="a-flood-of-qfieldcloud-improvements">A flood of QFieldCloud improvements</h2>
<p>This new version of QField is packed with <a href="https://qfield.cloud/" rel="noopener" target="_blank">QFieldCloud</a>
 improvements. The biggest one is the retirement of the cloud projects ‘community’ tab in favor of a <strong>completely revamped – and we believe improved – experience around cloud project searching and filtering</strong>. Users can now easily filter projects by organization and teammate ownership as well as by keywords. The new user interface also makes searching through the countless cloud projects that have been made public by authors around the world far more intuitive.</p>
<p><img alt="" src="/img/subscribers/qfield/qfield-4.2-coral-sea-reaching-sub-centimeter-accuracy-out-of-the-box/qfc.webp"/></p>
<p>A brand new <strong>cloud storage indicator has been added to QField</strong> to let users know of their current used and remaining storage size. This will help users keep on top of their storage and provide an early warning when space is about to run out. Upgrades are available for users to keep working on these growing cloud projects that were started using the <a href="https://qfield.cloud/pricing" rel="noopener" target="_blank">free community plan</a>
.</p>
<p>Beyond that, we’ve been hard at work hunting bugs and increasing the overall stability. We’ve also transformed a number of obscure and intimidating error messages into helpful notifications.</p>
<h2 id="coral-sea-release-name">‘Coral Sea’ release name</h2>
<p>The Coral Sea stretches across the southwest Pacific, bordered by Australia, Papua New Guinea, Solomon Islands, and Vanuatu. Home to the Great Barrier Reef and some of the most biodiverse coastal ecosystems on the planet, it is also one of the most climate-pressured, with bleaching events and coastal change outpacing many monitoring programs.</p>
<p>Field workers across the region are already responding with QField: mapping seagrass and mangroves for blue carbon conservation with the <a href="https://www.macblue-pacific.info/" rel="noopener" target="_blank">MACBLUE project</a>
, building national environmental monitoring capacity through <a href="https://www.sprep.org/news/regional-training-on-geographic-information-system-gis-tools-and-environmental-data-management-held-in-apia" rel="noopener" target="_blank">SPREP’s regional GIS training</a>
, running standardized tropical field data collection at the <a href="https://www.leibniz-zmt.de/de/" rel="noopener" target="_blank">Leibniz Centre for Tropical Marine Research</a>
, and driving land cover surveys across 10 Pacific Island nations through <a href="https://digitalearthpacific.org/" rel="noopener" target="_blank">Digital Earth Pacific</a>
 and the <a href="https://livelihoods-and-landscapes.com/about.html" rel="noopener" target="_blank">maplandscape project</a>
.</p>
<p>At OPENGIS.ch, the Coral Sea is a reminder that the places most in need of reliable field data are often the hardest to reach. That is precisely what QField is built for.</p>
<p>Happy field mapping!</p>
