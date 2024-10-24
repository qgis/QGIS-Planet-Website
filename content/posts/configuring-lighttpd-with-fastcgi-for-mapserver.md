---
source: "blog"
title: "Configuring Lighttpd with FastCGI for MapServer"
date: "2006-10-17T18:31:47+0000"
link: "http://spatialgalaxy.net/2006/10/17/configuring-lighttpd-with-fastcgi-for-mapserver/"
draft: "false"
showcase: "planet"
subscribers: ["spatialgalaxy_net"]
author: "Spatial Galaxy"
tags: []
---

In an effort to obtain a faster and lightweight solution, I decided to use Lighttpd (AKA Lighty) with FastCGI to power MapServer. Snooping around the MapServer site yielded no clues on how to configure Lighty. It turns out to be fairly simple.
Here is the Lighttpd configuration:
fastcgi.server = ( "/maps" = ( "localhost" = ( "socket" = "/tmp/mapserver-fastcgi.socket", "check-local" = "disable", "bin-path" = "/usr/lib/cgi-bin/mapserv", "min-procs" = 1, "max-procs" = 6, "
