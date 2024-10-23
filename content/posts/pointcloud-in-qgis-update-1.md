---
source: "blog"
title: "Point cloud and QGIS 3D improvements - progress report 1"
date: "2022-03-15T01:00:00-0500"
link: "https://lutraconsulting.co.uk/blog/2022/03/15/pointcloud-in-qgis-update-1/"
draft: "false"
showcase: "planet"
subscribers: ["lutragis"]
author: "Lutra Consulting"
tags: []
---

<p>This is a part of series of blog posts to update QGIS community with the outcome of the <a href="https://www.lutraconsulting.co.uk/crowdfunding/elevation-pointcloud-enhancements-qgis/">funding we had raised during late 2021</a> to improve elevation and point clouds in collaboration with <a href="https://north-road.com/">North Road</a> and <a href="https://hobu.co/">Hobu</a>. For other updates see <a href="https://www.lutraconsulting.co.uk/blog/2022/04/05/pointcloud-in-qgis-update-2/">part 2</a> and <a href="https://www.lutraconsulting.co.uk/blog/2022/06/16/pointcloud-in-qgis-update-3/">part 3</a>.</p>

<h2 id="a-big-thanks">A big thanks!</h2>
<p>This work was made possible with generous donations and support by the individuals and organisations below (not in a particular order):</p>

<p>Stuart Smith, <a href="http://bayesmap.com/">BayesMap Solutions</a>, <a href="https://www.researchgate.net/profile/Tibor-Lieskovsky">Tibor Lieskovský</a>, <a href="http://www.balrisk.com/">Balanced Risk Strategies</a>, Yoichi Kayama, <a href="https://www.gva.bs.ch/">Basel Land Registry and Surveying Office (GVA)</a>, <a href="https://www.rudaz.ch/index.php/en/">Rudaz + Partner</a>, Jakub Fuska, Richard Barnes, <a href="https://spatialthoughts.com">Spatial Thoughts</a>, <a href="https://twitter.com/hansakwast">Hans van der Kwast</a>, António Pestana, Richard Lorion, <a href="http://www.eagleresources.com/">Eagle Resources</a>, Suresh Muthukrishnan, <a href="https://www.12p.consulting/">12P Consulting</a>, <a href="https://www.alta.is/">Alta</a>, <a href="https://jcis.net.au/">JCIS Consultants</a>, Brenna Hughes, <a href="https://www.baselland.ch/">Amt für Geoinformation Basel-Landschaft</a>, Darren Farmer, F.A.R.M. Facilitazioni Agroecologiche Regionali Mobili, Ali Nayeri, <a href="https://vorarlberg.at/">Land Vorarlberg, Landesamt für Vermessung und Geoinformation</a>, <a href="https://qgis.ch/en">QGIS User Group Switzerland</a>, Robert Thunen, <a href="https://twomile.com">Twomile Heavy Industries, Inc.</a>, Roberto Moyano, Jens Grehl, Pēteris Daknis, Rob Willson (Ecophylla Consulting), Daniel Löwenborg, <a href="https://www.vevey.ch/">Ville de Vevey</a>, Alfredo Toledo (Suriyaco), <a href="https://qtibia.ro/">QTIBIA Engineering</a>, Ian Burrows (FAS), Pascal Obstetar, <a href="http://www.lidarguys.com/">Lidar Guys</a>, <a href="https://mappingautomation.com/">Mapping Automation, LLC</a>, Featherstone Survey and Civil, Peter Schmitz, Fernando Michel Tuesta Chichipe, Hugo Sørensen, Bernie Connors, <a href="https://www.thewatershedcenter.com/">Watershed Research and Training Center</a>, <a href="https://mbsenvironmental.com.au/">MBS Environmental</a>, Andreas Neumann, Adrian Matter, <a href="http://mapfly.fr/">Mapfly</a>, <a href="https://www.lutraconsulting.co.uk/blog/categories/qgis/www.ensogeospatial.com">Enso</a>, João Gaspar, Eric van Dijk, <a href="https://www.uster.ch/">City of Uster, Switzerland</a>, <a href="https://www.lutraconsulting.co.uk/blog/categories/qgis/qgis.dk">QGIS Usergroup Denmark</a>, <a href="https://www.staerea.net/">STAEREA</a>, <a href="https://ogh.ch/">Ostschweizerische Gesellschaft für Höhlenforschung</a>, <a href="https://www.delwp.vic.gov.au/">Department of Environment, Land, Water and Planning (Victoria)</a>, <a href="https://www.ignfi.fr/">IGN FI</a>, Travis Flohr, <a href="https://www.baselland.ch/">Amt für Wald beider Basel</a>, Matthew Bodnar, <a href="http://www.surfacelibre.fr/">Surface libre</a>, <a href="https://uk.osgeo.org/">OSGeo:UK</a>, <a href="https://www.maanmittauslaitos.fi/en">National Land Survey of Finland</a>,<a href="https://www.nrcan.gc.ca/home">Natural Resources Canada</a>, <a href="http://zie.ch/">Fonds Brukhalter, Arbeitsgemeinschaft Höllochforachung AGH</a>, <a href="http://gisxperts.de/">gis experts</a>, <a href="https://bnhr.xyz">BNHR</a>, <a href="http://roguegeoscience.com/">Rogue Geoscience Ltd.</a>, <a href="https://www.erdc.usace.army.mil/Locations/CRREL/">USACE CRREL</a> and Ian Huitson.</p>

