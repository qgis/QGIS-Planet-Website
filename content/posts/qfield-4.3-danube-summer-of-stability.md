---
source: "blog"
title: "QField 4.3 “Danube”: Summer of stability"
date: "2026-09-08T00:02:00+0000"
link: "https://qfield.org/blog/2026/09/08/qfield-4.3-danube-summer-of-stability/"
draft: "false"
showcase: "planet"
subscribers: ["qfield"]
author: "QField"
tags: ["releases", "highlights", "qfield", "qgis.org"]
languages: ["en_gb"]
available_languages: ["en_gb"]
---

<p>The next version of QField is here. While this time of the year is a well-deserved holiday period for many, we’ve dedicated ourselves to improving the stability and refining of your favorite field mapping tool.</p>
<p>We’re calling this effort the “summer of stability”, a sprint we will undertake on a yearly basis. But there are plenty of improvements to cover, so let’s go over them.</p>
<h2 id="main-highlights">Main highlights</h2>
<p><img alt="" src="/img/subscribers/qfield/qfield-4.3-danube-summer-of-stability/splash43.webp"/></p>
<h3 id="bookmark-manager">Bookmark manager</h3>
<p>First, we’ve introduced <strong>a new bookmark manager to make QField’s experience around spatial bookmarking feel more complete</strong>. With the manager accessible via the dashboard’s main menu – users will be able to browse their bookmarks as a full list with the ability to quickly jump to a bookmark’s location by tapping its name, as well as edit its properties.</p>
<p>Furthermore, users will also be able to <strong>export bookmarks as a geopackage</strong>, which means the data captured through spatial bookmarks is no longer locked within users’ devices anymore. And, if users’ bookmarks become irrelevant, the manager also allows for <strong>bulk deletion of bookmarks</strong>.</p>
<p><img alt="" src="/img/subscribers/qfield/qfield-4.3-danube-summer-of-stability/bookmark-navigation.webp"/></p>
<p>While improving the relevance and usefulness of bookmarks, we added a <strong>“navigate to bookmark” action to the search bar results</strong>.</p>
<h3 id="rock-solid-camera">Rock-solid camera</h3>
<p>As mentioned above, this release focused on refinement and polish, and the camera got special attention. We’ve added <strong>logic to ensure that the rotation of snapped photos matches expectations</strong>. When the device angle gets too tricky for that to work, <strong>users can now manually rotate and flip photos</strong> while previewing them. We also improved camera stability by preventing auto-focus and auto-white balance from freezing the process when the hardware or the operating system fails us.</p>
<p><img alt="" src="/img/subscribers/qfield/qfield-4.3-danube-summer-of-stability/camera-flip-rotate.webp"/></p>
<p>Image stamping has been improved too: it’s now possible to <strong>write details on your images coming from the layer and features</strong> the images will be attached to. This is sure to please many of our users as it was requested more than once across our <a href="https://community.qfield.org/" rel="noopener" target="_blank">community discourse</a>
 and <a href="https://ideas.qfield.org/" rel="noopener" target="_blank">ideas platform</a>
