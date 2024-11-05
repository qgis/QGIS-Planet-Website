---
source: "blog"
title: "Final GSoC report"
date: "2015-08-24T16:40:21+0000"
link: "https://qgisgsoc2015.wordpress.com/2015/08/24/final-gsoc-report/"
draft: "false"
showcase: "planet"
subscribers: ["marcus_soc_reports"]
author: "Marcus SOC reports"
tags: ["reports"]
---

<p><strong>What do I have completed this week?</strong></p>
<ul>
<li>
<p align="justify">Added&nbsp;a dedicated threadPool for the Processing Toolbox to run the algorithms.</p>
</li>
<li>Bugfix on the cancel option. Avoid connecting &nbsp;the&nbsp;signals every time the algorithm runs. This was making&nbsp;the slots to be called multiple times when running and cancelling the algorithm several times.</li>
</ul>
<p><strong>Is there any blocking issue?</strong></p>
<ul>
<li>
<p align="justify">I wasn&#8217;t able to fix the issue with the cancel option when you have more than one algorithm running. The issue turned out to be more complicated than I first expected.</p>
</li>
</ul>
