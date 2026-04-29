---
source: "blog"
title: "QField 3.6 “Gondwana”: Locking on greatness"
date: "2025-06-03T07:46:38+0000"
link: "https://qfield.org/blog/2025/06/03/qfield-3.6-gondwana-locking-on-greatness/"
draft: "false"
showcase: "planet"
subscribers: ["qfield"]
author: "QField"
tags: ["qfield", "highlights", "qgis", "qfield", "qgis.org"]
languages: ["en_gb"]
available_languages: ["en_gb"]
---

<p>Building on top of the last release which introduced background tracking, this development cycle focused on polishing functionalities and building on top of preexisting features. The variety of improvements is sure to make our diverse user base and community excited to upgrade to QField 3.6.</p>
<h2 id="main-highlights">Main highlights</h2>
<figure class="figure text-center mb-4"><img alt="" class="figure-img img-fluid gallery-img" height="736" src="/img/subscribers/qfield/qfield-3.6-gondwana-locking-on-greatness/splash_hu_d195f43e84a3cfc6.webp" width="1200"/></figure>
<p>One of the most noticeable improvement in this version is the addition of “map preview rendering”. <strong>QField now renders partial map content immediately beyond the edge of the screen</strong>, offering a much nicer experience when panning around as well as zooming in and out. Long-time QGIS users will recognise the behaviour, and we’re delighted to bring this experience to the field</p>
<p>This upgrade was the foundation upon which we built the following enhancement: as of QField 3.6, <strong>using the “lock to position” mode now keeps your position at the very center of the screen while the canvas slips through smoothly</strong>. This greatly improves the usability of the function as your eyes never need to spend time locating the position within the screen: it’s dead center and it stays there!</p>
<p><a href="https://videopress.com/v/kJg69l49?resizeToParent=true&amp;cover=true&amp;preloadContent=metadata&amp;useAverageColor=true" rel="noopener" target="_blank">https://videopress.com/v/kJg69l49?resizeToParent=true&amp;cover=true&amp;preloadContent=metadata&amp;useAverageColor=true</a></p>
<p><em>Reminder, the “lock to position” mode is activated by clicking on the bottom-right positioning button, with the button’s background turning blue when the mode is activated.</em></p>
<p>The improvements did not stop there. Panning and zooming around used to drop users out of the lock mode immediately. While this had its upsides, it also meant that simple scale adjustments to try and view more of the map as it follows the position was not possible. With QField 3.6, <strong>the lock has been hardened. Moving the map around will temporarily disable the lock, with a visual countdown embedded within a toast message informs users of when the lock will return</strong>. An action button to terminate the lock is located within the toaster to permanently leave the mode.</p>
<p>Moving on to QFieldCloud, this cycle saw tons of improvements. To begin with, <strong>it is now possible to rely on shared datasets across multiple cloud projects</strong>. Known as localised data paths in QGIS, this functionality enables users to reduce storage usage by storing large datasets in QFieldCloud only once, serving multiple cloud projects, and also easing the maintenance of read-only datasets that require regular updates.</p>
<figure class="figure text-center mb-4"><img alt="" class="figure-img img-fluid gallery-img" height="632" src="/img/subscribers/qfield/qfield-3.6-gondwana-locking-on-greatness/upload_shared_datasets.webp" width="690"/></figure>
<p><em>QFieldSync users will see a new checkbox when synchronising their projects, letting them upload shared datasets onto QFieldCloud.</em></p>
<p>Furthermore, <strong>QField has</strong> <strong>introduced a new cloud project details view to provide additional details</strong> on QFieldCloud-hosted projects before downloading them to devices. The new view includes a cloud project thumbnail, more space for richer description text, including interactive hyperlinks, and author details, as well as creation and data update timestamps. Finally, the view offers a QR code, which allows users to scan it quickly and access cloud projects, provided they have the necessary access permission. Distributing a public project has never been easier!</p>
<p>Beyond that, tons more has made its way into QField, including <strong>map layer notes viewable through a legend badge</strong> in the side dashboard, <strong>support for feature identification on online raster layers</strong> on compatible WMS and ArcGIS REST servers, <strong>atlas printing of a relationship’s child feature</strong> directly within the parent feature form, and much more. There’s something for everybody out there.</p>
<h2 id="focus-on-feature-form-polishing">Focus on feature form polishing</h2>
<p>This new version of QField coincides with the release of <strong><a href="https://qfield.org/2025/06/02/xlsform-converter-unlock-a-world-of-surveys-with-our-brand-new-qgis-plugin/">XLSForm Converter</a></strong>, a new QGIS plugin created by OPENGIS.ch’s very own ninjas. As its title implies, the plugin converts an <a href="https://xlsform.org/en/" rel="noopener" target="_blank">XLSForm spreadsheet file (.xls, .xlsx, .ods)</a> into a full-fledged QGIS project ready to be used in QField with a pre-configured survey layer matching the content of the provided XLSForm.</p>
<p>This was a golden opportunity to focus on polishing QField’s feature form. As a result, advanced functionalities such as <strong>data-driven editable flag and label attribute properties are now supported</strong>. In addition, tons of paper-cut bugs, visual inconsistencies, and UX shortcomings have been addressed. Our favourite one might just be the ability to drag the feature addition drawer’s header up and down to toggle its full-screen state :)</p>
