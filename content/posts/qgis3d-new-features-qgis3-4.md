---
source: "blog"
title: "New 3D features in QGIS 3.4"
date: "2018-10-17T04:00:00-0500"
link: "https://lutraconsulting.co.uk/blog/2018/10/17/qgis3d-new-features-qgis3-4/"
draft: "false"
showcase: "planet"
subscribers: ["lutragis"]
author: "Lutra Consulting"
tags: []
---

<p>Thanks to the great response from the QGIS community to our <a href="https://www.lutraconsulting.co.uk/crowdfunding/more-qgis-3d/">crowdfunding call</a>, we have added several new features to the upcoming release (3.4).</p>

<p>Here are the highlights of the features:</p>

<!-- more -->

<h1 id="print-layout">Print layout</h1>

<p>With this new feature, you can embed a 3D scene to the print layout. In addition, there are camera and view setting tools available to adjust the scene from within the map frame. This will allow you to generate high resolution outputs similar to the other map frames.</p>

<p><img alt="QGIS 3D configuration" src="https://www.lutraconsulting.co.uk/img/posts/qgis3d_print_layout.png" /></p>

<h1 id="animation">Animation</h1>

<p>You can create an animation based on a set of keyframes - camera positions at particular times. QGIS 3D then interpolates the camera positions/rotations in between the keyframes.</p>

<p>To create the keyframes, first set the scene for your map, by rotating, zooming or moving the camera. Then assign a time to the frame. There are several methods for interpolations between keyframes.</p>

<p><img alt="QGIS 3D configuration" src="https://www.lutraconsulting.co.uk/img/posts/qgis3d_animation.gif" /></p>

<h1 id="identify-tool-in-3d-map">Identify tool in 3d map</h1>
<p>A new <strong>Identify Tool</strong> was introduced to 3D map. Using this tool, you can inspect features from the 3D scene. Thanks to our friends from <a href="https://www.faunalia.eu/en/">Faunalia</a> for funding this feature.</p>

<h1 id="3d-lines">3D lines</h1>

<p>If you have a 3D linestring, you can now use the elevation of vertices to display it in 3D map.</p>

<p><img alt="QGIS 3D configuration" src="https://www.lutraconsulting.co.uk/img/posts/qgis_3d_lines.png" /></p>

<h1 id="camera-control">Camera control</h1>

<p>There are more control on how you can pan, rotate and zoom the camera within the scene:</p>
<ul>
  <li><strong>Page up/down</strong>: to move the camera up/down:
<img alt="Page up/down keys for moving the camera" src="https://www.lutraconsulting.co.uk/img/posts/qgis3d_page_up_down.gif" /></li>
  <li><strong>Free camera movements</strong>: also possible to look from below:
<img alt="Page up/down keys for moving the camera" src="https://www.lutraconsulting.co.uk/img/posts/qgis3d_free_camera_movement.gif" /></li>
  <li><strong>Shift key and drag</strong>:  the camera rotates around a point on terrain:
<img alt="Page up/down keys for moving the camera" src="https://www.lutraconsulting.co.uk/img/posts/qgis3d_shift_left_click.gif" /></li>
  <li><strong>Ctrl key and drag</strong>: this will rotate camera while it stays in one position
<img alt="Page up/down keys for moving the camera" src="https://www.lutraconsulting.co.uk/img/posts/qgis3d_ctrl_drag.gif" /></li>
</ul>

<p>In addition, the point towards which the camera is looking is dynamically adjusted based on the terrain. The rotation in scenes where a DEM used for terrain has been enhanced significantly. This is more pronounced with presence of higher hills in the terrain.</p>

<h1 id="further-development">Further development</h1>
<p>There are still some exciting features from the crowdfunding which will be incorporated in QGIS 3.6. You can check the <a href="https://github.com/qgis/QGIS">QGIS development</a> or follow us on <a href="https://www.twitter.com/lutraconsulting">Twitter</a>.</p>

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
