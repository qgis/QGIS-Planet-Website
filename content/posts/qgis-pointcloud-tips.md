---
source: "blog"
title: "Tips & tricks for point clouds in QGIS"
date: "2021-04-06T01:00:01-0500"
link: "https://lutraconsulting.co.uk/blog/2021/04/06/qgis-pointcloud-tips/"
draft: "false"
showcase: "planet"
subscribers: ["lutragis"]
author: "Lutra Consulting"
tags: []
---

<p>Just few weeks ago, QGIS 3.18 has been released - the first version
to include support for point cloud data, thanks to the great support from
the QGIS community in our joint <a href="https://www.lutraconsulting.co.uk/crowdfunding/pointcloud-qgis/">crowdfunding campaign with North Road and Hobu</a>.</p>

<p>We have received a lot of feedback from users and we would like to summarise
the most common problems people have faced, and add a couple of tips on useful
features that are otherwise easy to overlook.</p>

<p><strong>1. I am unable to load LAS/LAZ files</strong></p>

<p>If your QGIS installation does not recognize .las or .laz files (which are the two
point cloud formats that we currently support in QGIS), the most likely source of
the problem will be that the PDAL library needed for reading LAS/LAZ is missing
in your installation. Unfortunately not all installers include it at this point.
Particularly on Windows, there are several options how to install QGIS, and only
one choice is the right one for PDAL support. At the time of writing (April 2021), you need to download
installer from section called “Standalone installers from OSGeo4W testing packages (MSI)”,
here’s a screenshot of what to look for:</p>

<p><img alt="" src="https://www.lutraconsulting.co.uk/img/posts/point-cloud-download-win.png" /></p>

<p>On macOS the official all-in-one installers include point cloud support. On Linux, PDAL support depends on the particular distribution/packages, but probably most of them
include point PDAL library.</p>

<p><strong>2. Point cloud is completely flat in 3D</strong></p>

<p>It may happen that you load a point cloud layer, then open the 3D map view and the point
is displayed as a flat surface like on this screenshot:</p>

<p><img alt="" src="https://www.lutraconsulting.co.uk/img/posts/point-cloud-no-3d.png" /></p>

<p>The reason for this is that the 3D renderer is not enabled for your point cloud layer. To enable 3D renderer, open the Layer Styling panel (there’s F7 shortcut to open it!), then switch to
the second tab (“3D View” - with a cube icon) and change the “No Rendering” option
to some other option - for example “Classification” in case your point cloud is classified.
You should then see your point cloud in 3D.</p>

<p><strong>3. Point cloud is rendered twice - in 3D and in 2D (“flat”)</strong></p>

<p>Commonly when people open 3D view with a point cloud, they may see the point cloud rendered
twice, like in the following screenshot:</p>

<p><img alt="" src="https://www.lutraconsulting.co.uk/img/posts/point-cloud-twice.png" /></p>

<p>The reason is that both 3D rendering and 2D rendering of point cloud is enabled, and therefore
the layer is also rendered as a 2D map texture on top of terrain (which is flat by default).
An easy way how to fix this is to set 2D rendering of the point cloud layer to “Extent Only”
in Layer Styling panel (in the first tab):</p>

<p><img alt="" src="https://www.lutraconsulting.co.uk/img/posts/point-cloud-extent-only.png" /></p>

<p>If the dashed rectangle marking the extent is still bothering you, it is possible to change
the line symbol to use white (or transparent) colour.</p>

<p>Hopefully in near future we would address unexpected behaviour and layers with a 3D renderer defined
would not be rendered as 2D.</p>

<p><strong>4. I still can’t see my point cloud in 3D view</strong></p>

<p>It could happen that if your point cloud is for a small area, yet the elevation of points is
relatively high: when you first open 3D view or when you click “Zoom Full” button, the view may
get zoomed too close and the actual point cloud data may be behind the camera. Try zooming out
a bit to see if it helps. (This is a bug in QGIS - at this point “zoom full” ignores extra
entities and only takes into account terrain.)</p>

<p><strong>5. Enable “Eye Dome Lighting” in 3D view</strong></p>

<p>For a much better 3D perception of your point cloud, try clicking the “Options” button (with a wrench
icon) in the toolbar of 3D view and enable “Show Eye Dome Lighting” in the pop-up menu. This will
apply extra post-processing that adds slight shading based on the positions of nearby points, and adds
silhouettes when there is a sudden change in depth:</p>

<p><img alt="" src="https://www.lutraconsulting.co.uk/img/posts/point-cloud-edl.png" /></p>

<p>As soon as you zoom into your point cloud more, to the point when individual points can be seen,
the eye dome lighting effect will start to disappear. You can try experimenting with the point size
(in Layer Panel, 3D View tab) - increasing the point size will help.</p>

<p><img alt="" src="https://www.lutraconsulting.co.uk/img/posts/point-cloud-edl-zoom-in-2.png" /> - A view with point size 2.0 pixels</p>

<p><img alt="" src="https://www.lutraconsulting.co.uk/img/posts/point-cloud-edl-zoom-in-6.png" /> - The same view with point size 6.0 pixels</p>

<p><strong>6. Try the new camera navigation mode in 3D view</strong></p>

