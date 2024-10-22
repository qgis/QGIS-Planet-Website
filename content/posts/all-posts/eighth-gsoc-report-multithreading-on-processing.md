---
source: "blog"
title: "Eighth GSoC Report – Multithreading on Processing"
date: "2015-07-19T22:32:56+0000"
link: "https://qgisgsoc2015.wordpress.com/2015/07/19/eighth-gsoc-report-multithreading-on-processing/"
draft: "false"
showcase: "planet"
folder: "marcus_soc_reports"
author: "Marcus SOC reports"
---

What do I have completed this week? Created a mechanism to hold the result of the algorithm taking into account that there can be several algorithms running at the same time. The results are stored in a global variable called algResults. This variable is accessible via python console (e.g. &#8220;processing.algResults&#8221;). The signals are connected in &#8230; <a class="more-link" href="https://qgisgsoc2015.wordpress.com/2015/07/19/eighth-gsoc-report-multithreading-on-processing/">Continue reading <span class="screen-reader-text">Eighth GSoC Report &#8211; Multithreading on&#160;Processing</span></a>