<p>In addition to the list above, we thank several anonymous donors who chose not to be listed.</p>

<p>If you have made a donation towards this work and your name or your organisation name does not appear here, please contact us (info@lutraconsulting.co.uk).</p>

<h2 id="3d-view-manager">3D view manager</h2>
<p>Previously, if you closed a project with a 3D map view, the 3D map view and all its settings were lost when you reopen that project. So in <a href="https://www.qgis.org/en/site/forusers/visualchangelog324/index.html#feature-3d-map-view-manager">QGIS 3.24</a> we’ve added a “3D map view manager” that takes care of listing, removing, renaming and duplicating 3D map views in your projects! We’ve also added a new “3D Map Views” menu, which contains all your created 3D map views for easy access.</p>

<p>To summarise, these are the advantages of this new feature:</p>

<ul>
  <li>Saving 3D map views within QGIS project (similar to other settings) and being able to retrieve the 3D view after closing (either the view or the project)</li>
  <li>3D map view manager: which allows you to duplicate, rename and delete 3D map views</li>
</ul>

<center>
  <p><img alt="3D Map Views Manager" src="https://lutraconsulting.co.uk/img/posts/3d_map_view_manager.png" title="3d map view manager" /></p>
</center>

<h2 id="dockundock-3d-views">Dock/undock 3D views</h2>
<p>3D map canvas panel was difficult to move, resize and often resulting in unwanted docking. With <a href="https://www.qgis.org/en/site/forusers/visualchangelog324/index.html#feature-dock-undock-3d-views">QGIS 3.24</a> we added the ability to switch 3D maps from a dockable widget to a top-level window (and back to a dock widget), so that these map views can now be managed, resized and moved just like a standard application window. In addition, you can now use 3D map view in full screen mode.</p>

<center>
  <p><img alt="Docking and undocking 3D view" src="https://lutraconsulting.co.uk/img/posts/dock_undock.gif" title="Docking and undocking 3D view" /></p>
</center>

<h2 id="respect-z-ordering-of-point-clouds-in-2d">Respect Z ordering of point clouds in 2D</h2>
<p>We’ve added an option to render point clouds according to their Z-order in 2D map views. With the new bottom-to-top ordering option enabled, points with larger Z values will cover lower points – resulting in the appearance of a true orthographic photo. There’s also an option for reverse sorting (top-to-bottom), where the scene appears as if viewed from below. This feature is available in <a href="https://www.qgis.org/en/site/forusers/visualchangelog324/index.html#feature-respect-z-ordering-when-rendering-point-clouds-in-2d">QGIS 3.24</a></p>

<p>The image below displays the default Z ordering of a LAS file when loaded in QGIS:</p>

<center>
  <p><img alt="Default Z ordering" src="https://lutraconsulting.co.uk/img/posts/pc_z_order_default.png" title="Default Z ordering" /></p>
</center>

<p>The same layer with the ordering of Z switched to bottom-to-top:</p>

<center>
  <p><img alt="Z ordering bottom to top" src="https://lutraconsulting.co.uk/img/posts/pc_z_order_btm_to_top.png" title="Z ordering bottom to top" /></p>
</center>

<h2 id="visualisation-of-point-cloud-as-solid-surfaces">Visualisation of point cloud as solid surfaces</h2>
<p>With this feature you can render point cloud layer in the 3D view as solid surfaces generated by triangulation. The triangulation is available for all the 3D point cloud renderers: unique color, ramp color, classification and RGB. This feature will be available in QGIS 3.26 and you can try it in the current QGIS nightly/master.</p>

<center>
  <p><img alt="Triangle rendering of point clouds" src="https://lutraconsulting.co.uk/img/posts/mesh_rendering.gif" title="Triangle rendering of point clouds" /></p>
</center>