<p>In QGIS 3.18 we have added a new “Walk Mode” camera navigation mode that is much better suited
for inspection of point clouds (compared to the default “Terrain Based” camera navigation mode).
Open 3D map view configuration dialogue, pick “Camera &amp; Skybox” tab and set it here:</p>

<p><img alt="" src="https://www.lutraconsulting.co.uk/img/posts/point-cloud-navigation-mode.png" /></p>

<table>
  <thead>
    <tr>
      <th>Control                                          </th>
      <th>Action                                          </th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Mouse move</td>
      <td>Rotate camera</td>
    </tr>
    <tr>
      <td>Mouse wheel</td>
      <td>Change movement speed</td>
    </tr>
    <tr>
      <td>W / Up</td>
      <td>Move forward</td>
    </tr>
    <tr>
      <td>S / Down</td>
      <td>Move backward</td>
    </tr>
    <tr>
      <td>A / Left</td>
      <td>Move left</td>
    </tr>
    <tr>
      <td>D / right</td>
      <td>Move right</td>
    </tr>
    <tr>
      <td>Q / Page up</td>
      <td>Move up</td>
    </tr>
    <tr>
      <td>E / Page dn</td>
      <td>Move down</td>
    </tr>
  </tbody>
</table>

<p><strong>7. Use elevation scaling and offset to your advantage</strong></p>

<p>Sometimes it is useful to modify offset and/or scale of the elevation of points (Z values).
For example, if the point elevations do not match your other 3D data, or maybe you have
source data where X,Y coordinates are in meters and Z coordinate is in feet!</p>

<p>Another case when this can be useful, is when your point cloud data are further away from the terrain and
the default “Terrain Based” navigation mode does not work nicely - it expects that data are
near the terrain, and the camera rotates around a point terrain, which may feel strange when
browsing point clouds. A workaround is to apply offset to the point cloud layer to move the points
near the terrain. For example, this is a point cloud which is roughly at 200 meters elevation
(the grey plane is the terrain):</p>

<p><img alt="" src="https://www.lutraconsulting.co.uk/img/posts/point-cloud-offset-0.png" /></p>

<p>When an offset of -200 is applied to the point cloud in Layer Styling panel, data show up much closer
to the terrain and camera navigation feels more natural:</p>

<p><img alt="" src="https://www.lutraconsulting.co.uk/img/posts/point-cloud-offset-200.png" /></p>

<p><strong>8. Try circular points in 2D maps</strong></p>

<p>By default QGIS draws points as squares as this is the fastest option. But for higher quality
output you may want to change point symbol style to circle in Layer Styling panel, which
makes things look a little less jagged:</p>

<p><img alt="" src="https://www.lutraconsulting.co.uk/img/posts/point-cloud-squares.png" /> – using squares
<img alt="" src="https://www.lutraconsulting.co.uk/img/posts/point-cloud-circles.png" /> – using circles</p>

<p>At this point we always use square points in 3D views - in the future we will likely offer
circular points in 3D views as well.</p>

<p><strong>9. Give us your feedback</strong></p>

<p>We would love to hear from you about your experience with point clouds in QGIS so far, what
features you are missing or what problems you have encountered - feel free to drop us a mail
at info@lutraconsulting.co.uk. If you think you have found a bug, best to file an issue
for it in the <a href="https://github.com/qgis/QGIS/issues">QGIS GitHub repository</a>.</p>

<p>With the QGIS 3.18 release, we know we are only at the beginning of a long journey to provide great
point cloud support to the users. The decreasing cost of laser scanning (LIDAR) hardware and increasing
availability of photogrammetric methods means that we will be be seeing point cloud data in GIS
more and more often. There is still a lot of functionality missing for efficient work with raw point clouds,
for easy processing of data and we are still using only a fraction of what the PDAL point cloud library
offers. We are dedicated to provide first class support for point clouds in QGIS - however this cannot
be done without funding. Therefore, if you would like to help us to push point clouds in QGIS
to the next level, please do not hesitate to contact us at info@lutraconsulting.co.uk.</p>

    <div class="input-promo">
    <h2>You may also like...</h2>
    <a href="https://merginmaps.com">Mergin Maps, a field data collection app based on QGIS</a>. Mergin Maps makes field work easy with its simple interface and cloud-based sync. Available on Android, iOS and Windows.
    <img alt="Screenshots of the Mergin Maps mobile app for Field Data Collection" src="https://lutraconsulting.co.uk/img/posts/input_app_for_field_data_collection.jpg" /><br />
    <a href="https://play.google.com/store/apps/details?id=uk.co.lutraconsulting&amp;utm_source=lutra-atom&amp;utm_medium=lutra-blog-footer&amp;utm_campaign=input">
      <img alt="Get it on Google Play" src="https://play.google.com/intl/en_us/badges/images/generic/en_badge_web_generic.png" width="180px" />
    </a>
    <a href="https://apps.apple.com/us/app/input/id1478603559?ls=1&amp;utm_source=lutra-atom&amp;utm_medium=lutra-blog-footer&amp;utm_campaign=input">
      <img alt="Get it on Apple store" src="https://www.lutraconsulting.co.uk/img/posts/App_Store.svg" style="padding-top: 0px;" width="144px" />
    </a>
  </div>
