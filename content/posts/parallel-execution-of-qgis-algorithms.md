---
source: "blog"
title: "Parallel execution of QGIS algorithms"
date: "2015-08-19T17:16:30+0000"
link: "https://qgisgsoc2015.wordpress.com/2015/08/19/parallel-execution-of-qgis-algorithms/"
draft: "false"
showcase: "planet"
subscribers: ["marcus_soc_reports"]
author: "Marcus SOC reports"
tags: ["reports"]
---

<p align="justify">This is just an example of the advantage provided by the multithreading on the Toolbox. As each algorithm is running in a separate thread, this allows us to run more than one algorithm at the same time.</p>
<div class="jetpack-video-wrapper"></div>
<p>&nbsp;</p>
<p align="justify">I&#8217;m polishing the implementation and trying to find some major problems in the current implementation.  It has some minor bugs that can be easily solved by adding a parameter to the  cancel signal (e.g. when you have two algorithms running and try to cancel one of them, the signal emitted will cancel two algorithms instead of just one)</p>
