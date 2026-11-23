---
source: "blog"
title: "QompliGIS 2.0: New features for validating your geographic data"
date: "2026-11-19T16:29:35"
link: "https://oslandia.com/en/2026/11/23/qompligis-2-0-de-nouvelles-fonctionnalites-pour-valider-vos-donnees-geographiques/"
draft: "false"
showcase: "planet"
subscribers: ["qgis_oslandia"]
author: "QGIS Oslandia"
tags: ["news", "open source", "qgis", "open source", "plugin qgis"]
languages: ["en_gb"]
available_languages: ["en_gb"]
---

<p dir="auto"><img alt="" class="wp-image-10861 alignleft" height="119" src="/img/subscribers/qgis_oslandia/qompligis-2-0-de-nouvelles-fonctionnalites-pour-valider-vos-donnees-geographiques/logo-qompligis.webp" width="122"/></p>
<p>We are pleased to announce the release of a new version of QompliGIS. This QGIS plugin, launched by Oslandia in 2021, has reached a new milestone, with new features and a more user-friendly interface.</p>
<p>Three major new features are available in QompliGIS.</p>
<h2>Constraints on attribute fields</h2>
<p>QompliGIS now allows you to add validity constraints on the attribute values of fields. There are three types of constraints:</p>
<ul dir="auto">
<li>minimum and/or maximum value constraints;</li>
<li>relational constraints between two tables in the dataset;</li>
<li>regular expression constraints on text fields.</li>
</ul>
<h2><img alt="" class="aligncenter size-full wp-image-10866" height="732" src="/img/subscribers/qgis_oslandia/qompligis-2-0-de-nouvelles-fonctionnalites-pour-valider-vos-donnees-geographiques/qompligis-en-1.webp" width="1095"/>The end of dependence on source data</h2>
<p>Verifying compliance for a dataset no longer requires access to the reference dataset used to build that configuration. The configuration file alone provides all the necessary information: coordinate system, list of files and fields, minimum and maximum area and length, and so on. The fields in the interface are pre-filled with values from the reference dataset, but you can modify them if you wish. This simplifies the process.</p>
<p dir="auto"><img alt="" class="aligncenter size-full wp-image-10867" height="759" src="/img/subscribers/qgis_oslandia/qompligis-2-0-de-nouvelles-fonctionnalites-pour-valider-vos-donnees-geographiques/qompligis-en-2.webp" width="1086"/>However, this new version does not allow you to retrieve your old configuration files and use them directly without their reference data. You will need to generate new configurations based on the data.</p>
<h2>QGIS 4 Compatibility</h2>
<p>QompliGIS has also been made compatible with QGIS 4, which means it is now compatible with Qt 6, among other things.</p>
<p>For more details on the changes in this new version, please see the project’s <a href="https://gitlab.com/Oslandia/qgis/qompligis/-/blob/master/CHANGELOG.md?ref_type=heads">CHANGELOG</a>.</p>
<p>Now it’s your turn to test the new version of QompliGIS on your datasets. You can take this opportunity to update your configuration files.</p>
<p>Feel free to contact us at <a href="mailto:infos@oslandia.com">infos@oslandia.com</a> if you think QompliGIS is a software component that meets your needs and you’d like to help improve it!</p>
<p> </p>
