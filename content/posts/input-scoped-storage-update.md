---
source: "blog"
title: "Scoped storage in Input for Android"
date: "2021-10-26T04:00:00-0500"
link: "https://lutraconsulting.co.uk/blog/2021/10/26/input-scoped-storage-update/"
draft: "false"
showcase: "planet"
subscribers: ["lutragis"]
author: "Lutra Consulting"
tags: []
---

<p>Android has forced app to use <a href="https://developer.android.com/training/data-storage#scoped-storage">Scoped Storage</a> for all app related data. If you are using Input app on Android please read carefully for the upcoming update (1.1) of the app in the Google Play Store.</p>

<!-- more -->

<h2 id="what-is-scoped-storage">What is Scoped Storage?</h2>
<p>In summary, apps need to use a specific part of folders on Android devices to store app related data.</p>

<p>Currently, Input stores your QGIS project and some other settings (e.g. grid shift projection) on <code class="highlighter-rouge">/Internal storage/INPUT</code>. With the new Android requirements, the app related data should be stored on <code class="highlighter-rouge">/Internal storage/Android/data/uk.co.lutraconsulting</code>.</p>

<h2 id="update-process">Update process</h2>
<p>For the 1.1 release of Input on Android, there will be an extra process. This process will be a on-off action. When you launch the app after the upgrade, it will copy the data from <code class="highlighter-rouge">/Internal storage/INPUT</code> to <code class="highlighter-rouge">/Internal storage/Android/data/uk.co.lutraconsulting</code>. Depending on the size of your projects, this can take a couple of minutes. During the process you will see a screen similar to this one:</p>

<center>
<img alt="Input project migration" src="https://lutraconsulting.co.uk/img/posts/input-scoped-storage-migration.png" title="Input project migration" width="360" />
</center>

<h2 id="best-practices">Best practices</h2>
<p>The upgrade and copy process should work smoothly. But we suggest to take the following actions to ensure you will not lose any data during the process:</p>

<ul>
  <li>
    <p>Sync all you changes: before upgrading the app, open Input and sync all your local changes to Mergin.</p>
  </li>
  <li>
    <p>Storage space: if you work with several projects and large volume of data, make sure you have enough storage. The process will make a copy of your existing <code class="highlighter-rouge">/Internal storage/INPUT</code> without deleting it. So, you need at least the size of <code class="highlighter-rouge">/Internal storage/INPUT</code> storage available.</p>
  </li>
</ul>

<h2 id="troubleshooting">Troubleshooting</h2>
<p>In case you have encountered any issues, you can take the following steps to fix the problem manually:</p>

<ul>
  <li>Lack of storage space:
    <ul>
      <li><a href="https://merginmaps.com/docs/howto/data_sync">Transfer the data through USB cable to your PC</a>.</li>
      <li>Make a back up of data on your PC.</li>
      <li>Delete <code class="highlighter-rouge">/Internal storage/INPUT</code> on your Android phone/tablet</li>
      <li>Transfer the data from PC through USB to <code class="highlighter-rouge">/Internal storage/Android/data/uk.co.lutraconsulting</code></li>
    </ul>

    <center>
<img alt="Input project migration - storage warning" src="https://lutraconsulting.co.uk/img/posts/input-scoped-storage-space-warning.jpeg" title="Input project migration" width="321" />
</center>
  </li>
  <li>
    <p>Missing data: the migration process does not delete <code class="highlighter-rouge">/Internal storage/INPUT</code> folder. It will rename it <code class="highlighter-rouge">/Internal storage/INPUT_migrated</code>. Similar to step above, you can copy the data to the PC and move them to <code class="highlighter-rouge">/Internal storage/Android/data/uk.co.lutraconsulting</code>. Alternatively, you can use a file browser app on your device to copy files around.</p>
  </li>
  <li>If you use Input app on a shared device, the migration process will transfer all the project data from <code class="highlighter-rouge">/Internal storage/INPUT</code> and marks the folder as <code class="highlighter-rouge">/Internal storage/INPUT_migrated</code>. Therefore, when the next user starts up the app, no data will be present. To fix the issue, you need to manually move the data from <code class="highlighter-rouge">/Internal storage/INPUT_migrated</code> to <code class="highlighter-rouge">/Internal storage/Android/data/uk.co.lutraconsulting</code> (as described above) for the other users on the device.</li>
</ul>

<center>
<img alt="Input project migration problem" src="https://lutraconsulting.co.uk/img/posts/input-scoped-storage-problem.jpeg" title="Input project migration" width="321" />
</center>

<h2 id="need-help">Need help</h2>
<p>If you need further help, please join us on the <a href="https://merginmaps.com/community/join">community chatroom</a> and we will be able to help you with the upgrade issue (or other Input/Mergin related problems.)</p>
