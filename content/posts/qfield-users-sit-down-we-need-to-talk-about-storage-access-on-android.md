---
source: "blog"
title: "QField Users Sit Down, We Need to Talk About Storage Access on Android"
date: "2022-03-05T00:48:44+0000"
link: "https://qfield.org/blog/2022/03/05/qfield-users-sit-down-we-need-to-talk-about-storage-access-on-android/"
draft: "false"
showcase: "planet"
subscribers: ["qfield"]
author: "QField"
tags: ["qfield", "qgis.org"]
languages: ["en_gb"]
available_languages: ["en_gb"]
---

<blockquote>
<p><em>TLDR: Since November 2021, Google has enforced new storage access limitations for apps published on its Play store which prohibits direct storage access on Android 11 and above forcing QField to adapt and rely on importing projects and datasets to access those.</em></p></blockquote>
<p>If you are a QField beta user on Android 11 and above, you might have noticed a significant change in the way the app is handling storage in the latest set of betas released in early February of 2022. This blog post will go over the changes, explain why those <strong>had to be made</strong> (looking at you, Google), how to work in this new paradigm, and showcase some new benefits from the hard work done by OPENGIS.ch’s geoninjas.</p>
<h2 id="its-all-gone-how-can-i-access-my-projects-and-datasets"><strong>It’s all gone! How can I access my projects and datasets?!</strong></h2>
<p>Starting with Android 11, apps are denied full access to main and external storage content. For QField, this means direct access to projects and datasets transferred and/or downloaded into storage folders is not possible anymore.</p>
<p>To work within this new confine, QField now has to import project folders or individual datasets into an app-dedicated storage location where Android allows for unrestricted read/write access.</p>
<p>Practically, this means that instead of being shown and having access to the full storage tree when clicking on the “Open local files” button, users are now shown a set of new folders named ‘QField files directory’, ‘Imported datasets’, and ‘Imported projects’ as well as a drop-down menu accessible via a top-right three-dot button.</p>
<figure class="figure text-center mb-4"><img alt="" class="figure-img img-fluid gallery-img" src="/img/subscribers/qfield/qfield-users-sit-down-we-need-to-talk-about-storage-access-on-android/unknown/image_aXJ5dpFU.webp"/></figure>
<h3 id="import-project-from-folder"><em>Import project from folder</em></h3>
<p>When importing a project from a folder, users will be asked to grant permission for QField to read the content of a given folder on the device’s storage via a system folder picker. When the folder is selected, QField copies the folder content (including its sub-folders) into the app’s ‘Imported projects’ location. Users can then open the project from there.</p>
<p>Re-importing a given folder through the drop-down menu action will overwrite preexisting projects given an identical folder name. That allows users to be able to update projects.</p>
<p><em>Note that feature editing, addition, and deletion will be saved into the imported project’s datasets, not in the original folder selected during the import process. More on how to find and handle those project datasets will come later in this post.</em></p>
<h3 id="import-project-from-zip-archive"><em>Import project from ZIP archive</em></h3>
<p>Having to adapt to Google’s new set of rules did not come without its benefits. Users can now easily transfer projects into a given device by compressing the project content into a ZIP archive and having QField import that compressed project automatically. This can greatly ease remote deployment of projects by being able to send a single file to users.</p>
<h3 id="import-datasets"><em>Import dataset(s)</em></h3>
<p>QField can also import individual dataset(s). Users will be asked to select one or more files via a system file picker, which will be copied into the ‘Imported datasets’ folder. Users will have to ensure that all sidecar files are selected when importing (e.g. a shapefile dataset would require users to select the .shp, .shx, .dbf, .prj, and .cpg files).</p>
<p><em>Just like imported projects, editing of datasets will be saved into the imported datasets, and not reflected in the original files.</em></p>
<h2 id="alright-but-how-can-i-retrieve-modified-projects-and-datasets"><strong>Alright, but how can I retrieve modified projects and datasets?</strong></h2>
<p>Imported projects and datasets can be accessed directly using a USB cable. The location on storage is displayed in the top navigation bar when opening a local file.</p>
<p>On most devices plugged into a computer via USB cable connection, the path will be :/Android/data/ch.opengis.qfield/files/ where you will find both the Imported Datasets and Imported Projects folders within which your edited content will be located.</p>
<p>However, we’ve also added a nice new ‘Send to…’ functionality that allows for users to share and send datasets straight from QField using Android APIs. This allows for the sending of edited datasets directly to third party apps (Gmail, Drive, Dropbox, Nextcloud, your favourite messenger app, etc.).</p>
<figure class="figure text-center mb-4"><img alt="" class="figure-img img-fluid gallery-img" src="/img/subscribers/qfield/qfield-users-sit-down-we-need-to-talk-about-storage-access-on-android/unknown/image_XbWRvzEm.webp"/></figure>
<h3 id="is-direct-copying-via-usb-cable-gone-altogether"><strong>Is direct copying via USB cable gone altogether?</strong></h3>
<p>Users can still avoid going through the import process by copying files via a USB cable connection directly into the QField app’s files directory. As mentioned above, the location on most devices will be :/Android/data/ch.opengis.qfield/files/.</p>
<h2 id="what-are-the-benefits-from-these-changes"><strong>What are the benefits from these changes?</strong></h2>
<p>Working out a functional solution to meet Google’s newly-enforced restrictions did not come without its benefits.</p>
<p>On top of what was already covered above - importing of compressed project ZIP files and sharing functionalities – QField is now fully integrated with Android’s cross-application document sharing APIs. This means that users can now directly open projects and files sent to them via their favourite browser/email/cloud/messenger app without the need to first download those files onto the device.</p>
<p>Altogether, the newly-coded importing mechanisms and integration with Android document APIs don’t only improve the ease of use for the average person, it also makes viewing and editing spatial datasets on QField far more secure. The imported projects and datasets reside in a location with access limited to QField only, meaning that its content is inherently far more protected from malicious access from third-party apps.</p>
<h2 id="why-were-these-drastic-changes-needed"><strong>Why were these drastic changes needed?</strong></h2>
<p>As mentioned in the introduction, the changes were needed to comply with a set of new Google Play policies that came into force in November 2021. Users can read more on Google’s rationale on this page <a href="https://developer.android.com/google/play/requirements/target-sdk" rel="noopener" target="_blank">https://developer.android.com/google/play/requirements/target-sdk</a>.</p>
<p>As part of the enforcement of these new policies, Google came up with an arbitrary mechanism to whitelist some apps which allows those to retain full storage access given the user explicitly allowed for it. We here at OPENGIS.ch believes QField had ample justifications to be whitelisted, however, Google’s appeal process judged otherwise after a series of email exchanges detailing our reasoning. While we have so far lost this argument with Google, we will continue fighting for our users and for their freedom to choose. If by any chance you have a good contact at Google that might be willing to listen to our reasoning, we would be grateful if you’d <a href="https://opengis.ch/#contact" rel="noopener" target="_blank">get in touch with us</a>.</p>
<p>We hope this clarifies the recent changes and helps QField users adapt to those.</p>
