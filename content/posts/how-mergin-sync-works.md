---
source: "blog"
title: "How Mergin/Input sync changes in your QGIS projects"
date: "2021-05-11T00:00:00-0500"
link: "https://lutraconsulting.co.uk/blog/2021/05/11/how-mergin-sync-works/"
draft: "false"
showcase: "planet"
subscribers: ["lutragis"]
author: "Lutra Consulting"
tags: []
---

<p>People often ask whether <a href="http://merginmaps.com/">the Mergin service</a> and the <a href="https://merginmaps.com">Input app</a> can deal with multiple team members doing edits at the same time.</p>

<!-- more -->

<p>They happily find out that the answer is yes - it is one of the core features that greatly simplifies life of our users. In this post we will shed some light on how things work behind the scenes.</p>

<p align="center">
  <img alt="Mergin promo" src="https://www.lutraconsulting.co.uk/img/Products_10.jpg" />
</p>

<h2 id="getting-started">Getting started</h2>

<p>Let’s think of a simple project directory that needs to be synchronised between multiple desktop or mobile users, containing just two files:</p>

<ul>
  <li>a QGIS project file <code class="highlighter-rouge">my-project.qgz</code> that sets up map layers, styling, …</li>
  <li>a GeoPackage file <code class="highlighter-rouge">my-data.gpkg</code> containing all GIS data</li>
</ul>

<p>Our sample GIS data will contain a tree survey table, containing location, species and age of various trees:</p>

<p align="center">
  <img alt="tree survey table" src="https://www.lutraconsulting.co.uk/img/posts/tree_survey_table.png" />
</p>

<p>When users edit data in <code class="highlighter-rouge">my-data.gpkg</code>, the traditional cloud storage solutions (such as Dropbox, Google Drive, Microsoft OneDrive and others) simply copy the modified files there. They do not understand the file content though - so if two people modify the same file, they have no way of knowing how to merge changes together. In the worse case, when two versions of the same file are uploaded, they keep just the version which was synchronised last. Or slightly better, they resort to creation of conflicting copies which need to be manually merged later. As one can imagine, merging and consolidating modifications from multiple GeoPackages back to one copy is a slow, tedious and error-prone job.</p>

<p><a href="http://merginmaps.com/">the Mergin service</a> has been designed to understand spatial data, especially GeoPackages that are becoming the most popular format to store vector &amp; attribute data. This is thanks to the open source <a href="https://github.com/lutraconsulting/geodiff">geodiff library</a> that we have developed while working on Mergin.</p>

<h2 id="synchronising-data-using-diffs">Synchronising data using “diffs”</h2>

<p>The first trick is that synchronisation of GeoPackage files between Mergin server and clients (Input app, QGIS or other apps) only transfers actual changes in tables (“diffs” in technical jargon).</p>

<p>Our Mergin project with the tree survey has been prepared and downloaded by users. Jack did a field survey and he added or updated some rows in the survey table (changes highlighted in yellow and green):</p>

<p align="center">
  <img alt="Jack table" src="https://www.lutraconsulting.co.uk/img/posts/tree_survey_changes_jack.png" />
</p>

<p>After pressing sync button, his changes are detected and uploaded to Mergin, encoded as a list of changes to the survey table:</p>

<p align="center">
  <img alt="Jack diff" src="https://www.lutraconsulting.co.uk/img/posts/tree_jack_diff.png" />
</p>

<p>Another user, Jill, also downloaded the tree survey project to her mobile device prior to Jack’s changes. When Jill synchronises the project to get the latest version, the changes as uploaded by Jack are downloaded and applied to her local copy of the project, getting the same data as seen by Jack.</p>

<p>At this point, the advantage of uploading/download only changes in tables may not seem obvious besides saving some network bandwidth… Read on to learn how this is used to support multi-user editing.</p>

<h2 id="merging-changes-from-multiple-users">Merging changes from multiple users</h2>

<p>So far we have expected that Jill does not have any pending changes to sync, so that was easy. Now let’s assume that Jill has also done some changes on her device:</p>

