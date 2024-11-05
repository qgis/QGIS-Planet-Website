---
source: "blog"
title: "Getting multipolygon vertexes using PostGIS"
date: "2015-11-06T00:49:01+0000"
link: "https://gisunchained.wordpress.com/2015/11/06/getting-multipolygon-vertexes-using-postgis/"
draft: "false"
showcase: "planet"
subscribers: ["alexandre_netos_blog"]
author: "Alexandre Neto's blog"
tags: ["uncategorized", "postgis"]
---

<p>EN | <a href="https://sigsemgrilhetas.wordpress.com/?p=625">PT</a></p>
<p>Today I needed to create a view in <a href="http://postgis.net/">PostGIS</a> that returned the vertexes of a multi-polygon layer. Besides, I needed that they were numerically ordered starting in 1, and with the respective XY coordinates.</p>
<p><img alt="Screenshot from 2015-11-05 23:58:19" class="aligncenter size-full wp-image-645" height="411" src="https://gisunchained.files.wordpress.com/2015/11/screenshot-from-2015-11-05-235819.png" width="660" /></p>
<p>It seemed to be a trivial task – all I would need was to use the <a href="http://postgis.net/docs/ST_DumpPoints.html">ST_DumpPoints()</a> function to get all vertexes – if it wasn&#8217;t for the fact that PostGIS polygons have a duplicate vertex (the last vertex must be equal to the first one) that I have no interess in showing.</p>
<p>After some try-and-fail, I came up with the following query:</p>
<pre class="brush: sql; title: ; notranslate">
CREATE OR REPLACE VIEW public.my_polygons_vertexes AS
WITH t AS -- Transfor polygons in sets of points
    (SELECT id_polygon,
            st_dumppoints(geom) AS dump
     FROM public.my_polygons),
f AS -- Get the geometry and the indexes from the sets of points 
    (SELECT t.id_polygon,
           (t.dump).path[1] AS part,
           (t.dump).path[3] AS vertex,
           (t.dump).geom AS geom
     FROM t)
-- Get all points filtering the last point for each geometry part
SELECT row_number() OVER () AS gid, -- Creating a unique id
       f.id_polygon,
       f.part,
       f.vertex,
       ST_X(f.geom) as x, -- Get point's X coordinate
       ST_Y(f.geom) as y, -- Get point's Y coordinate
       f.geom::geometry('POINT',4326) as geom -- make sure of the resulting geometry type
FROM f 
WHERE (f.id_polygon, f.part, f.vertex) NOT IN
      (SELECT f.id_polygon,
              f.part,
              max(f.vertex) AS max
       FROM f
       GROUP BY f.id_polygon,
                f.part);
</pre>
<p>The interesting part occurs in the WHERE clause, basically, from the list of all vertexes, only the ones not included in the list of vertexes with the maximum index by polygon part are showed, that is, the last vertex of each polygon part.</p>
<p>Here&#8217;s the result:</p>
<p><a href="https://gisunchained.files.wordpress.com/2015/11/screenshot-from-2015-11-05-235840.png"><img alt="Screenshot from 2015-11-05 23:58:40" class="aligncenter size-full wp-image-646" height="411" src="https://gisunchained.files.wordpress.com/2015/11/screenshot-from-2015-11-05-235840.png" width="660" /></a></p>
<p>The advantage of this approach (using PostGIS) instead of using &#8220;Polygons to Lines&#8221; and &#8220;Lines to points&#8221; processing tools is that we just need to change the polygons layer, and save it, to see our vertexes get updated automatically. It&#8217;s because of this kind of stuff that I love <a href="http://postgis.net/">PostGIS</a>.</p>
