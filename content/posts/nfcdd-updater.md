---
source: "blog"
title: "NFCDD Updater"
date: "2012-07-09T13:00:00-0500"
link: "https://lutraconsulting.co.uk/blog/2012/07/09/nfcdd-updater/"
draft: "false"
showcase: "planet"
subscribers: ["lutragis"]
author: "Lutra Consulting"
tags: []
---

<p>NFCDD Updater is a QGIS extension developed by Lutra Consulting for Halcrow Group to automate the process of updating geometry and attribute data in the Environment Agency's National Flood and Coastal Defence Database (NFCDD).</p>

<!-- more -->

<p>As part of their <em>Ravensbourne Raised Defences</em> project, Halcrow were required to update flood defence crest level and standard of protection data for defence assets along the rivers Ravensbourne and Quaggy, south-east London based on the results from extensive ISIS modelling.</p>

<p><img alt="NFCDD Updater User Interface" src="https://www.lutraconsulting.co.uk/img/posts/nfcdd-updater-ui.png" /></p>
<p>The updates were originally carried out as a manual GIS task, requiring GIS technicians to edit NFCDD geometry and attributes manually.  The editing was prone to human error and was a complex and time-consuming process.</p>
<p>Lutra Consulting were commissioned to develop NFCDD Updater - a bespoke extension (plugin) to the free and open-source GIS platform QGIS.  NFCDD Updater automates the task of updating NFCDD while allowing the user to maintain a high level of control over the process.</p>

<p>NFCDD Updater performs the following tasks:</p>
<ul>
    <li>Imports NFCDD dataset and reads user control file</li>
    <li>Creates new defence features between ISIS nodes of interest based on existing geometry</li>
    <li>Populates the new defence features with information from the user control file</li>
    <li>Performs any necessary update of attributes to neighbouring 'parent' defence features (length etc.)</li>
    <li>Exports the updated table in MapInfo format, ready to be imported back into NFCDD</li>
</ul>

<p>NFCDD Updater was designed to be simple to use and to allow user-interaction where required, for example, prompting the user to visually select a single defence line to update when more than one candidate defence line has been selected for updating automatically.</p>

<p>NFCDD Updater performed very well in terms of reducing manual GIS work required to complete the project and allowed approximately 30% of the project budget to be saved.  With minor modifications, NFCDD updater can be updated to automate manual GIS tasks on other Halcrow projects.</p>

<p>For more information on NFCDD Updater or to find out more about the development of bespoke QGIS plugins, contact <a href="mailto:peter.wells.lutraconsulting.co.uk">Peter Wells</a>.</p>

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
