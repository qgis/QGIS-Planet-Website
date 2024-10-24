---
source: "blog"
title: "QGIS development on macOS"
date: "2020-04-22T02:00:00-0500"
link: "https://lutraconsulting.co.uk/blog/2020/04/22/qgis-macos-development/"
draft: "false"
showcase: "planet"
subscribers: ["lutragis"]
author: "Lutra Consulting"
tags: []
---

<p>We introduced a new packaging and build environment for QGIS and its dependencies for macOS. This will bring a completely new experience for QGIS macOS developers and subsequently, the users.</p>

<!-- more -->

<p>Overview of the changes</p>

<ul>
  <li><a href="https://www.lutraconsulting.co.uk/blog/categories/qgis/atom.xml#what-is-new">What is new?</a></li>
  <li><a href="https://www.lutraconsulting.co.uk/blog/categories/qgis/atom.xml#qgis-development-on-macos">QGIS development on macOS</a></li>
  <li><a href="https://www.lutraconsulting.co.uk/blog/categories/qgis/atom.xml#development-of-the-qgis-deps-package">Development of the QGIS-Deps package</a></li>
  <li><a href="https://www.lutraconsulting.co.uk/blog/categories/qgis/atom.xml#next-steps">Next steps</a></li>
</ul>

<h2 id="what-is-new">What is new</h2>
<p>In <a href="https://www.lutraconsulting.co.uk/blog/2019/02/18/qgis-for-macos-update/">2019</a>, we upgraded the <a href="http://blog.qgis.org/2019/07/29/introducing-new-qgis-macos-packages/">QGIS macOS packaging</a> to address several issues at the time. This was made possible with the help of the <a href="https://www.lutraconsulting.co.uk/blog/categories/qgis/qgis.org">QGIS project</a> and <a href="https://www.lutraconsulting.co.uk/blog/2019/02/18/qgis-for-macos-update/">donors who supported our work</a>.</p>

<p>The upgraded system had a more transparent and automated packaging approach. But it came with its own limitation. We have been using <a href="https://github.com/OSGeo/homebrew-osgeo4mac">Homebrew</a> to fetch the QGIS dependencies and to compile only QGIS for the <a href="https://qgis.org/downloads/macos/">LTR, PR and nightly releases</a>. The main problems with this approach are:</p>

<ul>
  <li>
    <p>Homebrew can only support one version of a package. This will limit QGIS to be built against multiple versions of, for example <a href="https://gdal.org/">GDAL</a> or <a href="https://proj.org/">Proj</a> libraries. In one hand, we want QGIS nightlies to use more bleeding edge versions of the dependencies (e.g. for plugin or core developers) . On the other hand, using a more stable and tested versions of the dependencies for PR or LTR are not recommended (e.g. users and organisations). OSGeo4W offers the same approach for different versions of QGIS in Windows. Unfortunately, <a href="https://github.com/OSGeo/homebrew-osgeo4mac">Homebrew</a> does not offer such an option.</p>
  </li>
  <li>
    <p>Continuous integration has been a major part of QGIS infrastructure to ensure <a href="https://github.com/qgis/QGIS/pulls">pull requests</a> by developers do not break workflows in certain Operating Systems. Microsoft Windows and Linux have been well supported in the CI. But with the macOS packages, it was left to user to test and report back any bugs after Pull Requests were merged to QGIS source code.</p>
  </li>
</ul>

<p><a href="https://github.com/qgis/QGIS/pull/35407">With the recent work</a>, we have addressed both of the above issues. QGIS and almost all of its dependencies are built from sources. It will be also possible to easily integrate the code with the current CI for macOS with GitHub Workflows. This will bring more stability and control over the way we build and package QGIS for our users, whilst helping developers to identify issues with their pull requests for macOS platform, before merging them to the QGIS source code.</p>

<h2 id="qgis-development-on-macos">QGIS development on macOS</h2>

<p>If you want to check the latest QGIS master on macOS or tweak the code to see some new exciting features, now it should be
easier with the following steps, to compile QGIS from source code an a clean machine:</p>

<h3 id="1-install-xcode">1. Install XCode</h3>

