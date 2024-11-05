---
source: "blog"
title: "Eleventh GSoC report – Multithreading on Processing"
date: "2015-08-10T02:05:28+0000"
link: "https://qgisgsoc2015.wordpress.com/2015/08/10/eleventh-gsoc-report-multithreading-on-processing/"
draft: "false"
showcase: "planet"
subscribers: ["marcus_soc_reports"]
author: "Marcus SOC reports"
tags: ["reports"]
---

<p><strong>What do I have completed this week?</strong></p>
<ul>
<li>
<p align="justify">During this week I have changed the multithreading implementation to use the QThreadPool to allow thread recycling and avoid thread creation costs every time we want to run an algorithm. This new implementation adds some flexibility to the multithread support and avoid unexpected behaviours in different machines. The number of threads in the QThreadPool is initialised accordingly to the number of cores in the PC and may happen that the QT is not able to detect the number of cores. In this case we will only have one thread in the thread pool, which can be occupied with something else. I’m trying to detect when there is no available threads on the ThreadPool and increase the number of threads if necessary.</p>
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
<li>
<p align="justify">I have spotted some issues when testing the code in a different machine (with Linux Mint 17) that may have to do with thread unavailability.  Therefore, I decided to postpone the current tasks and focus on changing the multithreading implementation in order to correct this kind of unexpected behaviours.</p>
</li>
</ul>
