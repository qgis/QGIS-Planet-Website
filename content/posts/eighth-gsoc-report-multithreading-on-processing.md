---
source: "blog"
title: "Eighth GSoC Report – Multithreading on Processing"
date: "2015-07-19T22:32:56+0000"
link: "https://qgisgsoc2015.wordpress.com/2015/07/19/eighth-gsoc-report-multithreading-on-processing/"
draft: "false"
showcase: "planet"
subscribers: ["marcus_soc_reports"]
author: "Marcus SOC reports"
tags: ["reports"]
---

<p><strong>What do I have completed this week?</strong></p>
<ul>
<li>Created a mechanism to hold the result of the algorithm taking into account that there can be several algorithms running at the same time. The results are stored in a global variable called algResults. This variable is accessible via python console (e.g. &#8220;processing.algResults&#8221;).</li>
</ul>
<p><a href="https://qgisgsoc2015.wordpress.com/wp-content/uploads/2015/07/algresults.png"><img alt="algResults" class="aligncenter size-full wp-image-121" height="244" src="https://qgisgsoc2015.wordpress.com/wp-content/uploads/2015/07/algresults.png?w=676&#038;h=244" width="676" /></a></p>
<ul>
<li>The signals are connected in a different way in order to close the dialog and quit the thread when the algorithm is finished.</li>
<li>I have updated my fork and merged my work into the master branch.</li>
<li>Added the runalgIterating method to the AlgorithmExecutor with some changes to support the signals to set the progress</li>
<li>AlgorithmDialog refactored.</li>
<li>I have been searching for a solution to stop the algorithm execution and I think that is possible to create a sort of checkpoints inside the algorithm to check if we want to stop the execution and raise an exception to stop the thread event loop.</li>
</ul>
<p><strong>What am I going to achieve for the next week?</strong></p>
<ul>
<li>Allow the user to cancel the execution when running the runalgIterating.</li>
<li>Solve the problem with QGIS dependencies on Ubuntu and test the refactored algorithms.</li>
<li>Continue working on the algorithm iterating.</li>
</ul>
<p><strong>Is there any blocking issue?</strong></p>
<ul>
<li>I had to postpone the tests due to some problems installing QGIS dependencies on Ubuntu.</li>
<li>Didn&#8217;t had time to implement a solution to stop the execution of the algorithm.</li>
</ul>
