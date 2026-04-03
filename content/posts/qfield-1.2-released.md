---
source: "blog"
title: "QField 1.2 released"
date: "2019-10-03T05:29:45+0000"
link: "https://qfield.org/blog/2019/10/03/qfield-1.2-released/"
draft: "false"
showcase: "planet"
subscribers: ["qfield"]
author: "QField"
tags: ["gis", "qfield", "highlights", "qgis.org"]
languages: ["en_gb"]
available_languages: ["en_gb"]
---

<p>After an intensive testing period, we are proud to announce the release of <strong>QField 1.2</strong></p>
<p>As usual, <a href="https://play.google.com/store/apps/details?id=ch.opengis.qfield" rel="noopener" target="_blank">get it on play store</a> or <a href="https://github.com/opengisch/QField/releases/tag/v1.2.0" rel="noopener" target="_blank">download it from GitHub.</a></p>
<h2 id="qfield-crowdfunding-campaign">QField Crowdfunding Campaign</h2>
<p>Before digging into all the new goodness that you will find in QField 1.2, let’s get some big “Thanks” out. What QField currently is was mostly possible <strong>thanks to customer projects</strong> of which the outcome could be mutualized. Thanks a lot to all of you that agreed open source is all about making things possible together!</p>
<p>Over the years at OPENGIS.ch we have also <strong>donated an unimaginable amount of hours</strong> to make QField the project you have grown to love and this makes us very proud!</p>
<p>To keep the momentum we now rely on all QField users to help us move one step further. Therefore we created a <strong>crowdfunding campaign for improved camera support</strong>. As well as another round of <strong>general polishing and bug-fixing</strong>.</p>
<p>If you like QField, now is the time to show some love and <strong><a href="https://opengis.ch/qfield-love/" rel="noopener" target="_blank">support our crowdfunding campaign</a></strong>.</p>
<h2 id="new-features">New features</h2>
<p>This new release comes with exciting new features and also contains some first usability enhancements. More of that later.</p>
<h3 id="value-relation-widget">Value relation widget</h3>
<figure class="figure text-center mb-4"><img alt="" class="figure-img img-fluid gallery-img" height="397" src="/img/subscribers/qfield/qfield-1.2-released/value-relation.gif" width="639"/></figure>
<p>If you need to choose the type of a material of the manhole you are inspecting or to select the owner of the parcel which you are drawing, that’s when you want a <strong>combo box with available values</strong>. This has been possible in QField for a long time, but was hard to set up. Since this release it’s much easier thanks to the integration of value relation widgets.</p>
<p>Not only do they make configuration easier, they also allow for a completely new functionality: managing <strong>multiple selections</strong>. This will offer a checkbox for every possible value from the list and you are free to save any combination of values.</p>
<h3 id="authentication-dialog-for-protected-services">Authentication dialog for protected services</h3>
<figure class="figure text-center mb-4"><img alt="" class="figure-img img-fluid gallery-img" height="375" src="/img/subscribers/qfield/qfield-1.2-released/login.gif" width="601"/></figure>
<p>Just as well as we love open source, we love open data. But not all data are meant for public and some deserve protection. Even more you don’t want to allow everyone to edit your data.</p>
<p>QField will now <strong>show an authentication dialog</strong>, whenever one of your <strong>WMS, WFS, WFS-T or Postgres layers</strong> requires a login.</p>
<h3 id="improved-snapping-support-in-expressions">Improved snapping support in expressions</h3>
<p>One of the main reasons for <strong>QField’s incredible versatility</strong> is the <strong>use of</strong> <a href="https://docs.qgis.org/2.8/en/docs/user_manual/working_with_vector/expression.html" rel="noopener" target="_blank"><strong>expressions</strong></a> everywhere. We have just added yet another piece to that: when you snap to a feature, <strong>all the snapping details</strong> <strong>are available for your new feature</strong>. With this in place, if you add a new signpost on a street, you can fill in the <code>street_id</code> attribute automatically.</p>
<p>As a nice little extra, the Z (and M) values of snapping results are automatically applied to the new vertices and points.</p>
<h2 id="usability-enhancements-and-bugfixes">Usability enhancements and Bugfixes</h2>
<p>We also started to improve on the usability of the user interface. We are working on this with a usability expert to get the user interface to be even more appealing and user-friendly.</p>
<p>This is just the start, stay tuned for <strong>more usability improvements</strong> which are inbound.</p>
<p>As usual, a number of additional bugs have also been corrected, most notably the checkbox widget is now behaving as expected.</p>
<h2 id="latest-qt-513-and-arm64-v8a-support">Latest Qt 5.13 and Arm64-v8a support</h2>
<p>According to Google guidelines, we added support for the Arm64-v8a architecture and while we were at it, we also migrated to the shiny new Qt 5.13 and it’s next-gen menu system.</p>
<p>For this release, we did not upload any x86 packages to the play store since it would have forced us to also have to upload an x86_64 package. If you need the x86 package, you can find it on <a href="https://github.com/opengisch/QField/releases/download/v1.2.0/qfield-v1.2.0-x86.apk" rel="noopener" target="_blank">Github</a>. Obviously, in future releases we’ll add those to the play store as well.</p>