<ul>
  <li>Upgrade to latest MacOS version</li>
  <li>Install latest XCode from the official AppStore</li>
  <li>Open XCode and accept license</li>
  <li>Install command line tools from XCode, AppStore or from command line by <code class="highlighter-rouge">sudo xcode-select --install</code></li>
</ul>

<h3 id="2-install-qt-and-qgis-deps">2. Install Qt and QGIS-Deps</h3>

<ul>
  <li>Download the latest <a href="https://qgis.org/downloads/macos/deps">install qgis-deps script</a> and check the version of Qt required</li>
  <li>Install the required Qt version referenced from the official Qt download area. Or alternatively download <a href="https://qgis.org/downloads/macos/deps">qt-version.tar.gz from deps area</a></li>
  <li>Download latest <a href="https://qgis.org/downloads/macos/deps">qgis-deps package</a> too.</li>
  <li>Run <code class="highlighter-rouge">install_qgis_deps.bash</code> script to install Qt in <code class="highlighter-rouge">/opt/Qt/5.14.1/clang_64</code> and QGIS-Deps to <code class="highlighter-rouge">/opt/QGIS/qgis-deps-0.3.0</code> folder. You may need to use root privileges or create those folders under <code class="highlighter-rouge">/opt/</code> and assign the right permission beforehand.</li>
</ul>

<h3 id="3-install-other-tools">3. Install other tools</h3>

<ul>
  <li>Install Homebrew</li>
  <li>Install minimal set of packages required for macOS build tools listed in <a href="https://github.com/qgis/QGIS-Mac-Packager/blob/master/scripts/install_brew_dev_packages.bash">this list</a></li>
</ul>

<p>You may use MacPorts, Conda or other packaging system, but by the end you need <code class="highlighter-rouge">cmake</code>, <code class="highlighter-rouge">git</code>, <code class="highlighter-rouge">astyle</code> and other useful tools to be on the system PATH</p>

<h3 id="4-download-and-compile-qgis">4. Download and compile QGIS</h3>

<ul>
  <li>Open the terminal (Note that the qgis-deps package is not yet signed, so you may need to add Terminal to System Preferences -&gt; Security &amp; Privacy -&gt; Privacy -&gt; Developer Tools)</li>
  <li>In your work folder (e.g. <code class="highlighter-rouge">~/Projects/</code>), clone QGIS with <code class="highlighter-rouge">git clone git@github.com:qgis/QGIS.git</code></li>
  <li>Create a build folder <code class="highlighter-rouge">mkdir -p ~/Projects/build-QGIS</code></li>
  <li>Go to the created empty directory <code class="highlighter-rouge">cd ~/Projects/build-QGIS</code></li>
  <li>Run CMake to generate the build system (use your download qgis-deps and qt package)
    <div class="language-bash highlighter-rouge"><div class="highlight"><pre class="highlight"><code><span class="nv">QGIS_DEPS_VERSION</span><span class="o">=</span>0.3.0<span class="p">;</span><span class="se">\</span>
<span class="nv">QT_VERSION</span><span class="o">=</span>5.14.1<span class="p">;</span><span class="se">\</span>
<span class="nv">PATH</span><span class="o">=</span>/opt/QGIS/qgis-deps-<span class="k">${</span><span class="nv">QGIS_DEPS_VERSION</span><span class="k">}</span>/stage/bin:<span class="nv">$PATH</span><span class="p">;</span><span class="se">\</span>
cmake <span class="nt">-DQGIS_MAC_DEPS_DIR</span><span class="o">=</span>/opt/QGIS/qgis-deps-<span class="k">${</span><span class="nv">QGIS_DEPS_VERSION</span><span class="k">}</span>/stage <span class="se">\</span>
    <span class="nt">-DCMAKE_PREFIX_PATH</span><span class="o">=</span>/opt/Qt/<span class="k">${</span><span class="nv">QT_VERSION</span><span class="k">}</span>/clang_64 <span class="se">\</span>
    ../QGIS
</code></pre></div>    </div>
  </li>
</ul>

