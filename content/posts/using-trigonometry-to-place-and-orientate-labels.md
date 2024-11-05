---
source: "blog"
title: "Using Trigonometry To Place And Orientate Labels"
date: "2017-07-14T08:20:07+0000"
link: "https://ieqgis.com/2017/07/14/using-trigonometry-to-place-and-orientate-labels/"
draft: "false"
showcase: "planet"
subscribers: ["ireland_qgis_user_group_blog"]
author: "Ireland QGIS User Group Blog"
tags: ["2.18", "qgis", "tutorial", "labels", "map"]
---

<p>Geologists display the <a href="https://qph.ec.quoracdn.net/main-qimg-4c16f5811d1b58fffb01407df6850745" rel="noopener" target="_blank">dip and strike</a> of rock layers on <a href="https://ngmdb.usgs.gov/ngmdb/ngmdb_home.html" rel="noopener" target="_blank">geological maps</a> using a <a href="http://geologyclass.org/struct6.gif" rel="noopener" target="_blank">dip and strike symbol,</a> where dip in degrees indicates the maximum angle a rock layer descends relative to the horizontal. However, it is not directly possible in <a href="https://www.qgis.org/en/site/index.html" rel="noopener" target="_blank">QGIS 2.18</a>, using basic label settings, to place and orient a dip label next to a dip and strike symbol.</p>
<p>However, there is a way around this issue using <a href="https://en.wikipedia.org/wiki/Trigonometry" rel="noopener" target="_blank">Trigonometry</a> and editing the layer&#8217;s <a href="https://youtu.be/3clca1U8rG4" rel="noopener" target="_blank">Attribute Table</a>. This method may be useful for controlling the position and orientation of labels around <a href="http://desktop.arcgis.com/en/arcmap/10.3/manage-data/geodatabases/GUID-49497935-EDB0-4BCA-8861-8BE08F89AAA9-web.gif" rel="noopener" target="_blank">point features</a> in general. The first step involves adding values to the Attribute Table. First, add these two new columns:</p>
<ul>
<li>Angle &#8211; 0° is North and values increases clockwise up to 359°</li>
<li>Distance &#8211; label distance from a point feature</li>
</ul>
<p>You can add Angle and Distance values to these columns manually or use the Field Calculator (see below) to add values if you have lots of points. Also, I chose Map Units (not millimeters) for Symbol Size, Font Size and Distance for my map, as I prefered to keep symbol size, font size and position of labels fixed when zooming in and out.</p>
<h6><a href="https://ieqgis.wordpress.com/2017/07/14/using-trigonometry-to-place-and-orientate-labels/fieldcalculator/#main" rel="attachment wp-att-937"><img alt="" class="alignnone wp-image-937 size-large" height="307" src="https://ieqgis.files.wordpress.com/2017/07/fieldcalculator.png?w=545&#038;h=307" style="border: 3px solid #c0c0c0;" width="545" /></a><br />
<em>Note &#8211; I use Strike (Angle) and Label Distance (Distance)  in my Attribute Table</em></h6>
<p>The next step is to control the position of the label around the points using trigonometry. Right click the points layer and choose:</p>
<p><em>Properties &#8211; Labels &#8211; Placement</em></p>
<p>Check that Offset From Point is checked and then click the Data Defined Override next to the Offset X, Y boxes and choose Edit. The Expression String Builder will appear. Enter the following expression in the Expression String Builder window:</p>
<p><span style="color: #ccffff;"><em>to_string ( ((-1) * ( &#8220;Distance&#8221; )) * cos ( radians ( &#8220;Angle&#8221; ))) ||&#8217;,&#8217;|| to_string (((-1) * ( &#8220;Distance&#8221; )) * sin ( radians ( &#8220;Angle&#8221; )) )</em></span></p>
<p><a href="https://ieqgis.wordpress.com/2017/07/14/using-trigonometry-to-place-and-orientate-labels/attributedia3/#main"><img alt="" class="alignnone wp-image-927 size-large" height="186" src="https://ieqgis.files.wordpress.com/2017/07/attributedia3.png?w=545&#038;h=186" style="border: 2px solid #c0c0c0;" width="545" /></a></p>
<p>The expression takes the angle and distance values from the Attribute Table (edited earlier) and calculates an X, Y label position relative to the point feature. You may also optionally control the angle of a symbol or icon itself via:</p>
<p><em>Layer Properties &#8211; Style &#8211; click Data Defined Override icon &#8211; Edit </em></p>
<p>Then enter the following expression in the Data Defined Override dialogue:</p>
<p><span style="color: #ccffff;"><em>&#8220;Angle&#8221; &#8211; 90</em></span></p>
<p>Finally, to control the rotation of label text, so text follows the orientation (angle) of a rotating symbol or icon, choose:</p>
<p><em>Layer Properties &#8211; Labels &#8211; Placement &#8211; Data Defined &#8211; Rotation</em></p>
<p>Click the Data Defined Override Icon again and then choose Edit. Enter the following expression in the Data Defined Override dialogue:</p>
<p><span style="color: #ccffff;"><em>(&#8220;Angle&#8221; &#8211; 90) * -1</em></span></p>
<p>The following geological map of the Old Head of Kinsale in southern Ireland shows the results of the above procedure. We see that the dip labels rotate and currently follow the orientation of the dip and strike symbols (note that the points are at the intersection of the T symbol).</p>
<h6><a href="https://ieqgis.wordpress.com/2017/07/14/using-trigonometry-to-place-and-orientate-labels/hook-head-geology/#main"><img alt="" class="alignnone wp-image-904 size-large" height="495" src="https://ieqgis.files.wordpress.com/2017/05/hook-head-geology2-e1494120832983.png?w=545&#038;h=495" style="border: 2px solid #c0c0c0;" width="545" /></a><br />
<em>Geological Survey of Ireland &#8211; Creative Commons Attribution 4.0 license</em></h6>
<p>You may have several different symbols, of various sizes, each requiring an appropriate label distance expressed in the Attribute Table. It took me a few tries before I found the right distances for my geological symbols, from 90 to 230 meters distance depending on the symbol size and type.</p>
<p>Lastly, the expressions <em>&#8220;Angle&#8221; &#8211; 90 and (&#8220;Angle&#8221; &#8211; 90) * -1</em> were necessary in my case because I needed to place my labels next to the dip and strike symbol&#8217;s barb. You may need to use a different expression <em>e.g.</em> &#8220;<em>Angle&#8221; and (&#8220;Angle&#8221;) * -1</em>, or a value other than 90° depending on the symbol used and the prefered label placement location. Some trial and error is may be required to find the correct label position.</p>
