---
source: "blog"
title: "Introducing First Aid Plugin"
date: "2016-06-12T07:00:00-0500"
link: "https://lutraconsulting.co.uk/blog/2016/06/12/introducing-first-aid-plugin/"
draft: "false"
showcase: "planet"
subscribers: ["lutragis"]
author: "Lutra Consulting"
tags: []
---

<p>Software development often consists of a brief period of pure excitement
while writing the bulk of the source code, followed by a long and dreaded
period of finding bugs and fixing them. This scheme is no different when
writing plugins for QGIS.</p>

<!-- more -->

<p>Because we also write QGIS plugins ourselves,
we were thinking of how to ease the pain of getting rid of bugs – and
so we ended up creating the <a href="https://github.com/wonder-sk/qgis-first-aid-plugin">First Aid plugin</a>,
now available in the official QGIS plugin repository.</p>

<p>It is meant to be a Swiss army knife for QGIS plugin developers, a tool
that allows easy inspection of any Python code running within QGIS.
This is important because it can potentially save developers a lot
of their valuable time.</p>

<p>How many times did you end up adding “print” statements
into the code to find out what was going wrong in your code? With First Aid
plugin this should be no longer necessary.</p>

<h2 id="error-handler">Error Handler</h2>

<p>So let me explain what does it do. First of all, it comes with an improved
Python error handler. What this means is that whenever an error occurs in code
of a plugin, a window with all the details comes up.</p>

<p>Previously in QGIS you could only find out what was the exception’s type, message and stack trace.
First Aid plugin adds source code view, variables view and even an embedded
Python console where you can further inspect the state of the plugin at the
time of the error. Here is how it looks like in action:</p>

<p><img alt="Error Handler Screenshot" src="https://www.lutraconsulting.co.uk/img/posts/first-aid-error-handler.png" /></p>

<h2 id="debugger">Debugger</h2>

<p>Plugins however do not always come up with errors that can be caught and handled
by QGIS. More often plugins simply do not behave as one would expect them to.
Here is when people usually resort to using debuggers. There are IDEs like
PyDev or PyCharm - or even standalone tools like Winpdb - that allow developers
to do remote debugging. Basically they can connect to the Python environment within
QGIS and debug the code there. Personally, I have never been a big fan of this
approach and found remote debugging cumbersome to set up and use. And trying to debug
something on a client’s computer is even a greater challenge.</p>

<p>First Aid fortunately integrates a debugger into QGIS environment. This allows
developers to simply open the debugger window, load some Python files, set
breakpoints and everything is ready. Once QGIS reaches a line with a breakpoint,
the debugger window will be activated and it is possible to step through
the code and inspect the variables to understand what is going on in the code.</p>

<p><img alt="Debugger Screenshot" src="https://www.lutraconsulting.co.uk/img/posts/first-aid-debugger.png" /></p>

<p>The great thing is that once the execution of Python code is stopped, it is
possible to step into code, step over, step out or run to cursor, just like in any other debugger.
It is also possible to run custom scripts from within debugger window – they
will be also run in debug mode.</p>

<p>Debugging is active only while the debugger window is still open. While debugging,
there is some extra overhead when running any Python code (even for code that
you do not intend to debug), so it is better to close the debugger when not needed.</p>

<p>The plugin has already helped us various times to quickly identify problems
in plugins. Having said that,  please note that the plugin is still quite
young and may not work perfectly in all cases. We would be happy to hear
your feedback. Any <a href="https://github.com/wonder-sk/qgis-first-aid-plugin/issues">issues</a> or
<a href="https://github.com/wonder-sk/qgis-first-aid-plugin/pulls">pull requests</a> on GitHub
would be greatly appreciated!</p>

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
