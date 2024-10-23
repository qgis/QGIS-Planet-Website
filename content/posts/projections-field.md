---
source: "blog"
title: "Why are my survey points shifted?"
date: "2021-04-21T19:00:02-0500"
link: "https://lutraconsulting.co.uk/blog/2021/04/21/projections-field/"
draft: "false"
showcase: "planet"
subscribers: ["lutragis"]
author: "Lutra Consulting"
tags: []
---

<p>It happens that when you collect data and then checking it in the office on your
desktop using QGIS, the points are misplaced and shifted. This blog post explains the possible root cause of this issue?
(Read time 5 min)</p>

<!-- more -->

<p>This article <a href="https://merginmaps.com/docs/concepts/projections/">follows the help document</a> about the projections and coordinate reference system handling in QGIS.</p>

<p>The accuracy of the captured points is affected by two main factors</p>
<ul>
  <li>GPS receiver and accuracy</li>
  <li>Selection of coordinate reference systems used in the project</li>
</ul>

<p>Lets take a closer look at both problems in context of field surveys.</p>

<h2 id="gps-accuracy">GPS accuracy</h2>

<p>GPS accuracy depends on the quality of your GPS receiver and the number of visible GPS
satellites your receiver can use at the moment of capturing the point.</p>

<p>When you load the map in Input app, the bottom bar contains the GPS marker with a coloured dot.
The dot can have the following three colours:</p>
<ul>
  <li><strong>green</strong>: The actual accuracy is below the threshold</li>
  <li><strong>orange</strong>: The actual accuracy is above the threshold</li>
  <li><strong>red</strong>: The GPS is unavailable</li>
</ul>

<p><img alt="GPS accuracy low" src="https://www.lutraconsulting.co.uk/img/posts/tracks-input-stream.png" /></p>

<p>For different use cases, acceptable accuracy is different. So the threshold for the
colour scheme could be adjusted in the Input app settings. Always adjust the settings
based on your project needs and check the GPS accuracy when capturing data.</p>

<p><img alt="Input app GPS settings" src="https://www.lutraconsulting.co.uk/img/posts/Input_settings.png" /></p>

<p>The GPS receiver itself can be either improved by usage of device with a better internal
hardware or usage of powerful external GPS receivers If you want to use the external
GPS receiver, read the following <a href="https://merginmaps.com/docs/howto/external_gps">help article</a>
for setup.</p>

<h2 id="projection-problems">Projection problems</h2>

<p>First of all, there could be multiple problems with setup of coordinate reference systems and
transformations. To solve it, you need to load the project in QGIS, using
<a href="https://plugins.qgis.org/plugins/Mergin/">Mergin Plugin</a> and check for various situations
as described in <a href="https://merginmaps.com/docs/concepts/projections/">this help article</a>.</p>

<p><a href="https://merginmaps.com">Input app</a> checks for missing datum shift files or other transformation problems and notify
you once at the project load by following message.</p>

<p><img alt="shift of the point" src="https://www.lutraconsulting.co.uk/img/posts/Input_projection_err.png" /></p>

<p>To be able to use the datum grid shift in your mobile app:</p>

<ul>
  <li>Copy the <code class="highlighter-rouge">proj</code> folder from your QGIS working directory (see <a href="https://merginmaps.com/docs/concepts/projections/">help page</a> for different platforms)</li>
  <li>Paste the folder to your survey project downloaded fromt he Mergin server</li>
  <li>Sync the changes</li>
</ul>

<p>For our example with the British national grid on Windows, the grid file is called
<code class="highlighter-rouge">OSTN15_NTv2_OSGBtoETRS.gsb</code> and if the Mergin project is in
<code class="highlighter-rouge">C:\users\qgis\myproject</code> then it should be copied to
<code class="highlighter-rouge">C:\users\qgis\myproject\proj</code> directory and synchronised by the Mergin service to  the Input app.</p>

<p><strong>Notes</strong>:</p>
<ul>
  <li>This is one-off process. <a href="https://merginmaps.com">Input app</a> will transfer the grid shift datum to its own working directory on your mobile device.</li>
  <li>There might be more than one datum grid shift in your QGIS working directory. Use the appropriate one for your survey project.</li>
</ul>

<p>You can find a short summary of this article on the Input app <a href="https://merginmaps.com/docs/howto/proj/">help pages</a></p>
