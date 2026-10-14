---
source: "blog"
title: "Meet the QGIS Hub — sharing is caring!"
date: "2026-10-13T16:35:20+0000"
link: "https://anitagraser.com/2026/10/13/meet-the-qgis-hub-sharing-is-caring/"
draft: "false"
showcase: "planet"
subscribers: ["anita_graser"]
author: "Anita Graser"
tags: ["gis", "qgis", "cartography"]
languages: ["en_gb"]
available_languages: ["en_gb"]
---

<p class="wp-block-paragraph">Everyone knows the QGIS Plugin Repo but have you had a look at the <a href="https://hub.qgis.org">QGIS Hub</a> yet? </p>
<figure class="wp-block-image size-large"><a href="https://hub.qgis.org"><img alt="" class="wp-image-9857" height="503" src="/img/subscribers/anita_graser/meet-the-qgis-hub-sharing-is-caring/image.webp" width="1024"/></a></figure>
<p class="wp-block-paragraph">It’s similar to the plugin repository in that it allows sharing of resources between community members, but it so many different types of resources, that warrants multiple blog posts: from styles and projects all the way to processing scripts.</p>
<figure class="wp-block-image size-large"><img alt="" class="wp-image-9860" height="388" src="/img/subscribers/anita_graser/meet-the-qgis-hub-sharing-is-caring/image-1.webp" width="488"/></figure>
<p class="wp-block-paragraph">Today, I want to have a look at the (a little cryptic) <a href="https://hub.qgis.org/layerdefinitions/?sort=upload_date&amp;order=desc">QLR option</a>.</p>
<blockquote class="wp-block-quote is-layout-flow wp-block-quote-is-layout-flow">
<p class="wp-block-paragraph">The QGIS Layer Definition (QLR) format makes it possible to share “complete” QGIS layers with other QGIS users. QLR files contain links to the data sources and all the QGIS style information necessary to style the layer.</p>
</blockquote>
<figure class="wp-block-image size-large"><a href="https://hub.qgis.org/layerdefinitions/?sort=upload_date&amp;order=desc"><img alt="" class="wp-image-9864" height="425" src="/img/subscribers/anita_graser/meet-the-qgis-hub-sharing-is-caring/image-2.webp" width="1024"/></a></figure>
<p class="wp-block-paragraph">To test the features, I uploaded QLRs for the two <a href="https://anitagraser.com/2026/07/26/new-open-basemaps-for-austria/">BEV basemap COGs I first wrote about a few weeks ago</a>.</p>
<figure class="wp-block-image size-large"><a href="https://hub.qgis.org/layerdefinitions/?sort=upload_date&amp;order=desc"><img alt="" class="wp-image-9866" height="951" src="/img/subscribers/anita_graser/meet-the-qgis-hub-sharing-is-caring/image-3.webp" width="798"/></a></figure>
<p class="wp-block-paragraph">The cool thing about sharing the COGs like this is that: 1. users don’t have to mess with the COG URLs and 2. the QLR stores styling information such as the recommended raster resampling settings which were previously only available in the dataset documentation.</p>
<p class="wp-block-paragraph">To use the resources from the hub in QGIS, you’ll want to install the QGIS Hub plugin:</p>
<figure class="wp-block-image size-large"><a href="https://anitagraser.com/wp-content/uploads/2026/10/image-4.png"><img alt="" class="wp-image-9869" height="242" src="/img/subscribers/anita_graser/meet-the-qgis-hub-sharing-is-caring/image-4.webp" width="788"/></a></figure>
<p class="wp-block-paragraph">Once installed, this plugin will show you all the resources published on the hub:</p>
<figure class="wp-block-image size-large"><a href="https://anitagraser.com/wp-content/uploads/2026/10/image-6.png"><img alt="" class="wp-image-9872" height="699" src="/img/subscribers/anita_graser/meet-the-qgis-hub-sharing-is-caring/image-6.webp" width="1024"/></a></figure>
<p class="wp-block-paragraph">As you can see, we are only just starting out and there are not many QLRs uploaded yet. </p>
<p class="wp-block-paragraph">So I’d like to encourage you join our efforts and share, for example, your national basemap layer definition files with the QGIS community.</p>
<p class="wp-block-paragraph">It’s never been so easy. </p>
<p class="wp-block-paragraph">To create a QLR, just right-click a layer in QGIS and go to Export | Save as Layer Definition File.</p>
<p class="wp-block-paragraph">To share a QLR, head to <a href="https://hub.qgis.org">hub.qgis.org</a>, log in, and upload. </p>
<p class="wp-block-paragraph">And there is good news regarding logins: besides the good old OSGeo account, you can now use third party accounts from Github or Google (I think more options are to come) to log into the hub:</p>
<figure class="wp-block-image size-large"><a href="https://hub.qgis.org/accounts/login/"><img alt="" class="wp-image-9874" height="735" src="/img/subscribers/anita_graser/meet-the-qgis-hub-sharing-is-caring/image-7.webp" width="624"/></a></figure>
<p class="wp-block-paragraph">Big thanks to the QGIS infrastructure team who have been working on this feature during the <a href="https://blog.qgis.org/2026/10/13/qgis-user-conference-2026-brings-open-source-to-new-heights-in-the-swiss-alps/">contributor meeting</a> last week!</p>
