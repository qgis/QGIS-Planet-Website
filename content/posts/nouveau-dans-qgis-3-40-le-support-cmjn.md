---
source: "blog"
title: "New in QGIS 3.40 : CMYK Support"
date: "2025-11-24T12:30:21"
link: "https://oslandia.com/en/2024/10/02/nouveau-dans-qgis-3-40-le-support-cmjn/"
draft: "false"
showcase: "planet"
subscribers: ["qgis_oslandia"]
author: "QGIS Oslandia"
tags: ["newsfr", "open source", "qgis", "cartographie", "open source", "qt"]
languages: ["en_gb"]
available_languages: ["en_gb"]
---

<p><em>Credits : <a href="https://pixabay.com/users/bru-no-1161770/">Bru-nO</a> (Pixabay Content License)</em></p>
<p>Thanks to funding from the Bordeaux Metropolis, I had the chance to work on CMYK (Cyan Magenta Yellow blacK) support in QGIS. The metropolis’ goal is to remove the last barrier preventing their complete migration from ArcGIS to QGIS.</p>
<p>The developments are now complete and will be available in QGIS version 3.40, scheduled for release in October 2024, before becoming the next LTR in February 2025. It should be noted, however, that CMYK support will only be complete in QGIS versions built with Qt 6 (still unofficial version) for reasons explained in the article. On Windows, this version can currently only be installed using <a href="https://www.qgis.org/resources/installation-guide/#osgeo4w-installer">OSGeo4W</a> (qgis-qt6-dev version).</p>
<p><strong>EDIT: </strong>Actually, QGIS version built with Qt 6.8, which ships the needed modifications for CMYK PDF export, is not yet released. More information <a href="https://github.com/qgis/QGIS-Enhancement-Proposals/issues/283#issuecomment-2388600692">here</a>.</p>
<h2>What is CMYK?</h2>
<p>You probably know RGB, which allows you to code a color on screen by choosing the amount of red, green and blue in that color. You may also use <a href="https://en.wikipedia.org/wiki/HSL_and_HSV">TSL or TSV</a>.</p>
<p><em><img alt="" class="size-medium wp-image-8889 aligncenter" height="284" src="/img/subscribers/qgis_oslandia/nouveau-dans-qgis-3-40-le-support-cmjn/rvb-300x284.webp" width="300"/></em></p>
<p style="text-align: center;"><em>RVB – Credits : <a href="https://pixabay.com/users/blendertimer-9538909/">Daniel Roberts</a> (Pixabay Content License)</em></p>
<p>These 3 color references allow a color to be coded for a screen, while CMYK targets printers by allowing to set the exact quantity of ink that will be released during printing (hence the 4 CMYK components, one per ink cartridge).</p>
<p> </p>
<p style="text-align: center;"><em><img alt="" class="alignnone size-medium wp-image-8888" height="225" src="/img/subscribers/qgis_oslandia/nouveau-dans-qgis-3-40-le-support-cmjn/cartouches-300x225.webp" width="300"/></em></p>
<p style="text-align: center;"><em>CMYK ( here from left to right KCMY ) – Credits : <a href="https://pixabay.com/users/magnascan-653134/">Magnascan</a> (Pixabay Content License)</em></p>
<p>The characteristics of CMYK differ greatly from RGB, it’s considered a subtractive colorimetric mode, because the ink absorbs light unlike RGB which is said to be additive, the more red, green, blue you have the closer you are to full light, white.</p>
<p>The intrinsically different nature of these 2 color spaces means that it is strongly advised not to convert from one to the other. The best is to choose a color in a space (CMYK for printing, RGB for rendering on screen) and stick to it.</p>
<p>Worse, printing the same color is different depending on the printer, ink, paper… The choice of a CMYK color has to be done in a color space, represented by a <a href="https://en.wikipedia.org/wiki/ICC_profile">ICC</a> profile file, provided by your printer. It is a bit like a color chart used when choosing paint.</p>
<p> </p>
<p style="text-align: center;"><em><img alt="" class="alignnone size-medium wp-image-8887" height="225" src="/img/subscribers/qgis_oslandia/nouveau-dans-qgis-3-40-le-support-cmjn/nuancier-300x225.webp" width="300"/></em></p>
<p style="text-align: center;"><em>Now you can argue about the REALLY good color of a road line – Credits : <a href="https://pixabay.com/users/yanns-1271950/">Yanis Ladjouzi</a> (Pixabay Content License)</em></p>
<h2>Developments in QGIS… and Qt</h2>
<p>It is now possible in QGIS to:</p>
<ul>
<li>Enter colors in CMYK format, and in floating precision;</li>
<li>Define your preferred color mode (RGB or CMYK) and your color space;</li>
<li>Generate a file in <a href="https://en.wikipedia.org/wiki/PDF/X">PDF/X-4</a> format (ready for printing) embedding a color space and using CMYK colors;</li>
<li>Allow the expression engine to manipulate CMYK colors without converting them to RGB;</li>
<li>Manage CMYK color ramps;</li>
<li>Lots of other small improvements and corrections about color management.</li>
</ul>
<p> </p>
<p style="text-align: center;"><em><img alt="" class="alignnone size-full wp-image-8886" height="492" src="/img/subscribers/qgis_oslandia/nouveau-dans-qgis-3-40-le-support-cmjn/colorwidget.webp" width="671"/></em></p>
<p style="text-align: center;"><em>Selecting colors in QGIS in CMYK</em></p>
<h2>The beautiful story of Open source</h2>
<p>I took great pleasure in participating in this development because it is the result of the collaboration of many players in free software.</p>
<p>During a first phase of study concerning the support of CMYK in QGIS, we quickly identified that <a href="https://en.wikipedia.org/wiki/Qt_(software)">Qt</a>, the framework used by QGIS for rendering maps, has limitations. It converts all colors to RGB when rendering maps in PDF format and its support for CMYK color spaces is incomplete.</p>
<p>It is therefore necessary to make it evolve. We therefore turn to our preferred partner when it comes to Qt, <a href="https://www.kdab.com/">KDAB</a>, and more precisely Giuseppe D’Angelo who then carries out the necessary developments.</p>
<p>Regarding new features, these are only available in Qt 6 (Qt 5 is end of life). This is why CMYK support is incomplete in official versions of QGIS still based on Qt 5.</p>
<p>QGIS.org, the association that oversees the QGIS project, decided to fund the developments on Qt. Oslandia, on the other hand would have to manage these developments and then to carry out the integration in QGIS. This integration as well as the related new features was funded by the Bordeaux metropolis.</p>
<p>My developments were then reviewed by other QGIS contributors. (If you want to know more about the QGIS contribution process, you can read a previous blog post about <a href="https://oslandia.com/en/2024/02/09/la-qualite-logicielle-dans-qgis/">software quality in QGIS</a>)</p>
<p>Finally, I wanted to give a special thanks to Jehan, developer on the <a href="https://www.gimp.org/">GIMP</a> project. His availability and thoroughness in our mail exchanges greatly helped me understand the technical and functional issues of CMYK, and most certainly contributed to the quality of the result.</p>
<h2>Next</h2>
<p>QGIS 3.40 will therefore be able to generate a PDF/X-4 file using CMYK colors. Qt, for its part, improves CMYK support, PDF writing, and color space management.</p>
<p>Thanks again to the Bordeaux metropolis and QGIS.org for funding these developments, and all the people involved in their realization.</p>
<p>We would be delighted to have feedback from users on your use cases related to color management in QGIS. Do not hesitate to write to us or comment on our posts to tell us how you use these features.</p>
<p>These foundations in the management of color spaces in QGIS open the door to future improvements. If you are interested in this topic and would like to contribute, please contact us at <a href="mailto:infos+qgis@oslandia.com">infos+qgis@oslandia.com</a> and check out our QGIS support offer.</p>
