---
source: "blog"
title: "QField 2.6: perfecting high-accuracy positioning"
date: "2023-01-26T06:46:00+0000"
link: "https://qfield.org/blog/2023/01/26/qfield-2.6-perfecting-high-accuracy-positioning/"
draft: "false"
showcase: "planet"
subscribers: ["qfield"]
author: "QField"
tags: ["qfield", "highlights", "qgis.org"]
languages: ["en_gb"]
available_languages: ["en_gb"]
---

<p>It’s only been a few weeks into the new year, but we’ve got great news for you: a brand new QField 2.6 “Geeky Gecko ?” has been released with a focus on positioning improvements, including Bluetooth support for Windows. And with that, we are delighted to remove the ‘beta’ status from QField for Windows.</p>
<h2 id="new-positioning-features">New positioning features</h2>
<figure class="figure text-center mb-4"><img alt="" class="figure-img img-fluid gallery-img" height="501" src="/img/subscribers/qfield/qfield-2.6-perfecting-high-accuracy-positioning/26_cover-1.webp" width="800"/></figure>
<p><strong>Let’s open with a bang: QField 2.6 now supports NMEA streaming from external GNSS devices over TCP, UDP, and serial ports, in addition to preexisting Bluetooth connectivity.</strong> This new functionality means that QField is now compatible with a much larger range of GNSS devices out there.</p>
<p>These new receivers unlock NTRIP-driven centimetre accuracy for devices that use the Bluetooth connection to a manufacturer’s application to connect to NTRIP servers. In this scenario, QField could not initiate a Bluetooth connection since it was already taken. With the new TCP and UDP receivers - provided the manufacturer’s application offers NMEA streaming over either of those Internet protocols - QField can connect and consume high-accuracy positioning.</p>
<p>The presence of a serial port receiver provides support for external GNSS devices using Bluetooth on Windows via the virtual serial port created by the operating system. The lack of Bluetooth support on Windows was a long-wanted enhancement from QField users on that platform and was the last blocker for the ‘beta’ status to go away.</p>
<p><strong>In addition, QField 2.6 allows users to pick from half a dozen metrics a value to attach to the measure (M) dimension of geometries being digitized when locked to the current position.</strong> This functionality is available to both users digitizing and the positioning tracker. The measurement values available as of 2.6 are timestamp, ground speed, bearing, horizontal accuracy and vertical accuracy, as well as PDOP, HDOP and VDOP values.</p>
<h2 id="growing-continuous-integration-ci-testing-framework-now-covers-positioning">Growing Continuous Integration (CI) testing framework now covers positioning</h2>
<p>Starting with version 2.6, <strong>QField ships with increased quality assurances</strong> thanks to the addition of tests covering positioning functionalities in its growing CI framework.</p>
<p>Practically speaking, this means that every single line of QField code changed is now being tested against positioning-related regression, significantly decreasing the risks of shipping a new version of QField with broken functionality in the area of antenna height, vertical grid shift, and ellipsoidal height adjustments.</p>
<p>We would like to commend <a href="https://www.bahn.com/en" rel="noopener" target="_blank">Deutsche Bahn</a> for funding the required work here. This could not have come in soon enough as more and more people are opting for QField and relying on it for their crucial day-to-day fieldwork.</p>