<p>Note that all libraries are picked from qgis-deps and not from system <code class="highlighter-rouge">/usr/lib</code> or Homebrew’s <code class="highlighter-rouge">/usr/local/</code>
or system Frameworks <code class="highlighter-rouge">/Library/Frameworks/</code>. Especially check Proj, GDAL, sqlite3 and Python paths.
You should see output similar to this:</p>

<div class="highlighter-rouge"><div class="highlight"><pre class="highlight"><code>-- QGIS version: 3.13.0 Master (31300)
-- Found OpenCL: /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX10.15.sdk/System/Library/Frameworks/OpenCL.framework (found version "1.2")
-- Found OpenCL C++ headers: /Users/peter/Projects/mesh/QGIS/external/opencl-clhpp/include
-- Found GRASS 7: /opt/QGIS/qgis-deps-0.3.0/stage/grass78 (7.8.2, off_t size = 8)
-- Looking for openpty
-- Looking for openpty - found
-- Found Proj: /opt/QGIS/qgis-deps-0.3.0/stage/lib/libproj.dylib version 6 (6.3.1)
-- Found GEOS: /opt/QGIS/qgis-deps-0.3.0/stage/lib/libgeos_c.dylib (3.8.1)
-- Found GDAL: /opt/QGIS/qgis-deps-0.3.0/stage/lib/libgdal.dylib (3.0.4)
-- Found Expat: /opt/QGIS/qgis-deps-0.3.0/stage/lib/libexpat.dylib
-- Found Spatialindex: /opt/QGIS/qgis-deps-0.3.0/stage/lib/libspatialindex.dylib
-- Found Qwt: /opt/QGIS/qgis-deps-0.3.0/stage/lib/qwt.framework (6.1.4)
-- Found LibZip: /opt/QGIS/qgis-deps-0.3.0/stage/lib/libzip.dylib
-- Found libzip: /opt/QGIS/qgis-deps-0.3.0/stage/lib/libzip.dylib
-- Found Sqlite3: /opt/QGIS/qgis-deps-0.3.0/stage/lib/libsqlite3.dylib
-- Found Protobuf: /opt/QGIS/qgis-deps-0.3.0/stage/lib/libprotobuf.dylib (found version "3.11.4")
-- Found Protobuf: /opt/QGIS/qgis-deps-0.3.0/stage/lib/libprotobuf.dylib
-- Found ZLIB: /opt/QGIS/qgis-deps-0.3.0/stage/lib/libz.dylib (found version "1.2.11")
-- Found zlib: /opt/QGIS/qgis-deps-0.3.0/stage/lib/libz.dylib
-- Found PostgreSQL: /opt/QGIS/qgis-deps-0.3.0/stage/lib/libpq.dylib
-- Found SpatiaLite: /opt/QGIS/qgis-deps-0.3.0/stage/lib/libspatialite.dylib
-- Qt WebKit support enabled
-- Found Qt version: 5.14.1
-- Found QScintilla2: /opt/QGIS/qgis-deps-0.3.0/stage/lib/libqscintilla2_qt5.dylib (2.11.4)
-- Found QtKeychain: /opt/QGIS/qgis-deps-0.3.0/stage/lib/libqt5keychain.dylib
-- Found QCA: /opt/QGIS/qgis-deps-0.3.0/stage/lib/qca-qt5.framework (2.3.0)
-- Found QCA OpenSSL plugin
-- Found Libtasn1: /opt/QGIS/qgis-deps-0.3.0/stage/include
-- Pedantic compiler settings enabled
-- Found PythonInterp: /opt/QGIS/qgis-deps-0.3.0/stage/bin/python3 (found suitable version "3.7.7", minimum required is "3")
-- Found Python executable: /opt/QGIS/qgis-deps-0.3.0/stage/bin/python3
-- Found Python version: 3.7.7
-- Found Python library: /opt/QGIS/qgis-deps-0.3.0/stage/lib/libpython3.7m.dylib
-- Found Python site-packages: /opt/QGIS/qgis-deps-0.3.0/stage/lib/python3.7/site-packages
-- Found PyQt5 version: 5.14.1
-- Found SIP version: 4.19.21
-- Found QScintilla2 PyQt module: 2.11.4
-- txt2tags not found - disabled
-- Performing Test COMPILER_HAS_HIDDEN_VISIBILITY
-- Performing Test COMPILER_HAS_HIDDEN_VISIBILITY - Success
-- Performing Test COMPILER_HAS_HIDDEN_INLINE_VISIBILITY
-- Performing Test COMPILER_HAS_HIDDEN_INLINE_VISIBILITY - Success
-- Performing Test COMPILER_HAS_DEPRECATED_ATTR
-- Performing Test COMPILER_HAS_DEPRECATED_ATTR - Success
-- Found exiv2: /opt/QGIS/qgis-deps-0.3.0/stage/lib/libexiv2.dylib
-- HDF5: Using hdf5 compiler wrapper to determine C configuration
-- Found HDF5: /opt/QGIS/qgis-deps-0.3.0/stage/lib/libhdf5.dylib;/opt/QGIS/qgis-deps-0.3.0/stage/lib/libz.dylib;/usr/lib/libdl.dylib;/usr/lib/libm.dylib (found version "1.10.0")
-- Found PkgConfig: /usr/local/bin/pkg-config (found version "0.29.2")
-- Found NetCDF: /opt/QGIS/qgis-deps-0.3.0/stage/lib/libnetcdf.dylib
-- Found LibXml2: /opt/QGIS/qgis-deps-0.3.0/stage/lib/libxml2.dylib (found version "2.9.10")
-- Looking for updwtmpx
-- Looking for updwtmpx - not found
-- Found GSL: -L/opt/QGIS/qgis-deps-0.3.0/stage/lib -lgsl -lgslcblas
-- Using PROJ 6 srs database.
-- Ctest Binary Directory set to: /Users/peter/Projects/mesh/build-QGIS/output/bin
-- Configuring done
-- Generating done
-- Build files have been written to: /Users/peter/Projects/mesh/build-QGIS
</code></pre></div></div>

