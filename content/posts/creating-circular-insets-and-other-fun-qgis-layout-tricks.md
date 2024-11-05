---
source: "blog"
title: "Creating circular insets and other fun QGIS layout tricks"
date: "2022-11-04T03:05:00+0000"
link: "https://north-road.com/2022/11/04/creating-circular-insets-and-other-fun-qgis-layout-tricks/"
draft: "false"
showcase: "planet"
subscribers: ["north_road"]
author: "North Road"
tags: ["cartography", "qgis", "cartography", "composer", "html", "layouts", "qgis"]
---

<p><em><strong>Thanks to the recent popularity of the &#8220;<a href="https://twitter.com/hashtag/30DayMapChallenge">30 Day Map Challenge</a>&#8220;, the month of November has become synonymous with beautiful maps and cartography. During this November we&#8217;ll be sharing a bunch of tips and tricks which utilise some advanced QGIS functionality to help create beautiful maps.</strong></em></p>
<p>One technique which can dramatically improve the appearance of maps is to swap out rectangular inset maps for more organic shapes, such as circles or ovals.</p>
<p>Back in 2020, we had the opportunity to add support for directly creating circular insets in QGIS Print Layouts (thanks to sponsorship from the City of Canning, Australia!). While this functionality makes it easy to create non-rectangular inset maps the steps, many QGIS users may not be aware that this is possible, so we wanted to highlight this functionality for our first 30 Day Map Challenge post.</p>
<p>Let&#8217;s kick things off with an example map. We&#8217;ve shown below an extract from the <a href="https://stillmed.olympics.com/media/Documents/Olympic-Games/Brisbane-2032/General/IOC-Feasibility-Assessment-Brisbane.pdf?_ga=2.48780838.1295957495.1666960789-1227590087.1665520398">2032 Brisbane Olympic Bid</a> that some of the North Road team helped create (on behalf of <a href="https://www.smec.com/au/">SMEC </a>for <a href="https://www.eks.com">EKS</a>). This map is designed to highlight potential venues around South East Queensland and the travel options between these regions:</p>
<figure class="wp-caption aligncenter" id="attachment_212431" style="width: 719px;"><a href="https://stillmed.olympics.com/media/Documents/Olympic-Games/Brisbane-2032/General/IOC-Feasibility-Assessment-Brisbane.pdf?_ga=2.48780838.1295957495.1666960789-1227590087.1665520398"><img alt="Venue Masterplan Brisbane 2032 Olympics" class="wp-image-212431" height="732" src="https://north-road.com/wp-content/uploads/2022/11/Olympic-map-2-1006x1024.png" width="719" /></a><figcaption class="wp-caption-text" id="caption-attachment-212431">Venue Masterplan for 2032 Olympic Games, IOC Feasibility Assessment &#8211; Olympic Games, Brisbane February 2021</figcaption></figure>
<p>Circles featured heavily in previous Olympic bid maps (such as Budapest) where we took our inspiration from. This may, or may not, play a part in using the language of the target map audience &#8211; think Olympic rings!</p>
<p style="text-align: center;"><a href="https://architectureofthegames.net/tag/budapest/"><img alt="Budapest Olympics 2024 Masterplan" class="wp-image-212407 aligncenter" height="470" src="https://north-road.com/wp-content/uploads/2022/11/2024-Bid-Masterplan-Budapest-2024-1-1024x691.jpg" width="696" /></a>Budapest Olympics 2024 Masterplan</p>
<p>&nbsp;</p>
<h3>Step by Step Guide to Creating a Circle Inset</h3>
<p>Firstly, prepare a print layout with both a main map and an inset map. Make sure that your inset map is large enough to cover your circular shape:</p>
<p><img alt="" class="wp-image-212432 alignnone" height="451" src="https://north-road.com/wp-content/uploads/2022/11/base-map-1024x730.png" width="633" /></p>
<p>From the Print Layout toolbar, click on the <b>Add Shape</b> button and then select <strong>Add </strong><strong>Ellipse</strong><i>:</i></p>
<p><img alt="" class="wp-image-212421 alignnone" height="164" src="https://north-road.com/wp-content/uploads/2022/11/add-shape.png" width="250" /></p>
<p>Draw the ellipse over the middle of your inset map (hint: holding down Shift while drawing the ellipse will force it to a circular shape!). If you didn&#8217;t manage to create an exact circle then you can manually specify the width and height in the shape item&#8217;s properties. For this one, we went with a 50mm x 50mm circle:</p>
<p><img alt="" class="alignnone wp-image-212410" height="352" src="https://north-road.com/wp-content/uploads/2022/11/Ellipse-measurements.png" width="577" /></p>
<p>Next, select the Inset Map item and in its <strong>Item Properties</strong> click on the <b>Clipping Settings button:</b></p>
<p><img alt="" class="alignnone size-full wp-image-212409" height="90" src="https://north-road.com/wp-content/uploads/2022/11/clipping-settings.png" width="393" /></p>
<p>In the <b>Clipping Settings</b>, scroll down to the second section and tick the <i>Clip to Item</i> box and select your Ellipse item from the list. (If you have labels shown in your inset map you may also want to check the &#8220;force labels inside clipping shape&#8221; option to force these labels inside the circle. If you don&#8217;t check this option then labels will be allowed to overflow outside of the circle shape.)</p>
<p><img alt="" class="alignnone size-full wp-image-212426" height="186" src="https://north-road.com/wp-content/uploads/2022/11/clipping-settings2.png" width="552" /></p>
<p>Your inset map will now be bound to the ellipse!</p>
<p><img alt="" class="alignnone size-full wp-image-212408" height="427" src="https://north-road.com/wp-content/uploads/2022/11/clipped-inset.png" width="478" /></p>
<p>Here’s a bit more magic you could add to this map &#8211; in the Main Map&#8217;s properties, click on <i>Overviews</i> and set create one for the Inset map &#8211; it will nicely show the visible circular area and not the rectangle!</p>
<p><img alt="" class="alignnone size-full wp-image-212413" height="537" src="https://north-road.com/wp-content/uploads/2022/11/overview-map.png" width="829" /></p>
<h3>Bonus Points: Circular Title Text!</h3>
<p>For advanced users, we&#8217;ve another fun tip…and when we say fun, we mean &#8216;let’s play with radians&#8217;! Here we&#8217;re going to create some title text and a wedged background which curves around the outside of our circular inset. This takes some fiddly playing around, but the end result can be visually striking! Here we&#8217;re going to push the QGIS print layout &#8220;HTML&#8221; item to create some advanced graphics, so some HTML and CSS coding experience is advantageous. (An alternative approach would be to use a vector illustration application like <a href="https://inkscape.org/">Inkscape</a>, and add your title and circular background as an SVG item in the print layout).</p>
<p>We&#8217;ll start by creating some curved circular text:</p>
<p><img alt="" class="alignnone size-full wp-image-212415" height="239" src="https://north-road.com/wp-content/uploads/2022/11/text.png" width="265" /></p>
<p>First, add a &#8220;HTML frame&#8221; to your print layout:</p>
<p><img alt="" class="alignnone size-full wp-image-212411" height="77" src="https://north-road.com/wp-content/uploads/2022/11/html-frame-tool.png" width="113" /></p>
<p>HTML frames allow placement of dynamic content in your layouts, which can use HTML, CSS and JavaScript to create graphical components.</p>
<p>In the HTML item&#8217;s &#8220;<strong>source&#8221;</strong> box, add the following code:</p>
<pre>&lt;svg height="300" width="350"&gt;
        &lt;defs&gt;
            &lt;clipPath id="circleView"&gt;
                &lt;circle id="curve" cx="183" cy="156" r="25" fill="transparent" /&gt;
            &lt;/clipPath&gt;
        &lt;/defs&gt;
        &lt;path id="forText" d="M 28,150, C 25,50, 180,-32,290,130" stroke="" fill="none"/&gt;
            &lt;text x="0" y="35" width="100"&gt;
                &lt;textpath xlink:href="#forText"&gt;
                    &lt;tspan font-weight="bold" fill="black"&gt;Place text here&lt;/tspan&gt;
                &lt;/textpath&gt;
            &lt;/text&gt;
             &lt;style&gt;
    &lt;![CDATA[
      text{
        dominant-baseline: hanging;
        font: 20px Arial;
      }
    ]]&gt;
  &lt;/style&gt;
&lt;/svg&gt;</pre>
<p>Now, let&#8217;s add in a background to bring more focus onto the title!</p>
<p><img alt="" class="alignnone size-medium wp-image-212427" height="277" src="https://north-road.com/wp-content/uploads/2022/11/text-with-background-1-300x277.png" width="300" /></p>
<p>To add in the background, create another HTML item. We&#8217;ll again create the arc shape using an SVG element, so add the following code into the item&#8217;s <strong>source</strong> box:</p>
<pre>&lt;svg width="750" height="750" xmlns="http://www.w3.org/2000/svg"&gt;
  &lt;path d="M 90 70
           A 56 56, 0, 0, 0, 133 140
           L 150 90 Z" fill="#414042" transform=" scale(2.1) rotate(68 150 150) " /&gt;/&gt;
&lt;/svg&gt;</pre>
<p>(You can read more about <a href="https://developer.mozilla.org/en-US/docs/Web/SVG/Tutorial/Paths">SVG  curves and arcs paths over</a> at MDN<a href="https://developer.mozilla.org/en-US/docs/Web/SVG/Tutorial/Paths">)</a></p>
<p><em><strong>So there we go! These two techniques can help push your QGIS map creations further and make it easier to create beautiful cartography directly in QGIS itself. If you found these tips useful, keep an eye on this blog as we post more tips and tricks over the month of November. And don&#8217;t forget to follow the <a href="https://30daymapchallenge.com/">30 day Map Challenge</a> for a smorgasbord of absolutely stunning maps.</strong></em></p>
<div class="supsystic-social-sharing supsystic-social-sharing-package-flat supsystic-social-sharing-hide-on-homepage supsystic-social-sharing-spacing supsystic-social-sharing-content supsystic-social-sharing-content-align-left" style="font-size: 0.7em!important; display: none;"><a class="social-sharing-button sharer-flat sharer-flat-1 counter-standard without-counter twitter" href="https://twitter.com/share?url=https%3A%2F%2Fnorth-road.com%2F2022%2F11%2F04%2Fcreating-circular-insets-and-other-fun-qgis-layout-tricks%2F&amp;text=Creating+circular+insets+and+other+fun+QGIS+layout+tricks" rel="nofollow" target="_blank" title="Twitter"><i class="fa-ssbs fa-ssbs-fw fa-ssbs-twitter"></i><div class="counter-wrap standard"><span class="counter">0</span></div></a><a class="social-sharing-button sharer-flat sharer-flat-1 counter-standard without-counter linkedin" href="https://www.linkedin.com/shareArticle?mini=true&amp;title=Creating+circular+insets+and+other+fun+QGIS+layout+tricks&amp;url=https%3A%2F%2Fnorth-road.com%2F2022%2F11%2F04%2Fcreating-circular-insets-and-other-fun-qgis-layout-tricks%2F" rel="nofollow" target="_blank" title="Linkedin"><i class="fa-ssbs fa-ssbs-fw fa-ssbs-linkedin"></i><div class="counter-wrap standard"><span class="counter">0</span></div></a><a class="social-sharing-button sharer-flat sharer-flat-1 counter-standard without-counter facebook" href="http://www.facebook.com/sharer.php?u=https%3A%2F%2Fnorth-road.com%2F2022%2F11%2F04%2Fcreating-circular-insets-and-other-fun-qgis-layout-tricks%2F" rel="nofollow" target="_blank" title="Facebook"><i class="fa-ssbs fa-ssbs-fw fa-ssbs-facebook"></i><div class="counter-wrap standard"><span class="counter">0</span></div></a></div>
