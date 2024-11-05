---
source: "blog"
title: "Exploring variables in QGIS pt 3: layer level variables"
date: "2015-12-12T00:40:53+0000"
link: "http://nyalldawson.net/2015/12/exploring-variables-in-qgis-pt-3-layer-level-variables/"
draft: "false"
showcase: "planet"
subscribers: ["nyalldawson_net"]
author: "nyalldawson.net"
tags: ["qgis", "2.12", "geospatial", "layers", "osgeo", "qgis"]
---

<p>In part 3 of my exploration of variables in QGIS 2.12, I&#8217;m going to dig into how variables are scoped in QGIS and what layer level variables are available (you can read parts <a href="http://nyalldawson.net/2015/12/exploring-variables-in-qgis-2-12-part-1/">1</a> and <a href="http://nyalldawson.net/2015/12/exploring-variables-in-qgis-pt-2-project-management/">2</a> for a general introduction to variables).</p>
<h3>Some background</h3>
<p>Before we get to the good stuff, a bit of background in how variables work behind-the-scenes is important. Whenever an expression is evaluated in QGIS the <em>context</em> of the expression is considered. The context is built up from a set of <em>scopes</em>, which are all stacked on top of each other in order from least-specific to most-specific. It&#8217;s easier to explain with an example. Let&#8217;s take an expression used to set the source of a picture in a map composer. When this expression is evaluated, the context will consist of:</p>
<ol>
<li>The <em>global</em> scope, consisting of variables set in the QGIS options dialog, and other installation-wide properties</li>
<li>The <em>project</em> scope, which includes variables set in the Project Properties dialog and the auto-generated project variables like @project_path, @project_title (you can read more about this in <a href="http://nyalldawson.net/2015/12/exploring-variables-in-qgis-pt-2-project-management/">part 2</a>)</li>
<li>A <em>composer</em> scope, with any variables set for the current composer, plus variables for @layout_pagewidth, @layout_pageheight, @layout_numpages, etc.</li>
<li>A <em>composer item</em> scope for the picture, with item-specific variables including @item_id</li>
</ol>
<p>The more specific scopes will override any existing clashing variables from less specific scopes. So a global @my_var variable will be overridden by an @my_var variable set for the composer:</p>
<p><a href="http://nyalldawson.net/wp-content/uploads/2015/12/overridden.png" rel="attachment wp-att-685"><img alt="overridden" class="aligncenter size-full wp-image-685" height="208" src="http://nyalldawson.net/wp-content/uploads/2015/12/overridden.png" width="473" /></a></p>
<p>Another example. Let&#8217;s consider now an expression set for a data-defined label size. When this expression is evaluated the context will depend on <em>where</em> the map is being rendered. If it&#8217;s in the main map canvas then the context will be:</p>
<ol>
<li>The <em>global</em> scope</li>
<li>The <em>project</em> scope</li>
<li>A <em>map settings</em> scope, with variables relating to how the map is being rendered. Eg @map_rotation, @map_scale, etc</li>
<li>A <em>layer</em> scope. More on this later, but the layer scope includes layer-level variables plus preset variables for @layer_name and @layer_id</li>
</ol>
<p>If instead the map is being rendered <strong>inside a map item in a map composer</strong>, the context will be:</p>
<ol>
<li>The <em>global</em> scope</li>
<li>The <em>project</em> scope</li>
<li>The <em>composer</em> scope</li>
<li>An <em>atlas</em> scope, if atlas is enabled. This contains variables like @atlas_pagename, @atlas_feature, @atlas_totalfeatures.</li>
<li>A <em>composer item</em> scope for the map item</li>
<li>A <em>map settings</em> scope (with scale and rotation determined by the map item&#8217;s settings)</li>
<li>The <em>layer</em> scope</li>
</ol>
<h3>Using layer level variables</h3>
<p>Ok, enough with the details. The reason I&#8217;ve explained all this is to help explain when layer level variables come into play. Basically, they&#8217;ll be available whenever an expression is evaluated <strong>inside</strong> of a particular layer. This includes data defined symbology and labeling, field calculator, and diagrams. You can&#8217;t use a layer-level variable inside a composer label, because there&#8217;s no layer scope used when evaluating this. Make sense? Great! To set a layer level variable, you use the <em>Variables</em> section in the Layer Properties dialog:</p>
<div class="wp-caption aligncenter" id="attachment_680" style="width: 835px;"><a href="http://nyalldawson.net/wp-content/uploads/2015/12/layer_variables.png"><img alt="Setting a layer variablee" class="wp-image-680 size-full" height="646" src="http://nyalldawson.net/wp-content/uploads/2015/12/layer_variables.png" width="825" /></a><p class="wp-caption-text" id="caption-attachment-680">Setting a layer variable</p></div>
<p>Any layer level variables you set will be saved inside your current project, i.e. layer variables are per-layer and per-project. You can also see in the above screenshot that as well as the layer level variables QGIS also lists the existing variables from the Project and Global scopes. This helps show exactly what variables are accessible by the layer and whether they&#8217;ve been overridden by any scopes. You can also see that there&#8217;s two automatic variables, <em>@layer_id</em> and <em>@layer_name</em>, which contain the unique layer ID and user-set layer name too.</p>
<h3>Potential use cases for layer-level variables</h3>
<p>In the screenshot above I&#8217;ve set two variables, <em>@class1_threshold</em> and <em>@class2_threshold</em>. I&#8217;m going to use these to sync up some manual class breaks between rule based symbology and rule based labeling. Here&#8217;s how I&#8217;ve set up the rule-based symbols for the layer:</p>
<div class="wp-caption aligncenter" id="attachment_681" style="width: 796px;"><a href="http://nyalldawson.net/wp-content/uploads/2015/12/symbols.png"><img alt="Rule based symbology using layer level variables" class="wp-image-681 size-full" height="108" src="http://nyalldawson.net/wp-content/uploads/2015/12/symbols.png" width="786" /></a><p class="wp-caption-text" id="caption-attachment-681">Rule based symbology using layer level variables</p></div>
<p>In a similar way, I&#8217;ve also created matching rule-based labeling (another <a href="http://www.lutraconsulting.co.uk/blog/2015/10/25/rule-based-labeling/">new feature in QGIS 2.12</a>):</p>
<div class="wp-caption aligncenter" id="attachment_682" style="width: 650px;"><a href="http://nyalldawson.net/wp-content/uploads/2015/12/rule_based_labels.png"><img alt="Matching rule-based labels" class="wp-image-682 size-full" height="102" src="http://nyalldawson.net/wp-content/uploads/2015/12/rule_based_labels.png" width="640" /></a><p class="wp-caption-text" id="caption-attachment-682">Matching rule-based labels</p></div>
<p>Here&#8217;s what my map looks like now, with label and symbol colors matched:</p>
<div class="wp-caption aligncenter" id="attachment_683" style="width: 598px;"><img alt="*Map for illustrative purposes only... not for cartographic/visual design excellence!" class="size-full wp-image-683" height="107" src="http://nyalldawson.net/wp-content/uploads/2015/12/rule_based_result.png" width="588" /><p class="wp-caption-text" id="caption-attachment-683">*Map for illustrative purposes only&#8230; not for cartographic/visual design excellence!</p></div>
<p>If I&#8217;d hard-coded the manual class breaks, it would be a pain to keep the labeling and symbology in sync. I&#8217;d have to make sure that the breaks are updated everywhere I&#8217;ve used them in both the symbology and labeling settings. Aside from being boring, tedious work, this would also prevent immediate before/after comparisons. Using variables instead means that I can update the break value in a single place (the variables panel) and have all my labeling and symbols immediately reflect this change when I hit apply!</p>
<p>Another recent use case I had was teaming layer-level variables along with Time Manager. I wanted my points to falloff in both transparency and size with age, and this involved data defined symbol settings scattered all throughout my layer symbology. By storing the decay fall-off rate in a variable, I could again tweak this falloff by changing the value in a single place and immediately see the result. It also helps with readability of the data defined expressions. Instead of trying to decipher a random, hard-coded value, it&#8217;s instead immediately obvious that this value relates to a decay fall-off rate. Much nicer!</p>
<p>I&#8217;m sure there&#8217;s going to be hundreds of novel uses of layer-level variables which I never planned for when adding this feature. I&#8217;d love to hear about them though &#8211; leave a comment if you&#8217;d like to share your ideas!</p>
<h3>One last thing &#8211; the new &#8220;layer_property&#8221; function</h3>
<p>This isn&#8217;t strictly related to variables, but another new feature which was introduced in QGIS 2.12 was a new &#8220;<em>layer_property</em>&#8221; expression function. This function allows you to retrieve any one of a bunch of properties relating to a specific map layer, including the layer CRS, metadata, source path, etc.</p>
<p>This function can be used anywhere in QGIS. For instance, it allows you to insert dynamic metadata about layers into a print composer layout. In the screenshot below I&#8217;ve used expressions like <em>layer_property(&#8216;patron&#8217;,&#8217;crs&#8217;)</em> and <em>layer_property(&#8216;patron&#8217;,&#8217;source&#8217;) </em>to insert the CRS and source path of the <em>&#8220;patron&#8221;</em> layer into the label. If either the CRS or the file path ever changes, this label will be automatically updated to reflect the new values.</p>
<div class="wp-caption aligncenter" id="attachment_684" style="width: 847px;"><a href="http://nyalldawson.net/wp-content/uploads/2015/12/layer_property.png"><img alt="Inserting dynamic layer properties into a composer label" class="wp-image-684 size-full" height="195" src="http://nyalldawson.net/wp-content/uploads/2015/12/layer_property.png" width="837" /></a><p class="wp-caption-text" id="caption-attachment-684">Inserting dynamic layer properties into a composer label</p></div>
<p>&nbsp;</p>
<p>So there you go &#8211; layer level variables and the layer_property function &#8211; here in QGIS 2.12 and making your workflow in QGIS easier. In the final part of this series, we&#8217;ll explore the magical <em>@value</em> variable. Trust me, I&#8217;ve saved the best for last!</p>
