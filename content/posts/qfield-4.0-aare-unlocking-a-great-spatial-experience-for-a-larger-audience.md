---
source: "blog"
title: "QField 4.0 "Aare": Unlocking a great spatial experience for a larger audience"
date: "2025-12-17T00:00:00+0000"
link: "https://qfield.org/blog/2025/12/17/qfield-4.0-aare-unlocking-a-great-spatial-experience-for-a-larger-audience/"
draft: "false"
showcase: "planet"
subscribers: ["qfield"]
author: "QField"
tags: ["releases", "highlights", "qgis.org"]
languages: ["en_gb"]
available_languages: ["en_gb"]
---

<p>Just in time for the end of 2025, <strong>QField 4.0</strong> is now available in a virtual store near you. This release brings significant improvements and marks an important usability milestone, worthy of a new major version. It’s truly never been easier to get started with QField - whether you’re a seasoned GIS professional or new to spatial data collection.</p>
<h2 id="main-highlights">Main highlights</h2>
<p><img alt="" src="/img/subscribers/qfield/qfield-4.0-aare-unlocking-a-great-spatial-experience-for-a-larger-audience/image.webp"/></p>
<p>One of the most significant feature additions in this new version is right there on the welcome screen: <strong>a simple wizard for creating new projects</strong>. The wizard guides users through a set of questions covering the desired basemap style and actions such as note taking and position tracking. These projects can be published directly on <a href="https://qfield.cloud/" rel="noopener" target="_blank">QFieldCloud</a>, so users can upload images, notes, and tracks that are accessible through web browsers or QGIS using QFieldSync.</p>
<p>The project creation framework also unlocked another feature we’re proud of: <strong>on-the-fly conversion of imported projects to cloud projects</strong>. The ability to upgrade pre-existing projects to cloud projects means that users can push spatial data and attachments residing on their devices to QFieldCloud and instantly collaborate with coworkers.</p>
<p>On the QFieldCloud front, we’ve done significant code refactoring to make synchronization and attachment uploads even more reliable. Users now see a progress bar showing attachment upload status.</p>
<p>The cloud projects list also lets users push changes and sync projects without opening them first. Indicator badges show whether you have pending local changes or if updates are available from the cloud.</p>
<h2 id="a-leaner-clearer-and-more-focused-user-interface">A leaner, clearer, and more focused user interface</h2>
<p>Early on in this development cycle, our ninjas decided to make a significant leap forward with QField’s UX focusing on making the user interface leaner when possible, clearer when needed, and more focused throughout.</p>
<p>QField now has a <strong>vastly more readable feature form when</strong> viewing feature attributes. We’ve also <strong>made the interface more consistent</strong> by updating all editor widgets to use Qt’s Material style, so comboboxes, text fields, and other elements now have a unified look.</p>
<p><img alt="" src="/img/subscribers/qfield/qfield-4.0-aare-unlocking-a-great-spatial-experience-for-a-larger-audience/image-1.webp"/></p>
<p>We’ve also <strong>simplified the user experience around positioning</strong>. The map canvas now has a single positioning button at the bottom right. Click the location marker overlay to reveal a new pie menu with quick access to positioning features: start tracking sessions, copy position to clipboard, show the positioning panel, lock the coordinate cursor to position, lock the map canvas to position, and add bookmarks at your position.</p>
<p>Now when users set accuracy thresholds, tracking sessions and averaged positioning will automatically filter out “bad accuracy” readings.</p>
<p>QField also animates transitions when jumping to your GNSS position, features, or coordinates, making navigation feel smoother and more intuitive.</p>
<h2 id="wait-theres-more">Wait, there’s more</h2>
<p>Beyond these major improvements, QField 4.0 includes tons of new features:</p>
<ul>
<li><strong>Multilingual projects</strong> - <a href="https://www.opengis.ch/2018/09/11/qgis-speaks-a-lot-of-languages/" rel="noopener" target="_blank">a feature we added to QGIS several years ago</a> - are now supported in QField</li>
<li>When connected to the internet, QField now displays online legend graphics for WMS and Esri map services, providing crucial context for field users</li>
<li>Additional feature form widgets are now supported, including the spacer widget and color editor widget, further improving interoperability with QGIS</li>
</ul>
<p>A <a href="https://github.com/opengisch/QField/releases/tag/v4.0.0" rel="noopener" target="_blank">complete list of changes is available in the QField release notes</a> on GitHub.</p>
<h2 id="a-new-release-cycle-focused-on-water-bodies">A new release cycle focused on water bodies</h2>
<p>With the <strong>QField 4.X</strong> series, we’re introducing a new naming theme focused on <strong>water bodies</strong>.</p>
<p>Oceans, rivers, lakes, wetlands, and coastal waters are fundamental to life on Earth. They provide drinking water, support ecosystems and agriculture, regulate climate, and sustain communities worldwide. Yet these vital resources are increasingly under pressure from pollution, overuse, and climate change.</p>
<p>At <strong>OPENGIS.ch</strong>, we believe that better spatial data leads to better decisions. By making field data collection easier and more accessible, we aim to support those working to understand, protect, and manage these fragile systems. Dedicating this release cycle to water bodies reflects our commitment to using technology responsibly and connects naturally with the <strong>United Nations Sustainable Development Goals</strong>, which we consistently strive to support through our work.</p>
<p>For the first release in this cycle, we chose a water body of particular significance to QField: Switzerland’s longest river entirely within the country, <strong>Aare</strong>.</p>
<p>As always, we hope you enjoy this new release.</p>
<p>Happy field mapping!</p>
