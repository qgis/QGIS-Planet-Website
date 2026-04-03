---
source: "blog"
title: "How we build QField for many platforms - A look behind the curtain"
date: "2022-09-20T05:48:00+0000"
link: "https://qfield.org/blog/2022/09/20/how-we-build-qfield-for-many-platforms-a-look-behind-the-curtain/"
draft: "false"
showcase: "planet"
subscribers: ["qfield"]
author: "QField"
tags: ["qfield", "qgis.org"]
languages: ["en_gb"]
available_languages: ["en_gb"]
---

<p><em>In the past year, <strong>the build system behind QField has been ported to <a href="https://vcpkg.io/en/index.html" rel="noopener" target="_blank">vcpkg, a modern C++ dependency management system</a></strong>. It has been a great success for QField and considerably helped to streamline efforts, improve the development experience and to guarantee an outstanding stability of the application. In this blog post we will look at the history of building QGIS based applications for mobile systems and how it has become what it is today.</em></p>
<p>When <a href="https://qfield.org/2011/08/24/gsoc-2011-final-report/">Marco Bernasocchi (CEO of OPENGIS.ch and chair of QGIS.org) started working on <strong>QGIS for Android</strong> in Google Summer of Code</a> a decade ago, the main job was to also build all QGIS dependencies for Android. This includes well-known libraries like <strong>proj</strong> and <strong>gdal</strong> and less-known ones like libxml2 or iconv. Each of them has its particularities and specific build flags. Working on this appears to be an endless iterative trial-and-error journey where you hope each day that eventually you will see the <a href="https://qfield.org/2021/06/08/qfieldcloud-now-opensource-happy-10-years-of-field-mapping-with-qgis/">QGIS splash screen on your Android phone</a> while all you see are endless lines of code and compiler errors.</p>
<p>As we know nowadays QGIS for Android has eventually seen the sunlight and its achievements are still the base for <a href="https://qfield.org/" rel="noopener" target="_blank">QGIS-based mobile apps like QField</a>.</p>
<p>Sometime later we decided to modernize the build infrastructure into OSGeo4A a set of scripts where each dependency was built with a “recipe”. Modularized this way, it was easier to maintain, and general build code common for all libraries could be isolated. It was good enough to help drive QField for a couple of years, and a copy of it is still in use <strong>as the base for nowadays <a href="https://github.com/qgis/QGIS-Mac-Packager/tree/master/qgis_deps" rel="noopener" target="_blank">QGIS builds for macOS</a></strong>.</p>
<p>When we decided to make QField also available on other platforms like <strong>iOS, Windows and macOS</strong> we quickly realized that duplicating build chains scales really bad and maintaining this is an immense effort we wanted to avoid. There are a couple of existing C++ dependency management systems, none of which convinced us ultimately. Lucky for us a mail on the <a href="https://www.mail-archive.com/qgis-developer@lists.osgeo.org/msg52302.html" rel="noopener" target="_blank">QGIS mailing list mentioned a new one called vcpkg</a> which looked very promising.</p>
<p>A couple of days later we had a build for Windows and later in the same year for macOS. With many dependencies already available in modern versions. Cheers.</p>
<p>What’s left to do than just enable it for Android, and all our problems are suddenly solved? Alas, it’s not so easy. <strong>Cross-compiling is always a bit trickier.</strong> And so we started another journey to improve the situation. After a while, we had a working build chain based on vcpkg for Android in our R&amp;D labs. Interestingly, this added a couple of features just because the community around vcpkg had already added them. For example using <a href="https://www.cogeo.org/" rel="noopener" target="_blank">COG</a>-based raster data via HTTP was suddenly working <em>(for the record: thanks to the availability of curl which we never took care of adding ourselves in OSGeo4A)</em>.</p>
<p>Soon after we also wanted to try building for <strong>iOS with vcpkg</strong>, which after a few attempts also was successful, and even managed to resolve some weird crashes and other issues we had experienced with the old buildchain.</p>
<figure class="figure text-center mb-4"><img alt="" class="figure-img img-fluid gallery-img" height="338" src="/img/subscribers/qfield/how-we-build-qfield-for-many-platforms-a-look-behind-the-curtain/Peek-2022-09-19-17-01_hu_47348f18fa928eb7.gif" width="1200"/></figure>
<p>The main benefit was that we could upgrade the QGIS base libraries in one single place for every platform, in an isolated branch without playing the Jenga game on each upgrade.</p>
<p>The only unfinished business we still had was that support for iOS and Android was still available only in our own vcpkg fork.</p>
<p>So the last few weeks and months <strong>we have been working closely with upstream</strong> to bring building for Android and iOS up to the same level as desktop platforms. The relevant parts are now in a clean state.</p>
<p>Advantages of this approach:</p>
<ul>
<li>• Mutualized efforts on all the base libraries, also with programmers outside the geoverse</li>
<li>• A vibrant community that ensures a noticeably fast upgrade of libraries</li>
<li>• A clean dependency management system</li>
<li>• A consistent set of dependency versions (gdal, geos, libpq, …) across all platforms</li>
<li>• A clean caching system that will only recompile reverse dependencies on updates</li>
<li>• We can upgrade a dependency in an isolated branch and only release it when it works on all platforms</li>
<li>• We can optimize the code for a given set of dependency versions and if a bug is fixed in a certain dependency version, we are sure we can ship this fix on all platforms promptly</li>
<li>• We maintain the QField source code as well as dependency versions in a single repository, what makes development more streamlined</li>
</ul>
<p>Big thanks go to Alexander Neumann and Kai Pastor who both stand out for doing things the right and future-proof way.</p>
<p>As always, things come at a price, there was a steep learning curve involved, and some edge cases require attention. However, we are thrilled by the simplification this has brought us.</p>
<p>If you are maintaining a customized fork of QField, it is now a good time to <strong>start upgrading to vcpkg</strong>, since <a href="https://github.com/opengisch/OSGeo4A" rel="noopener" target="_blank">OSGeo4A has been archived</a> and will no longer be maintained. The <a href="https://github.com/opengisch/QField/blob/master/doc/dev.md" rel="noopener" target="_blank">developer documentation of QField</a> has been updated with relevant instructions.</p>
<p>If you have time to test the new build system, <a href="https://github.com/opengisch/QField/discussions" rel="noopener" target="_blank">we will be happy to read about your experiences</a> with it.</p>
