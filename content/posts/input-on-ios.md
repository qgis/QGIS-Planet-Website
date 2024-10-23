---
source: "blog"
title: "Input on iOS"
date: "2019-09-10T19:00:00-0500"
link: "https://lutraconsulting.co.uk/blog/2019/09/10/input-on-ios/"
draft: "false"
showcase: "planet"
subscribers: ["lutragis"]
author: "Lutra Consulting"
tags: []
---

<p>After a long wait and weeks of development, we finally managed to release <a href="https://merginmaps.com">Input</a> on iOS platform.</p>

<!-- more -->
<p><strong>Update</strong>:
Input app is now available through <a href="https://apps.apple.com/us/app/input/id1478603559?ls=1">Apple App Store</a>:</p>

<p><a href="https://apps.apple.com/us/app/input/id1478603559?ls=1"><img alt="Get it on App Store" src="https://www.lutraconsulting.co.uk/img/posts/App_Store.svg" style="padding-top: 12px;" width="138px" /></a></p>

<p><del>We are pleased to announce the Beta release of <a href="https://www.lutraconsulting.co.uk/blog/categories/qgis/merginmaps.com">Input</a> on iOS TestFlight. To install the app, simply click on <a href="https://testflight.apple.com/join/JO5EIywn">this link</a> from your iOS device: <strong>https://testflight.apple.com/join/JO5EIywn</strong>. This will open a window to first install TestFlight app. After that, you should be able to install Input on your device.</del></p>

<p><img alt="Input on iPhone" src="https://www.lutraconsulting.co.uk/img/posts/input_on_iphone.jpeg" /></p>

<p><a href="https://merginmaps.com">Input</a> is the first <a href="https://www.lutraconsulting.co.uk/blog/categories/qgis/www.qgis.org">QGIS</a> based app to be released for iOS. Using <a href="https://merginmaps.com">Input</a>, you can open, view and edit your QGIS projects and data on your iPhone/iPad.</p>

<p>For setting QGIS projects, transferring data/projects and capturing data, you can see the documentation <a href="https://github.com/lutraconsulting/input/blob/master/docs/users/introduction.md">here</a>.</p>

<p>In addition to the great works of the QGIS community in the past to port QGIS to Android devices, we had to do major changes to be able to have Input on iOS. Below are the steps we had taken in the past couple of years, to pave the way:</p>

<h2 id="qgis-quick">QGIS Quick</h2>
<p>As a first step, we decided to create a new library in QGIS based on <a href="https://en.wikipedia.org/wiki/Qt_Quick">Qt Quick</a> for QGIS. This allowed us to easily create platform independent apps for touch devices.</p>

<p>The library has been built on components ported from QField project. In addition, we have been improving the library and added support for new types of edit form widgets. Details of the QGIS Enhancement Proposal for QGIS Quick can be found <a href="https://github.com/qgis/QGIS-Enhancement-Proposals/issues/109">here</a>.</p>

<h2 id="static-data-providers">Static data providers</h2>
<p>By providing static data providers, it was possible to compile code of data providers directly into qgis_core library. This was a major step, as iOS does not support dynamic libraries. Details of this QGIS enhancement can be found <a href="https://github.com/qgis/QGIS-Enhancement-Proposals/issues/149">here</a>.</p>

<h2 id="feedback-and-suggestions">Feedback and suggestions</h2>
<p>We will be delighted to hear your suggestions and feedback, mainly critical ones so that we can improve the application and user experience. After ironing out any issues reported during the Beta testing in the TestFlight, we will publish the app to the App Store.</p>
