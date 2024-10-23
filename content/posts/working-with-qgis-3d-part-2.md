---
source: "blog"
title: "Working with QGIS 3D - Part 2"
date: "2020-02-28T06:00:00-0600"
link: "https://lutraconsulting.co.uk/blog/2020/02/28/working-with-qgis-3d-part-2/"
draft: "false"
showcase: "planet"
subscribers: ["lutragis"]
author: "Lutra Consulting"
tags: []
---

<p>In an <a href="https://www.lutraconsulting.co.uk/blog/2018/03/01/working-with-qgis-3d-part-1/">earlier blog post</a>, we looked into how to visualise rasters and terrains in QGIS 3D.</p>

<p>In this post, we will explore 3d vectors and how to view buildings and trees.</p>

<!-- more -->

<h1 id="data-sources">Data Sources</h1>

<p>For the purpose of this blog post, we will be using</p>

<ul>
  <li><a href="https://data.public.lu/en/datasets/5cecd25a4384b06ad27e5c58/">Buildings dataset</a>.</li>
  <li><a href="https://download.geofabrik.de/europe/luxembourg.html">Background vector data and tree points</a>.</li>
  <li><a href="https://download.data.public.lu/resources/ANA_LUREF_NGL_DTM.zip">Terrain data</a>.</li>
</ul>

<p>You can download all the dataset and final QGIS project from our <a href="https://merginmaps.com/projects/saber/luxembourg/tree">Mergin service</a>. Note that the DTM has been resized from 1m resolution to 5m. All of the datasets have been clipped to Luxembourg commune extent.</p>

<p>After styling the layers you should be able to see an image like the one below in your map view.</p>

<p><img alt="Options" src="https://www.lutraconsulting.co.uk/img/posts/buildings_3d_image1.png" /></p>

<h1 id="3d-buildings">3D Buildings</h1>

<p>You can open a new 3D map window and set the DTM layer as your terrain as shown in the <a href="https://www.lutraconsulting.co.uk/blog/2018/03/01/working-with-qgis-3d-part-1/">earlier blog post</a>.</p>

<p>The other layer we want to view in 3D canvas is the building layer. To adjust the settings, you need to change the layer styling (by pressing F7 to open the styling panel):</p>

<p><img alt="Options" src="https://www.lutraconsulting.co.uk/img/posts/buildings_3d_image2.png" /></p>

<ul>
  <li>By default, the 3D rendering of vector layer is set to <strong>No symbol</strong>. Click on it and set it to <strong>Single symbol</strong>.</li>
</ul>

<p>The buildings layer contain height information:</p>

<ul>
  <li>Change <strong>Altitude clamping</strong> to <strong>Absolute</strong>.</li>
  <li>Change <strong>Altitude binding</strong> to <strong>Vertex</strong>.</li>
</ul>

<p>In case, your building layer is not a 3D dataset, you can apply height and/or extrusion to be able to see them in 3D map view.</p>

<p><strong>Culling mode</strong> helps rendering your scenes faster by not drawing certain features facing the camera. You can read more about culling modes <a href="https://learnopengl.com/Advanced-OpenGL/Face-culling">here</a> and <a href="https://en.wikipedia.org/wiki/Back-face_culling">here</a>.</p>

<p>You can change <strong>Diffuse</strong>, <strong>Ambient</strong>, <strong>Specular</strong> and <strong>Shininess</strong> of the polygons using relevant widgets. These parameters are based on <a href="https://en.wikipedia.org/wiki/Phong_reflection_model">Phong reflection model</a>.</p>

<p>Finally to better display the buildings, you can define the <strong>Edges</strong>.</p>

<p>You should be able to see a 3d scene similar to the one below:</p>

<p><img alt="Options" src="https://www.lutraconsulting.co.uk/img/posts/buildings_3d_image3.png" /></p>

<h1 id="3d-points">3D Points</h1>

<p>Points can be displayed in 3D map view as different type of objects. In this example, we are going to display trees as combination of predefined shapes. You can extract tree points from the OpenStreetMap data (the <strong>osm_pois</strong> layer with filter: <code class="highlighter-rouge">"fclass" LIKE 'tree'</code>).</p>

<p>For tree trunks, we can set the 3D properties as follows:</p>

<p><img alt="Options" src="https://www.lutraconsulting.co.uk/img/posts/buildings_3d_image4.png" /></p>

<p>The tree trunks are represented by a <strong>Cylinder</strong> shape. As you have noted, the <strong>Altitude clamping</strong> method for this layer is <strong>Relative</strong>.</p>

<p>For the tree top, we can duplicate the same tree layer in the layer panel and change the styling to be a <strong>Sphere</strong> shape. You will also need to set the <strong>Transformation</strong> for <strong>Y</strong> to e.g. <strong>10</strong>, so that the spheres sit on top of the cylinders. For the example below, we have set the styling to be a mix of spheres and cones (<strong>Rule-based</strong> instead of <strong>Single symbol</strong>).</p>

<p>3D point renderer allows you to import 3d models supported by <a href="https://en.wikipedia.org/wiki/Open_Asset_Import_Library">Open Asset Import Library</a>.</p>

<p><img alt="Options" src="https://www.lutraconsulting.co.uk/img/posts/buildings_3d_image5.png" /></p>

<h1 id="fly-over-animations">Fly-over animations</h1>

<p>You can create animations of 3d scenes, by defining key frames. Click on the <strong>Animation</strong> icon from the 3D map view window. A new toolbar will appear at the bottom of your window.</p>

<p>Click on the green plus sign to add the timing of the key frames and then move the camera to a different location. You can then play the fly-over using different interpolation methods. Alternatively, you can export them as images and generate an animation outside QGIS.</p>

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
