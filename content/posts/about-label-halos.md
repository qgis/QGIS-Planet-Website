---
source: "blog"
title: "About label halos"
date: "2017-04-28T10:46:33+0000"
link: "http://nyalldawson.net/2017/04/about-label-halos/"
draft: "false"
showcase: "planet"
subscribers: ["nyalldawson_net"]
author: "nyalldawson.net"
tags: ["qgis", "3.0", "cartography", "colour", "geospatial", "labelling", "osgeo", "qgis"]
---

<p>A lot of cartographers have a love/hate relationship with label halos. On one hand they can be an essential technique for improving label readability, especially against complex background layers. On the other hand they tend to dominate maps and draw unwanted attention to the map labels.</p>
<p>In this post I&#8217;m going to share my preferred techniques for using label halos. I personally find this technique is a good approach which minimises the negative effects of halos, while still providing a good boost to label readability. (I&#8217;m also going to share some related QGIS 3.0 news at the end of this post!)</p>
<p>Let&#8217;s start with some simple white labels over an aerial image:</p>
<p><img alt="" class="alignnone wp-image-719 size-full" height="411" src="http://nyalldawson.net/wp-content/uploads/2017/04/2017-04-27.png" width="412" /></p>
<p>These labels aren&#8217;t very effective. The complex background makes them hard to read, especially the &#8220;Winton Shire&#8221; label at the bottom of the image. A quick and nasty way to improve readability is to add a black halo around the labels:</p>
<p><img alt="" class="alignnone wp-image-720 size-full" height="426" src="http://nyalldawson.net/wp-content/uploads/2017/04/2017-04-27-1.png" width="454" /></p>
<p>Sure, it&#8217;s easy to read the labels now, but they stand out way too much and it&#8217;s difficult to see anything here except the labels!</p>
<p>We can improve this somewhat through a better choice of halo colour:</p>
<p><img alt="" class="alignnone wp-image-721 size-full" height="423" src="http://nyalldawson.net/wp-content/uploads/2017/04/2017-04-27-2.png" width="391" /></p>
<p>This is much better. We&#8217;ve got readable labels which aren&#8217;t too domineering. Unfortunately the halo effect is still very prominent, especially where the background image varies a lot. In this case it works well for the labels toward the middle of the map, but not so well for the labels at the top and bottom.</p>
<p>A good way to improve this is to take advantage of blending (or &#8220;composition&#8221;) modes (which QGIS has <a href="http://nyalldawson.net/2013/03/coming-soon-in-qgis-2-0-blend-modes-for-layers/">native support</a> for). The white labels will be most readable when there&#8217;s a good contrast with the background map, i.e. when the background map is dark. That&#8217;s why we choose a halo colour which is darker than the text colour (or vice versa if you&#8217;ve got dark coloured labels). Unfortunately, by choosing the mid-toned brown colour to make the halos blend in more, we are actually lightening up parts of this background layer and both reducing the contrast with the label and also making the halo more visible. By using the &#8220;darken&#8221; blend mode, the brown halo will only be drawn for pixels were the brown is darker then the existing background. It will darken light areas of the image, but avoid lightening pixels which are already dark and providing good contrast. Here&#8217;s what this looks like:</p>
<p><img alt="" class="alignnone wp-image-722 size-full" height="420" src="http://nyalldawson.net/wp-content/uploads/2017/04/2017-04-27-3.png" width="428" /></p>
<p>The most noticeable differences are the labels shown above darker areas &#8211; the &#8220;Winton Shire&#8221; label at the bottom and the &#8220;Etheridge Shire&#8221; at the top. For both these labels the halo is almost imperceptible whilst still subtly doing it&#8217;s part to make the label readable. (If you had dark label text with a lighter halo color, you can use the &#8220;lighten&#8221; blend mode for the same result).</p>
<p>The only issue with this map is that the halo is still very obvious around &#8220;Shire&#8221; in &#8220;Richmond Shire&#8221; and &#8220;McKinlay&#8221; on the left of the map. This can be reduced by applying a light blur to the halo:</p>
<p><img alt="" class="alignnone wp-image-723 size-full" height="409" src="http://nyalldawson.net/wp-content/uploads/2017/04/2017-04-27-5.png" width="406" /></p>
<p>There&#8217;s almost no loss of readability by applying this blur, but it&#8217;s made those last prominent halos disappear into the map. At first glance you probably wouldn&#8217;t even notice that there&#8217;s any halos being used here. But if we compare back against the original map (which used no halos) we can see the huge difference in readability:</p>
<p><img alt="" class="alignnone wp-image-719 size-full" height="411" src="http://nyalldawson.net/wp-content/uploads/2017/04/2017-04-27.png" width="412" /></p>
<p>Compare especially the Winton Shire label at the bottom, and the Richmond Shire label in the middle. These are much clearer on our tweaked map versus the above image.</p>
<p>Now for the good news&#8230; when QGIS 3.0 is released you&#8217;ll no longer have to rely on an external illustration/editing application to get this effect with your maps. In fact, QGIS 3.0 is bringing native support for applying many types of <a href="http://nyalldawson.net/2015/04/introducing-qgis-live-layer-effects/">live layer effects</a> to label buffers and background shapes, including blur. This means it will be possible to reproduce this technique directly inside your GIS, no external editing or tweaking required!</p>
