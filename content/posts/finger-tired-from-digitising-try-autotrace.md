---
source: "blog"
title: "Finger Tired From Digitising? Try AutoTrace"
date: "2014-02-11T12:30:25-0600"
link: "https://lutraconsulting.co.uk/blog/2014/02/11/finger-tired-from-digitising-try-autotrace/"
draft: "false"
showcase: "planet"
subscribers: ["lutragis"]
author: "Lutra Consulting"
tags: []
---

<p>My first brush with GIS was back in 2004. I was just getting into building river models and spent a considerable amount of time digitising model inputs. These would often include tens and sometimes hundreds of kilometres of river banks. Many of the input features (e.g. flood embankments) would be traced to snap exactly to existing polygon features.</p>

<p>This was not a big issue at the time as MapInfo had a really nice autotrace feature which made these tasks a doddle. However, when I moved to QGIS I could not find such a feature.</p>

<p><img alt="AutoTrace in Action" src="https://www.lutraconsulting.co.uk/img/posts/autotrace.gif" /></p>

<p>The image above shows AutoTrace in action. <strong>Please see the <a href="https://www.lutraconsulting.co.uk/projects/trace_digitizing/">AutoTrace project page</a></strong> for full documentation and a list of co-funders.</p>

<!-- more -->

<h2>Origins of AutoTrace Development</h2>

<p>The idea to develop a plugin to do MapInfo-style tracing was born at the QGIS developer conference (AKA Hackfest) in Lisbon in early 2011. It was there that Paolo Cavalini pointed me towards the traceDigitize plugin already developed by C&eacute;dric M&ouml;ri. traceDigitize already supported tracing but required the user to move the cursor along the edge of the feature being traced. I still had my heart set on achieving that MapInfo-style tracing.</p>

<p>Rather than re-inventing the wheel, traceDigitize was modified to add MapInfo-style tracing as an optional component. This was my development focus for the HF (and the flight back). At this stage the basic functionality was in-place but the plugin had many bugs and was not reliable to use. Unfortunately the plugin was mothballed until recently.</p>

<h2>Release of AutoTrace</h2>

<p>It was at the first QGIS UK User Group that I met Matt Travis (GIS Officer at Dartmoor NPA) and we got talking about AutoTrace. It transpired that there were a number of local government organisations interested in getting this auto-tracing functionality into QGIS. We soon had commitment from a number of organisations (including and organised by Kevin Williams at Neath Port Talbot Council) to fund the work required to release a stable version of the tool.</p>

<h2>Future Plans</h2>

<p>There's talk of extending the functionality of AutoTrace to also implement some of he more complex tracing techniques seen in ArcGIS. If this is something you'd be interested in then please let us know.</p>

<p>Many thanks to all those who have supported us in this project.</p>

    <div class="input-promo">
    <h2>You may also like...</h2>
    <a href="https://merginmaps.com">Mergin Maps, a field data collection app based on QGIS</a>. Mergin Maps makes field work easy with its simple interface and cloud-based sync. Available on Android, iOS and Windows.
    <img alt="Screenshots of the Mergin Maps mobile app for Field Data Collection" src="https://lutraconsulting.co.uk/img/posts/input_app_for_field_data_collection.jpg" /><br />
    <a href="https://play.google.com/store/apps/details?id=uk.co.lutraconsulting&amp;utm_source=lutra-atom&amp;utm_medium=lutra-blog-footer&amp;utm_campaign=input">
      <img alt="Get it on Google Play" src="https://play.google.com/intl/en_us/badges/images/generic/en_badge_web_generic.png" width="180px" />
    </a>
    <a href="https://apps.apple.com/us/app/input/id1478603559?ls=1&amp;utm_source=lutra-atom&amp;utm_medium=lutra-blog-footer&amp;utm_campaign=input">
      <img alt="Get it on Apple store" src="https://www.lutraconsulting.co.uk/img/posts/App_Store.svg" style="padding-top: 0px;" width="144px" />
    </a>
  </div>
