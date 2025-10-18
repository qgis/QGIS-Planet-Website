---
source: "blog"
title: "Using Data Defined Overrides in QGIS"
date: "2025-06-10T16:15:54+0000"
link: "https://qgis.tips/using-data-defined-overrides-in-qgis/"
draft: "false"
showcase: "planet"
subscribers: ["qgis_dot_tips"]
author: "QGIS.tips"
tags: ["settings", "data", "qgis"]
languages: ["en_gb"]
available_languages: ["en_gb"]
---

<p>Using Data Defined Overrides are a powerful tool in QGIS, but I’ve got the impression that too little people use this feature. So in this blog post you can learn what they are and I’ll show you a simple example of how to use them. You will notice this blog post is pretty long, but that doesn’t mean Data Defined Overrides are difficult, they just have loads of options and I wanted to show you every step I took to use them.</p>
<h2 class="wp-block-heading">What are Data Defined Overrides?</h2>
<p>In QGIS you can use data from a layer or an expression to change the value of a setting in a layer for that specific map object. This means that a setting is dynamically changed based on a value in the attribute table of that object or a value that is generated using an expression. In other words, if you use a Data Defined Override, the manually entered setting is ignored, and instead something else is used.</p>
<span id="more-138"></span>
<h2 class="wp-block-heading">Where do I find these Data Defined Overrides?</h2>
<p>If you see a button like this one: <img alt="" class="wp-image-139" height="30" src="/img/subscribers/qgis_dot_tips/using-data-defined-overrides-in-qgis/data_defined_override_icon.webp" style="width: 32px;" width="32"/> next to a symbology or label setting, then that’s a setting you can change using Data Defined Overrides. You will notice this button is available all over the place in the symbology and label settings of a layer.</p>
<h2 class="wp-block-heading">How to use Data Defined Overrides?</h2>
<p>If you click on a <img alt="" class="wp-image-139" height="30" src="/img/subscribers/qgis_dot_tips/using-data-defined-overrides-in-qgis/data_defined_override_icon.webp" style="width: 32px;" width="32"/> button. A menu will open:</p>
<figure class="wp-block-image size-full"><img alt="" class="wp-image-144" height="296" src="/img/subscribers/qgis_dot_tips/using-data-defined-overrides-in-qgis/data_defined_override_first_menu.webp" width="632"/></figure>
<p>In this menu you will find different ways to enter a Data Defined Override. The first, and maybe simplest way is to select “Field” in this menu. This will show a list of fields that can be used. When you select one of the available fields, the content for that field will be used as a setting.</p>
<figure class="wp-block-image size-full"><img alt="" class="wp-image-143" height="294" src="/img/subscribers/qgis_dot_tips/using-data-defined-overrides-in-qgis/data_defined_override_first_menu_with_fields.webp" width="636"/></figure>
<p>Another simple way to create a Data Defined Overrides is the Assistant. </p>
<figure class="wp-block-image size-full"><img alt="" class="wp-image-174" height="272" src="/img/subscribers/qgis_dot_tips/using-data-defined-overrides-in-qgis/data_defined_override_first_menu_assistant.webp" width="473"/></figure>
<p>If you click on that option, a new window will open:</p>
<figure class="wp-block-image size-full"><img alt="" class="wp-image-173" height="325" src="/img/subscribers/qgis_dot_tips/using-data-defined-overrides-in-qgis/data_defined_override_Assistant.webp" width="357"/></figure>
<p>In that window you get information on what kind of value QGIS expects for this setting. There is also the option to select a field or use the expression editor using the <img alt="" class="wp-image-177" height="26" src="/img/subscribers/qgis_dot_tips/using-data-defined-overrides-in-qgis/expression_button.webp" style="width: 26px;" width="26"/> button in this settings window. In the example above you see the Assistant for the Rotation setting. And you will see it has a lot more options than just the field. The content of this Assistant window will be different depending on the setting you want to override.</p>
<p>Another way to use expressions to create Data Defined Overrides, is selecting “Edit” in the main Data Defined Override menu. This option will also allow you to edit the expression afterwards, if you want to change it.</p>
<figure class="wp-block-image size-full"><img alt="" class="wp-image-142" height="366" src="/img/subscribers/qgis_dot_tips/using-data-defined-overrides-in-qgis/data_defined_override_first_menu_edit.webp" width="625"/></figure>
<p>In the Expression Builder you can use all possibilities the expressions give you, but you have to make sure the result of your expression is a value the setting expects. The expected format is shown under the expression input box. The preview of the expressions result is a good way to check if the result are compatible with the expected format.</p>
<figure class="wp-block-image size-full"><img alt="" class="wp-image-141" height="332" src="/img/subscribers/qgis_dot_tips/using-data-defined-overrides-in-qgis/data_defined_override_expression_builder.webp" width="627"/></figure>
<h2 class="wp-block-heading">The button turned yellow!</h2>
<p>If a Data Defined Override is used the <img alt="" class="wp-image-139" height="30" src="/img/subscribers/qgis_dot_tips/using-data-defined-overrides-in-qgis/data_defined_override_icon.webp" style="width: 32px;" width="32"/> turns into <img alt="" class="wp-image-195" height="23" src="/img/subscribers/qgis_dot_tips/using-data-defined-overrides-in-qgis/data_defined_override_icon_yellow.webp" style="width: 35px;" width="35"/>. That way QGIS notifies you that the setting itself is ignored by the program, but instead the Data Defined Override is used. If you want disable the Data Defined Override, you can go to edit and remove the expression or you can select the option “Clear” after you pressed the <img alt="" class="wp-image-195" height="23" src="/img/subscribers/qgis_dot_tips/using-data-defined-overrides-in-qgis/data_defined_override_icon_yellow.webp" style="width: 35px;" width="35"/> button.</p>
<figure class="wp-block-image size-full"><img alt="" class="wp-image-196" height="298" src="" width="239"/></figure>
<h2 class="wp-block-heading">What can I enter into a Data Defined Override?</h2>
<p>The answer to that question depends on the setting you want to override. The Expression builder or the Assistant will probably make it clear what kind of value from a field or expression is expected. For example:</p>
<ul class="wp-block-list">
<li>The setting <em>rotation </em>will expect a “double” value between 0 and 360. So 122.5 would be a valid value.</li>
<li>An <em>opacity </em>setting will expect an “integer” value between 0 and 100. So 50 would be a valid value, but 50.1 wouldn’t.</li>
<li>A <em>color </em>expects a “text” in one of the following kinds of forms:
<ul class="wp-block-list">
<li>[r,g,b,a] where r is red, g is green, b is blue and a is the alpha value. Each of these is an integer value between 0 and 255. The entire setting without the square brackets must be a text. So for example ‘250,25,100,200’ <span>▮</span> including the single quotes would be a valid color setting.</li>
<li>Hex color codes in the forms #AARRGGBB or #RRGGBB as a text value like they are used in HTML and CSS are possible to define a color. So for example ‘#FF5000’ <span style="color: #FF5000;">▮</span> is a possible color.</li>
<li>A third way to define a color is to use the name of the color. A list of color names can be found on <a href="https://developer.mozilla.org/en-US/docs/Web/CSS/named-color">https://developer.mozilla.org/en-US/docs/Web/CSS/named-color</a>. So for example ‘skyblue’ <span style="color: skyblue;">▮</span> is a possible color.</li>
</ul>
</li>
</ul>
<p>Units like degrees or percentages are not part of the value. QGIS will assume these units based on the setting you want to override. Sometimes the units are a separate setting, and so for a width you first set the unit setting and for the main width setting you can use the Data Defined Override.</p>
<h2 class="wp-block-heading">A simple example</h2>
<p>To make Data Defined Overrides easier to understand I’ll show it with this simple example below. We start with a simple point layer. In this example the points are the locations of arrows we want to place along a route. We want the arrows to be rotated so they are aligned along the route. To accomplish this I have added a field called “rotation” and for each point I have entered a number into that field that has the rotation value (between 0° and 360°) of each arrow.</p>
<figure class="wp-block-image size-full"><img alt="" class="wp-image-147" height="444" src="/img/subscribers/qgis_dot_tips/using-data-defined-overrides-in-qgis/data_defined_override_attribute_table.webp" width="224"/></figure>
<p>On the map below you can see each point labelled with it’s rotation value.</p>
<figure class="wp-block-image size-full"><img alt="" class="wp-image-153" height="883" src="/img/subscribers/qgis_dot_tips/using-data-defined-overrides-in-qgis/pointlayer.webp" width="930"/></figure>
<p>After that we will change the symbol of the points to arrows. You can style them anyway you want, but I chose to make them as a simple marker with a simple red arrows. At this moment all arrows will point up.</p>
<figure class="wp-block-image size-full"><img alt="" class="wp-image-186" height="883" src="/img/subscribers/qgis_dot_tips/using-data-defined-overrides-in-qgis/arrowlayer.webp" width="967"/></figure>
<p>To change the rotation we will now use Data Defined Overrides. First we have to click on the <img alt="" class="wp-image-139" height="30" src="/img/subscribers/qgis_dot_tips/using-data-defined-overrides-in-qgis/data_defined_override_icon.webp" style="width: 32px;" width="32"/> button next to the rotation setting. There I click on the option “Field”, and select the field “orientation” I previously created in my shapefile.</p>
<figure class="wp-block-image size-full"><img alt="" class="wp-image-143" height="294" src="/img/subscribers/qgis_dot_tips/using-data-defined-overrides-in-qgis/data_defined_override_first_menu_with_fields.webp" width="636"/></figure>
<p>After I did that, you will see that each arrow is rotated based on its value in the field “rotation” in my shapefile.</p>
<figure class="wp-block-image size-full"><img alt="" class="wp-image-188" height="883" src="/img/subscribers/qgis_dot_tips/using-data-defined-overrides-in-qgis/rotatedarrowlayer.webp" width="967"/></figure>
<p>After that I also added the route as a separate blue layer and added the field “rotation” also as a label on top of the arrows. I also used Data Defined Override for the rotation setting of the label and that results in the map below.</p>
<figure class="wp-block-image size-full"><img alt="" class="wp-image-140" height="883" src="/img/subscribers/qgis_dot_tips/using-data-defined-overrides-in-qgis/result_rotation.webp" width="930"/></figure>
<h2 class="wp-block-heading">Another example</h2>
<p>As said before you can find Data Defined Overrides in lots of settings. In the example below I used the same “rotation” setting on the field “Size”. Ans I used “Meters at scale” as unit for Size.</p>
<figure class="wp-block-image size-full"><img alt="" class="wp-image-192" height="883" src="/img/subscribers/qgis_dot_tips/using-data-defined-overrides-in-qgis/resizedarrowlayer.webp" width="967"/></figure>
<h2 class="wp-block-heading">To conclude</h2>
<p>I hope this explanation helps you understand that Data Defined Overrides are a powerful tool to create symbologies. I used the a lot in my examples for Geometry Generators you can find on <a href="https://codeberg.org/gis-projects/qgis-geometry-generator-examples/" rel="noreferrer noopener" target="_blank">Codeberg</a>, because those two QGIS functionalities make a great combination. But more about that will follow in one of the next posts on this blog.</p>
<p>Please tell about how and why you use Data Defined Overrides in QGIS in the comments below. I’d love to hear about other use cases.</p>
<p></p>
