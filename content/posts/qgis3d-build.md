---
source: "blog"
title: "Building QGIS3D on (K)ubuntu 16.04"
date: "2017-08-06T04:00:00-0500"
link: "https://lutraconsulting.co.uk/blog/2017/08/06/qgis3d-build/"
draft: "false"
showcase: "planet"
subscribers: ["lutragis"]
author: "Lutra Consulting"
tags: []
---

<p>QGIS support for 3D canvas is ready for testing. A possible hurdle in getting QGIS compiled with 3D support may be the fact that
we require Qt in version at least 5.8 and it is recommended to use Qt 5.9 which introduces further enhancements.
The current QGIS master branch (to be 3.0 release) is usually built against earlier versions of Qt. For example in Ubuntu 16.04, the default Qt package version is 5.5.</p>

<p>Continue reading for more detail on how to build QGIS with the latest Qt on Ubuntu …</p>

<!-- more -->

<h2 id="build-of-qgis">Build of QGIS</h2>

<p>The default Qt (from official repositories) on (K)Ubuntu 16.04 is too old and does not include the new Qt 3D framework.
We build QGIS with Qt 5.9.1. We are going to install QT to <code class="highlighter-rouge">/opt/Qt5.9.1/</code> and QGIS dependencies built with Qt5.9 to <code class="highlighter-rouge">/opt/qt59_libs</code>,
so make sure you have these folders created and ready to use.</p>

<h3 id="qt-591">Qt 5.9.1</h3>

<p>To add Qt 5.9.1, we can use a ppa:</p>

<div class="highlighter-rouge"><div class="highlight"><pre class="highlight"><code>sudo add-apt-repository ppa:beineri/opt-qt591-xenial
sudo apt-get update
sudo apt-get install qt59-meta-full
</code></pre></div></div>
<p>This will install Qt 5.9.1 side-by-side your current system Qt under /opt folder. You can later remove the package without affecting dependencies in your system.</p>

<p>alternatively you can download QT 5.9.1 installer from http://download.qt.io/official_releases/qt/5.9/5.9.1/qt-opensource-linux-x64-5.9.1.run and install it
to the same location.</p>

<h3 id="qwt-613">Qwt 6.1.3</h3>

<p>Another dependency is Qwt. You can download the package and build it with Qt 5.9.1.
To download the package, click here: https://sourceforge.net/projects/qwt/files/qwt/6.1.3/
Make a new folder and move the zip file there:</p>

<div class="highlighter-rouge"><div class="highlight"><pre class="highlight"><code>mkdir /tmp/qgis_deps
mv ~/Downloads/qwt-6.1.3.zip /tmp/qgis_deps
cd /tmp/qgis_deps
unzip qwt-6.1.3.zip
cd qwt-6.1.3
</code></pre></div></div>

<p>We need to define the prefix path. To do that, open <code class="highlighter-rouge">qwtconfig.pri</code>  in a text editor and change the prefix path:</p>

<div class="highlighter-rouge"><div class="highlight"><pre class="highlight"><code>nano qwtconfig.pri
</code></pre></div></div>

<p>change <code class="highlighter-rouge">QWT_INSTALL_PREFIX = /opt/qt59_libs/qwt-6.1.3</code> (more occurrences in the file!)</p>

<p>You can now compile the project:</p>

<div class="highlighter-rouge"><div class="highlight"><pre class="highlight"><code>/opt/qt59/bin/qmake qwt.pro
make -j4
make install
</code></pre></div></div>

<p>Check if the library has been installed correctly:</p>
<div class="highlighter-rouge"><div class="highlight"><pre class="highlight"><code>ls /opt/qt59_libs/qwt-6.1.3
</code></pre></div></div>

<h3 id="qscintilla2-2101">QScintilla2 2.10.1</h3>

<p>Use the compressed file from here: https://www.riverbankcomputing.com/software/qscintilla/download</p>

