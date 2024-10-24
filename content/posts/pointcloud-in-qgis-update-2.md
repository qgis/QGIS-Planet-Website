---
source: "blog"
title: "Point cloud and QGIS 3D improvements - progress report 2"
date: "2022-04-05T01:00:00-0500"
link: "https://lutraconsulting.co.uk/blog/2022/04/05/pointcloud-in-qgis-update-2/"
draft: "false"
showcase: "planet"
subscribers: ["lutragis"]
author: "Lutra Consulting"
tags: []
---

<p>This is a part of series of blog posts to update QGIS community with the outcome of the <a href="https://www.lutraconsulting.co.uk/crowdfunding/elevation-pointcloud-enhancements-qgis/">funding we had raised during late 2021</a> to improve elevation and point clouds in collaboration with <a href="https://north-road.com/">North Road</a> and <a href="https://hobu.co/">Hobu</a>. For other updates see <a href="https://www.lutraconsulting.co.uk/blog/2022/03/15/pointcloud-in-qgis-update-1/">part 1</a> and <a href="https://www.lutraconsulting.co.uk/blog/2022/06/16/pointcloud-in-qgis-update-3/">part 3</a>.</p>

<h2 id="point-cloud-filtering">Point cloud filtering</h2>
<p>With this feature, you can filter the point cloud data based on the classes or any other attributes. This is very similar to filtering available for vector layers.</p>

<p>Filtering data allows you superimpose for example building on top of the raster representation of your point cloud data:</p>

<center>
  <p><img alt="Filtering of point clouds" src="https://lutraconsulting.co.uk/img/posts/filtering_pointcloud.png" title="Filtering of point clouds" /></p>
</center>

<center>
  <p><img alt="Filtering of point clouds" src="https://lutraconsulting.co.uk/img/posts/filtering_pointcloud.gif" title="Filtering of point clouds" /></p>
</center>

<p>Examples of filtering you can use:</p>

<ul>
  <li>
    <p><code class="highlighter-rouge">Classification = 2</code> - only show ground points</p>
  </li>
  <li>
    <p><code class="highlighter-rouge">ReturnNumber = 1</code> - only show the first return or <code class="highlighter-rouge">ReturnNumber = NumberOfReturns</code> for the last return</p>
  </li>
  <li>
    <p><code class="highlighter-rouge">Z &gt;= 10 AND Z &lt;= 50</code> - only show a slice from the range of elevations</p>
  </li>
</ul>

<p>The filtering window also displays statistics of some of the parameters.</p>

<h2 id="2d3d-camera-sync">2D/3D Camera sync</h2>
<p>When you navigate in the 2D map, you often want to see the 3D map view also updated and vice versa. This feature also allows you to view the extent and camera angle  of your 3D map view on 2D map.</p>

<center>
  <p><img alt="2D-3D camera sync" src="https://lutraconsulting.co.uk/img/posts/camera_2d_3d_sync_extent.gif" title="2D-3D camera sync" /></p>
</center>

<h2 id="new-point-clouds-styling-method">New point clouds styling method</h2>
<p>There is a new 3D styling mode for point cloud which follows the 2D styling. This means you do not need to apply the same styling, e.g. Classification twice: once for the 2D map view and another for the 3D map view. Once you set the 3D style to follow 2D map, any changes in 2D map  style will be automatically displayed in 3D map.</p>

<center>
  <p><img alt="Follow 2D style for 3D point clouds" src="https://lutraconsulting.co.uk/img/posts/follow-2d_symbology.gif" title="Follow 2D style for 3D point clouds" /></p>
</center>

<h2 id="camera-and-navigation-improvements">Camera and navigation improvements</h2>
<p>This feature was funded by QGIS.org to improve 3D map navigation. Users can now better move, rotate both the map and camera. The 3D map navigation is now more inline with other applications like Google Earth.</p>

<center>
  <p><img alt="Camera navigation" src="https://lutraconsulting.co.uk/img/posts/camera_navigation.gif" title="Camera navigation" /></p>
</center>
