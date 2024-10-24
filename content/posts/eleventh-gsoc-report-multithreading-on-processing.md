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

What do I have completed this week? During this week I have changed the multithreading implementation to use the QThreadPool to allow thread recycling and avoid thread creation costs every time we want to run an algorithm. This new implementation adds some flexibility to the multithread support and avoid unexpected behaviours in different machines. The number of threads in the &#8230; <a class="more-link" href="https://qgisgsoc2015.wordpress.com/2015/08/10/eleventh-gsoc-report-multithreading-on-processing/">Continue reading <span class="screen-reader-text">Eleventh GSoC report &#8211; Multithreading on&#160;Processing</span></a>
