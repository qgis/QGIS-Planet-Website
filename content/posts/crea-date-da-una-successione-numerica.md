---
source: "blog"
title: "Crea date da una successione numerica"
date: "2023-11-30T00:00:00+0000"
link: "https://hfcqgis.opendatasicilia.it/blog/2023/11/30/crea-date-da-una-successione-numerica/"
draft: "false"
showcase: "planet"
subscribers: ["hfcqgis"]
author: "HfcQGIS"
tags: ["qgis", "blog", "data", "espressioni", "intervallo"]
languages: ["it_it"]
available_languages: ["it_it"]
---

<h1>Crea date da una successione numerica</h1> <h2>Introduzione</h2> <p>Data una data iniziale e una serie di numeri da 0 a 999, popolare un attributo <em>data</em> che segue il seguente pattern: a 0 corrisponde la data 01/01/2019, a 1 corrisponde la data 02/01/2019 e così via fino a 999, ovvero 26/09/2021.</p> <p>!!! Abstract "make_date &amp; make_interval" <strong>Queste due funzioni permettono di risolvere il quesito esposto sopra, vediamo come</strong></p>
