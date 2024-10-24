---
source: "blog"
title: "Organising Charitable Collection Routes with Offline Mobile Maps"
date: "2021-09-09T00:05:00-0500"
link: "https://lutraconsulting.co.uk/blog/2021/09/09/charity-case-study/"
draft: "false"
showcase: "planet"
subscribers: ["lutragis"]
author: "Lutra Consulting"
tags: []
---

<p>Significant time saved when route maps distributed with Input and Mergin.</p>

<!-- more -->

<p>This case study was originally written in Czech. <a href="https://lutraconsulting.co.uk/blog/2021/09/09/charity-case-study_cz/">The Czech version can be found here</a>.</p>

<p>Every year, teams of volunteers walk door-to-door through the Czech town of Litomyšl collecting charitable donations. Event organisers define routes for the various volunteer teams by marking-up paper maps with pens. The process has a number of issues both in the making and usage of the maps which organisers worked to overcome by making the maps digital using open source GIS software.</p>

<p>Maps were developed using QGIS and made available on volunteers’ phones using <a href="https://merginmaps.com">the Input app</a>. Volunteers are now able to easily orientate themselves on maps which clearly show their routes. Organisers have reduced the time it takes to update routes and distribute these to volunteers.</p>

<p>Veronika Peterková works for the <a href="https://litomysl.charita.cz">Litomyšl Parish Charity</a>, a non-profit organisation providing health and social services to people in need since 1993.</p>

<p>Veronika describes the charity’s activities: “We provide home medical services and nursing care to the residents of Litomyšl and its surrounding villages. This includes helping families where the healthy development of a child is at risk and providing respite stays for clients who are otherwise cared for by their families at home. We provide care for about 1000 clients a year.”</p>

<p>She added: “We also coordinate the activities of volunteers who visit the elderly, help with tutoring children and with various leisure and cultural activities.”</p>

<p>One of the parish charity’s biggest fundraising events is the <a href="https://litomysl.charita.cz/trikralova-sbirka/">“Tříkrálová sbírka”</a> (Three Kings Collection), a door-to-door carol-singing collection taking part around the 6th of January each year.</p>

<center>
<img alt="Tříkrálová sbírka Litomyšl" src="https://lutraconsulting.co.uk/img/case-studies/charita_litomysl/kolednici.jpg" title="Tříkrálová sbírka Litomyšl" width="600" />
<p><em>Volunteers participating in the Three Kings Collection.</em></p>
</center>

<p>“The Three Kings Collection is the largest national volunteer event in the Czech Republic. In the Litomyšl region alone, nearly 300 volunteers are involved each year with the carol-singers collecting over 500,000 Czech crowns (~20,000 EUR) in sealed boxes. The proceeds are intended to help the sick, the disabled, the elderly, mothers with children in need and other in-need groups in the local area.” Veronika explains.</p>

<p>The Three Kings Collection is organised by <a href="https://www.charita.cz/en/">Caritas Czech Republic</a> and at least 10% of its proceeds are allocated for humanitarian aid abroad.</p>

<center>
<img alt="charita logo" src="https://lutraconsulting.co.uk/img/case-studies/charita_litomysl/charita_logo.jpg" title="charita logo" width="100" />
</center>

<h2 id="the-challenge">The Challenge</h2>

<p>Veronika is responsible for planning routes for the carol-singers so they efficiently visit households in the Litomyšl area. Singers are split into groups and paper maps are provided which show groups which households to visit.</p>

<center>
<img alt="Old map © mapy.cz" src="https://lutraconsulting.co.uk/img/case-studies/charita_litomysl/old_maps.jpg" title="Old map © mapy.cz" width="600" />
<p><em>An example of previous paper maps, image courtesy of Farní charita Litomyšl.</em></p>
</center>

<p>The above maps were produced by printing screenshots from a national web mapping provider and marking-up printouts for each of the 50 teams using marker pens.</p>

<p>This method proved to have a number of issues as Veronika describes: “On maps of larger areas, house numbers were not always visible due to the scale. This made it even harder for coordinators not familiar with the area to orient themselves, leading to confusion. Coordinators also found it hard to keep the maps dry and undamaged during unfavourable weather. If new groups signed-up afterwards or others opted-out, we’d have to redo/redivide the areas which would be very time-consuming as the maps would need to be marked-up manually once again.”</p>

<h2 id="the-solution-and-implementation">The Solution and Implementation</h2>
<p>Veronika wanted to try a new solution for organising the 2021 Three Kings Collection with the goal of making volunteer tasks clearer and less reliant on paper maps. She wanted the new solution to allow her to:</p>

<ul>
  <li>reduce work through the reuse of maps in future Three Kings Collection events</li>
  <li>easily update maps if new groups sign in/out and areas need editing</li>
  <li>allow carol singers to see exactly where they are on the map</li>
  <li>gradually replace paper maps while still allowing the use of paper maps where preferred</li>
  <li>group and colour buildings to be visited on the computer</li>
  <li>record a building’s use (e.g. commercial) to direct volunteers more effectively</li>
  <li>clearly show how areas are assigned so anyone can see who is responsible for a given area</li>
