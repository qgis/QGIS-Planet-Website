---
source: "blog"
title: "Rule-based labelling in QGIS 2.12"
date: "2015-10-25T11:00:00-0500"
link: "https://lutraconsulting.co.uk/blog/2015/10/25/rule-based-labeling/"
draft: "false"
showcase: "planet"
subscribers: ["lutragis"]
author: "Lutra Consulting"
tags: []
---

<p>The new <a href="http://www2.qgis.org/en/site/" target="_blank">QGIS</a> 2.12 (Lyon) will be out soon!</p>

<p>In this release, we have revamped the labelling engine and made it more flexible in-line with the rest of vector styling.</p>

<p>In this release, we have:</p>

<ul>
  <li>Revamped the labelling engine</li>
  <li>Added support for mutually exclusive layer tree groups</li>
  <li>Developed raster alignment tool</li>
</ul>

<!-- more -->

<h2 id="for-users">For users</h2>

<p>In previous versions of QGIS, users can select a field value or use an expression as labels for a vector layer. In QGIS 2.12, users can  additionally define rules to label vector layers. Rule-based labelling works in the similar way as “Style”. A list of rules will be defined by users and they will be applied from top-to-bottom.</p>

<center>
<a href="https://www.lutraconsulting.co.uk/img/posts/field-labeling.png" rel="lightbox"><img src="https://www.lutraconsulting.co.uk/img/posts/field-labeling_499.png" title="Field based labelling (Click to enlarge)" /></a>
<p class="caption">Field based labelling (Click to enlarge)</p>
</center>

<center>
<a href="https://www.lutraconsulting.co.uk/img/posts/rule-based-labeling.png" rel="lightbox"><img src="https://www.lutraconsulting.co.uk/img/posts/rule-based-labeling_499.png" title="Rule based labelling (Click to enlarge)" /></a>
<p class="caption">Rule based labelling (Click to enlarge)</p>
</center>

<p>To achieve  the same effect in the earlier versions of QGIS, users should add a complex expression.The example below shows the expression used in earlier versions of QGIS:</p>

<div class="highlighter-rouge"><div class="highlight"><pre class="highlight"><code>CASE WHEN  length( "htmlname" ) &gt; 13 AND strpos("htmlname",' ') &gt; 6  THEN  replace("htmlname",' ','  ') WHEN  length( "htmlname" ) &gt; 20 AND "htmlname"  LIKE '%Golf Course' THEN  regexp_replace("htmlname",'Golf Course',' Golf Course') WHEN  length( "htmlname" ) &gt; 20 AND "htmlname"  LIKE '%Nature Reserve' THEN  regexp_replace("htmlname",'Nature Reserve',' Nature Reserve') WHEN  length( "htmlname" ) &gt; 20 AND "htmlname"  LIKE '%Church Of England%' THEN  regexp_replace("htmlname",'Church Of England',' Church Of England ')  WHEN  length( "htmlname" ) &gt; 13 AND "htmlname"  LIKE '% Of The %' THEN  regexp_replace("htmlname",'Of The','Of The ') WHEN  length( "htmlname" ) &gt; 13 AND "htmlname"  LIKE '% of %' AND  "fontcolour" &lt;&gt; 2 AND  "fontcolour" &lt;&gt;  4 THEN  regexp_replace("htmlname",' of ',' of  ')  WHEN "htmlname" LIKE '%/%' THEN regexp_replace("htmlname",'/','/  ') WHEN  length( "htmlname" ) &gt; 30 THEN  replace("htmlname",' ','  ')  ELSE  "htmlname"  END
</code></pre></div></div>

<p>As you can see, without rule-based labelling users have to define each case and the labelling text. Additionally, with the cumbersome task of defining each case, users are limited to using specific labelling formats (e.g. font color, font size, visibility range, etc). With the new labelling engine, users can define their labels similarly to styles - in fact they can copy the rules from styling tabs and use it within the new labelling section!</p>

<center>
<a href="https://www.lutraconsulting.co.uk/img/posts/rule-based_rules.png" rel="lightbox"><img src="https://www.lutraconsulting.co.uk/img/posts/rule-based_rules_499.png" title="Example of label rules (Click to enlarge)" /></a>
<p class="caption">Examples of label rules (Click to enlarge)</p>
</center>

<h2 id="for-developers">For developers</h2>
<p>In order to facilitate addition of rule-based labelling, some internal changes were made to the QGIS labelling engine interface. The labelling is now driven by the new class <code class="highlighter-rouge">QgsLabelingEngineV2</code> which may have several label providers associated with it.
The label providers are objects derived from <code class="highlighter-rouge">QgsAbstractLabelProvider</code> and they are responsible
for:</p>

<ol>
  <li>
    <p>providing “label features” that define properties of each label and geometry of the feature they represent; and</p>
  </li>
  <li>
    <p>drawing of labels at the positions determined by the engine.</p>
  </li>
</ol>

<p>Currently there are label provider implementations for diagrams, simple labelling and rule-based labelling.</p>

<p>The existing labelling engine (<code class="highlighter-rouge">QgsPalLabeling</code> class) is now built on top of the new labelling engine and works as a wrapper for it so that existing code that uses <code class="highlighter-rouge">QgsPalLabeling</code> still works.</p>

<p>As of now, the API for the new labelling engine is not considered as complete and therefore not available in Python. The idea is to make it easier to use, more polished and better prepared for the future use cases. It will be likely finished during the 2.14 release cycle
and some changes may need to be postponed to QGIS 3.0 where backwards incompatible API changes will be allowed (as of now, QGIS 3.0 is being intensively discussed on QGIS developer mailing list).</p>

<h2 id="funding">Funding</h2>
<p>This rule-based labeling has been funded by Tuscany Region (Italy). Special thanks also to the QGIS developers for their help with bug fixing.</p>

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
