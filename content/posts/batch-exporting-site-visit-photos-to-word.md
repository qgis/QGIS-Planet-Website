---
source: "blog"
title: "Quickly Get Site Photos Into Word"
date: "2021-02-10T02:00:00-0600"
link: "https://lutraconsulting.co.uk/blog/2021/02/10/batch-exporting-site-visit-photos-to-word/"
draft: "false"
showcase: "planet"
subscribers: ["lutragis"]
author: "Lutra Consulting"
tags: []
---

<p>Preparing reports with lots of survey photos takes time - this plugin automates the process.</p>

<p>Nowadays, it’s really easy to take georeferenced photos on site visits.  Tools like <a href="https://merginmaps.com/">Input</a> can capture photos, descriptions and location information and bringing it all into GIS is straight-forward.  However.. I recently discovered that people still spend significant amounts of time organising their photos into reports outside of GIS.  This small plugin automates the process of getting the photos and their descriptions into Microsoft Word.</p>

<p><img alt="Using Input to Survey My Garden" src="https://www.lutraconsulting.co.uk/img/posts/using_input_to_survey_my_garden.png" /></p>

<p>For this blog post I knocked-up a simple survey project based on the <a href="https://merginmaps.com/docs/tutorials/capturing-first-data/">Field notes Mergin template</a>.  Points can have a photo, title and description amongst other fields.  No comments on my gardening skills please!</p>

<p>When I sync the data back to QGIS, the attribute table looks something like this:</p>

<p><img alt="The Input Survey Layer's Table of Attributes" src="https://www.lutraconsulting.co.uk/img/posts/input_survey_layers_table_of_attributes.png" /></p>

<p>We’ll now use the <em>HTML Table Exporter</em> plugin to export the layer as an HTML table (this will let us get it into Word).</p>

<p>First install the plugin.</p>

<p>It’s an experimental plugin so you’ll first need to check the <em>Show also experimental plugins</em> option under <em>Plugins &gt; Manage and Install Plugins… &gt; Settings</em>.</p>

<p>When you have installed the plugin, open it using this button <img alt="HTML Table Exporter Icon" src="https://www.lutraconsulting.co.uk/img/posts/html_table_exporter.png" /> or via <em>Plugins &gt; HTML Table Exporter &gt; Export table as HTML</em>.</p>

<p>You should now see this:</p>

<p><img alt="HTML Table Exporter Dialog" src="https://www.lutraconsulting.co.uk/img/posts/html_table_exporter_dialog.png" /></p>

<p>Set <em>Table</em> to the layer you want to export.  The image scaling option is described later, leave it at a small setting for the time being.  Click OK to export and tell the plugin where to save the HTML file.</p>

<p>Now the data should be out of QGIS.. the next steps are in.. MS Word :o</p>

<p>Right click on the exported html file and open it with Microsoft Word:</p>

<p><img alt="Open Exported HTML With Word" src="https://www.lutraconsulting.co.uk/img/posts/open_with_word.png" /></p>

<p>Let’s see what it looks like:</p>

<p><img alt="First Export in Word" src="https://www.lutraconsulting.co.uk/img/posts/first_export_in_word.png" /></p>

<p>OK.. we’re getting somewhere!  At this point you’ll want to:</p>

<ul>
  <li>Enable <em>Print Layout</em> mode in Word so you can see what the printed page will look like</li>
  <li>Set the page orientation as desired (I chose landscape in the image above)</li>
  <li>Experiment with image rotation if required (Right click photo &gt; <em>Size and position &gt; Rotation</em>)</li>
</ul>

<p>If playing with rotation, just focus on rotating a single image, we’ll batch rotate later as required.  For now you want to get a feel of whether you want to adjust the scale factor in QGIS (to make the images smaller or larger) to save you having to resize them individually in Word.</p>

<p>I’ve decided to increase the scale factor from 10% to 15% so will now re-export.</p>

<p><strong>Beware that Word has an exclusive lock on the html file when it’s open so you need to close it in Word before you can export it again from QGIS.</strong></p>

<p>I settled for 10% in the end so I could get multiple images on each page in portrait mode.  After removing the columns I didn’t want, the table in Word now looks like this:</p>

<p><img alt="A Better Export to Word" src="https://www.lutraconsulting.co.uk/img/posts/better_export_to_word.png" /></p>

<p>To rapidly rotate images by 90 degrees, rotate the first one using <em>Right click on photo &gt; Size and position &gt; Rotation</em> then select subsequent photos and press the F4 key.  <a href="https://www.datanumen.com/blogs/6-effective-ways-batch-rotate-multiple-images-word-document/">This method is described in more detail here</a> as well as other Word batch image rotation methods.</p>

<p>My document is almost finished.  There are just a few small issues to iron out.  Currently, the images are <strong>referenced</strong> by the Word document, <strong>not embedded</strong>.  This means if I email the document to someone, the images will be missing.  Let’s fix that by embedding the images in the word document.</p>

<p>First save the document as a Word document in Word’s native format (e.g. *.docx).</p>

<p>Next, locate the <em>Edit Links to Files</em> option:</p>

<p><img alt="Edit Links to Documents" src="https://www.lutraconsulting.co.uk/img/posts/edit_links_to_documents.png" /></p>

<p>Select all the linked images (the shift and arrow keys help here) and check the <em>Save picture in document</em> option and click OK:</p>

<p><img alt="Save Picture In Document" src="https://www.lutraconsulting.co.uk/img/posts/save_picture_in_document.png" /></p>

<p>Save the document, your photos should now be embedded within the document.</p>

<p>If you find your word document gets huge, you can <a href="https://support.microsoft.com/en-us/office/reduce-the-file-size-of-a-picture-in-microsoft-office-8db7211c-d958-457c-babd-194109eb9535">use the method here to quickly batch compress all images in the document</a>.</p>

<p>Input is a free and open source field data collection and mobile GIS app based on QGIS.</p>

<p><a href="https://play.google.com/store/apps/details?id=uk.co.lutraconsulting&amp;utm_source=lutra-atom&amp;utm_medium=lutra-blog&amp;utm_campaign=input"><img alt="Get it on Google Play" src="https://play.google.com/intl/en_us/badges/images/generic/en_badge_web_generic.png" width="180px" /></a><a href="https://apps.apple.com/us/app/input/id1478603559?ls=1&amp;utm_source=lutra-atom&amp;utm_medium=lutra-blog&amp;utm_campaign=input"><img alt="Get it on Apple store" src="https://www.lutraconsulting.co.uk/img/posts/App_Store.svg" style="padding-top: 0px;" width="144px" /></a></p>

<p>If this guide saved you some time and you feel like doing something awesome for us, a review of Input on the <a href="https://apps.apple.com/gb/app/input/id1478603559?utm_source=lutra-atom&amp;utm_medium=lutra-blog&amp;utm_campaign=input">Apple App Store</a> or <a href="https://play.google.com/store/apps/details?id=uk.co.lutraconsulting&amp;utm_source=lutra-atom&amp;utm_medium=lutra-blog&amp;utm_campaign=input">Google Play Store</a> would be really well appreciated.</p>