<ul>
  <li>Compile QGIS <code class="highlighter-rouge">make -j4</code> and wait for <code class="highlighter-rouge">[100%]</code> mark :)</li>
  <li>Now you can run QGIS with command <code class="highlighter-rouge">./output/bin/QGIS.app/Contents/MacOS/QGIS</code> or <code class="highlighter-rouge">open ./output/bin/QGIS.app</code></li>
</ul>

<p><strong>Notes:</strong></p>

<ul>
  <li>If you use QT Creator, you can open already generated project to modify files from it.</li>
  <li>The critical CMake variable is <code class="highlighter-rouge">QGIS_MAC_DEPS_DIR</code> and you must ensure it contains valid qgis-deps installation</li>
  <li>You can add more variables to CMake command to tweak the build settings, e.g. enable 3D with ‘-DWITH_3D’, etc.</li>
  <li>Consult QGIS’s [INSTALL]https://github.com/qgis/QGIS/blob/master/INSTALL) for latest developement tips</li>
</ul>

<h2 id="development-of-the-qgis-deps-package">Development of the QGIS-Deps package</h2>

<p>If you want to help with development of the qgis packages on macOS, please feel free to contact <a href="https://www.lutraconsulting.co.uk/blog/categories/qgis/peter.petrik@lutraconsulting.co.uk">peter.petrik@lutraconsulting.co.uk</a>.
The development is taking place on public <a href="https://github.com/qgis/QGIS-Mac-Packager/tree/master/qgis_deps">QGIS-Mac-Packager repository</a>.</p>

<h2 id="next-steps">Next steps</h2>

<p>Currently, we are carrying out the following tasks:</p>

<ul>
  <li>
    <p>to move all-in-one QGIS bundle for LTR/PR/nighlies to use this new package of dependencies. Check out <a href="https://twitter.com/lutraconsulting">Twitter</a> for for any news on the packages. We are aiming to have the new packaging in place for the QGIS 3.14 release, which will bring GDAL 3 and Proj 6 to macOS users</p>
  </li>
  <li>
    <p>to sign the qgis-deps packages, so that developers do not need to tweak Privacy settings to use it for compiling QGIS and its dependencies.</p>
  </li>
</ul>

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