</ul>

<p>In addition, Veronika wanted the solution to be affordable and work offline without volunteers needing internet connectivity in the field.</p>

<p>Peter Petrík, a regular participant of the Litomyšl Three Kings Collection suggested Veronika try using <a href="https://merginmaps.com">the Input app</a> for coordinating the collection in 2021. Peter works for Lutra Consulting, the company behind Input and Mergin.</p>

<p>He showed Veronika how to create the maps in QGIS, a free and open source mapping software. Using map data from OpenStreetMap, they created a project showing the buildings to be visited, coloured by their associated volunteer group number.</p>

<center>
<img alt="qgis map © OpenStreetMap contributors" src="https://lutraconsulting.co.uk/img/case-studies/charita_litomysl/qgis_map.png" title="QGIS map © OpenStreetMap contributors" width="600" />
<p><em>Houses grouped by team in QGIS, image courtesy of Farní charita Litomyšl.</em></p>
</center>

<p>The styled map was uploaded to <a href="https://merginmaps.com">Mergin</a>, a collaborative mapping platform, making it readily available for viewing interactively on volunteer’s phones using the <a href="https://merginmaps.com">Input mobile app</a>. Both QGIS and Input integrate closely with Mergin which meant that maps could be adjusted in QGIS with the resulting changes being visible to volunteers shortly thereafter.</p>

<h2 id="outcomes">Outcomes</h2>
<p>Veronika reflects on the solution: “The solution met all our requirements and the maps we’ve prepared can easily be reused in upcoming events, saving us time. The fact that the new maps were made publicly accessible means volunteers can just download them using Input which makes distributing and updating them very easy.”</p>

<center>
<img alt="qgis map © OpenStreetMap contributors" src="https://lutraconsulting.co.uk/img/case-studies/charita_litomysl/inputapp_project.jpg" title="Input App map © OpenStreetMap contributors" width="300" />
<p><em>Volunteer routes and position information shown in Input, screenshot courtesy of Farní charita Litomyšl.</em></p>
</center>

<p>She adds: “All the districts we wanted to visit were distinguished from each other by colour and we were also pleased to be able to clearly mark the areas not to be visited like industrial areas by colouring them in grey.”</p>

<p>Unfortunately COVID meant that Veronika’s plans changed as she explains: “Using these new methods we were able to prepare for the 2021 Three Kings Collection in a short time. Unfortunately however, the COVID situation meant we could not go out on the streets to use the new maps as intended. We hope that in 2022 we’ll be able to more closely evaluate the positives and negatives of the field aspect of the project.”</p>

<p>She adds: “We already see it’s now much easier to allocate areas of the town to our volunteers in a clear and fair manner using QGIS. Producing printed maps for those who prefer them is also now easy and the maps look much more professional. Those who only wanted to use the <a href="https://merginmaps.com">Input app</a> could see the same information as on the paper maps, but had the advantage of being able to pinpoint their exact location and clearly see the house numbers of each building.”</p>

<center>
<img alt="new map © OpenStreetMap contributors" src="https://lutraconsulting.co.uk/img/case-studies/charita_litomysl/new_map.png" title="QGIS printed map © OpenStreetMap contributors" width="600" />
<p><em>Example printed map created for volunteers wanting also paper maps, image courtesy of Farní charita Litomyšl.</em></p>
</center>

<p>She concludes: “Overall we found the solution user-friendly, and appreciated being able to discuss the process with Lutra Consulting who helped us solve issues as required. About a third of our volunteers are interested in using <a href="https://merginmaps.com">Input</a>, which I consider positive.”</p>

<p>The Litomyšl Parish Charity are on <a href="https://www.facebook.com/farnicharitalitomysl">Facebook</a> and <a href="https://www.instagram.com/farni_charita_litomysl/">Instagram</a>.</p>

<h2 id="download-mergin-maps-today">Download Mergin Maps Today</h2>

<p><img alt="Screenshots of the Input App for Field Data Collection" src="https://lutraconsulting.co.uk/img/posts/input_app_for_field_data_collection.jpg" /></p>

<p><a href="https://play.google.com/store/apps/details?id=uk.co.lutraconsulting&amp;utm_source=lutra-atom&amp;utm_medium=lutra-blog&amp;utm_campaign=input"><img alt="Get it on Google Play" src="https://play.google.com/intl/en_us/badges/images/generic/en_badge_web_generic.png" width="180px" /></a><a href="https://apps.apple.com/us/app/input/id1478603559?ls=1&amp;utm_source=lutra-atom&amp;utm_medium=lutra-blog&amp;utm_campaign=input"><img alt="Get it on Apple store" src="https://www.lutraconsulting.co.uk/img/posts/App_Store.svg" style="padding-top: 0px;" width="144px" /></a></p>
