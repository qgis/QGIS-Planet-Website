---
source: "blog"
title: "Mergin and PostGIS in action"
date: "2021-01-10T18:00:01-0600"
link: "https://lutraconsulting.co.uk/blog/2021/01/10/mergin-dbsync/"
draft: "false"
showcase: "planet"
subscribers: ["lutragis"]
author: "Lutra Consulting"
tags: []
---

<p>One of the challenges of data collection projects is consolidating all the data a central database, such as Postgres/PostGIS. Using PostGIS as a live survey layer is not usually recommended:</p>
<ul>
  <li>Security: exposing your database to the wider internet</li>
  <li>Access and connectivity: internet connection is not always guaranteed for field survey projects</li>
</ul>

<p>A more cumbersome way around this, is to convert your tables from PostGIS to a file based GIS layer (e.g. GeoPackage) and take the files with you to the field. This will create a new problem: keeping all the tables (from multiple surveyors) and the PostGIS table up-to-date.</p>

<p>During a survey to assess water access for villages in Limpopo province, South Africa, our friends at <a href="https://kartoza.com/en/">Kartoza</a> have commissioned us to extend the Mergin service to support PostGIS. The Mergin service already supports file-based data synchronisation. The aim was to bridge the gap between the Mergin service and PostGIS so that the changes from Mergin immediately appear on PostGIS and vice versa.</p>

<p>To facilitate that, we further developed <a href="https://github.com/lutraconsulting/geodiff/">the Geodiff library</a> to support Postgres driver. In addition, we developed <a href="https://github.com/lutraconsulting/mergin-db-sync">mergin-db-sync tool</a> to sync the tables from Postgres database with the Mergin service. The mergin-db-sync tool runs as a service (daemon) that keeps an eye on a particular Mergin project, and if there is a new version of the project, it will fetch the most recent changes and apply them to database tables in PostgreSQL. It works also the other way around at the same time: it looks for changes in the configured PostgreSQL schema and upload them in a new version of the Mergin project if any changes were detected. This service can be easily started on the local Intranet (where the PostgreSQL database is run) and therefore it does not need any adjustments to the firewall to allow access to the local database from public Internet.</p>

<p><img alt="DB-Sync schema" src="https://www.lutraconsulting.co.uk/img/posts/dbsync-scheme.png" /></p>

<p>The above diagram details how Postgres/PostGIS synchronisation works with the Mergin service via the DB-Sync tool.</p>

<ul>
  <li>Tables 1 and 2 from the Postgres/PostGIS server are set up to work with the Mergin service</li>
  <li>DB-Sync tool runs on a server on a regular interval to sync with the Mergin service</li>
  <li>An offline version of Tables 1 and 2 are provided within the QGIS survey project on Mergin</li>
  <li>Several surveyors download the project and add their data mostly while offline. The data are then synced with the Mergin.</li>
</ul>

<p>From the surveyors’ point of view, the extra set up to sync with the Postgres/PostGIS does not affect their workflow. In fact, <a href="https://github.com/lutraconsulting/mergin-db-sync">mergin-db-sync tool</a> acts as another client syncing data to the Mergin project, therefore it is possible to see all the changes in the project log originated from <a href="https://github.com/lutraconsulting/mergin-db-sync">mergin-db-sync tool</a>.</p>

<p>The tool is available on <a href="https://github.com/lutraconsulting/mergin-db-sync">GitHub</a> with a permissive open source license (MIT). At this point it supports PostgreSQL, but the mechanism is fairly generic and support for other database engines may be added in the future without great effort. All the heavy lifting is done by <a href="https://github.com/lutraconsulting/geodiff/">the Geodiff library</a> which has been significantly enhanced during the development of <a href="https://github.com/lutraconsulting/mergin-db-sync">mergin-db-sync tool</a>.</p>

<p>To try the tool, please follow the instructions on the <a href="https://github.com/lutraconsulting/mergin-db-sync/blob/master/README.md">project’s readme on GitHub</a>. The easiest way is to use it in a <a href="https://github.com/lutraconsulting/mergin-db-sync/blob/master/Dockerfile">Docker container</a>.</p>

<p>If you have any issues or feedback to enhance the tool, you can <a href="https://github.com/lutraconsulting/mergin-db-sync/issues">file a ticket on the project repo</a>.</p>

<p>If you’d like to set up DB-Sync tool with your Mergin survey projects, you can contact us on info@lutraconsulting.co.uk</p>
