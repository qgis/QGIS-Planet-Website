---
source: "blog"
title: "QGIS 4.2: DB Manager lascia il core (ma non subito)"
date: "2026-07-04T00:00:00+0000"
link: "https://hfcqgis.opendatasicilia.it/blog/2026/07/04/qgis-42-db-manager-lascia-il-core-ma-non-subito/"
draft: "false"
showcase: "planet"
subscribers: ["hfcqgis"]
author: "HfcQGIS"
tags: ["qgis", "blog", "db manager", "novita", "plugin", "qgis-4-2"]
languages: ["it_it"]
available_languages: ["it_it"]
---

<h1>QGIS 4.2: DB Manager lascia il core (ma non subito)</h1> <h2>Introduzione</h2> <p>Chi usa QGIS da anni conosce bene <strong>DB Manager</strong>: il pannello che permette di sfogliare, interrogare e gestire i database supportati (PostGIS, SpatiaLite, GeoPackage...) direttamente dall'interfaccia, senza uscire dal programma. Con QGIS 4.2 questo strumento smette di essere parte del core e diventa un plugin di terze parti, con un percorso di transizione più complicato del previsto.</p> <p>Ne ho parlato in una <a href="https://discourse.osgeo.org/t/drop-db-manager/154234">discussione aperta su OSGeo Discourse</a>: questo post riprende e approfondisce quel filo, incrociando la proposta ufficiale, le pull request e la mailing list degli sviluppatori.</p> <p>!!! Abstract "In breve" DB Manager viene "degradato" a plugin community per il <a href="https://github.com/qgis/QGIS-Enhancement-Proposals/blob/master/qep-426-demote_dbmanager.md">QEP-426</a>: troppa duplicazione con il Browser Panel, poca copertura di test, manutenzione onerosa. La rimozione completa dal core (<a href="https://github.com/qgis/QGIS/pull/66545">PR #66545</a>) è ancora <strong>aperta e discussa</strong>; per la 4.2 è stato invece mergiato un approccio più graduale (<a href="https://github.com/qgis/QGIS/pull/66613">PR #66613</a>): un avviso di deprecazione all'avvio con un pulsante per installare la versione community. Il plugin, però, è al momento <strong>bloccato</strong> nel repository ufficiale da oltre 100 warning di sicurezza.</p>
