---
source: "blog"
title: "QGIS Abstract Connections API"
date: "2020-01-17T11:59:51+0000"
link: "https://www.itopen.it/qgis-abstract-connections-api/"
draft: "false"
showcase: "planet"
subscribers: ["itopen"]
author: "ItOpen"
tags: ["qgis"]
---

<p>&nbsp;</p>
<p>The goal of the new API is twofold:</p>
<ol>
	<li>provide a unified way to store and retrieve data provider connections in the QGIS settings</li>
	<li>provide an abstract set of methods to perform most common operation on DB data sources (e.g. browse tables, drop/create a table/schema, run arbitrary SQL commands etc.)</li>
</ol>
<p>&nbsp;</p>
<p>The new API is documented in <a href="https://qgis.org/api/classQgsAbstractProviderConnection.html">https://qgis.org/api/classQgsAbstractProviderConnection.html</a> and it provides a few specializations for DB connections (<a href="https://qgis.org/api/classQgsAbstractDatabaseProviderConnection.html">https://qgis.org/api/classQgsAbstractDatabaseProviderConnection.html</a>) and an initial PR implementation for web service-based connections (<a href="https://github.com/qgis/QGIS/pull/33045">https://github.com/qgis/QGIS/pull/33045</a>).</p>
<p>&nbsp;</p>
<p>While the whole of the desired refactoring work was too big for a single grant request, the first work package has been completed and the following data providers have been partially or totally refactored to make use of the new connections API:</p>
<ul>
	<li>postgres</li>
	<li>geopackage (OGR)</li>
	<li>spatialite</li>
</ul>
<p>&nbsp;</p>
<p>The new API was also used to implement the automatic loading of layer dependencies (not part of the grant program).</p>
<p>&nbsp;</p>
<p>For developers interested in working with the new API, a set Python tests are available to show how to use the methods:  <a href="https://github.com/qgis/QGIS/blob/master/tests/src/python/test_qgsproviderconnection_ogr_gpkg.py">https://github.com/qgis/QGIS/blob/master/tests/src/python/test_qgsproviderconnection_ogr_gpkg.py</a> (see also the postgres and spatialite companion tests).</p>
<p>&nbsp;</p>
<p>There is still a large amount of work to be done in order to complete all the desired refactoring and to remove all the Python and C++ code that will be ultimately be made redundant. In particular, future work should be undertaken to:</p>
<ul>
	<li>port all remaining data providers to the new API</li>
	<li>refactor and eliminate the remaining DB-manager connectors to make use of the abstract API</li>
	<li>eliminate duplicate and untested code inside the Processing framework for working with Postgres databases and port the code to the new, stable, well-tested API</li>
	<li>refactor and eliminate the remaining QGIS browser data items to make use of the abstract API </li>
</ul>
<p>&nbsp;</p>
<p>For further information, the following paragraphs (taken from the original grant proposal) will provide full details about the background of this work.</p>
<h2>Background/motivation</h2>
<ul>
	<li>DB-Manager is an important part of the QGIS interface, which allows browsing/previews of different DB-based data sources, complex queries, management of layers, import-export etc., DB creation and deletion etc.</li>
	<li>After the QGIS 3.0 release, improvements within the core browser widgets implemented in C++ have resulted in a (constantly growing) degree of overlapping functionality between the browser and db manager.</li>
	<li>After QGIS 3 API improvements concerning layer import and export functionality, there are many duplicated implementations between browser and db manager &#8211; some functionality is better in browser, some functionality is better in db manager. Users are forced to choose between two competing semi-complete alternatives, instead of having one, complete, well integrated solution.</li>
	<li>There are no unit tests for DB-Manager and this leads to frequent regressions, which (aside from being frustrating for users) consume a substantial part of our development time and budget during the bugfixing programs. Furthermore the nature of large Python codebases like db manager makes it very easy to accidentally break functionality with no warning or errors during development.</li>
</ul>
<p>&nbsp;</p>
<h2>Proposed solution</h2>
<p>We propose to start refactoring the DB-manager plugin functionality into core C++ implementation, reusing existing core API and replacing redundant duplicate functionality.</p>
<p>The clear advantages are:</p>
<ul>
	<li>no duplicate functionality, so it&#8217;s easier for users to understand and use</li>
	<li>more usage of well-tested and well-maintained core C++ API</li>
	<li>testability and immediate feedback on API breaks (an advantage of C++ is that the application won’t even build if an API is changed or accidentally misused)</li>
	<li>better performance</li>
	<li>the ability to expose database management functionality via stable PyQGIS API, allowing other plugins and scripts to utilise this functionality. In future, Processing algorithms may also be developed which would take advantage of these functions (e.g. “create schema”, “drop table”, “vacuum table” algorithms)</li>
	<li>DB management functionality would be available within the main QGIS window (from the Browser panel), instead of as a separate dialog.</li>
</ul>
<p>&nbsp;</p>
<h2>Grant proposal package</h2>
<p>The above mentioned work is too large to be completed within a single grant, so what we propose here is to start the refactoring needed in order to have a core stable C++ API that can be used by the application and the plugins and that will be available to fully move DB manager to C++ API in the future avoiding duplication of code and functionality.</p>
<ul>
	<li>create an interface for databases that expose the required functions to a coherent API</li>
	<li>add missing tests and documentation for the a.m. API</li>
	<li>porting some basic functions from db manager to the new api:

<ul>
	<li>create table (with native field types support)</li>
	<li>create schema</li>
	<li>delete table</li>
	<li>Rename table</li>
</ul>
</li>
</ul>
<p>The API will be exposed through the browser and it will be used by the DB manager instead of the Python implementation that is currently used.</p><p>The post <a href="https://www.itopen.it/qgis-abstract-connections-api/">QGIS Abstract Connections API</a> first appeared on <a href="https://www.itopen.it">Open Web Solutions, GIS & Python Development</a>.</p>
