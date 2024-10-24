---
source: "blog"
title: "Rasters in the Database---Why Bother?"
date: "2008-02-15T06:34:29+0000"
link: "http://spatialgalaxy.net/2008/02/15/rasters-in-the-database-why-bother/"
draft: "false"
showcase: "planet"
subscribers: ["spatialgalaxy_net"]
author: "Spatial Galaxy"
tags: []
---

I&rsquo;ve come to the conclusion that storing rasters in a database is of dubious value, particularly from a data warehouse perspective.
If you manage a collection of rasters that are updated on a frequent basis, storing them in a relational database with ArcSDE quickly becomes a pain. I&rsquo;m not talking about a dozen or so rasters, but rather tens of thousands. The overhead of the database and middleware just doesn&rsquo;t seem to be worth it.
