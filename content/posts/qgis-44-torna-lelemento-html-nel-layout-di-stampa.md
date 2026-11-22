---
source: "blog"
title: "QGIS 4.4: torna l'elemento HTML nel layout di stampa"
date: "2026-11-21T00:00:00+0000"
link: "https://hfcqgis.opendatasicilia.it/blog/2026/11/21/qgis-44-torna-lelemento-html-nel-layout-di-stampa/"
draft: "false"
showcase: "planet"
subscribers: ["hfcqgis"]
author: "HfcQGIS"
tags: ["qgis", "blog", "espressioni", "html", "layout di stampa", "novita", "qgis-4-4", "tabella attributi"]
languages: ["it_it"]
available_languages: ["it_it"]
---

<h1>QGIS 4.4: torna l'elemento HTML nel layout di stampa</h1> <h2>Introduzione</h2> <p><a href="https://changelog.qgis.org/en/qgis/version/4.4/">QGIS 4.4 Auckland</a>, rilasciata il 20 novembre 2026, è la <strong>candidata alla Long Term Release (LTR)</strong>: dopo alcuni cicli di correzione diventerà la versione stabile di riferimento per il prossimo anno. Il changelog conta 48 feature in 18 categorie, e il grosso del lavoro si concentra su <strong>Processing</strong> e sulle correzioni:</p> <p>| Categoria | Feature | |---|--:| | Processing | 11 | | Notable Fixes | 9 | | 3D Features | 4 | | QGIS Server | 3 | | Symbology, Annotations, Labelling, Rendering, Expressions, Data Management, Programmability | 2 ciascuna | | Documentation, User Interface, Print Layouts, Digitising, Forms and Widgets, Application and Project Options, Profile Plots | 1 ciascuna |</p> <p>Anche questa volta la firma più ricorrente è quella di Nyall Dawson (North Road), autore di 21 feature su 48.</p> <p>La novità che però interessa di più a chi produce cartografia e report <strong>non compare nel changelog</strong>: con QGIS 4.4 torna a funzionare l'<strong>elemento HTML nel layout di stampa</strong>, che con il passaggio a Qt6 era rimasto di fatto inutilizzabile.</p> <p>!!! Abstract "In breve" <strong>Layout di stampa</strong>: l'elemento HTML torna a essere renderizzato ed esportato, ora con il motore QtWebEngine al posto di QtWebKit (<a href="https://github.com/qgis/QGIS/pull/68161">PR #68161</a>). <strong>Espressioni</strong>: nuovi argomenti per <code>uuid</code> (UUID v7) ed <code>extend</code> (angoli di deviazione). <strong>Tabella attributi e moduli</strong>: pulsante di aiuto e widget QML modificabile. Inoltre DB Manager lascia definitivamente il core e diversi strumenti idrologici di SAGA diventano algoritmi nativi.</p>
