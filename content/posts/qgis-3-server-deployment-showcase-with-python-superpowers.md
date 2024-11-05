---
source: "blog"
title: "QGIS 3 Server deployment showcase with Python superpowers"
date: "2018-03-20T13:38:54+0000"
link: "https://www.itopen.it/qgis-3-server-deployment-showcase-with-python-superpowers/"
draft: "false"
showcase: "planet"
subscribers: ["itopen"]
author: "ItOpen"
tags: ["qgis", "qgis server"]
---

<p>Recently I was invited by the colleagues from <a href="http://www.opengis.ch/">OpenGIS.ch</a> to lend a hand in a training session about QGIS server.</p>
<p>This was a good opportunity to update my presentation for QGIS3, to fix a few bugs and to explore the powerful capabilities of QGIS server and Python.</p>
<p>As a result, I published the full recipe of a Vagrant VM on github: <a href="https://github.com/elpaso/qgis3-server-vagrant#qgis-server-3x-vagrant-testing-vms-with-apache-and-nginx">https://github.com/elpaso/qgis3-server-vagrant</a></p>
<p>The presentation is online here: <a href="http://www.itopen.it/bulk/qgis3-server/">http://www.itopen.it/bulk/qgis3-server/</a></p>
<p>What&#8217;s worth mentioning is the sample plugins (I&#8217;ll eventually package and upload them to the official plugin site):</p>
<ul>
	<li>XYZ: add simple XYZ tile server, ready to use within QGIS XYZ connections: <a href="https://github.com/elpaso/qgis3-server-vagrant/tree/master/resources/web/plugins/xyz">https://github.com/elpaso/qgis3-server-vagrant/tree/master/resources/web/plugins/xyz</a></li>
	<li>custom service, does nothing but shows how to create a Python custom service by exploiting the new service capabilities available in QGIS3: <a href="https://github.com/elpaso/qgis3-server-vagrant/tree/master/resources/web/plugins/customservice">https://github.com/elpaso/qgis3-server-vagrant/tree/master/resources/web/plugins/customservice</a></li>
	<li>HTTP Basic auth (how to add your auth scheme to QGIS server): <a href="https://github.com/elpaso/qgis3-server-vagrant/tree/master/resources/web/plugins/httpbasic">https://github.com/elpaso/qgis3-server-vagrant/tree/master/resources/web/plugins/httpbasic</a></li>
	<li>more &#8230;</li>
</ul>
<p>&nbsp;</p>
<p>The VM uses 4 different (although similar) deployment strategies:</p>
<ul>
	<li>good old Apache + mod_fcgi and plain CGI</li>
	<li>Nginx + Fast CGI</li>
	<li>Nginx + standalone HTTP Python wrapped server</li>
	<li>Nginx + standalone WSGI Python wrapped server</li>
</ul>
<p>Have fun with QGIS server: it was completely refactored in QGIS 3 and it&#8217;s now better than ever!</p>
<p>&nbsp;</p><p>The post <a href="https://www.itopen.it/qgis-3-server-deployment-showcase-with-python-superpowers/">QGIS 3 Server deployment showcase with Python superpowers</a> first appeared on <a href="https://www.itopen.it">Open Web Solutions, GIS & Python Development</a>.</p>
