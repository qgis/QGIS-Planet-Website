---
source: "blog"
title: "QGIS Report Plugin Release"
date: "2016-05-12T09:00:00-0500"
link: "https://lutraconsulting.co.uk/blog/2016/05/12/qgis-report-plugin/"
draft: "false"
showcase: "planet"
subscribers: ["lutragis"]
author: "Lutra Consulting"
tags: []
---

<center>
	<img alt="Issue Reporting" src="https://raw.githubusercontent.com/lutraconsulting/qgis-report-plugin/master/images/icon_128.png" />
</center>

<p>We develop several public and private plugins for QGIS users and our clients. During the testing phase, they often come across some bugs. To enable them to report the issues and include the right type of information, we have developed The Report plugin to simplify the process <a href="http://plugins.qgis.org/plugins/report/">Report plugin</a>.</p>

<!-- more -->

<p>The Report plugin helps developers get better bug reports from users, by auto-populating the relevant information. It also simplifies the bug reporting process for users.</p>

<p>The Report plugin can automatically extract information from the plugin crash as well as other important information for developers. With just one click you can report the issue to the official plugin issue tracker. No need of searching for a plugin’s tracker on the internet or copy-pasting long tracebacks to your browser.</p>

<p><img alt="bug report plugin" src="https://www.lutraconsulting.co.uk/img/posts/bug_report.png" /></p>

<h3 id="installation">Installation</h3>
<ul>
  <li>Install Report plugin from QGIS plugin offical repository</li>
  <li>Create a <a href="https://github.com/">GitHub</a> account if you do not have any existing</li>
  <li>Create a public access token <a href="https://github.com/settings/tokens/new">GitHub</a> with public_repo scope</li>
  <li>Click on the Report plugin toolbar button, Configure link and copy generated GitHub access token to the configuration dialog.</li>
  <li>Wait for next error and report the problem to the developers</li>
</ul>

<h3 id="testing">Testing</h3>
<ul>
  <li>Feel free to download <a href="https://github.com/lutraconsulting/qgis-dev-null-plugin" title="devnull">DevNull plugin</a> from QGIS plugin offical repository to be able to test Report plugin</li>
  <li>After installation fo DevNull plugin, click on the new button /dev/null in your toolbar and watch how report plugin catches the exception</li>
  <li>Report any number of testing issues to DevNull Issue tracker, they are going to be deleted anyway!</li>
</ul>

<center>
  &lt;iframe width="420" height="315" src="https://www.youtube.com/embed/40aiJ793mjs"; frameborder="0" allowfullscreen&gt;&lt;/iframe&gt;
</center>

<h3 id="notes">Notes</h3>
<ul>
  <li>Report plugin works only with GitHub issue trackers</li>
  <li>Plugins must have “tracker” metadata filled in, so the Report plugin can detect the plugin issue tracker correctly</li>
</ul>

<p>When/if QGIS issue tracker moves to GitHub, a similar tool can be added to the core to automatically report bugs and crashes.</p>

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
