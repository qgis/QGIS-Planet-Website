---
source: "blog"
title: "Towering QGIS 2.8 Release"
date: "2015-02-19T10:00:00-0600"
link: "https://lutraconsulting.co.uk/blog/2015/02/19/towering-qgis-release/"
draft: "false"
showcase: "planet"
subscribers: ["lutragis"]
author: "Lutra Consulting"
tags: []
---

<p>The new <a href="http://www2.qgis.org/en/site/" target="_blank">QGIS</a> 2.8 release (codename: Wien) is out tomorrow!</p>

<p>Lutra’s very own QGIS core developer Martin Dobiaš has been working hard with others on bringing you new stuff.  So, what exciting new features are provided by this jauntily-angled new release?  There are plenty of eagerly-anticipated additions - both big new features, and under-the-hood improvements - as well as bugfixes.</p>

<!-- more -->

<h2 id="multiple-stylings">Multiple Stylings</h2>

<p>Have you ever found yourself duplicating layers just so you could display the same data but with additional styles?  Those days are now <em>over</em>.</p>

<p>You can now define multiple styles for a single layer, and easily switch between them in the layer view or layer properties dialog.</p>

<p align="center"><img alt="Multiple styles in the legend" src="https://www.lutraconsulting.co.uk/img/posts/blog_28_styles_legend.png" /></p>

<p align="center"><img alt="Multiple styles in the layer dialog" src="https://www.lutraconsulting.co.uk/img/posts/blog_28_styles_layer_dialog.png" /></p>

<p>Just so our webmapping colleagues don’t feel left out this new behaviour is extended to the WMS server too. The available multiple styles are advertised in GetCapabilities and can be used in other requests, such as GetMap.</p>

<p>And of course it all works in the map composer too - which means more maps with the same layers displayed in different styles.</p>

<p align="center"><img alt="Multiple styles in the map composer" src="https://www.lutraconsulting.co.uk/img/posts/blog_28_styles_composer.png" /></p>

<p>Work carried out in cooperation with <a href="http://www.gis3w.it/" rel="nofollow" target="_blank">Gis3W</a> for <a href="http://www.regione.toscana.it/" rel="nofollow" target="_blank">Regione Toscana</a>.</p>

<h2 id="making-it-snappy">Making It Snappy</h2>

<p>Snapping is made simpler with the addition of new modes for snapping, so you can now:</p>

<ul>
  <li>Snap to current layer</li>
  <li>Snap to all layers</li>
  <li>Perform advanced per-layer snapping (previously the only mode)</li>
</ul>

<p align="center"><img alt="New snapping modes" src="https://www.lutraconsulting.co.uk/img/posts/blog_28_snap_all.png" /></p>

<p>There’s also less confusion with snapping tolerances being to map units or layer units, so those anticipated 1 metre tolerances don’t become 1 degree tolerances without you knowing.</p>

<p>Snapping is not only more straightforward - it’s now much faster too thanks to using an index of geometries built when first needed.  Because everybody loves <em>faster</em>, right?</p>

<p>For our developer colleagues there is an easy to use API which - amongst other things - adds fast point in polygon queries.</p>

<p>Funded by <a href="http://www.vevey.ch/" rel="nofollow" target="_blank">Ville de Vevey</a>, <a href="http://www.nyon.ch/" rel="nofollow" target="_blank">SITNyon</a> and <a href="http://www.qgis.ch/" rel="nofollow" target="_blank">QGIS Usergroup Switzerland</a>.</p>

<p>More info <a href="https://github.com/qgis/QGIS-Enhancement-Proposals/blob/master/qep-13-efficient-snapping-and-geometry-queries.rst" target="_blank">here</a>.</p>

<h2 id="simplify-simplified">Simplify Simplified</h2>

<p>QGIS has had a simplify tool for a while, but now it’s been significantly improved with lots of tasty new ingredients.</p>

<p align="center"><img alt="Improved simplify tool" src="https://www.lutraconsulting.co.uk/img/posts/blog_28_simplify.png" /></p>

<p>Simplify tool tolerances used to be different for every feature - but not any more, and users can specify exact tolerances - which can be in map units or layer units.</p>

<p>Also new is on-the-fly reprojection support, tolerance settings are now persistent between sessions, dragging a rectangle instead of just clicking to simplify multiple features, support for multi-part features, and statistics about reduction of the number of vertices - because if you’re simplifying, it’s nice to know by how much!  Oh yes, and faster too!</p>

<p>Work carried out in cooperation with <a href="http://kartoza.com/" rel="nofollow" target="_blank">Kartoza</a>.</p>

<h2 id="one-legend-to-rule-them-all">One Legend To Rule Them All</h2>

<p>The display of rules in the legend for rule-based rendering has continued its evolution in features from QGIS 2.4:</p>

<p>QGIS 2.4: Good - a flat list of rules, but you can’t see the nesting.</p>

<p align="center"><img alt="Rules in 2.4" src="https://www.lutraconsulting.co.uk/img/posts/blog_28_rules_24.png" /></p>

<p>QGIS 2.6: Better - shown as a pseudo-tree with checkboxes.</p>

<p align="center"><img alt="Rules in 2.6" src="https://www.lutraconsulting.co.uk/img/posts/blog_28_rules_26.png" /></p>

<p>QGIS 2.8: Best - great for power-users who use complex styling rules to give their maps that extra zing.</p>

<p align="center"><img alt="Rules in 2.8" src="https://www.lutraconsulting.co.uk/img/posts/blog_28_rules_28.png" /></p>

<p>Funded by <a href="http://www.sige.ch/" rel="nofollow" target="_blank">SIGE</a>.</p>

<h2 id="long-term-love">Long-Term Love</h2>

<p>QGIS is also the first Long-Term Release (LTR) version - starting with 2.8 every third release is a long-term-release - maintained until the next long-term-release occurs.</p>

<p>Even if you’re a new-feature-junkie, you’ll appreciate the commitment by the project to both innovation <em>and</em> stability, and this of course underlines the burgeoning success of QGIS in enterprise environments.</p>

<p>So, start your engines, and get ready to download!</p>

<h2 id="making-it-happen">Making It Happen</h2>

<p>While you’re still reeling from finding out about some of the new goodies that QGIS 2.8 brings (and check the <a href="http://changelog.qgis.org/qgis/version/2.8/" target="_blank">official QGIS changelog</a> for more!), I’ll remind you that all this cool stuff somehow needed to be paid for.</p>

<p>Thanks go to the organisations and individuals that <a href="http://www2.qgis.org/en/site/about/sponsorship.html" target="_blank">sponsor</a> or contribute to the QGIS project, and those that fund development of specific features.  They make the software better for everyone, and you or your organisation could become one of them!</p>

<p>We at Lutra Consulting are Bronze level sponsors of the QGIS project, and use our <a href="https://www.lutraconsulting.co.uk/services/" target="_blank">development</a> experience to contribute code and develop plugins for QGIS.</p>

<p>We tackle this in several ways, including direct approaches from clients to fund custom development, and <a href="https://www.lutraconsulting.co.uk/crowdfunding/autotrace-phase-2/" target="_blank">crowdfunding</a> campaigns. So, if you’re interested in some functionality that isn’t yet there - <a href="mailto:info@lutraconsulting.co.uk" rel="nofollow" target="_blank">get in touch</a>!</p>

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
