---
source: "blog"
title: "Geodiff version 1.0"
date: "2021-06-09T00:00:00-0500"
link: "https://lutraconsulting.co.uk/blog/2021/06/09/geodiff-and-mergin-news/"
draft: "false"
showcase: "planet"
subscribers: ["lutragis"]
author: "Lutra Consulting"
tags: []
---

<p>We are excited to announce that the <a href="https://github.com/lutraconsulting/geodiff">geodiff library</a> has finally reached version 1.0. We have started to develop geodiff back in 2019 as a part of our efforts to allow synchronisation of changes between the <a href="https://merginmaps.com/">Input mobile app</a> and <a href="https://merginmaps.com/">Mergin platform</a>.</p>

<p><img alt="geodiff-diff.png" src="https://raw.githubusercontent.com/lutraconsulting/geodiff/master/docs/img/geodiff-diff.png" /></p>

<p>At the core, geodiff library provides functionality to:</p>

<ul>
  <li>compare a pair of GeoPackage databases and create “diff” files containing changes between them</li>
  <li>apply a “diff” file to a GeoPackage database</li>
  <li>rebase changes in a “diff” file</li>
  <li>invert, concatenate diffs and other utility functions</li>
</ul>

<p>Thanks to the above low-level operations, any changes to data stored in spatial/non-spatial tables in GeoPackages can be easily transferred to others and applied. And thanks to the “rebase” functionality - inspired by source code management systems like git - we can automatically merge changes from multiple users capturing data offline in Input/Mergin (see our recent <a href="https://www.lutraconsulting.co.uk/blog/2021/05/11/how-mergin-sync-works/">blog post that covers rebasing</a> for more).</p>

<p>The library is written in C++, providing stable C API and offering Python bindings as well (look for <code class="highlighter-rouge">pygeodiff</code> <a href="https://pypi.org/project/pygeodiff/">package</a> in <code class="highlighter-rouge">pip</code>). It also comes with a command line interface tool <code class="highlighter-rouge">geodiff</code> covering all major features. The whole package has a very permissive MIT license.</p>

<h2 id="support-for-drivers">Support for drivers</h2>

<p>Initially, geodiff library only worked with SQLite / GeoPackage files. This has changed with the version 1.0 - geodiff supports drivers, allowing use of different database backends to compare and apply diffs. In the 1.0 release we have added PostGIS driver in addition to SQLite/GeoPackage driver.</p>

<p>This means that users can compare tables or apply diffs in PostGIS databases using the same APIs as with GeoPackages. And not only that - diff files are compatible across different drivers. That means it is possible to take a diff file from a GeoPackage and apply it to PostGIS database!</p>

<p>Using the PostGIS driver we were able to create <a href="https://github.com/lutraconsulting/mergin-db-sync">mergin-db-sync</a> tool as a companion to Mergin platform. With DB sync, one can keep a local PostGIS database always in sync with a project in Mergin, supporting automatic transfer of changes from Mergin to PostGIS and the other way round as well - from PostGIS to back Mergin.</p>

<h2 id="try-it">Try it</h2>

<p>The library is hosted on GitHub in <a href="https://github.com/lutraconsulting/geodiff">lutraconsulting/geodiff</a> repository. We would love to hear your feedback!</p>

<h2 id="stay-tuned-for-more">Stay tuned for more!</h2>

<p>As <a href="https://twitter.com/qgis/status/1375363795028217869">announced earlier</a>, next week we will be open sourcing Mergin, our platform for easy sharing of spatial data in teams (whether they are in office or in the field). If you have not heard about Mergin platform yet, please have a look at the <a href="https://merginmaps.com/">Mergin website</a>, try <a href="https://plugins.qgis.org/plugins/Mergin/">Mergin plugin for QGIS</a> and <a href="https://merginmaps.com/">Input app</a>, a mobile app based on QGIS for iPhone/iPad and Android devices. Since the initial release in early 2019, Mergin and Input have been used by thousands of users around the world.</p>

<p>At Lutra Consulting, we are dedicated to improving free and open source software for geospatial. We will be releasing Mergin as open source to solve another missing piece in the puzzle, providing open source end-to-end solution for mobile data capture for QGIS users. Watch our blog and <a href="https://twitter.com/lutraconsulting/">Twitter</a> for further updates!</p>

<p><img alt="Mergin" src="https://www.lutraconsulting.co.uk/img/Products_10.jpg" /></p>
