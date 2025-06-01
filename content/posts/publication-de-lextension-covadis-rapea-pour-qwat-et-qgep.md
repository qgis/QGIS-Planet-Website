---
source: "blog"
title: "Publication de l&#8217;extension COVADIS RAPEA pour QWAT et QGEP"
date: "2020-08-26T10:07:51"
link: "https://oslandia.com/en/2020/08/25/publication-de-lextension-covadis-rapea-pour-qwat-et-qgep/"
draft: "false"
showcase: "planet"
subscribers: ["qgis_oslandia"]
author: "QGIS Oslandia"
tags: ["gis", "non classé", "qgis", "postgis", "water"]
languages: ["en_gb"]
available_languages: ["en_gb"]
---

<div class="wpb_row vc_row-fluid vc_row standard_section" id="fws_683c441b8b0f1" style="padding-top: 0px; padding-bottom: 0px;"><div class="row-bg-wrap"><div class="inner-wrap"> <div class="row-bg"></div></div> </div><div class="col span_12 dark left">
<div class="vc_col-sm-12 wpb_column column_container vc_column_container col no-extra-padding">
<div class="vc_column-inner">
<div class="wpb_wrapper">
<div class="wpb_text_column wpb_content_element">
<div class="wpb_wrapper">
<p><a href="https://qwat.github.io/docs/master/en/html/index.html">QWAT</a> est une application open source de gestion des réseaux d’eau potable <a href="http://qwat.org/history/">émanant</a> des collectivités de Pully, le SIGE à Vevey, Morges et Lausanne.<br/>
<a href="https://qgep.github.io/docs/fr/">QGEP</a> est son homologue dédiée à la gestion des eaux usées et pluviales, initiée par <a href="https://www.qgis.ch/fr">le groupe utilisateur QGIS Suisse</a>.</p>
<p>L’échange de données entre institutions est une pierre angulaire des politiques de l’eau. Ces échanges se basent sur des formats d’échanges standardisés. Ainsi les Cantons de Fribourg (format <a href="https://www.fr.ch/energie-agriculture-et-environnement/eau/aquafri-le-cadastre-des-infrastructures-deau-potable">aquaFRI</a>) ou de Vaud (format <a href="https://www.vd.ch/themes/environnement/eaux/eau-potable/systeme-dinformation-des-reseaux-deau-sire/">SIRE</a>) conditionnent certaines subventions publiques à la transmission des données selon des formats pré-définis et permettent à ces échelons administratifs d’avoir une vision globale des réseaux humides.</p>
<p>Dans le cadre d’une expérimentation des outils QWAT (eau potable) et QGEP (eaux usées), <a href="https://charente-eaux.fr/le-syndicat/qui-sommes-nous/">Charentes Eaux</a> a souhaité mettre en œuvre des extensions dédiées au standard d’échange de données sur les réseaux d’eau Français, le Géostandard <a href="http://www.geoinformations.developpement-durable.gouv.fr/geostandard-reseaux-d-adduction-d-eau-potable-et-d-a3478.html">Réseaux d’adduction d’eau potable et d’assainissement (RAEPA)</a> défini par la <a href="http://www.geoinformations.developpement-durable.gouv.fr/covadis-r425.html">Commission de validation des données pour l’information spatialisée (COVADIS)</a>.</p>
<p>Oslandia a été mandaté pour mettre en œuvre des instances de QWAT et QGEP, réaliser les extensions RAEPA pour chacun de ces outils, et aider Charente Eaux à charger les données des collectivités membres de ce syndicat mixte.</p>
<p>https://charente-eaux.fr/le-syndicat/qui-sommes-nous/</p>
<p>Le travail a été publié pour QWAT sous forme d’une <em>extension standardisée</em> dans le dépôt l’organisation QWAT https://github.com/qwat/extension_fr_raepa/</p>
<p>Pour QGEP, il n’existe pas encore de fonctionnalité pour gérer d’extension, le dépôt https://gitlab.com/Oslandia/qgep_extension_raepa/ contient donc les définitions de données et de vues à rajouter manuellement au modèle de données.</p>
<p>La compatibilité des modèles de données a été évaluée et le choix a été fait de ne faire que des vues dédiées à l’export de données. Il est techniquement possible de faire des vues éditables pour permettre le chargement de données via ces vues depuis des fichiers suivant le gabarit de données RAEPA. Le niveau de simplification et d’agrégation des listes de valeurs rend ce travail peu générique dans l’état actuel du géostandard (v1.1), il est donc plus pertinent à ce stade de réaliser des scripts de chargement sans passer par ce pivot dans le cas de Charente-Eaux</p>
</div>
</div>
</div>
</div>
</div>
</div></div>
