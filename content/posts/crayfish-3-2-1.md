---
source: "blog"
title: "Overview of QGIS 3.12 Mesh Features"
date: "2020-01-15T03:00:00-0600"
link: "https://lutraconsulting.co.uk/blog/2020/01/15/crayfish-3-2-1/"
draft: "false"
showcase: "planet"
subscribers: ["lutragis"]
author: "Lutra Consulting"
tags: []
---

<p>Ready for 3D meshes, vector streamlines or contour export?</p>

<!-- more -->

<p>The releases of QGIS 3.12, MDAL 0.5.0 and Crayfish 3.2.1 are planned for end of February 2020.
We are proud to present you few of upcoming features we implemented for this release:</p>
<ul>
  <li>vector trace animation</li>
  <li>3D stacked meshes</li>
  <li>mesh calculator enhancements</li>
  <li>export contours</li>
  <li>various smaller enhancements (reference time support, resampling, export plot data, mdal_translate utility)</li>
</ul>

<p>If you are hesitant to wait till end of February, feel free to get nightly build and test it out!</p>

<p>Do you want to use QGIS Mesh Layers in your projects? <a href="https://www.lutraconsulting.co.uk/projects/mdal/">Read more…</a></p>

<h2 id="support-for-vector-trace-animation-and-streamlines-qgis">Support for vector trace animation and streamlines (QGIS)</h2>

<p>Last feature from QGIS 2.x/Crayfish 2.x series that was not ported to QGIS 3 is finally available. You would be able to 
visualize streamlines and particles for vector datasets in mesh layers. In QGIS main menu, under Mesh&gt;Crayfish&gt;Export Trace
you are also able to export animation with the particle traces to various video formats</p>

<p><img alt="Trace animation" src="https://www.lutraconsulting.co.uk/img/posts/2020-1-15-crayfish/trace-animation.png" /></p>

<p>This feature was funded by <a href="https://www.bmt.org">TUFLOW</a></p>

<h2 id="support-for-3d-stacked-meshes-eg-tuflow-fv-format">Support for 3d Stacked Meshes (e.g. TUFLOW FV format)</h2>

<p>MDAL and QGIS now supports 3D Stacked Meshes, particularly for TUFLOW-FV format.
For this release, you need to choose appropriate averaging method in the QGIS interface and you are able to browse the data similarly 
to any other 2D dataset.
<img alt="3d stacked" src="https://www.lutraconsulting.co.uk/img/posts/2020-1-15-crayfish/3d-mesh.png" /></p>

<p>In Crayfish 3.2.1, you can create plots of the profile showing the variation along Z-axis.</p>

<p><img alt="3d stacked plot" src="https://www.lutraconsulting.co.uk/img/posts/2020-1-15-crayfish/3dmesh2.png" /></p>

<p>The technical description can be found in the following <a href="https://github.com/qgis/QGIS-Enhancement-Proposals/issues/158">QEP</a></p>

<p>This feature was funded by <a href="https://www.lutraconsulting.co.uk/blog/categories/qgis/www.tuflow.com">TUFLOW</a></p>

<h2 id="on-the-fly-resampling-of-data-defined-on-faces-to-vertices">On the fly resampling of data defined on faces to vertices</h2>

<p>For datasets defined on faces, one can choose to interpolate data to vertices with neighbour average method. When no data interpolation
method is chosen, each pixel on a single face has a single value/color. With data on vertices, the rendering for each pixel is 
interpolated from the values on the vertices, making smoother figures.</p>

<p>Use mesh contours styling panel to switch between the data interpolation methods.</p>

<p><img alt="No Mesh Data Resampling Dialog" src="https://www.lutraconsulting.co.uk/img/posts/2020-1-15-crayfish/data-interpolation-dialog.png" />
<img alt="Mesh Data Resampling" src="https://www.lutraconsulting.co.uk/img/posts/2020-1-15-crayfish/no-data-interpolation.png" />
<img alt="Mesh Data Resampling Dialog" src="https://www.lutraconsulting.co.uk/img/posts/2020-1-15-crayfish/data-interpolation.png" /></p>

<p>This feature was funded by <a href="https://www.bmlfuw.gv.at/">Austrian Ministry of Agriculture, Forestry, Environment and Water Management</a></p>

<h2 id="smooth-export-of-the-contours-crayfish-processing-algorithm">Smooth export of the contours (Crayfish processing algorithm)</h2>

<p>We have implemented a new algorithm in QGIS’s analysis library to export directly contour lines and polygons. The method is not 
based on GDAL as it was in the Crayfish 2.x releases. It is both faster and with smoother shapes, matching rendered images from QGIS. 
You can find the new processing algorithm in Crayfish processing toolbox.</p>

<p><img alt="Mesh Contours" src="https://www.lutraconsulting.co.uk/img/posts/2020-1-15-crayfish/contours.png" /></p>

<p>This feature was funded by <a href="https://www.bmlfuw.gv.at/">Austrian Ministry of Agriculture, Forestry, Environment and Water Management</a></p>

<h2 id="support-of-datasets-defined-on-faces-in-qgis-mesh-calculator">Support of datasets defined on faces in QGIS Mesh Calculator</h2>

<p>From QGIS 3.12 you can use mesh calculator for all datasets, both defined on faces and vertices. 
Additionally, it allows users to store the result of mesh calculator under different name or format.  This allows for 
example to work with FLO-2D or HEC-RAS data in the QGIS mesh calculator</p>

<p>This feature was funded by <a href="https://www.bmlfuw.gv.at/">Austrian Ministry of Agriculture, Forestry, Environment and Water Management</a></p>

<h2 id="support-for-reference-time-qgis">Support for reference time (QGIS)</h2>

<p>For various dataset type, for example GRIB and NetCDF, the reference time in QGIS time settings dialog is prepopulated from the 
raw data and does not need to be set manually. Also we fixed various bugs related to time parsing, so in QGIS 3.12 it should be 
possible to format and show your time in plots/animations in proper way.</p>

<p><img alt="Reference Time" src="https://www.lutraconsulting.co.uk/img/posts/2020-1-15-crayfish/reference-time.png" /></p>

<p>This feature was funded by <a href="https://www.lutraconsulting.co.uk/blog/categories/qgis/www.tuflow.com">TUFLOW</a></p>

<h2 id="support-for-conversion-of-2dm-to-ugrid-mesh-mdal_translate-utility">Support for conversion of 2dm to UGRID mesh (mdal_translate utility)</h2>

<p>MDAL library now has a new utility: mdal_translate. For now, use can use the utility to convert text-based 2dm mesh definition files 
to UGRID NetCDF/HDF5 binary-based format and save up to 80% disk and speed up loading of your mesh by similar amount.</p>

<p>This feature was funded by <a href="https://www.lutraconsulting.co.uk/blog/categories/qgis/www.tuflow.com">TUFLOW</a></p>

<h2 id="support-for-export-of-2d-plot-data-processing">Support for export of 2D plot data (processing)</h2>

<p>With Crayfish 3.2.1 you can export your time series or cross section raw dat to CSV format for further processing.</p>

<p>This feature was funded by Lutra Consulting</p>

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
