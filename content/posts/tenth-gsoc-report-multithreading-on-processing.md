---
source: "blog"
title: "Tenth GSoC report –  Multithreading on Processing"
date: "2015-08-03T00:21:21+0000"
link: "https://qgisgsoc2015.wordpress.com/2015/08/03/tenth-gsoc-report-multithreading-on-processing/"
draft: "false"
showcase: "planet"
subscribers: ["marcus_soc_reports"]
author: "Marcus SOC reports"
tags: ["reports"]
---

<p><strong>What do I have completed this week?</strong></p>
<ul>
<li>
<p align="justify">During this week I worked on a mechanism to stop the algorithm execution on QGIS algorithms. The approach used to cancel the execution explores python exceptions and QT signals to stop the algorithm from the main thread without having to wait in order to stop the execution and terminate the worker thread. I have used signals to trigger an exception inside the algorithm and stop the execution from the main thread. Since there is a significant amount of algorithms, the mechanism had to be implemented in just two of the QGIS algorithms. This implementation can be further replicated  towards the remaining  QGIS algorithms.</p>
</li>
</ul>
<p><strong>What am I going to achieve for the next week?</strong></p>
<ul>
<li>
<p align="justify">Start working on a test suite for the multithreading to ensure the correct behaviour of the multithreading implementation. The test suite must check if the worker thread is starting, check if signals are triggering the functions when it is supposed to and verify if the cancel option is working properly.</p>
</li>
<li>Figure out how to stop the execution of a non-QGIS algorithm.</li>
</ul>
<p><strong>Is there any blocking issue?</strong></p>
<ul>
<li>No blocking issues</li>
</ul>
