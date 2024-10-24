---
source: "blog"
title: "Input version 1.0 release"
date: "2021-10-06T04:00:00-0500"
link: "https://lutraconsulting.co.uk/blog/2021/10/06/input-v1-release/"
draft: "false"
showcase: "planet"
subscribers: ["lutragis"]
author: "Lutra Consulting"
tags: []
---

<p><a href="https://merginmaps.com">Input app</a> has reached a new milestone. Earlier in September, we have released version 1.0 of the app with many new features and enhancements.</p>

<!-- more -->

<h2 id="make-syncs-faster">Make syncs faster</h2>
<p>When you work in a team with several collaborators adding data and photos to the project, the size of the project can get really big. Every time you try to sync your changes, photos from all users will be transferred to your phone. This can take a long while when there are several hundreds of photos collected by other collaborators.</p>

<p>Image below illustrates the difference between having selective sync or the default behaviour (selective sync is disabled):</p>

<center>
<img alt="With and without sync" src="https://lutraconsulting.co.uk/img/posts/selective-sync.png" title="GSOC &amp; OSGeo" width="412" />
</center>

<p>The configuration file for enabling the selective sync is stored in <code class="highlighter-rouge">mergin-config.json</code> which should be placed in the root of your folder. By opening the file in a text editor and adding the following option, the sync will be enabled for photos within your project root folder:</p>

<p><code class="highlighter-rouge">{
  "input-selective-sync": true
}</code></p>

<p>Currently, the editing of the file is manual and through the text editor, but we plan to incorporate it within the Mergin plugin for QGIS.</p>

<p>To learn more about how to set up selective sync for your project, you can see the <a href="https://merginmaps.com/projects/documentation/selective-sync">example project</a>. Read more on our <a href="https://merginmaps.com/docs/howto/project/selective_sync">help pages</a> for extra configuration options.</p>

<h2 id="one-too-many">One too many!</h2>
<p>It is often the case that you have a set of spatial features and you want to record some parameters every now and then. For example, there is a GIS layer representing the manholes and the surveyors carry out regular inspections of the manholes. Instead of duplicating the manhole layer and recording each inspection, you can create a non-spatial table and store each inspection as a new line.</p>

<center>
<img alt="1-N relations in Input" src="https://lutraconsulting.co.uk/img/posts/input_forms_one-to-many.png" title="GSOC &amp; OSGeo" width="300" />
</center>

<p>Another use-case for such a feature is that you’d like to attach multiple photos to a single feature.</p>

<center>
<img alt="Many photos to a single feature" src="https://lutraconsulting.co.uk/img/posts/input_forms_many-photos.png" title="GSOC &amp; OSGeo" width="300" />
</center>

<p>To learn more about how to configure these types of projects in QGIS you can see the example projects (<a href="https://merginmaps.com/projects/documentation/forms_one-to-many-relations">manhole example</a> and <a href="https://merginmaps.com/projects/documentation/forms_multiple_photos">multiple photos example</a>). The <a href="https://merginmaps.com/docs/howto/project/settingup_forms">documentation pages</a> describes the logic and process in QGIS in more details.</p>

<h2 id="accuracy-metadata">Accuracy metadata</h2>

<p>In addition to the display of the accuracy bubble in the app, we have recently added a whole set of new variables to capture the GPS accuracy, e.g. horizontal and vertical accuracy, ground speed and many more. See the <a href="https://merginmaps.com/docs/howto/position_variables">help pages</a> to find out how you can set up those variable within your form. Alternatively, you can clone the <a href="https://merginmaps.com/projects/input-testing/tc05_position_variables">example project</a> on Mergin website.</p>

<p>In addition to capturing GPS metadata, this feature can be used for geo-fencing: for example, you can only allow users to edit/capture data when they are physically (i.e. their GPS location) within a certain area:</p>

<center>
<blockquote class="twitter-tweet"><p dir="ltr" lang="en">An exciting new feature in the upcoming release of <a href="https://t.co/KXCwKEzzE3">https://t.co/KXCwKEzzE3</a>: capturing GPS accuracy, speed, position, etc. With this new feature, combined with <a href="https://twitter.com/hashtag/QGIS?src=hash&amp;ref_src=twsrc%5Etfw">#QGIS</a>, you can set geofencing rules. <a href="https://t.co/zoKsrI29bc">pic.twitter.com/zoKsrI29bc</a></p>&mdash; Lutra Consulting (@lutraconsulting) <a href="https://twitter.com/lutraconsulting/status/1388030561298665472?ref_src=twsrc%5Etfw">April 30, 2021</a></blockquote> 
</center>

<h2 id="join-our-community">Join our community</h2>

<p>If you have any questions, would like to interact with the rest of community or want to give us your feedback, you can <a href="https://merginmaps.com/community/join">join the Slack community channel</a>.</p>

<p>If you would like to add a new feature  or have suggestions to improve the app, do not hesitate to contact us on info@lutraconsulting.co.uk</p>
