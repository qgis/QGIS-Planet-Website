---
source: "blog"
title: "Upgrading PostGIS in a Database with Large Objects"
date: "2007-10-28T07:12:46+0000"
link: "http://spatialgalaxy.net/2007/10/28/upgrading-postgis-in-a-database-with-large-objects/"
draft: "false"
showcase: "planet"
subscribers: ["spatialgalaxy_net"]
author: "Spatial Galaxy"
tags: []
---

Following the instructions for a &ldquo;hard&rdquo; upgrade in Chapter 2. Installation of the PostGIS manual results in large objects not being restored to the database. If you create a dump using pg_dump -Fc &ndash;oids and then use the postgis_restore.pl script, the oids will be restored but not the large objects. This is not really a PostGIS issue, it can happen when dealing with any PostgreSQL database.
To remedy this situation I found that the pg_dumplo utility has the answer.
