---
source: "blog"
title: "Twelfth GSoC report – Multithreading on Processing"
date: "2015-08-17T00:04:51+0000"
link: "https://qgisgsoc2015.wordpress.com/2015/08/17/twelfth-gsoc-report-multithreading-on-processing/"
draft: "false"
showcase: "planet"
subscribers: ["marcus_soc_reports"]
author: "Marcus SOC reports"
tags: ["reports"]
---

<p><strong>What do I have completed this week?</strong></p>
<ul>
<li>
<p align="justify">I have finished the cancel option in order to stop the execution of non-QGIS algorithms. It&#8217;s important to remember that as well as the QGIS algorithms the cancel option do not cover all the non-QGIS algorithms and this implementation only covers GDAL and SAGA algorithms. However this option can be easily replicated to the othersthird party algorithms.</p>
</li>
<li>
<p align="justify">I have changed the python console to use the QThreadPool.</p>
</li>
<li>
<p align="justify">I have been testing and debugging the multithreading implementation looking for unexpected behaviours or incorrect results.</p>
</li>
<li>Core refactoring.</li>
</ul>
<p><strong>What am I going to achieve for the next week?</strong></p>
<ul>
<li>
<p align="justify">Write documentation for the multithreading implementation.</p>
</li>
<li>
<p align="justify">Code cleaning and refactoring.</p>
</li>
<li>
<p align="justify">Search for problems in the multithreading implementation and correct them.</p>
</li>
</ul>
<p><strong>Is there any blocking issue?</strong></p>
<ul>
<li>
<p align="justify">No.</p>
</li>
</ul>
