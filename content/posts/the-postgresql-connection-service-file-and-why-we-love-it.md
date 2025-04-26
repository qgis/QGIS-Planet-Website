---
source: "blog"
title: "The PostgreSQL Connection Service File and Why We Love It"
date: "2024-05-28T13:18:00+0000"
link: "https://www.opengis.ch/2024/05/28/the-postgresql-connection-service-file-and-why-we-love-it/"
draft: "false"
showcase: "planet"
subscribers: ["opengisch"]
author: "OPENGIS.ch blog"
tags: ["interlis", "postgresql", "qgis", "qgis plugins", "qgis.org"]
languages: ["en_gb"]
available_languages: ["en_gb"]
---

<p><strong><em>The PostgreSQL Connection Service File <code>pg_service.conf</code> is nothing new. It has existed for quite some time and maybe you have already used it sometimes too. But not only the new QGIS plugin <a href="https://github.com/opengisch/qgis-pg-service-parser-plugin">PG service parser</a> is a reason to write about our love for this file, as well we generally think it’s time to show you how it can be used for really cool things.</em></strong></p>
<h2 class="wp-block-heading"><strong>What is the Connection Service File?</strong></h2>
<p>The Connection Service File allows you to save connection settings for each so-called “service” locally.</p>
<p>So when you have a database called <code>gis</code> on a local PostgreSQL with port <code>5432</code> and username/password is <code>docker</code>/<code>docker</code> you can store this as a service called <code>my-local-gis</code>.</p>
<pre class="wp-block-code"><code># Local GIS Database for Testing purposes
</code></pre>


[my-local-gis]



<p>host=localhost port=5432 dbname=gis user=docker password=docker</p>
<p>This Connection Service File is called <code>pg_service.conf</code> and is by client applications (such as <a href="https://www.postgresql.org/docs/current/app-psql.html">psql</a> or <a href="https://qgis.org/en/site/">QGIS</a>) generally found directly in the user directory. In Windows it is then found in the user’s application directory <code>postgresql.pg_service.conf</code>. And in Linux it is by default located directly in the user’s directory <code>~/.pg_service.conf</code>. </p>
<p>But it doesn’t necessarily have to be there. The file can be anywhere on the system (or on a network drive) as long as you set the environment variable <code>PGSERVICEFILE</code> accordingly:</p>
<pre class="wp-block-code"><code>export PGSERVICEFILE=/home/dave/connectionfiles/pg_service.conf </code></pre>
<p>Once you have done this, the client applications will search there first – and find it.</p>
<p>If the above are not set, there is also another environment variable <code>PGSYSCONFDIR</code> which is a folder which is searched for the file <code>pg_service.conf</code>.</p>
<p>Once you have this, the service name can be used in the client application. That means in <a href="https://www.postgresql.org/docs/current/app-psql.html">psql</a> it would look like this:</p>
<pre class="wp-block-code"><code>~$ psql service=my-local-gis
psql (14.11 (Ubuntu 14.11-0ubuntu0.22.04.1), server 14.5 (Debian 14.5-1.pgdg110+1))
SSL connection (protocol: TLSv1.3, cipher: TLS_AES_256_GCM_SHA384, bits: 256, compression: off)
Type "help" for help.

gis=#</code></pre>
<p>And in QGIS like this:</p>
<figure class="wp-block-image"><img alt="" class="wp-image-14336" height="310" src="/img/subscribers/opengisch/the-postgresql-connection-service-file-and-why-we-love-it/image.webp" width="1279"/></figure>
<p>If you then add a layer in QGIS, only the name of the service is written in the project file. Neither the connection parameters nor username/password are saved. In addition to the security aspect, this has various advantages, more on this below.</p>
<p>But you don’t have to pass all of these parameters to a service. If you only pass parts of them (e.g. without the database), then you have to pass them when the connection is called:</p>
<pre class="wp-block-code"><code>$psql "service=my-local-gis dbname=gis"
psql (14.11 (Ubuntu 14.11-0ubuntu0.22.04.1), server 14.5 (Debian 14.5-1.pgdg110+1))
SSL connection (protocol: TLSv1.3, cipher: TLS_AES_256_GCM_SHA384, bits: 256, compression: off)
Type "help" for help.

