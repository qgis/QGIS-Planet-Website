---
source: "blog"
title: "QGIS versions life cycle"
date: "2026-05-22T06:50:53"
link: "https://oslandia.com/en/2026/05/12/le-cycle-des-versions-de-qgis/"
draft: "false"
showcase: "planet"
subscribers: ["qgis_oslandia"]
author: "QGIS Oslandia"
tags: ["newsfr", "qgis"]
languages: ["en_gb"]
available_languages: ["en_gb"]
---

<h2>Which version of QGIS should I use?</h2>
<p>With <a href="https://blog.qgis.org/2026/03/09/qgis-4-0-norrkoping-is-released/">the release of QGIS 4</a>, the question of the QGIS release cycle is arising again for many users.</p>
<p>Among the most common:</p>
<ul>
<li>what is the roadmap?</li>
<li>how long will this version be maintained?</li>
<li>is it a stable version?</li>
</ul>
<p>The official <a href="https://www.qgis.org/resources/roadmap/">QGIS roadmap page</a> shows the current versions, along with a countdown to the next one.</p>
<p>I have attempted to simplify the QGIS release cycle, which can be unclear if you go too much into detail. Here is my perspective as a core QGIS developer, simplified to present the release cycle in a schematic way.</p>
<p>There are 3 types of QGIS versions:</p>
<ul>
<li>the <strong>development</strong> version (dev/nightly)
<ul>
<li>with a lifespan of 24 hours</li>
<li>unstable</li>
<li>used to test a newly added feature</li>
<li>installable via the dedicated <a href="https://download.osgeo.org/osgeo4w/v2/osgeo4w-setup.exe">OSGeo4W installer</a> (OSGeo for Windows), or the Linux development repository</li>
</ul>
</li>
<li>the <strong>latest</strong> version (latest)
<ul>
<li>with a lifespan of 4 months</li>
<li>relatively stable</li>
<li>used to test new features and report bugs (issues to be created <a href="https://github.com/qgis/QGIS/issues/new/choose">on GitHub</a>)</li>
<li>installable via <a href="https://www.qgis.org/download/">the download page</a></li>
</ul>
</li>
<li>the <strong>long-term LTR</strong> version (long term release)
<ul>
<li>with a lifespan of 1 year</li>
<li>the most stable version</li>
<li>used in production environments</li>
<li>installable via <a href="https://www.qgis.org/download/">the download page</a></li>
</ul>
</li>
</ul>
<h2>A picture is worth a thousand words</h2>
<p>The diagram below illustrates how these different versions are built and highlights their end-of-life.</p>
<p>A few additional details:</p>
<ul>
<li>QGIS uses <a href="https://semver.org/lang/fr/">SemVer</a> versioning, where X.Y.Z correspond to the major, minor, and patch versions</li>
<li>each point represents the release of a new version, spaced one month apart</li>
<li>a patch version change does not introduce any new features</li>
</ul>
<p><a href="https://oslandia.com/wp-content/uploads/2026/05/QGIS-release-roadmap.png"><img alt="" class="aligncenter wp-image-10529 size-large" src="/img/subscribers/qgis_oslandia/le-cycle-des-versions-de-qgis/QGIS-release-roadmap-631x1024.webp" width="500"/></a></p>
<h2>Conclusion</h2>
<p class="part">For each new release, feel free to check out the visual changelog in video form, for example <a href="https://www.youtube.com/watch?v=wTK1exokBA8">the one for QGIS 4.0</a>.<br/>
The visual and video changelog for each version is available <a href="https://qgis.org/project/visual-changelogs/">on the dedicated page</a>.</p>
<p class="part">If you would like to contribute to QGIS, or if you have any other questions about QGIS, feel free to contact us at <a href="mailto:infos+qgis@oslandia.com" rel="noopener" target="_blank">infos+qgis@oslandia.com</a></p>
<p class="part">You can stay informed of Oslandia news through our <a href="https://oslandia.com/newsletter" rel="noopener" target="_blank">newsletter</a>, and <a href="https://www.linkedin.com/company/oslandia" rel="noopener" target="_blank">follow us on LinkedIn</a>.</p>