.</p>
<h3 id="qfieldcloud-delivered-project-templates">QFieldCloud-delivered project templates</h3>
<p>Leveraging <a href="https://qfield.cloud/" rel="noopener" target="_blank">QFieldCloud</a>
’s latest capabilities, this new version of QField introduces a <strong>new way to create projects while in the field: project templates</strong>.</p>
<p>When setting up projects in QFieldCloud, users can now flag them as templates. This newly-introduced type allows users to create new projects from these templates through QField itself in the field.</p>
<p><img alt="" src="/img/subscribers/qfield/qfield-4.3-danube-summer-of-stability/qfieldcloud-template.webp"/></p>
<p>Templates become super handy when shared within an organization where all affiliated members can have access to the template. And of course, when the templates are made public, they turn into a fantastic shared resource for the broader community. Trust us, it beats a GitHub repository archive any day of the week ;)</p>
<h3 id="polished-cloud-project-management">Polished cloud project management</h3>
<p>One of the most important ways to manage QFieldCloud data in QField is through its cloud project panel, accessed by tapping the blue cloud button at the top of the dashboard.</p>
<p>In this new version, <strong>the cloud project panel has gone through an evolutionary step</strong>. Changes include:</p>
<ul>
<li>
<p>We’ve made the language easier to understand by non-technical people. Words like “push” and “revert” are replaced with “upload” and “discard”.</p>
</li>
<li>
<p>We also re-ordered the interactive elements to ensure that the most important action was most visible: uploading changes.</p>
</li>
<li>
<p>QField will proactively remind users of pending local changes when they are about to end a mapping session.</p>
</li>
<li>
<p>To avoid accidental data loss, we’ve relocated the discarding or local changes action to a new ‘danger zone’ sub-panel.</p>
</li>
</ul>
<p><img alt="" src="/img/subscribers/qfield/qfield-4.3-danube-summer-of-stability/cloud-project-panel.webp"/></p>
<p>In addition, the cloud project control panel now offers a summary and detailed view of local changes. This allows for users to review the feature addition, editing, and deletion prior to uploading and synchronizing them back to QFieldCloud.</p>
<p>Haven’t tried QFieldCloud yet? <a href="https://app.qfield.cloud/accounts/signup/" rel="noopener" target="_blank">Sign up for a free community account</a>
!</p>
<h3 id="wait-theres-more">Wait, there’s more</h3>
<p>One of the main objectives of this development cycle has been to improve upon preexisting functionality.</p>
<p>Let’s go over a few notable improvements.</p>
<p>The <strong>QR code scanner can now capture codes from images picked through the device’s gallery</strong>. As more and more QR codes are shared digitally, You’ll never be stuck having to send a friend the QR code you need to scan on your smartphone ever again ;)</p>
<p>On the feature form side,the <strong>value relation editor widget now does accent-less searches</strong> allowing for faster data entry. The <strong>relation editor widgets respect the configured sorting order</strong> defined during project set up. And finally, the gallery editor’s chosen mode – thumbnail vs. list - will be remembered.</p>
<h2 id="still-wondering-what-the-summer-of-stability-means-for-you">Still wondering what the summer of stability means for you?</h2>
<p>As mentioned in the introduction, this release is the culmination of a new yearly sprint we call “summer of stability”. Let’s expand a bit on this.</p>
<p>One of the metrics used to judge whether our efforts were successful is the number of sessions that crashed reported on our anonymized metrics platform. By the end of the sprint, the platform showed a <strong>dramatic decrease in crashes (&gt;20% reduction in reported crashes)</strong>. That is a bottom line that tells us we are making QField more stable!</p>
<p>Beyond that, we’ve also increased our number of automated test cases that act as safeguard against silent regressions every time we commit a change in QField. An extra 27% lines of code were added covering C++ classes and QML items that were until now not tested. This is the way we ensured that the impact of this stability sprint will not dissipate overnight.</p>
<h2 id="danube-release-name">“Danube” release name</h2>
<p>The Danube is the longest river in the European Union. Rising in Germany’s Black Forest, it flows through ten countries and four capital cities — Vienna, Bratislava, Budapest, and Belgrade — before emptying into the Black Sea, sustaining ecosystems, agriculture, energy infrastructure, and the livelihoods of millions along its banks.</p>
<p><img alt="" src="/img/subscribers/qfield/qfield-4.3-danube-summer-of-stability/danube.webp"/></p>
<p><em>Photo by <a href="https://commons.wikimedia.org/wiki/File:Aerial_image_of_the_Danube_Gorge_near_Weltenburg.jpg" rel="noopener" target="_blank">Carsten Steger</a>
</em></p>
<p>This summer, the Danube made headlines for the wrong reasons. Record-low water levels, driven by unprecedented heatwaves, have exposed long-sunken WWII warships and forced drastic action to protect critical infrastructure. In Hungary, the Paks nuclear power plant, which generates nearly half of the country’s electricity using Danube water for cooling, was forced to take all but one of its reactors offline. The European Commission’s Joint Research Centre confirmed the Danube had reached record-low levels, with reduced flows putting pressure on navigation, water supplies, agriculture, and the energy sector. The river that has connected civilisations for millennia is telling us something urgent.</p>
<p>At OPENGIS.ch, we believe that rivers like the Danube are not just geography: they are living systems that require careful observation and data-driven management. Better field data, collected faster and more reliably, is part of how we respond to a changing world.</p>
<p>That is what QField is built for.</p>