gis=#</code></pre>
<p>You can also override parameters. If you have a database <code>gis</code> configured in the service, but you want to connect the database web, you can specify the service and explicit the database:</p>
<pre class="wp-block-code"><code>$psql "service=my-local-gis dbname=web"
psql (14.11 (Ubuntu 14.11-0ubuntu0.22.04.1), server 14.5 (Debian 14.5-1.pgdg110+1))
SSL connection (protocol: TLSv1.3, cipher: TLS_AES_256_GCM_SHA384, bits: 256, compression: off)
Type "help" for help.

web=#</code></pre>
<p>Of course the same applies to QGIS.</p>
<p>And regarding the environment variables mentioned, you can also set a standard service.</p>
<pre class="wp-block-code"><code>export PGSERVICE=my-local-gis</code></pre>
<p>Particularly pleasant in daily work with always the same database.</p>
<pre class="wp-block-code"><code>$ psql
psql (14.11 (Ubuntu 14.11-0ubuntu0.22.04.1), server 14.5 (Debian 14.5-1.pgdg110+1))
SSL connection (protocol: TLSv1.3, cipher: TLS_AES_256_GCM_SHA384, bits: 256, compression: off)
Type "help" for help.

gis=#</code></pre>
<h2 class="wp-block-heading"><strong>And why is it particularly cool?</strong></h2>
<p>There are several reasons why such a file is useful:</p>
<ul class="wp-block-list">
<li>Security: You don’t have to save the connection parameters anywhere in the client files (e.g. QGIS project files). Keep in mind that they are still plain text in the service file.</li>
<li>Decoupling: You can change the connection parameters without having to change the settings in client files (e.g. QGIS project files).</li>
<li>Multi-User: You can save the file on a network drive. As long as the environment variable of the local systems points to this file, all users can access the database with the same parameters.</li>
<li>Diversity: You can use the same project file to access different databases with the same structure if only the name of the service remains the same.</li>
</ul>
<p>For the last reason, here are three use cases.</p>
<h3 class="wp-block-heading"><strong>Support-Case</strong></h3>
<p>Someone reports a problem in QGIS on a specific case with their database. Since the problem cannot be reproduced, they send us a DB dump of a schema and a QGIS project file. The layers in the QGIS project file are linked to a service. Now we can restore the dump on our local database and access it with our own, but same named, service. The problem can be reproduced.</p>
<h3 class="wp-block-heading"><strong>INTERLIS</strong></h3>
<p>With INTERLIS the structure of a database schema is precisely specified. If e.g. the canton has built the physical database for it and configured a supernice QGIS project, they can provide the project file to a company without also providing the database structure. The company can build the schema based on the INTERLIS model on its own PostgreSQL database and access it using its own service with the same name.</p>
<h3 class="wp-block-heading"><strong>Test/Prod Switching</strong></h3>
<p>You can access a test and a production database with the same QGIS project if you have set the environment variable for the connection service file accordingly per <a href="https://docs.qgis.org/3.34/de/docs/user_manual/introduction/qgis_configuration.html#user-profiles">QGIS profile</a>.</p>
<p>You create two connection service files.</p>
<p>The one to the test database<code> /home/dave/connectionfiles/test/pg_service.conf</code>:</p>
<pre class="wp-block-code"><code>[my-local-gis]
host=localhost
port=54322
dbname=gis-test</code></pre>
<p>And the one for the production database <code>/home/dave/connectionfiles/prod/pg_service.conf</code>:</p>
<pre class="wp-block-code"><code>[my-local-gis]
host=localhost
port=54322
dbname=gis-productive</code></pre>
<p>In QGIS you create two profiles “Test” and “Prod”:</p>
<figure class="wp-block-image"><img alt="" src="/img/subscribers/opengisch/the-postgresql-connection-service-file-and-why-we-love-it/unknown/image_T2cjxkNM.webp"/></figure>
<p>And you set the environment variable for each profile <code>PGSERVICEFILE</code> which should be used (in the menu <em>Settings &gt; Options…</em> and there under <em>System</em> scroll down to <em>Environment</em></p>
<figure class="wp-block-image"><img alt="image" src="/img/subscribers/opengisch/the-postgresql-connection-service-file-and-why-we-love-it/unknown/image_EEIJ5716.webp"/></figure>
<p>or</p>
<figure class="wp-block-image"><img alt="image" src="/img/subscribers/opengisch/the-postgresql-connection-service-file-and-why-we-love-it/unknown/image_jOP9v7G8.webp"/></figure>
<p>If you now use the service <code>my-local-gis</code> in a QGIS layer, it connects the database <code>prod</code> in the “Prod” profile and the database <code>test</code> in the “Test” profile.</p>
<h2 class="wp-block-heading"><strong>The authentication configuration</strong></h2>
<p>Let’s have a look at the authentication. If you have the connection service file on a network drive and make it available to several users, you may not want everyone to access it with the same login. Or you generally don’t want any user information in this file. This can be elegantly combined with the authentication configuration in QGIS.</p>
<p>If you want to make a QGIS project file available to multiple users, you create the layers with a service. This service contains all connection parameters except the login information.</p>
<p>This login information is transferred using QGIS authentication.</p>
<figure class="wp-block-image"><img alt="image" src="/img/subscribers/opengisch/the-postgresql-connection-service-file-and-why-we-love-it/unknown/image_3eAcHyu3.webp"/></figure>
<p>You also configure this authentication per QGIS profile we mentioned above. This is done via Menu <em>Settings &gt; Options…</em> and there under <em>Authentication</em>:</p>
<figure class="wp-block-image"><img alt="image" src="/img/subscribers/opengisch/the-postgresql-connection-service-file-and-why-we-love-it/unknown/image_NkLwesBO.webp"/></figure>
<p>(or directly where you create the PostgreSQL connection)</p>
<p>If you add such a layer, the service and the ID of the authentication configuration are saved in the QGIS project file. This is in this case <code>mylogin</code>. Of course this name must be communicated to the other users so that they can also set  the ID for their login to <code>mylogin</code>.</p>
<p>Of course, you can use multiple authentication configurations per profile.</p>
<h2 class="wp-block-heading"><strong>QGIS Plugin</strong></h2>
<p>And yes, there is now a great plugin to configure these services directly in QGIS. This means you no longer have to deal with text-based INI files. It’s called <a href="https://github.com/opengisch/qgis-pg-service-parser-plugin">PG service parser</a>:</p>
<figure class="wp-block-image"><img alt="image" src="/img/subscribers/opengisch/the-postgresql-connection-service-file-and-why-we-love-it/unknown/image_b9Jx43dD.webp"/></figure>
<p>It finds the connection service file according to the mentioned environment variables <code>PGSERVICEFILE</code> or <code>PGSYSCONFDIR</code> or at its default location.</p>
<p>As well it’s super easy to create new services by duplicating existing ones.</p>
<figure class="wp-block-image"><img alt="" src="/img/subscribers/opengisch/the-postgresql-connection-service-file-and-why-we-love-it/unknown/image_8Pyz0R22.webp"/></figure>
<h3 class="wp-block-heading">And for the Devs</h3>
<p>And what would a blog post be without some geek food? The back end of this plugin is published on <a href="https://pypi.org/project/pgserviceparser/">PYPI</a> and can be easily installed with <code>pip install pgserviceparser </code>and then be used in Python.</p>
<p>For example to list all the service names. </p>
<pre class="wp-block-code"><code>&gt;&gt;&gt; import pgserviceparser
&gt;&gt;&gt; pgserviceparser.service_names()
['my-local-gis', 'another-local-gis', 'opengisch-demo-pg']</code></pre>
<p>Optionally you can pass a config file path. Otherwise it gets it by the mentioned mechanism.</p>
<p>Or to receive the configuration from the given service name as a dict.</p>
<pre class="wp-block-code"><code>&gt;&gt;&gt; pgserviceparser.service_config('my-local-gis')
{'host': 'localhost', 'port': '54322', 'dbname': 'gis', 'user': 'docker', 'password': 'docker'}</code></pre>
<p>There are some more functions. Check them out here on <a href="https://github.com/opengisch/pgserviceparser">GitHub</a> or in the <a href="https://opengisch.github.io/pgserviceparser/">documentation</a>.</p>
<h2 class="wp-block-heading">Well then</h2>
<p>We hope you share our enthusiasm for this beautiful file – at least after reading this blog post. And if not – feel free to tell us why you don’t in the comments <img alt="🙂" class="wp-smiley" src="/img/subscribers/opengisch/the-postgresql-connection-service-file-and-why-we-love-it/1f642.webp" style="height: 1em;"/></p>
