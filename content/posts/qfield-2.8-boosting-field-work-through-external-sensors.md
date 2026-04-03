---
source: "blog"
title: "QField 2.8: Boosting field work through external sensors"
date: "2023-05-30T04:00:00+0000"
link: "https://qfield.org/blog/2023/05/30/qfield-2.8-boosting-field-work-through-external-sensors/"
draft: "false"
showcase: "planet"
subscribers: ["qfield"]
author: "QField"
tags: ["gis", "qfield", "highlights", "qgis.org"]
languages: ["en_gb"]
available_languages: ["en_gb"]
---

<p>The latest version of QField is out, featuring as its main new feature sensor handling alongside the usual round of user experience and stability improvements. We simply can’t wait to see the sensor uses you will come up with!</p>
<figure class="figure text-center mb-4"><img alt="" class="figure-img img-fluid gallery-img" height="596" src="/img/subscribers/qfield/qfield-2.8-boosting-field-work-through-external-sensors/238116107-1792bb88-9fdb-41e7-9716-7fd65f8837ce.webp" width="925"/></figure>
<h2 id="the-main-highlight-sensors"><strong>The main highlight: sensors</strong></h2>
<p>QField 2.8 ships with <strong>out-of-the-box handling of external sensor streams</strong> over TCP, UDP, and serial port. The functionality allows for data captured through instruments – such as geiger counter, decibel sensor, CO detector, etc. - to be visualized and manipulated within QField itself.</p>
<p>Things get really interesting when sensor data is utilized as default values alongside positioning during the digitizing of features. You are always one tap away from adding a point locked onto your current position with spatially paired sensor readings saved as point attribute(s).</p>
<p>Not wowed yet? Try pairing sensor readings with QField’s tracking capability! ;) Head over <a href="https://docs.qfield.org/how-to/sensors/" rel="noopener" target="_blank">QField’s documentation on this</a> as well as <a href="https://docs.qgis.org/testing/en/docs/user_manual/introduction/qgis_configuration.html#sensors-properties" rel="noopener" target="_blank">QGIS’ section on sensor management</a> to know more.</p>
<p>The development of this feature involved the addition of a sensor framework in upstream QGIS which will be available by the end of this coming June as part of the 3.32 release. This is a great example of the synergy between QField and its big brother QGIS, whereas development of new functionality often benefits the broader QGIS community. Big thanks to <a href="https://sevenson.com/" rel="noopener" target="_blank">Sevenson Environmental Services</a> for sponsoring this exciting capability.</p>
<h2 id="notable-improvements"><strong>Notable improvements</strong></h2>
<p>A couple of refinements during this development cycle are worth mentioning. If you ever wished for QField to <strong>directly open a selected project or reloading the last session on app launch</strong>, you’ll be happy to know this is now possible.</p>
<p>For heavy users of value relations in their feature forms, QField is now a tiny bit more clever when displaying string searches against long lists, placing hits that begin with the matched string first as well as visually highlighting matches within the result list itself.</p>
<p>Finally, feature lists throughout QField are now sorted. By default, it will sort by the display field or expression defined for each vector layer, unless an advanced sorting has been defined in a given vector layer’s attribute table. It makes browsing through lists feel that much more natural.</p>
