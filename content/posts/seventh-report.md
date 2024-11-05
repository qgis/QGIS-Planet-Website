---
source: "blog"
title: "Seventh Report"
date: "2015-07-13T06:46:38+0000"
link: "https://qgisgsoc2015.wordpress.com/2015/07/13/seventh-report/"
draft: "false"
showcase: "planet"
subscribers: ["marcus_soc_reports"]
author: "Marcus SOC reports"
tags: ["reports"]
---

<p><strong>What do I have completed this week?</strong></p>
<ul>
<li>Processing refactored in order to create a non-blocking implementation of the python console. The algorithm is processed in another thread asynchronously and the result is printed to the python console when the execution is finished.</li>
<li>AlgorithmDialog refactored to create a non-blocking dialog interface with a button to cancel the execution.</li>
<li>R algorithms refactored to support the progress signal.</li>
</ul>
<p><strong>What am I going to achieve for the next week?</strong></p>
<ul>
<li>Create a mechanism to hold the result of the algorithm taking into account that there can be several algorithms running at the same time.</li>
<li>Figure out a way to stop the execution of the algorithm. In third-party algorithms it can not be possible to just interrupt the thread loop and quit the thread. The only available option is to discard the result because the algorithms don’t have any kind of check-point that allows to verify once in while if we want to stop the execution. Kill the thread during the execution can be dangerous and it is not a good option.</li>
<li>Test the refactored algorithms.</li>
</ul>
<p><strong>Is there any blocking issue?</strong></p>
<ul>
<li>It took more time than I expect to create a non-blocking interface.</li>
<li>Quitting the thread execution turned out to be far more complicated due to the fact that the algorithms don&#8217;t provide any mechanism to allow quitting the thread loop during the execution.</li>
</ul>
