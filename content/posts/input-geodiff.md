---
source: "blog"
title: "Tracking, calculating and merging vector changes with Input and QGIS"
date: "2019-11-23T18:00:01-0600"
link: "https://lutraconsulting.co.uk/blog/2019/11/23/input-geodiff/"
draft: "false"
showcase: "planet"
subscribers: ["lutragis"]
author: "Lutra Consulting"
tags: []
---

<p>The latest beta release of Input (v.0.4.90) comes with smart diff support for vectors. This will allow you to use the app (current beta version) in a collaborative environment, where several users can make changes to a single survey layer (geopackage).</p>

<!-- more -->

<h2 id="what-does-it-mean">What does it mean?</h2>
<p>It is often the case, where multiple users need to make changes to a single vector layer. If you work in office, this issue is usually addressed by having a central geodatabase (e.g. Postgres/PostGIS). If you want extra information (e.g. audit trails, versioning, latest changes, etc), you can modify your database, to keep track of it.</p>

<p>The problem arises when you want to collect data, without having access to the central geodatabase. You can do some manual work to handle this scenario, but it can easily lead into data management nightmare.</p>

<p>To simplify the workflow, we have developed <a href="https://github.com/lutraconsulting/geodiff">Geodiff</a>, a multi-platform library to keep track of changes, calculate the differences, merge and consolidate the differences.</p>

<h2 id="how-can-i-use-it">How can I use it?</h2>
<p><a href="https://github.com/lutraconsulting/geodiff">Geodiff</a> has been integrated into the beta version of <a href="https://merginmaps.com">Input</a>. This will allow you to share a project with your team and edit a single layer (geopackage format) all at the same time, even when you are offline.</p>

<p>To start with, you need to create a project and upload it to <a href="https://merginmaps.com/">Mergin</a>. You can then share the project (with write access) with your colleagues:</p>

<p><img alt="Sharing projects through Mergin" src="https://www.lutraconsulting.co.uk/img/posts/mergin_project_sharing.png" /></p>

<p>The project contains a survey layer (trees.gpkg). There is only one feature present within the layer:</p>

<p><img alt="Sharing projects through Mergin" src="https://www.lutraconsulting.co.uk/img/posts/survey-project-qgis.png" /></p>

<p>The project is shared with two users. Both users download the project and take their devices to the field:</p>

<p>User 1, carried out a survey (using iPhone!), by adding a tree and editing the attribute table of the existing one. The changes were synchronised back through the <a href="https://merginmaps.com/">Mergin</a>:</p>

<center>
  
</center>

<p>Meanwhile, User 2 added a new feature to the survey layer. Once User 2 tries to synchronise the changes, Input automatically detects the changes not only made through User 2, but also the ones uploaded to the <a href="https://merginmaps.com/">Mergin</a>. The layer will be patched both locally and on the server to take all the changes into account:</p>

<center>
  
</center>

<p>The data administrator can now pull all the changes from both users in QGIS:</p>

<center>
  
</center>

<p>You can also see the history of changes to the project and the survey layer on the Mergin website. Below shows the changes from different users:</p>

<p><img alt="Sharing projects through Mergin" src="https://www.lutraconsulting.co.uk/img/posts/mergin_project_history.png" /></p>

<p>To see changes from each user, you can click on the version and it lists the changes. In this example, User 1 (jack) added a new feature and modified an existing feature:</p>

<p><img alt="Sharing projects through Mergin" src="https://www.lutraconsulting.co.uk/img/posts/mergin_project_history_extended.png" /></p>

<p>You can also see the extended history and see where the changes have been made:</p>

<p><img alt="Sharing projects through Mergin" src="https://www.lutraconsulting.co.uk/img/posts/mergin_project_history_advanced.png" /></p>

<h2 id="how-can-i-test-this-new-feature">How can I test this new feature?</h2>

<p>You can use Beta version of Input app in Android or TestFlight in iOS:</p>

<center>
<a href="https://play.google.com/apps/testing/uk.co.lutraconsulting"><img alt="Get it on Google Play" src="https://play.google.com/intl/en_us/badges/images/generic/en_badge_web_generic.png" width="170" />
</a> <a href="https://testflight.apple.com/join/JO5EIywn"><img alt="Get it on App Store" src="https://www.lutraconsulting.co.uk/img/posts/App_Store.svg" style="padding-top: 1px;" width="145px" /></a>
</center>

<p>For any issues or feedback, please file a ticket on <a href="https://github.com/lutraconsulting/input/issues">Input repository</a></p>
