---
source: "blog"
title: "Fifth Report"
date: "2015-06-29T00:09:54+0000"
link: "https://qgisgsoc2015.wordpress.com/2015/06/29/fifth-report/"
draft: "false"
showcase: "planet"
subscribers: ["marcus_soc_reports"]
author: "Marcus SOC reports"
tags: ["midterm", "reports"]
---

<p><strong>What do I have completed this week?</strong></p>
<ul>
<li>Solved the issue with the outputs.</li>
<li>Did some tests with QGIS algorithms which seems to be working fine.</li>
<li>Refactored all QGIS algorithms in order to remove the progress bar parameter and use the signal instead.</li>
<li>I have changed the Buffer used by QGIS algorithms: the Buffer is now a subclass of QObject. This new implementation allows the buffer to have a parent (the algorithm) and get access to the algorithm&#8217;s signal.</li>
<li>SagaUtils refactored in the same way I did with the Buffer.</li>
<li>SAGA algorithms refactored in order to use the signals instead of the progress parameter (Not finished yet)</li>
</ul>
<p><strong>What am I going to achieve for the next week?</strong></p>
<ul>
<li>Solve the issue with SAGA algorithms.</li>
<li>Code refactoring in order to improve the previous implementation on the AlgorithmDialog.</li>
<li>Refactor Grass/Grass7.</li>
<li>Bug fixes.</li>
</ul>
<p><strong>Is there any blocking issue?</strong></p>
<p>There is an issue with SAGA algorithms that makes the Toolbar crash.</p>
