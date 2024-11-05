---
source: "blog"
title: "Ninth GSoC Report – Multithreading on Processing"
date: "2015-07-26T23:12:53+0000"
link: "https://qgisgsoc2015.wordpress.com/2015/07/26/ninth-gsoc-report-multithreading-on-processing/"
draft: "false"
showcase: "planet"
subscribers: ["marcus_soc_reports"]
author: "Marcus SOC reports"
tags: ["reports"]
---

<p><strong>What do I have completed this week?</strong></p>
<ul>
<li>Solved an issue that makes QGIS crash when the main thread doesn&#8217;t wait for the worker thread to start.</li>
<li>I spent most of the time looking up some tutorials about unit testing on QGIS and trying to configure python paths to run the processing tests.</li>
</ul>
<p><strong>What am I going to achieve for the next week?</strong></p>
<ul>
<li>This week I&#8217;ll change back to the multithreading implementation in order to add the cancel option to stop the algorithm execution. I will be working on a mechanism to stop the execution on QGIS algorithm.</li>
</ul>
<p><strong>Is there any blocking issue?</strong></p>
<ul>
<li>This week my mentor proposed to start working on a suite test and I changed the plan to start working on a unit test to ensure the correct behaviour of the multithreading implementation. At the end of the week we discussed about asking the community to test the new implementation and report the issues if there is any.</li>
</ul>