<p align="center">
  <img alt="Jill table" src="https://www.lutraconsulting.co.uk/img/posts/tree_survey_changes_jill.png" />
</p>

<p>Here comes the more tricky part - how do we merge changes from Jack and Jill back to a single table:</p>

<p align="center">
  <img alt="Merging Jack and Jill table" src="https://www.lutraconsulting.co.uk/img/posts/tree_survey_changes_jack_jill.png" />
</p>

<p>In Mergin, cases that require merging changes from multiple users are handled by the “rebase” operation, a concept we have borrowed from version control systems for source code.</p>

<p>Let’s assume that Jack has synchronised his changes first. Later, when Jill synchronises her changes, a couple of things happen on her device before uploading the changes: Jill’s changes will be temporarily undone, Jack’s changes get applied, and finally Jill’s changes are re-applied after being rebased on top of Jack’s changes.</p>

<p>What does it mean to rebase someone’s changes? There are a couple of possible edit conflicts that could happen between rows of a database table with matching IDs (insert/insert, update/delete, delete/delete, update/update). These edit conflicts need to be resolved in order to be able to merge changes from multiple users.</p>

<p>In our example, both Jack and Jill have added a row with ID = 4. This is not allowed, and therefore Jill’s new row ID will get changed to ID = 5 (any unused ID would do). As a result, here’s how the merged table will look at the end - combining changes of both users:</p>

<p align="center">
  <img alt="Final table" src="https://www.lutraconsulting.co.uk/img/posts/tree_surve_final_table.png" />
</p>

<p>If both Jack and Jill modified the same row (the update/update edit conflict), we can only accept one edit automatically. The conflicting edit of the other user is written to a special conflict file and uploaded to Mergin, so no data gets lost, and the conflict can be later inspected by the project admin. Fortunately, this kind of conflict does not happen often if the survey work is well planned to avoid users simultaneously modifying the same features within the GeoPackage data.</p>

<h2 id="what-if-conflict-files-appear">What if conflict files appear</h2>

<p>There are some cases when automatic merging is not supported. In those cases, Mergin is unable to find out details about changes in the data file(s) and has to resort to creation of a conflicting copy which gets uploaded to Mergin project along the original data file(s). In particular the problems may appear when:</p>

<ul>
  <li>Other format than GeoPackage is used for data storage (e.g. shapefiles)</li>
  <li>Database or table structure is changed (e.g. adding new columns or new tables)</li>
</ul>

<p>In the future, these limitation may be removed, but at this point it is good to keep them in mind.</p>

<p>If you plan to change structure of the survey tables and the project is already being used on multiple devices, it may be a good idea to create a new Mergin project with the modified database structure and instruct users to switch to the new project. Otherwise conflict files may start popping up as long as some users have older version of the project, adding more manual work to collate data.</p>

    <div class="input-promo">
    <h2>You may also like...</h2>
    <a href="https://merginmaps.com">Mergin Maps, a field data collection app based on QGIS</a>. Mergin Maps makes field work easy with its simple interface and cloud-based sync. Available on Android, iOS and Windows.
    <img alt="Screenshots of the Mergin Maps mobile app for Field Data Collection" src="https://lutraconsulting.co.uk/img/posts/input_app_for_field_data_collection.jpg" /><br />
    <a href="https://play.google.com/store/apps/details?id=uk.co.lutraconsulting&amp;utm_source=lutra-atom&amp;utm_medium=lutra-blog-footer&amp;utm_campaign=input">
      <img alt="Get it on Google Play" src="https://play.google.com/intl/en_us/badges/images/generic/en_badge_web_generic.png" width="180px" />
    </a>
    <a href="https://apps.apple.com/us/app/input/id1478603559?ls=1&amp;utm_source=lutra-atom&amp;utm_medium=lutra-blog-footer&amp;utm_campaign=input">
      <img alt="Get it on Apple store" src="https://www.lutraconsulting.co.uk/img/posts/App_Store.svg" style="padding-top: 0px;" width="144px" />
    </a>
  </div>
