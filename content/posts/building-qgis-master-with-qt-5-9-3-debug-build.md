---
source: "blog"
title: "Building QGIS master with Qt 5.9.3 debug build"
date: "2017-12-01T17:58:54+0000"
link: "https://www.itopen.it/building-qgis-master-with-qt-5-9-3-debug-build/"
draft: "false"
showcase: "planet"
subscribers: ["itopen"]
author: "ItOpen"
tags: ["gis", "qgis", "[lang_it]programmazione[/lang_it][lang_en]programming[/lang_en]"]
---

Building QGIS from sources is not hard at all on a recent linux box, but what about if you wanted to be able to step-debug into Qt core or if you wanted to build QGIS agains the latest Qt release?

Here things become tricky.

This short post is about my experiments to build Qt and and other Qt-based dependencies for QGIS in order to get a complete debugger-friendly build of QGIS.

&nbsp;

Start with downloading the latest Qt installer from Qt official website: <a href="https://www.qt.io/download-qt-for-application-development">https://www.qt.io/download-qt-for-application-development</a> choose the Open Source version.

&nbsp;

<a class="thumbnail cboxElement" href="https://www.itopen.it/wp-content/uploads/2017/12/Screenshot-2017-12-1-Download-Qt-for-Application-Development.png"><img alt="" class="aligncenter size-full wp-image-1838" height="264" src="https://www.itopen.it/wp-content/uploads/2017/12/Screenshot-2017-12-1-Download-Qt-for-Application-Development.png" width="740" /></a>

Now install the Qt version you want to build, make sure you check the <strong>Sources</strong> and the components you might need.

<a class="thumbnail cboxElement" href="https://www.itopen.it/wp-content/uploads/2017/12/qtmaintenance.png"><img alt="" class="aligncenter size-large wp-image-1839" height="800" src="https://www.itopen.it/wp-content/uploads/2017/12/qtmaintenance-754x800.png" width="754" /></a>

Whe you are done with that, you&#8217;ll have your sources in a location like <code>/home/user/Qt/5.9.3/Src/</code>

To build the sources, you can change into that directory and issue the following command &#8211; I assume that you have already installed all the dependencies normally needed to build C++ Qt programs &#8211; I&#8217;m using clang here but feel free to choose gcc, we are going to install the new Qt build into <code>/opt/qt593</code>.
<pre class="wp-code-highlight prettyprint">./configure -prefix /opt/qt593 -debug -opensource -confirm-license -ccache -platform linux-clang
</pre>
When done, you can build it with
<pre class="wp-code-highlight prettyprint">make -j9
sudo make install
</pre>
&nbsp;

To build QGIS you also need three additional Qt packages

&nbsp;

<strong>QtWebKit</strong> from <a href="https://github.com/qt/qtwebkit">https://github.com/qt/qtwebkit</a> (you can just download the zip):

<a class="thumbnail cboxElement" href="https://www.itopen.it/wp-content/uploads/2017/12/qtwebkit.png"><img alt="" class="aligncenter size-large wp-image-1840" height="382" src="https://www.itopen.it/wp-content/uploads/2017/12/qtwebkit-800x382.png" width="800" /></a>

Extract it somewhere and build it with
<pre class="wp-code-highlight prettyprint">/opt/qt593/bin/qmake WebKit.pro
make -j9
sudo make install
</pre>
&nbsp;

Same with <strong>QScintila2</strong> from <a href="https://www.riverbankcomputing.com/software/qscintilla">https://www.riverbankcomputing.com/software/qscintilla</a>
<pre class="wp-code-highlight prettyprint">/opt/qt593/bin/qmake qscintilla.pro
make -j9
sudo make install
</pre>
&nbsp;

<strong>QWT</strong> is also needed and it can be downloaded from <a href="https://sourceforge.net/projects/qwt/files/qwt/6.1.3/">https://sourceforge.net/projects/qwt/files/qwt/6.1.3/</a> but it requires a small edit in
<code>qwtconfig.pri</code> before you can build it: set <code>QWT_INSTALL_PREFIX = /opt/qt593_libs/qwt-6.1.3</code> to install it in a different folder than the default one (that would possibly overwrite a system install of QWT).

The build it with:
<pre class="wp-code-highlight prettyprint">/opt/qt593/bin/qmake qwt.pro
make -j9
sudo make install
</pre>
&nbsp;

If everything went fine, you can now configure Qt Creator to use this new debug build of Qt:

start with creating a new kit (you can probably clone a working Qt5 kit if you have one).

What you need to change is the <strong>Qt version</strong> (the path to cmake) to point to your brand new Qt build,:

<a class="thumbnail cboxElement" href="https://www.itopen.it/wp-content/uploads/2017/12/qt-creator-config.png"><img alt="" class="aligncenter size-large wp-image-1841" height="477" src="https://www.itopen.it/wp-content/uploads/2017/12/qt-creator-config-800x477.png" width="800" /></a>Pick up a name and choose the Qt version, but before doing that you need to click on Manage&#8230; to create a new one:

<a class="thumbnail cboxElement" href="https://www.itopen.it/wp-content/uploads/2017/12/qt-creator-config-qt-version.png"><img alt="" class="aligncenter size-large wp-image-1842" height="477" src="https://www.itopen.it/wp-content/uploads/2017/12/qt-creator-config-qt-version-800x477.png" width="800" /></a>Now you should be able to build QGIS using your new Qt build, just make sure you disable the bindings in the CMake configuration: unfortunately you&#8217;d also need to build PyQt in order to create the bindings.

&nbsp;

Whe QGIS is built using this debug-enabled Qt, you will be able to step-debug into Qt core libraries!

Happy debugging!

&nbsp;<p>The post <a href="https://www.itopen.it/building-qgis-master-with-qt-5-9-3-debug-build/">Building QGIS master with Qt 5.9.3 debug build</a> first appeared on <a href="https://www.itopen.it">Open Web Solutions, GIS & Python Development</a>.</p>