<p>Download and copy to <code class="highlighter-rouge">/tmp/qgis_deps</code></p>
<div class="highlighter-rouge"><div class="highlight"><pre class="highlight"><code>mv ~/Downloads/QScintilla_gpl-2.10.1.tar.gz /tmp/qgis_deps/
cd /tmp/qgis_deps
tar xvzf QScintilla_gpl-2.10.1.tar.gz
cd QScintilla_gpl-2.10.1/Qt4Qt5/
/opt/qt59/bin/qmake qscintilla.pro
make -j4
sudo make install
</code></pre></div></div>

<p>You should now have the compiled qscintilla in the following path:</p>

<div class="highlighter-rouge"><div class="highlight"><pre class="highlight"><code>ls /opt/qt59/lib/libqscintilla2_qt5.so
</code></pre></div></div>

<h3 id="qgis">QGIS</h3>

<p>First clone (or add as another remote) QGIS fork <code class="highlighter-rouge">wonder-sk/QGIS</code> and change branch to <code class="highlighter-rouge">3d</code></p>

<div class="highlighter-rouge"><div class="highlight"><pre class="highlight"><code>git clone git@github.com:wonder-sk/QGIS.git
cd QGIS
git checkout 3d
</code></pre></div></div>

<p>Now you can follow standard instructions on QGIS repo for building the applications:
https://raw.githubusercontent.com/qgis/QGIS/master/INSTALL</p>

<p>Once you have created the build directory (after step https://github.com/qgis/QGIS/blob/master/INSTALL#L266) you need to configure the cmake with the following options:</p>
<div class="highlighter-rouge"><div class="highlight"><pre class="highlight"><code>CMAKE_PREFIX_PATH=/opt/qt59/lib/cmake cmake \
   -GNinja \
   -DCMAKE_BUILD_TYPE=Debug \
   -DCMAKE_INSTALL_PREFIX=${HOME}/apps \
   -DWITH_3D=TRUE \
   -DWITH_QTWEBKIT=FALSE \
   -DENABLE_TESTS=FALSE \
   -DWITH_QWTPOLAR=FALSE \
   -DWITH_BINDINGS=FALSE \
   -DQWT_LIBRARY=/opt/qt59_libs/qwt-6.1.3/lib/libqwt.so \
   -DQWT_INCLUDE_DIR=/opt/qt59_libs/qwt-6.1.3/include \
   -DQSCINTILLA_LIBRARY=/opt/qt59/lib/libqscintilla2_qt5.so \
   -QSCINTILLA_INCLUDE_DIR=/opt/qt59/include \
   ..
</code></pre></div></div>

<p>The new flag is WITH_3D=TRUE.</p>

<p>In the output, make sure it has found built libraries (NOT Qt 5.7 line)</p>
<div class="highlighter-rouge"><div class="highlight"><pre class="highlight"><code>-- Found Qt version: 5.9
-- Found Qwt: /opt/qt59_libs/qwt-6.1.3/lib/libqwt.so (6.1.3)
-- Found QScintilla2: /opt/Qt5.9.1/5.9.1/gcc_64/lib/libqscintilla2_qt5.so (2.10.1)
</code></pre></div></div>

<p>Note that if you are using your own compiled version of GDAL, you need to define it using this flag: <code class="highlighter-rouge">-DGDAL_CONFIG=/PATH/TO/bin/gdal-config</code></p>

<p>If all dependencies are detected properly, you should be able to build QGIS using ninja:</p>

<div class="highlighter-rouge"><div class="highlight"><pre class="highlight"><code>ninja
</code></pre></div></div>

<p>To run QGIS from your build folder:</p>

<div class="highlighter-rouge"><div class="highlight"><pre class="highlight"><code>cd output/bin
./qgis
</code></pre></div></div>

<p>To verify that you are using the right version of QGIS, you can go to Help &gt; About and check which version of Qt your application has been built against.</p>

<h2 id="loading-the-data">Loading the data</h2>

<p>Now in QGIS, open 3D Canvas in menu: <code class="highlighter-rouge">View-&gt;New 3D Map View</code>. For 3D styling of vector layers, open Layer Styling dock widget and enable 3D Renderer in the newly added tab with 3D cube icon.</p>

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
