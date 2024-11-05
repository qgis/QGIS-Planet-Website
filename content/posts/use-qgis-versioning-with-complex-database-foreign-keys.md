---
source: "blog"
title: "QGIS Versioning now supports foreign keys!"
date: "2019-09-30T07:52:54"
link: "https://oslandia.com/en/2019/09/30/use-qgis-versioning-with-complex-database-foreign-keys/"
draft: "false"
showcase: "planet"
subscribers: ["qgis_oslandia"]
author: "QGIS Oslandia"
tags: ["database", "gis", "news", "", "open source", "postgresql", "python", "qgis", "versionning"]
---

<p><strong>QGIS-versioning</strong> is a <strong>QGIS</strong> and <strong>PostGIS</strong> plugin dedicated to data versioning and history management. It supports :</p>
<ul>
<li>Keeping <strong>full table history</strong> with all modifications</li>
<li>Transparent access to <strong>current data</strong></li>
<li><strong>Versioning</strong> tables with branches</li>
<li>Work <strong>offline</strong></li>
<li>Work on a data <strong>subset</strong></li>
<li><strong>Conflict management</strong> with a GUI</li>
</ul>
<div class="wp-caption aligncenter" style="width: 560px;"><img class="" height="300" src="https://oslandia.com/wp-content/uploads/2017/01/versioning_11-1024x558.png" width="550" /><p class="wp-caption-text">QGIS versioning conflict management</p></div>
<p>In a previous <a href="https://oslandia.com/en/2013/07/13/qgis-versioning-plugin/">blog article</a> we detailed how QGIS versioning can manage data history, branches, and work offline with PostGIS-stored data and QGIS. We recently added <strong>foreign key support</strong> to QGIS versioning so you can now historize any complex database schema.</p>
<p>This QGIS plugin is available in the official <a href="https://plugins.qgis.org/plugins/qgis_versioning/">QGIS plugin repository</a>, and <a href="https://github.com/Oslandia/qgis-versioning">you can fork it on GitHub too</a> !</p>
<h2>Foreign key support</h2>
<h3>TL;DR</h3>
<p>When a user decides to historize its PostgreSQL database with QGIS-versioning, the plugin alters the existing database schema and adds new fields in order to track down the different versions of a single table row. Every access to these versioned tables are subsequently made through updatable views in order to automatically fill in the new versioning fields.</p>
<p>Up to now, it was not possible to <strong>deal with primary keys and foreign keys : </strong>the original tables had to be constraints-free.  This limitation has been lifted thanks to this contribution.</p>
<p>To make it simple, the solution is to remove all constraints from the original database and transform them into a set of SQL check triggers installed on the working copy databases (SQLite or PostgreSQL). As verifications are made on the client side, it&#8217;s impossible to propagate invalid modifications on your base server when you &#8220;commit&#8221; updates.</p>
<h3>Behind the curtains</h3>
<p>When you choose to historize an existing database, a few fields are added to the existing table. Among these fields, <em>versioning_id</em>identifies  one specific version of a row. For one existing row, there are several versions of this row, each with a different <em>versioning_id</em> but with the same original primary key field. As a consequence, that field cannot satisfy the unique constraint, so it cannot be a key, therefore no foreign key neither.</p>
<p>We therefore have to drop the primary key and foreign key constraints when historizing the table. Before removing them, constraints definitions are stored in a dedicated table so that these constraints can be checked later.</p>
<p>When the user checks out a specific table on a specific branch, QGIS-versioning uses that constraint table to build constraint checking triggers in the working copy. The way constraints are built depends on the checkout type (you can checkout in a SQLite file, in the master PostgreSQL database or in another PostgreSQL database).</p>
<h3>What do we check ?</h3>
<p>That&#8217;s where the fun begins ! The first thing we have to check is key uniqueness or foreign key referencing an existing key on insert or update. Remember that there are no primary key and foreign key anymore, we dropped them when activating historization. We keep the term for better understanding.</p>
<p>You also have to deal with deleting or updating a referenced row and the different ways of propagating the modification : cascade, set default, set null, or simply failure, as explained in PostgreSQL <a href="https://www.postgresql.org/docs/11/ddl-constraints.html">Foreign keys documentation</a> .</p>
<p>Nevermind all that, this problem has been solved for you and everything is done automatically in QGIS-versioning. Before you ask, yes foreign keys spanning on multiple fields are also supported.</p>
<h3>What&#8217;s new in QGIS ?</h3>
<p>You will get a new message you probably already know about, when you try to make an invalid modification committing your changes to the master database</p>
<p><img alt="" class="alignnone size-full wp-image-5087" height="269" src="https://oslandia.com/wp-content/uploads/2019/09/erreur_commit-1.png" width="1004" /></p>
<p>Error when foreign key constraint is violated</p>
<h3>Partial checkout</h3>
<p>One existing Qgis-versioning feature is <em>partial checkout</em>. It allows a user to select a subset of data to checkout in its working copy. It avoids downloading gigabytes of data you do not care about. You can, for instance, checkout features within a given spatial extent.</p>
<p>So far, so good. But if you have only a part of your data, you cannot ensure that modifying a data field as primary key will keep uniqueness. In this particular case, QGIS-versioning will trigger errors on commit, pointing out the invalid rows you have to modify so the unique constraint remains valid.</p>
<p><img alt="" class="alignnone size-full wp-image-5085" height="221" src="https://oslandia.com/wp-content/uploads/2019/09/erreur_commit_2.png" width="1235" /></p>
<p>Error when committing non unique key after a partial checkout</p>
<h3>Tests</h3>
<p>There is a lot to check when you intend to replace the existing constraint system with your own constraint system based on triggers. In order to ensure QGIS-Versioning stability and reliability, we put some special effort on building a test set that cover all use cases and possible exceptions.</p>
<h2>What&#8217;s next</h2>
<p>There is now no known limitations on using QGIS-versioning on any of your database. If you think about a missing feature or just want to know more about QGIS and QGIS-versioning, feel free to contact us at <a href="mailto:infos+data@oslandia.com">infos+data@oslandia.com</a>. And please have a look at our <a href="https://qgis.oslandia.com">support offering for QGIS</a>.</p>
<p>Many thanks to <a href="https://www.ehealthafrica.org/"><strong>eHealth Africa </strong></a>who helped us develop these new features. <strong>eHealth Africa</strong> is a non-governmental organization based in Nigeria. Their mission is to build stronger health systems through the design and implementation of data-driven solutions.</p>
<h3><a href="https://www.ehealthafrica.org/"><img alt="" class="size-medium wp-image-4299 aligncenter" height="124" src="https://oslandia.com/wp-content/uploads/2019/05/ehealth-300x124.png" width="300" /></a></h3>
