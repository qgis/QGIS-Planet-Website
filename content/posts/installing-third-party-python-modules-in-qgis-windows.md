---
source: "blog"
title: "Installing Third-party Python Modules in QGIS (Windows)"
date: "2016-03-02T12:00:00-0600"
link: "https://lutraconsulting.co.uk/blog/2016/03/02/installing-third-party-python-modules-in-qgis-windows/"
draft: "false"
showcase: "planet"
subscribers: ["lutragis"]
author: "Lutra Consulting"
tags: []
---

<p>We’ve recently been developing a client plugin for forest management which relies on the Python <em>SQLAlchemy</em> module. When I installed the latest version of my colleague’s work I got a Python traceback error about a missing Python module (SQLAlchemy).</p>

<p>This blog is more of a note to myself for future reference of how to install third-party modules in QGIS’ Python environment.</p>

<!-- more -->

<h2 id="the-problem">The Problem</h2>

<p>Installing third-party modules in Windows is usually quite straight-forward, either download an installer (which will find the Python environment from the registry) or use <em>easy_install</em> from the Python <em>setuptools</em>.</p>

<p>The problem is that QGIS ships with its own Python installation that these methods cannot easily add to.</p>

<p>(Don’t get me wrong - I like the fact that each QGIS instance has its own Python environment as it keeps each version very self-contained).</p>

<h2 id="the-method">The Method</h2>

<p>So here’s the method I successfully used to install <em>SQLAlchemy</em> (which I’ll use here to install the <em>lxml</em> module):</p>

<ul>
  <li>Click Start</li>
  <li>Type <em>QGIS</em></li>
  <li>
    <p>Wait for the QGIS version / instance you want to modify to appear:</p>

    <p><img src="https://www.lutraconsulting.co.uk/img/posts/start-menu-qgis.png" /></p>
  </li>
  <li>Right-click it, select <em>Run as administrator</em></li>
  <li>In QGIS, select <em>Python Console</em> from the <em>Plugins</em> menu</li>
  <li>Download <em>ez_setup.py</em> from <a href="https://pypi.python.org/pypi/setuptools#windows-simplified" rel="nofollow" target="_blank">here</a>.</li>
  <li>Run the following code on the python console in QGIS:</li>
</ul>

<div class="highlighter-rouge"><div class="highlight"><pre class="highlight"><code>from subprocess import call
# Replace the path below to the location of ez_setup.py that
# you just downloaded
call(['python', r'C:\Users\Pete\Downloads\ez_setup.py'])

# This will install *setuptools* which is a package manager
# The previous command should return 0 on success

# Replace lxml with the package you wish to install
call(['easy_install', 'lxml'])

# Again this will return 0 on success
</code></pre></div></div>

<ul>
  <li>Restart QGIS (normally, not using the <em>Run as administrator</em> option)</li>
</ul>

<p>The new module should now be available, we can test this (again on the Python console in QGIS):</p>

<div class="highlighter-rouge"><div class="highlight"><pre class="highlight"><code>import lxml
</code></pre></div></div>

<p>That’s it!</p>

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
