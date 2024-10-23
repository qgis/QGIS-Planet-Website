---
source: "blog"
title: "Point cloud and QGIS 3D improvements - progress report 3"
date: "2022-06-16T01:00:00-0500"
link: "https://lutraconsulting.co.uk/blog/2022/06/16/pointcloud-in-qgis-update-3/"
draft: "false"
showcase: "planet"
subscribers: ["lutragis"]
author: "Lutra Consulting"
tags: []
---

<p>This is a part of series of blog posts to update QGIS community with the outcome of the <a href="https://www.lutraconsulting.co.uk/crowdfunding/elevation-pointcloud-enhancements-qgis/">funding we had raised during late 2021</a> to improve elevation and point clouds in collaboration with <a href="https://north-road.com/">North Road</a> and <a href="https://hobu.co/">Hobu</a>. For other updates see <a href="https://www.lutraconsulting.co.uk/blog/2022/03/15/pointcloud-in-qgis-update-1/">part 1</a> and <a href="https://www.lutraconsulting.co.uk/blog/2022/04/05/pointcloud-in-qgis-update-2/">part 2</a>.</p>

<h2 id="profile-tool">Profile tool</h2>

<p>With the new integrated profile tool, you can generate cross sections of point clouds, raster, vector and mesh data. For more information on this tool, you can see the excellent video introduction by <a href="https://north-road.com/">North Road</a> who implemented this part of the project.</p>

<center>
    
</center>

<p>To be able to view profiles from different data types, there is now a dedicated <strong>Elevation</strong> settings under layer properties. Users can set the elevation source, style and some other configurations. You can then enable elevation profile widget window by going to the main menu in QGIS, <strong>View &gt; Elevation Profile</strong>.</p>

<center>
  <p><img alt="Elevation Profile tool in QGIS" src="https://lutraconsulting.co.uk/img/posts/pointcloud_profile_raster_pc.png" title="Elevation Profile tool in QGIS" /></p>
</center>

<h2 id="support-for-copc">Support for COPC</h2>

<p>Cloud Optimized Point Cloud (COPC) is a new format for point cloud data and QGIS 3.26 comes with support for it (for both local files and data hosted on remote servers).</p>

<p>COPC is a very exciting addition to the ecosystem, because it is “just” a LAZ file (a format well established in the industry) that brings some interesting extra features. This means all software supporting LAZ file format will also be able to read COPC files without any extra development. If you are familiar with Cloud Optimized GeoTIFF (COG) for rasters, COPC is an extension of the same concept for point cloud data. Read more at https://copc.io/</p>

<p>Ordinary LAS/LAZ files have an issue that it is not possible to efficiently read a subset of data without reading the entire file. This is less of an issue when processing point cloud data, but much more important for point cloud viewers, which typically show only a small portion of the data (e.g. zoomed in to a particular object or zoomed out to show the entire dataset). For that reason, viewers need to index (pre-process) the data before being able to show it - QGIS also needs to do the indexing when a point cloud file is first loaded. The new feature that COPC brings is that data is re-organized in a way that reading just some parts of data is efficient and easy. Therefore when loading COPC files, QGIS can immediately show them without any indexing (that takes time and extra storage).</p>

<p>In addition to that, COPC files can be efficiently used also directly from remote servers - clients such as QGIS can only request small portions of data needed, without the need to download the entire file (that can have size of many gigabytes). This makes dissemination of point cloud data easier than before - just make COPC files available through a static server and clients are ready to stream the data.</p>

<p>A small note: until now, QGIS indexed point cloud files to EPT format upon first load. From QGIS 3.26 we have switched to indexing to COPC - it has the advantage of being just a single file rather than lots of small files in a directory. If you have point cloud data indexed in EPT format already, QGIS will keep using EPT index (rather than indexing also to COPC).</p>

<center>
  <p><img alt="Display of a remote COPC file" src="https://lutraconsulting.co.uk/img/posts/pointcloud_copc_melbourne.gif" title="display of a remote COPC file" /></p>
</center>

<center>
  <p><img alt="Display of a remote COPC file" src="https://lutraconsulting.co.uk/img/posts/add_copc_remote.png" title="display of a remote COPC file" /></p>
</center>

<h2 id="classified-renderer-improvements">Classified renderer improvements</h2>
<p>Classified renderer for point clouds has been improved to:</p>

<ul>
  <li>Show only classes that are in the dataset (instead of hard-coded list) &amp; show also non-standard classes</li>
  <li>Show percentage of points for each class</li>
  <li>Work also for other attributes (return number, number of returns, point source and few other classes)</li>
</ul>

<center>
    <p><img alt="Point cloud classification" src="https://lutraconsulting.co.uk/img/posts/pointcloud_classification.png" title="Point cloud classification" /></p>
  </center>

<h2 id="vector-transparency-in-3d-scene">Vector transparency in 3D scene</h2>
<p>This improvement is not part of the crowdfunding campaign and was exclusively funded by the <a href="https://www.lutraconsulting.co.uk/blog/categories/qgis/www.qgis.se">Swedish QGIS user group</a>, but it is somehow relevant to the audience of this blog post!</p>

<p>With this feature, you can set polygon transparency in 3D scenes.</p>

<center>
  <p><img alt="3D vector transparency" src="https://lutraconsulting.co.uk/img/posts/qgis_3d_vector_transparency.png" title="3D vector transparency" /></p>
</center>

<h2 id="want-to-see-more-features">Want to see more features?</h2>
<p>We are trying to improve QGIS to handle point clouds for visualisation and analysis. If you would like certain features to be added to QGIS, do not hesitate to contact us on info@lutraconsulting.co.uk with your idea(s).</p>
