---
source: "blog"
title: "QField 1.6 is out!"
date: "2020-08-18T05:00:00+0000"
link: "https://qfield.org/blog/2020/08/18/qfield-1.6-is-out/"
draft: "false"
showcase: "planet"
subscribers: ["qfield"]
author: "QField"
tags: ["android-qgis", "featured", "gis", "qfield", "highlights", "qgis.org"]
languages: ["en_gb"]
available_languages: ["en_gb"]
---

<p><strong>Editing multiple features at the same time, support for stylus pens, dynamic configuration of image names and much more.</strong><br/>
<strong>QField 1.6 Qinling 秦岭 comes packed with awesome new features and an improved user experience.</strong></p>
<p>We have been very busy over the last few months working on a new and shiny QField release. We have added many new features that increase efficiency on the field or allow for new workflows. In parallel, we have also been working on ironing out a series of issues and improving the overall user experience to make the app as pleasurable to use as possible. The result is QField 1.6 which has been published now.</p>
<p>Enough of the highlevel talking, let’s see what has been done.</p>
<h2 id="multi-editing">Multi editing</h2>
<p>Do you recall Geography lesson 101, Toblers first law? <em>Everything is related to everything else. But near things are more related than distant things.</em></p>
<p>Very often there are similar objects nearby which share a property, tree species tend to group, human created objects like street light types or street paint markings tend to be of the same type at the same location.</p>
<p>With QField 1.6 it is now much easier to select a couple of features and change an attribute with very few taps. Identify a feature, long press an identify results, select more features and click the edit attributes button.</p>
<p><img alt="" src=""/></p>
<p><img alt="" src="/img/subscribers/qfield/qfield-1.6-is-out/selection_00-1.webp"/></p>
<h2 id="stylus-support">Stylus support</h2>
<p>Sometimes it is just too cold to be working with fingers (although of course you can get capacitive gloves too). Or you just prefer to be working with a pen. QField 1.6 comes with support for stylus pens. If your device ships with one, give it a try.</p>
<h2 id="lock-geometries">Lock geometries</h2>
<p>For some scenarios, especially in asset management, you only need to change attributes of existing objects and never add new features, delete features or change geometries. This can be configured through QFieldSync and set in the layer properties.</p>
<h2 id="image-name-configuration">Image name configuration</h2>
<p>Did you ever want to have the file names of your pictures to match the feature id, the layer name or any free text? The expression based configuration in QFieldSync offers now complete freedom in naming your images.</p>
<figure class="figure text-center mb-4"><img alt="" class="figure-img img-fluid gallery-img" height="253" src="/img/subscribers/qfield/qfield-1.6-is-out/blog_imagepath.webp" width="630"/></figure>
<h2 id="legend-and-ux-and-legacy-code">Legend and UX and legacy code</h2>
<p>Didn’t expect to read UX and legacy code in one single title?</p>
<p>QML is the technology on which the QField user interface is built. QML ships a lot of user interface elements in a library called “Quick Controls”. A long time ago already it received an update from version 1 to version 2. Up to recently we still have been using some elements from version 1, which had an effect on high resolution displays not being able to properly display everything. To workaround that we introduced a lot of band aids, to improve the situation. We are very happy, that by migrating the legend and few other remaining elements to Quick Controls 2 in version 1.6, we have been able to completely drop this code.</p>
<h2 id="topological-editing">Topological editing</h2>
<p>QGIS can detect shared boundary by the features, so you only have to move a common vertex once, and QGIS will take care of updating the neighboring ones. So does his little college QField since this release.</p>
<h2 id="fast-editing-mode">Fast editing mode</h2>
<p>For the real adventurers who know what they are doing this release brings the fast editing mode. In this mode, the features will automatically be stored on every change. The user interface is lighter and it combines perfectly with the topological editing.</p>
<h2 id="unter-the-hood">Unter the hood</h2>
<p>We have brought the whole technology stack up to speed with modern requirements. Proj and GDAL have been updated to recent versions. This helped to mitigate a couple of issues with coordinate transformations that were <a href="https://github.com/opengisch/QField/issues/1072#issue-642290346" rel="noopener" target="_blank">completely misplaced</a>. It also paves the path for a future with datum corrections and always more important high precision measurements.</p>
<h2 id="known-issues">Known Issues</h2>
<p>Unfortunately, we are experiencing a crash on startup with 32 bit devices. These devices are not that common any more, but if you have a device that is already a couple of years old it’s very well possible that it comes with a 32 bit cpu builtin. Despite the team’s hard efforts to isolate the reason, we were not able to find out what it was yet. Because of this we will not be able to update to 1.6 for these devices at the moment. We still hope that we will find a solution for this but don’t know yet when this will be.</p>
<p>We have updated <a href="https://proj.org/" rel="noopener" target="_blank">proj</a> to version 6. This brings plenty of bug fixes with coordinate handling. Among other things it adds support for using datum grids (gsb files) for very precise transformations, it is not yet possible to install those on the device. You will get an information message in the about dialog if your project happens to fall into this category. In this case, as a workaround switch the CRS of the project to a CRS with a known conversion that works without grid files.</p>
<h2 id="what-will-the-future-bring">What will the future bring</h2>
<p>You guessed it already, we are not tired and have plenty of things stacked for the future. Prepare for more exciting updates for attribute forms and also for <a href="https://qfield.cloud/" rel="noopener" target="_blank">QFieldCloud</a> which is right now being tested in our R&amp;D labs.</p>
<p>Also keep an eye on the <a href="https://twitter.com/qfieldforqgis" rel="noopener" target="_blank">@QFieldForQgis Twitter account</a> to stay updated.</p>
<h2 id="open-source">Open Source</h2>
<p>QField is an open source project. This means that whatever is produced is available free of charge. To anyone. Forever. This also means that everyone has the chance to contribute. You can write code, but you don’t need to. You can also help <a href="https://www.transifex.com/opengisch/qfield-for-qgis/dashboard/" rel="noopener" target="_blank">translating the app to your language</a> or help out <a href="https://github.com/opengisch/QField-docs" rel="noopener" target="_blank">writing documentation or case studies</a> or by sponsoring a new feature.</p>
<h2 id="thanks-to-sponsors">Thanks to sponsors</h2>
<p>Various organisations have helped to make this new release become a reality. Without the support of people in organisations who believe in the future of QField and open source tool for geospatial in general. The whole team behind QField would like to thank you with a big applause!</p>
