---
source: "blog"
title: "QGIS 4.2: novità tra espressioni e tabella attributi"
date: "2026-07-04T00:00:00+0000"
link: "https://hfcqgis.opendatasicilia.it/blog/2026/07/04/qgis-42-novit%C3%A0-tra-espressioni-e-tabella-attributi/"
draft: "false"
showcase: "planet"
subscribers: ["hfcqgis"]
author: "HfcQGIS"
tags: ["qgis", "blog", "espressioni", "funzioni", "novita", "qgis-4-2", "tabella attributi"]
languages: ["it_it"]
available_languages: ["it_it"]
---

<h1>QGIS 4.2: novità tra espressioni e tabella attributi</h1> <h2>Introduzione</h2> <p><a href="https://changelog.qgis.org/en/qgis/version/4.2/">QGIS 4.2</a> è una release con 59 nuove feature, distribuite su 17 categorie e realizzate da 24 sviluppatori diversi. Il grosso del lavoro si concentra su <strong>3D</strong> e <strong>Symbology</strong>, seguiti da correzioni notevoli e da novità su point cloud e processing:</p> <p>| Categoria | Feature | |---|--:| | 3D Features | 12 | | Symbology | 10 | | Notable Fixes | 8 | | Point Clouds | 6 | | Processing | 5 | | Print Layouts | 3 | | Data Providers | 3 | | Expressions | 2 | | QGIS Server | 2 | | Breaking Changes | 1 | | User Interface | 1 | | Data Management | 1 | | Application and Project Options | 1 | | Sensors | 1 | | Profile Plots | 1 | | Browser | 1 | | Programmability | 1 |</p> <p>Buona parte del lavoro porta la firma di Nyall Dawson (North Road), autore di quasi un terzo delle feature:</p> <p>| # | Sviluppatore | Feature | Azienda | |--:|---|--:|---| | 1 | Nyall Dawson | 19 | North Road | | 2 | Dominik Cindric | 9 | — | | 3 | Jean Felder | 3 | Oslandia | | 4 | Julien Cabieces | 3 | Oslandia | | 5 | Martin Dobias | 3 | Lutra Consulting | | 6 | Stefanos Natsis | 3 | Lutra Consulting | | 7 | Mathieu Pellerin | 2 | OPENGIS.ch |</p> <p>In questo panorama, le <strong>espressioni</strong> ricevono "solo" 2 nuove funzioni (categoria Expressions), ma sono entrambe di uso quotidiano nel Field Calc, e la <strong>tabella attributi</strong> guadagna una scorciatoia molto pratica verso la calcolatrice di campi (categoria Data Management). Sono proprio questi due ambiti il focus di questo post: vediamo nel dettaglio le novità, con particolare attenzione alle espressioni e alla tabella attributi.</p> <p>!!! Abstract "In breve" <strong>2 nuove funzioni</strong>: <code>scale_cubic_bezier</code> (interpolazione con curva di Bézier cubica) e <code>concat_ws</code> (concatenazione con separatore). <strong>Tabella attributi</strong>: voce "Field Calculator" nel menu delle intestazioni di colonna. Inoltre alcuni fix rilevanti a <code>concat()</code>, all'operatore IN con <code>nodes()</code> e a crash della calcolatrice di campi.</p>
