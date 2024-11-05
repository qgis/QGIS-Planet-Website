---
source: "blog"
title: "A little QGIS3 Server wsgi experiment"
date: "2017-07-29T17:04:41+0000"
link: "https://www.itopen.it/a-little-qgis3-server-wsgi-experiment/"
draft: "false"
showcase: "planet"
subscribers: ["itopen"]
author: "ItOpen"
tags: ["qgis server"]
---

Here is a little first experiment for a wsgi wrapper to QGIS 3 Server, not much tested, but basically working:

&nbsp;
<pre class="wp-code-highlight prettyprint">
#!/usr/bin/env python

# Simple QGIS 3 Server wsgi test

import signal
import sys
from cgi import escape, parse_qs
from urllib.parse import quote
# Python&#039;s bundled WSGI server
from wsgiref.simple_server import make_server

from qgis.core import QgsApplication
from qgis.server import *

# Init QGIS
qgs_app = QgsApplication([], False)
# Init server
qgs_server = QgsServer()


def reconstruct_url(environ):
    &quot;&quot;&quot;Standard algorithm to retrieve the full URL from wsgi request
    From: https://www.python.org/dev/peps/pep-0333/#url-reconstruction
    &quot;&quot;&quot;
    url = environ[&#039;wsgi.url_scheme&#039;]+&#039;://&#039;

    if environ.get(&#039;HTTP_HOST&#039;):
        url += environ[&#039;HTTP_HOST&#039;]
    else:
        url += environ[&#039;SERVER_NAME&#039;]

        if environ[&#039;wsgi.url_scheme&#039;] == &#039;https&#039;:
            if environ[&#039;SERVER_PORT&#039;] != &#039;443&#039;:
                url += &#039;:&#039; + environ[&#039;SERVER_PORT&#039;]
        else:
            if environ[&#039;SERVER_PORT&#039;] != &#039;80&#039;:
                url += &#039;:&#039; + environ[&#039;SERVER_PORT&#039;]

    url += quote(environ.get(&#039;SCRIPT_NAME&#039;, &#039;&#039;))
    url += quote(environ.get(&#039;PATH_INFO&#039;, &#039;&#039;))
    if environ.get(&#039;QUERY_STRING&#039;):
        url += &#039;?&#039; + environ[&#039;QUERY_STRING&#039;]
    return url

def application (environ, start_response):

    headers = {} # Parse headers from environ here if needed

    # the environment variable CONTENT_LENGTH may be empty or missing
    # When the method is POST the variable will be sent
    # in the HTTP request body which is passed by the WSGI server
    # in the file like wsgi.input environment variable.
    try:
        request_body_size = int(environ.get(&#039;CONTENT_LENGTH&#039;, 0))
        request_body = environ[&#039;wsgi.input&#039;].read(request_body_size)
    except (ValueError):
        request_body_size = 0
        request_body = None

    request = QgsBufferServerRequest(reconstruct_url(environ), (QgsServerRequest.PostMethod 
        if environ[&#039;REQUEST_METHOD&#039;] == &#039;POST&#039; else QgsServerRequest.GetMethod), {}, request_body)
    response = QgsBufferServerResponse()
    qgs_server.handleRequest(request, response)
    headers_dict = response.headers()
    try:
        status = headers_dict[&#039;Status&#039;]
    except KeyError:
        status = &#039;200 OK&#039;
    start_response(status, [(k, v) for k, v in headers_dict.items()])
    return [bytes(response.body())]

# Instantiate the server
httpd = make_server (
    &#039;localhost&#039;, # The host name
    8051, # A port number where to wait for the request
    application # The application object name, in this case a function
)

print(&quot;Listening to http://localhost:8051 press CTRL+C to quit&quot;)

def signal_handler(signal, frame):
    &quot;&quot;&quot;Exit QGIS cleanly&quot;&quot;&quot;
    global qgs_app
    print(&quot;\nExiting QGIS...&quot;)
    qgs_app.exitQgis()
    sys.exit(0)

signal.signal(signal.SIGINT, signal_handler)

httpd.serve_forever()

</pre>
&nbsp;<p>The post <a href="https://www.itopen.it/a-little-qgis3-server-wsgi-experiment/">A little QGIS3 Server wsgi experiment</a> first appeared on <a href="https://www.itopen.it">Open Web Solutions, GIS & Python Development</a>.</p>
