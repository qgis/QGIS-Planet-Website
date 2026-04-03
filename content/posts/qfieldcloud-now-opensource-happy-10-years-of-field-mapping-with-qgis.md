---
source: "blog"
title: "QFieldCloud now opensource - Happy 10 Years of field mapping with QGIS"
date: "2021-06-08T06:01:00+0000"
link: "https://qfield.org/blog/2021/06/08/qfieldcloud-now-opensource-happy-10-years-of-field-mapping-with-qgis/"
draft: "false"
showcase: "planet"
subscribers: ["qfield"]
author: "QField"
tags: ["qfield", "highlights", "social-responsibility", "qgis.org"]
languages: ["en_gb"]
available_languages: ["en_gb"]
---

<p>Today, on QField’s 10th anniversary, we’re extremely proud to publish the results of over <a href="https://github.com/opengisch/qfieldcloud/graphs/contributors" rel="noopener" target="_blank">18 months</a> of development and give you <a href="https://github.com/opengisch/qfieldcloud/pull/3" rel="noopener" target="_blank">the source code of QFieldCloud</a> to go and make your awesome adaptations, solutions, and hopefully contributions :)</p>
<p>If you want to quickly try it out, head to <a href="https://qfield.cloud/" rel="noopener" target="_blank">https://qfield.cloud</a> where our hosted solution is running and secure yourself a spot in the beta program.</p>
<p>QFieldCloud’s unique technology allows your team to focus on what’s important, making sure you efficiently get the best field data possible. Thanks to the tight integration with the leading GIS fieldwork app QField, your team will be able to start surveying and digitising data in no time.</p>
<figure class="figure text-center mb-4"><img alt="QField git history" class="figure-img img-fluid gallery-img" height="280" src="/img/subscribers/qfield/qfieldcloud-now-opensource-happy-10-years-of-field-mapping-with-qgis/qfield-git-history.webp" width="660"/>
<figcaption class="figure-caption text-center">QField git history</figcaption></figure>
<p>What a journey it was and what plans do we already have… It has now been 10 years since I <a href="https://github.com/qgis/QGIS-Android/commit/664145015f31783a5687807a7b77049d4e6938c9" rel="noopener" target="_blank">pushed the first scripts</a> to build Quantum GIS for Android and it is incredible what we’ve been able to achieve thanks to a vibrant community, sponsors and especially our <a href="https://opengis.ch/#team" rel="noopener" target="_blank">fantastic team</a>.</p>
<p>At <a href="https://qfield.org/">OPENGIS.ch</a> we strongly believe in <a href="https://qfield.org/core-values/#give-back">giving back</a>. We live from open-source projects and are deeply committed to sustaining their technological and <a href="https://www.qgis.org/en/site/about/sustaining_members.html#list-of-current-sustaining-members" rel="noopener" target="_blank">economic</a> <a href="https://www.osgeo.org/sponsors/" rel="noopener" target="_blank">well-being</a>. We also believe everyone should have access to the best possible tools and knowledge. By committing ourselves to develop open-source applications, we give everyone access to powerful tools to plan, review and mitigate geospatial issues.</p>
<p>That is why we are even more thrilled to have created and open-sourced a professional data and team management solution for the best <a href="https://qfield.org" rel="noopener" target="_blank">QGIS fieldwork app</a> and would like to share a bit of the history of how we revolutionised field work by creating QField for QGIS.</p>
<h2 id="prehistory---qgis-for-android-is-born">Prehistory - QGIS for Android is born</h2>
<p>Stone-, bronze-, iron-age, you get it, the beginnings of field mapping in the QGIS world were pretty rough around the edges. It all started thanks to me <a href="https://qfield.org/2011/04/25/gsoc-2011-im-in/">being accepted</a> in the Google Summer of Code 2011 programme with the “QGIS mobile” <a href="https://issues.qgis.org/projects/qgis/wiki/QGIS_Mobile_GSoC_2011" rel="noopener" target="_blank">submission</a>. In the following 3 months, I’d try, with the help of my mentors Pirmin Kalberer and Marco Hugentobler, to get Quantum GIS to run on my tablet.</p>
<h3 id="the-first-start">The first start</h3>
<blockquote>
<p>Hi all, it is a pleasure to announce that I finally got Quantum GIS to start on an android (3.2) tablet (Asus transformer). I tested as well on a Samsung Galaxy phone with cyanogen mod 7 RC1 and it works well (with the obvious screen size limitations).<br/>
Qgis still doesn’t load many elements, but the GUI is there and the rest should be only minor issues. I’ll post more as soon as I make further developments. Meanwhile, if you want to test the apk, you can download it from my GitHub <a href="https://github.com/downloads/mbernasocchi/qgis-android/Qgis-debug.apk" rel="noopener" target="_blank">here</a>. For building your own, have a look at <a href="https://qgis.org/wiki/QGIS_Mobile_GSoC_2011" rel="noopener" target="_blank">qgis wiki</a></p>
<p><a href="https://qfield.org/2011/08/17/qgis-on-android/">/2011/08/17/qgis-on-android/</a></p></blockquote>
<p><a href="https://vimeo.com/27793965" rel="noopener" target="_blank">https://vimeo.com/27793965</a></p>
<p>The first ever video about QGIS on Android</p>
<h3 id="a-proper-gui">A proper GUI</h3>
<blockquote>
<p>See my last posts. In short, I managed to get qgis packaged as an APK and to properly run with only one major problem. The map canvas is always black. I’ll investigate this till Tuesday.<br/>
Cheers</p>
<p><a href="https://qfield.org/2011/08/18/qgis-on-android-has-a-proper-gui/">/2011/08/18/qgis-on-android-has-a-proper-gui/</a></p></blockquote>
<p><a href="https://vimeo.com/27854857" rel="noopener" target="_blank">https://vimeo.com/27854857</a></p>
<p>After 3 months of intensive work, QGIS for android finally has a a proper GUI</p>
<h3 id="blazing-fast-startup">Blazing fast startup</h3>
<blockquote>
<p>Hi, I just managed to create an APK with all the resources needed by qgis …</p>
<p>The only inconvenience at the moment is that at the first startup the app shows a black screen while it’s copying the files for about <strong>30 to 60sec</strong> so just be patient and remember that the whole app will take up to 230MB (it installs on external storage by default)</p>
<p><a href="https://qfield.org/2011/08/19/qgis-on-android-has-complete-gui-and-supports-translations/">/2011/08/19/qgis-on-android-has-complete-gui-and-supports-translations/</a></p></blockquote>
<h3 id="a-working-reality">A working reality</h3>
<p>I still remember the feeling that day when after almost 3 months, of fighting with shell scripts, patching of build systems, debugging via ADB, writing C++ in Java wrappers and so on, my Quantum GIS test project was suddenly running on my tablet… I Was so happy I just went running in the mountains :).</p>
<blockquote>
<p>Just a quick screenshot to show that qgis on android is now a working reality. Tomorrow I’ll make a video and so on. The major missing thing now is reading SHP files ad maybe spatialite… maybe tomorrow. Now it’s Sunday ?</p>
<p><a href="https://qfield.org/2011/08/21/qgis-android-works-2/">/2011/08/21/qgis-android-works-2/</a></p></blockquote>
<div class="gallery-wrapper">
<figure class="figure text-center mb-4"><img alt="First data is shown on the print composer" class="figure-img img-fluid gallery-img" height="750" src="/img/subscribers/qfield/qfieldcloud-now-opensource-happy-10-years-of-field-mapping-with-qgis/P20110820193600_hu_f6d5cf01ad53b6e9.webp" width="1200"/>
<figcaption class="figure-caption text-center">First data is shown on the print composer</figcaption></figure>
<figure class="figure text-center mb-4"><img alt="Map canvas still had some glitches" class="figure-img img-fluid gallery-img" height="750" src="/img/subscribers/qfield/qfieldcloud-now-opensource-happy-10-years-of-field-mapping-with-qgis/P20110820193325_hu_539a8a9244152df8.webp" width="1200"/>
<figcaption class="figure-caption text-center">Map canvas still had some glitches</figcaption></figure>
<figure class="figure text-center mb-4"><img alt="Finally a map is rendered in the canvas" class="figure-img img-fluid gallery-img" height="312" src="/img/subscribers/qfield/qfieldcloud-now-opensource-happy-10-years-of-field-mapping-with-qgis/wpid-P20110821115718.webp" width="499"/>
<figcaption class="figure-caption text-center">Finally a map is rendered in the canvas</figcaption></figure>
</div>
<h3 id="gsoc-2011-results">GSoC 2011 results</h3>
<p>At the end of the Google Summer of code, I received my MSc in geoinformatics and left for 3 Months to Indonesia working as a consultant/developer for the World-bank Global Facility for Disaster Reduction and Recovery.</p>
<blockquote>
<p>So, it is over, after 3 months of working on QGIS for android as a Google Summer of Code project it is now time to wrap up what I did and didn’t do.<br/>
First of all a QGIS android app exists now and it has many features including:<br/>
– reading/writing projects<br/>
– raster support<br/>
– spatialite support<br/>
– WMS support<br/>
– (apparent – untested) WFS and Postgres support<br/>
– partial shape files support (string attributes still crash the app)<br/>
– Fully functional GUI (SymbologyV2 doesn’t work yet)<br/>
– (all?) core C++ plugins beside globe (any takers? ?)<br/>
Furthermore, I created a series of build scripts that make it easier to set up a dev environment.<br/>
Unfortunately, I didn’t manage to implement live GPS tracking and a larger GUI optimisation, but all in all, I’m very happy with the results and seeing that few peoples are already testing it. Soon ill publish a video.<br/>
cheers</p>
<p><a href="https://qfield.org/2011/08/24/gsoc-2011-final-report/">/2011/08/24/gsoc-2011-final-report/</a></p></blockquote>
<p>Quantum GIS for Android was a reality and I was fully committed to keeping working on it. Turns out I wasn’t wrong :)</p>
<figure class="figure text-center mb-4"><img alt="" class="figure-img img-fluid gallery-img" height="602" src="/img/subscribers/qfield/qfieldcloud-now-opensource-happy-10-years-of-field-mapping-with-qgis/image-1_hu_30aedae01740db0f.webp" width="1200"/></figure>
<h2 id="classical---qgis-for-android-grows">Classical - QGIS for Android grows</h2>
<p>The Next Era of QGIS for android is what could be seen as the time of great knowledge enhancement, philosophical musings and the rise of the first great features including:</p>
<ul>
<li><a href="https://qfield.org/2012/01/31/qgis-on-android-gets-gps-support/">GPS support</a> including <a href="https://qfield.org/2012/05/01/qgis-on-android-using-external-gps-receivers/">external GPS</a></li>
<li><a href="https://qfield.org/2012/02/01/qgis-gets-compass-support/">Compass support</a></li>
<li><a href="https://qfield.org/2012/02/16/qgis-on-android-gets-right-click-support/">Right-click support</a></li>
<li><a href="https://qfield.org/2012/03/01/qgis-for-android-gets-pinch-zooming/">Pinch zooming, tap zooming and panning</a></li>
<li><a href="https://qfield.org/2012/02/23/qgis-for-android-alpha-6/">armeabi-v7a optimizations</a></li>
<li><a href="https://qfield.org/2012/03/30/qgis-on-android-phone/">the 3.2" screen experiment</a></li>
<li><a href="https://qfield.org/2012/05/12/qgis-4200m/">Extreme environment testing</a></li>
</ul>
<p><a href="https://vimeo.com/36862461" rel="noopener" target="_blank">https://vimeo.com/36862461</a></p>
<h2 id="middle-ages---qgis-mobile">Middle Ages - QGIS Mobile</h2>
<p>The dark ages, times of instability, change and some setbacks. Sounds terrifying, it was not at all, on the contrary it was a very formative period that apexed with the fantastic release of QGIS 2.0 for android.</p>
<h3 id="the-qml-app-experiment">The QML app experiment</h3>
<p>From the beginning on, the idea behind QGIS for android was to eventually ditch the GUI and build a dedicated one for touch devices. The <a href="https://web.archive.org/web/20120826232000/https://rcarrillo.org/%22%3ehttps://web.archive.org/web/20120826232000/https://rcarrillo.org/" rel="noopener" target="_blank">Google Summer of code 2012</a> by Ramon Carrillo mentored by myself set off to do that. Unfortunately, the project encountered some roadblocks and never took off as expected, but it did lay some ideas and <a href="https://github.com/rcarrillo/Quantum-GIS/commits/mobileapp-qml" rel="noopener" target="_blank">code</a> for the future.</p>
<div class="gallery-wrapper">
<figure class="figure text-center mb-4"><img alt="UX mockup for the first QML based app" class="figure-img img-fluid gallery-img" height="800" src="/img/subscribers/qfield/qfieldcloud-now-opensource-happy-10-years-of-field-mapping-with-qgis/Legend2-1.webp" width="480"/>
<figcaption class="figure-caption text-center">UX mockup for the first QML based app</figcaption></figure>
<figure class="figure text-center mb-4"><img alt="UX mockup for the first QML based app" class="figure-img img-fluid gallery-img" height="800" src="/img/subscribers/qfield/qfieldcloud-now-opensource-happy-10-years-of-field-mapping-with-qgis/Legend2-2.webp" width="480"/>
<figcaption class="figure-caption text-center">UX mockup for the first QML based app</figcaption></figure>
<figure class="figure text-center mb-4"><img alt="UX mockup for the first QML based app" class="figure-img img-fluid gallery-img" height="800" src="/img/subscribers/qfield/qfieldcloud-now-opensource-happy-10-years-of-field-mapping-with-qgis/Map.webp" width="480"/>
<figcaption class="figure-caption text-center">UX mockup for the first QML based app</figcaption></figure>
<figure class="figure text-center mb-4"><img alt="Screenshots of the first QML based UI" class="figure-img img-fluid gallery-img" height="559" src="/img/subscribers/qfield/qfieldcloud-now-opensource-happy-10-years-of-field-mapping-with-qgis/Screenshot-from-2021-06-06-19-24-45_hu_fed565adac509b8a.webp" width="1200"/>
<figcaption class="figure-caption text-center">Screenshots of the first QML based UI</figcaption></figure>
</div>
<h3 id="the-python-failure">The Python failure</h3>
<p>Probably the major setback in QGIS for android’s history was the non-completion of the Python support. I got really close to it multiple times but unfortunately never managed to tame the snake. Maybe something we’ll look into in future, who knows.</p>
<p>/2013/05/20/python-support-in-qgis-is-getting-there/</p>
<p>/2013/05/21/getting-closer-to-taming-the-snake/</p>
<p>/2013/05/21/python-suport-even-closer/</p>
<h3 id="the-qgis-20-release">The QGIS 2.0 release</h3>
<p>The pivotal point of the Middle Ages was definitely 20.09.2013, when Tim Sutton presented to a full auditorium the shiny new QGIS 2.0. And along with it it introduced the general availability of QGIS 2.0 on android. The first real QGIS version for mobile devices was finally available for the broad public.</p>
<div class="gallery-wrapper">
<figure class="figure text-center mb-4"><img alt="" class="figure-img img-fluid gallery-img" height="750" src="/img/subscribers/qfield/qfieldcloud-now-opensource-happy-10-years-of-field-mapping-with-qgis/wpid-Screenshot_2013-09-19-01-19-31_hu_90c0960e974237bb.webp" width="1200"/></figure>
<figure class="figure text-center mb-4"><img alt="" class="figure-img img-fluid gallery-img" height="750" src="/img/subscribers/qfield/qfieldcloud-now-opensource-happy-10-years-of-field-mapping-with-qgis/wpid-Screenshot_2013-09-17-23-31-39_hu_25660962f6eca66.webp" width="1200"/></figure>
<figure class="figure text-center mb-4"><img alt="" class="figure-img img-fluid gallery-img" height="750" src="/img/subscribers/qfield/qfieldcloud-now-opensource-happy-10-years-of-field-mapping-with-qgis/wpid-Screenshot_2013-09-20-14-30-15_hu_e08d04e9b2d4aa1b.webp" width="1200"/></figure>
<figure class="figure text-center mb-4"><img alt="QField interface preview" class="figure-img img-fluid gallery-img" height="559" src="/img/subscribers/qfield/qfieldcloud-now-opensource-happy-10-years-of-field-mapping-with-qgis/Screenshot-from-2021-06-06-19-24-45_hu_fed565adac509b8a.webp" width="1200"/>
<figcaption class="figure-caption text-center">QField interface preview</figcaption></figure>
<figure class="figure text-center mb-4"><img alt="QField UI improvements" class="figure-img img-fluid gallery-img" height="1126" src="/img/subscribers/qfield/qfieldcloud-now-opensource-happy-10-years-of-field-mapping-with-qgis/Screenshot-from-2021-06-07-00-08-00_hu_63cce7b8819b50cc.webp" width="1200"/>
<figcaption class="figure-caption text-center">QField UI improvements</figcaption></figure>
</div>
<p>After the launch followed a very active time of keeping QGIS for Android on pair with the desktop versions leading to a regular release of updates on the playstore between 2013 and late 2014. This is also when Matthias Kuhn started committing to the QGIS for Android <a href="https://github.com/qgis/QGIS-Android/graphs/contributors" rel="noopener" target="_blank">repository</a>.</p>
<p><a href="https://vimeo.com/75261402" rel="noopener" target="_blank">https://vimeo.com/75261402</a></p>
<h2 id="early-modern---qfield-for-qgis-is-here">Early Modern - QField for QGIS is here</h2>
<p>Humanism, Renaissance and Enlightenment are what we saw happening in the period between 2015 and early 2019. Field users were put at the centre of the design process, new ideas were explored and a new name was chosen to reflect the main goal of the application: <strong>Make fieldwork as efficient as possible</strong>.</p>
<p>Early 2015 was also when Matthias Kuhn and myself decided to join forces in OPENGIS.ch LLC.</p>
<h3 id="the-rebranding">The rebranding</h3>
<p>The project never had a clear name, at times it was called QGIS for Android at times QGIS mobile, we felt that to clearly convey what we were building we needed a clear, simple and poignant name.</p>
<figure class="figure text-center mb-4"><img alt="" class="figure-img img-fluid gallery-img" height="173" src="/img/subscribers/qfield/qfieldcloud-now-opensource-happy-10-years-of-field-mapping-with-qgis/image-6_hu_b88224c07947e9ba.webp" width="1200"/></figure>
<blockquote>
<p>It is with great pleasure that we want to announce the new name for what was briefly known as QGIS mobile.</p>
<p><strong>Please welcome QField for QGIS™!</strong></p>
<p>After long thinking about various names and variants including QGIS mobile, QTouch, OPENGIS.ch QGIS mobile, QWork, and many more, we felt that QField represents best what we want to archive. A field data capture and management app fully compatible with QGIS™.</p>
<p><a href="https://qfield.org/2015/01/28/qgis-mobile-is-now-qfield/">/2015/01/28/qgis-mobile-is-now-qfield/</a></p></blockquote>
<p><a href="https://vimeo.com/116231850" rel="noopener" target="_blank">https://vimeo.com/116231850</a></p>
<figure class="figure text-center mb-4"><img alt="" class="figure-img img-fluid gallery-img" height="173" src="/img/subscribers/qfield/qfieldcloud-now-opensource-happy-10-years-of-field-mapping-with-qgis/image-7_hu_df695522d6ee81da.webp" width="1200"/></figure>
<blockquote>
<p>QField Experimental is out, after a couple of months of requirements gathering, private early alpha testing and foremost tons of  emails requesting access to the testes group we decided today to put the current BETA version in the playstore.</p>
<p><a href="https://qfield.org/2015/06/15/qfield-in-the-wild/">/2015/06/15/qfield-in-the-wild/</a></p></blockquote>
<h3 id="streamlined-installation">Streamlined installation</h3>
<p>Since the beginning of QGIS for android, to distribute the needed Qt libraries, we used a project called “ministro”. This was interesting because it allowed to download the libraries only once but on the other hand, it was a very painful experience for the user that needed to install a second app before getting QField to start. Around the end of 2015 it was so far, we finally managed to get rid of that dependency and make the installation process as streamlined as possible.</p>
<figure class="figure text-center mb-4"><img alt="" class="figure-img img-fluid gallery-img" height="183" src="/img/subscribers/qfield/qfieldcloud-now-opensource-happy-10-years-of-field-mapping-with-qgis/image-8_hu_c76ab8f008015bc1.webp" width="1200"/></figure>
<blockquote>
<p>It’s done, finally we managed to get rid of Ministro so that we finally can say, QField runs on any android from 4.0.3 (ICS). This makes as of today (according to <a href="https://developer.android.com/about/dashboards/index.html" rel="noopener" target="_blank">google</a>) 96% of the android installations worldwide.</p>
<p><a href="https://qfield.org/2015/12/01/qfield-for-android-5/">/2015/12/01/qfield-for-android-5/</a></p></blockquote>
<h2 id="release-candidates">Release candidates</h2>
<p>In these 3.5 years, a continuous, mainly volunteer-driven iterative process led by Matthias Kuhn made QField grow to the point where we felt confident it was time to launch QField 1.0.</p>
<p>After a series of release candidates with lots of feedback from the community, we felt it was time to move into a New Era.</p>
<figure class="figure text-center mb-4"><img alt="" class="figure-img img-fluid gallery-img" height="202" src="/img/subscribers/qfield/qfieldcloud-now-opensource-happy-10-years-of-field-mapping-with-qgis/image-9_hu_7ffd594959f60726.webp" width="1200"/></figure>
<blockquote>
<p>It was a long and winding road but we are very excited to announce the general availability of QField 1.0 Release Candidate 1.</p>
<p>Packed with loads of useful features like online and offline features digitizing, geometry and attributes editing, attribute search, powerful forms, theme switching, GPS support, camera integration and much more, QField is a powerful tool for those who need to edit on the go and would like to avoid standing in the swamp with a laptop or paper charts.</p>
<p><a href="https://qfield.org/2019/01/08/qfield-1-0-rc1/">/2019/01/08/qfield-1-0-rc1/</a></p></blockquote>
<h2 id="modern-times---qfield-1x">Modern times - QField 1.X</h2>
<p>Fast forward to March 28th 2019,</p>
<figure class="figure text-center mb-4"><img alt="" class="figure-img img-fluid gallery-img" height="214" src="/img/subscribers/qfield/qfieldcloud-now-opensource-happy-10-years-of-field-mapping-with-qgis/image-10_hu_f8e4247320ea5fa.webp" width="1200"/></figure>
<blockquote>
<p>Let’s get straight to the point</p>
<p><strong>It’s official, QField for QGIS 1.0 is out!</strong></p>
<p>Get it while it’s hot on the Playstore ( <a href="https://qfield.org/get" rel="noopener" target="_blank">qfield.org/get</a>) or on <a href="https://github.com/opengisch/QField/releases" rel="noopener" target="_blank">GitHub</a></p>
<p>We are incredibly pleased and proud of just having released such a jewel and are convinced that thanks to all its features and conscious design choices, QField will make your field digitizing work much more efficient and pleasant.</p>
<p><a href="https://qfield.org/2019/03/28/qfield-1-0-is-here/">/2019/03/28/qfield-1-0-is-here/</a></p></blockquote>
<h3 id="recent-releases">Recent releases</h3>
<p>In the last 2 years the development pace increased tremendously, the sponsored featured grew as never before, QField rating skyrocketed to 4.7 ⭐ we currently have 100'000 active users and we’re getting around 500 new users every day.</p>
<p>Our QField core team grew more and now thanks to David Signer’s lead and Mathieu Pellerin keen eye for UX we’re pushing QField even further.</p>
<figure class="figure text-center mb-4"><img alt="" class="figure-img img-fluid gallery-img" height="1126" src="/img/subscribers/qfield/qfieldcloud-now-opensource-happy-10-years-of-field-mapping-with-qgis/Screenshot-from-2021-06-07-00-08-00_hu_63cce7b8819b50cc.webp" width="1200"/></figure>
<p>Going into all releases would be so much information that this post would turn into a 3 volumes classic, and since starting from QField 1.0 we’ve documented each new release, we’re just going to link them: <a href="https://qfield.org/category/qfield/highlights/">/category/qfield/highlights/</a></p>
<h2 id="the-future-is-cloudy---ehm-sunny-of-course-">The future is cloudy - ehm sunny of course ;)</h2>
<p>Yesterday we published QField 1.9.6, which is going to be the last 1.X release and will put QField 2.0 into the beta channel so that every beta tester can start using <a href="https://qfield.cloud" rel="noopener" target="_blank">QFieldCloud</a> without having to use the <a href="https://play.google.com/store/apps/details?id=ch.opengis.qfield_dev" rel="noopener" target="_blank">developer version</a>.</p>
<p>But that is a different story and you can read all about it in our latest <a href="https://mailchi.mp/opengis.ch/seamless-fieldwork-with-qfieldcloud-is-around-the-corner#qfieldcloud" rel="noopener" target="_blank">newsletter</a>…</p>
