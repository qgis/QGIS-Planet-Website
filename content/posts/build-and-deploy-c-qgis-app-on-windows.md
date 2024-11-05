---
source: "blog"
title: "Build and deploy c++ QGIS custom application on windows"
date: "2014-02-27T09:32:10+0000"
link: "https://3nids.wordpress.com/2014/02/27/build-and-deploy-c-qgis-app-on-windows/"
draft: "false"
showcase: "planet"
subscribers: ["qgis_tips"]
author: "QGIS Tips"
tags: ["cpp", "c++", "compile", "deploy", "qgis", "windows"]
---

<p>After a lot of troubles, I managed to compile and deploy a QGIS c++ app on windows. This small guide will describe the steps I followed. This has been tested on win xp and windows 7, both in 32 bits.</p>
<h1>Development environment</h1>
<p>Your app must be built using MSVC 9.0 (2008) since QGIS in OSGeo&#8217;s package was built with it. Hence, MinGW cannot be used.</p>
<ol>
<li>Install Microsoft Visual Studio Express 2008.</li>
<li>Install QGIS and Qt libs using <a href="https://trac.osgeo.org/osgeo4w/" target="_blank" title="OSGeo4W">OSGeo4W</a> installer</li>
<li>Install <a href="http://qt-project.org/downloads#qt-creator" target="_blank" title="Qt Creator">Qt Creator</a></li>
<li>If you want a debugger,you should install CDB. This can be achieved by installing Windows SDK environment. In the installation process, only select <em>Debugging toos for windows</em>.</li>
</ol>
<p>I wasn&#8217;t able to use the compiler yet, so I am not 100% sure about 4.</p>
<p>Now, if you want to build using Qt Creator, it must be started in a proper environment. Adapt this batch to launch Qt Creator:</p>
<pre class="brush: bash; title: ; notranslate">
ECHO Setting up QGIS DEV ENV

set PYTHONPATH=

set OSGEO4W_ROOT=C:\OSGeo4W
call &quot;%OSGEO4W_ROOT%\bin\o4w_env.bat&quot;

@set QMAKESPEC=win32-msvc2008
@set PATH=%OSGEO4W_ROOT%\bin;%OSGEO4W_ROOT%\apps\qgis-dev\bin;%PATH%

@set INCLUDE=%INCLUDE%;%OSGEO4W_ROOT%\include;%OSGEO4W_ROOT%\apps\qgis-dev\include
@set LIB=%LIB%;%OSGEO4W_ROOT%\lib;%OSGEO4W_ROOT%\apps\qgis-dev\lib

path %OSGEO4W_ROOT%\bin;%SYSTEMROOT%\System32;%SYSTEMROOT%;%SYSTEMROOT%\System32\wbem;C:\Progra~1\Git\bin;C:\Qt\qtcreator-3.0.1\bin;%PATH%

set VS90COMNTOOLS=C:\Program Files\Microsoft Visual Studio 9.0\Common7\Tools\
call &quot;C:\Program Files\Microsoft Visual Studio 9.0\VC\vcvarsall.bat&quot; x86

start &quot;Qt Creator&quot; /B C:\Qt\qtcreator-3.0.1\bin\qtcreator.exe %*
</pre>
<p>Then, you need to configure a proper kit in Qt Creator.</p>
<ol>
<li>Go to <em>Options -&gt; Build &amp; Run -&gt; Compilers</em> and check that <em>Microsoft Visual C++ Compiler 9.0</em> is correctly detected.</li>
<li>Then in <em>Qt Versions</em> tab, add Qt from the OSGeO installation, normally <em>c:\OSGeo4W\bin\qmake.exe</em></li>
<li>In <i>Debuggers</i> tab, add cdb.exe found in <em>c:\Debugging tools for windows\ </em></li>
<li>Finally, check in <em>Kits</em> that it is properly configured.</li>
</ol>
<h1>Building the application</h1>
<p>This is what looks like an application project file.</p>
<pre class="brush: css; title: ; notranslate">
QT += core gui xml
greaterThan(QT_MAJOR_VERSION, 4): QT += widgets
TARGET = hfp
TEMPLATE = app
SOURCES += YOURSOURCES
HEADERS +=YOUR HEADERS
FORMS += YOUR FORMS
RESOURCES += images/images.qrc

win32:CONFIG(Release, Debug|Release) {
 LIBS += -L&quot;C:/OSGeo4W/lib/&quot; -lQtCore4
 LIBS += -L&quot;C:/OSGeo4W/lib/&quot; -lQtGui4
 LIBS += -L&quot;C:/OSGeo4W/lib/&quot; -lQtXml4
 LIBS += -L&quot;C:/OSGeo4W/apps/qgis-dev/lib/&quot; -lqgis_core
 LIBS += -L&quot;C:/OSGeo4W/apps/qgis-dev/lib/&quot; -lqgis_gui
}
else:win32:CONFIG(Debug, Debug|Release) {
 PRE_TARGETDEPS += C:/OSGeo4W/lib/QtCored4.lib
 PRE_TARGETDEPS += C:/OSGeo4W/lib/QtGuid4.lib
 PRE_TARGETDEPS += C:/OSGeo4W/lib/QtXmld4.lib
 LIBS += -L&quot;C:/OSGeo4W/lib/&quot; -lQtCored4
 LIBS += -L&quot;C:/OSGeo4W/lib/&quot; -lQtGuid4
 LIBS += -L&quot;C:/OSGeo4W/lib/&quot; -lQtXmld4
 LIBS += -L&quot;C:/OSGeo4W/apps/qgis-dev/lib/&quot; -lqgis_core
 LIBS += -L&quot;C:/OSGeo4W/apps/qgis-dev/lib/&quot; -lqgis_gui
}
win32:{
 INCLUDEPATH += C:/OSGeo4W/include
 DEPENDPATH += C:/OSGeo4W/include
 INCLUDEPATH += C:/OSGeo4W/apps/qgis-dev/include
 DEPENDPATH += C:/OSGeo4W/apps/qgis-dev/include
 DEFINES += GUI_EXPORT=__declspec(dllimport) CORE_EXPORT=__declspec(dllimport)
}
unix {
 LIBS += -L/usr/local/lib/ -lqgis_core -lqgis_gui
 LIBS += -L/usr/local/lib/qgis/plugins/ -lgdalprovider
 INCLUDEPATH += /usr/local/include/qgis
 DEFINES += GUI_EXPORT= CORE_EXPORT=
}
</pre>
<p>Remarks</p>
<ul>
<li><span style="font-family: Consolas, Monaco, monospace; font-size: 12px; line-height: 18px;">GUI_EXPORT </span>and<span style="font-family: Consolas, Monaco, monospace; font-size: 12px; line-height: 18px;"> CORE_EXPORT</span> must be set to <span style="font-family: Consolas, Monaco, monospace; font-size: 12px; line-height: 18px;">__declspec</span><span style="font-family: Consolas, Monaco, monospace; font-size: 12px; line-height: 18px;">(dllimport)</span>. I don&#8217;t know exactly what it means, but I found out reading this <a href="http://permalink.gmane.org/gmane.comp.gis.qgis.devel/7276" target="_blank" title="thread">thread</a>, with some hazardous tries. If you don&#8217;t set these, you won&#8217;t be able to call any variable defined as extern in QGIS (e.g. cursors).</li>
<li>Qt release libraries shall not be mixed up with debug config in your project. In other words, use release libs for release mode and debug libs for debug mode.</li>
</ul>
<p>With this, you should be able to compile your QGIS application in Qt Creator!</p>
<p>You can find some coding examples on <a href="https://github.com/qgis/QGIS-Code-Examples">github</a> which are a bit old but still useful to start.</p>
<p>Now, to get the whole potential of QGIS libs, you must initialize the <a href="http://qgis.org/api/classQgsApplication.html" target="_blank">QgsApplication</a> in your main window class:</p>
<pre class="brush: cpp; title: ; notranslate">
#if defined(Q_WS_WIN)
  QString pluginPath = &quot;c:\\OSGeo4W\\apps\\qgis-dev\\plugins&quot;;
  QString prefixPath = &quot;c:\\OSGeo4W\\apps\\qgis-dev\\&quot;;
#else
  QString pluginPath = &quot;/usr/local/lib/qgis/plugins/&quot;;
  QString prefixPath = &quot;/usr/local&quot;;
#endif

  QgsApplication::setPluginPath( pluginPath );
  QgsApplication::setPrefixPath( prefixPath, true);
  QgsApplication::initQgis();
</pre>
<h1>Deploying on windows</h1>
<p>Since QGIS is not to be installed on the target computer, the built app will not be able to find the path declared in previous code.<br />
There is probably a better approach, but here is a way to solve this:<br />
Change the path to</p>
<pre class="brush: cpp; title: ; notranslate">
  QString pluginPath = &quot;c:\\myapp\\qgis\plugins&quot;;
  QString prefixPath = &quot;c:\\myapp\\qgis&quot;;
</pre>
<p>This means you must deploy the app to this exact location: c:\myapp. In this directory, you need to create a qgis folder in which you will copy c:\OSGeo4W\apps\qgis-dev\resources and c:\OSGeo4W\apps\qgis-dev\plugins.</p>
<p>Besides, this you will need to copy some DLLs to be able to run the applications. You might want to use the <a href="http://www.dependencywalker.com/">dependency walker</a> to find which are needed.</p>
<p>The batch file hereafter creates a folder on the building machine that will contain all the needed files in my case (it might be different in your case).</p>
<pre class="brush: bash; collapse: true; light: false; title: ; toolbar: true; notranslate">
rmdir c:\myapp /Q /S
mkdir c:\myapp
mkdir c:\myapp\iconengines
mkdir c:\myapp\qgis
mkdir c:\myapp\qgis\resources
mkdir c:\myapp\qgis\plugins

copy PATHTOMYAPP\build-myapp-Desktop-Release\release\myapp.exe c:\myapp\
copy c:\OSGeo4W\bin\QtCore4.dll c:\myapp\
copy c:\OSGeo4W\bin\QtGui4.dll c:\myapp\
copy c:\OSGeo4W\bin\QtXml4.dll c:\myapp\
copy c:\OSGeo4W\bin\QtNetwork4.dll c:\myapp\
copy c:\OSGeo4W\bin\QtSvg4.dll c:\myapp\
copy c:\OSGeo4W\bin\QtWebKit4.dll c:\myapp\

copy c:\OSGeo4W\bin\zlib_osgeo.dll c:\myapp\
copy c:\OSGeo4W\bin\msvcr71.dll c:\myapp\
copy c:\OSGeo4W\bin\phonon4.dll c:\myapp\
copy c:\OSGeo4W\bin\proj.dll c:\myapp\
copy c:\OSGeo4W\bin\geos_c.dll c:\myapp\
copy c:\OSGeo4W\bin\gdal110.dll c:\myapp\
copy c:\OSGeo4W\bin\ogdi_32b1.dll c:\myapp\
copy c:\OSGeo4W\bin\libexpat.dll c:\myapp\
copy c:\OSGeo4W\bin\xerces-c_3_1.dll c:\myapp\
copy c:\OSGeo4W\bin\LIBPQ.dll c:\myapp\
copy c:\OSGeo4W\bin\SSLEAY32.dll c:\myapp\
copy c:\OSGeo4W\bin\LIBEAY32.dll c:\myapp\
copy c:\OSGeo4W\bin\krb5_32.dll c:\myapp\
copy c:\OSGeo4W\bin\comerr32.dll c:\myapp\
copy c:\OSGeo4W\bin\k5sprt32.dll c:\myapp\
copy c:\OSGeo4W\bin\gssapi32.dll c:\myapp\
copy c:\OSGeo4W\bin\hdf_fw.dll c:\myapp\
copy c:\OSGeo4W\bin\mfhdf_fw.dll c:\myapp\
copy c:\OSGeo4W\bin\jpeg_osgeo.dll c:\myapp\
copy c:\OSGeo4W\bin\jpeg12_osgeo.dll c:\myapp\
copy c:\OSGeo4W\bin\netcdf.dll c:\myapp\
copy c:\OSGeo4W\bin\geotiff.dll c:\myapp\
copy c:\OSGeo4W\bin\libtiff.dll c:\myapp\
copy c:\OSGeo4W\bin\sqlite3.dll c:\myapp\
copy c:\OSGeo4W\bin\spatialite4.dll c:\myapp\
copy c:\OSGeo4W\bin\freexl.dll c:\myapp\
copy c:\OSGeo4W\bin\iconv.dll c:\myapp\
copy c:\OSGeo4W\bin\libxml2.dll c:\myapp\
copy c:\OSGeo4W\bin\LIBMYSQL.dll c:\myapp\
copy c:\OSGeo4W\bin\hdf5.dll c:\myapp\
copy c:\OSGeo4W\bin\szip.dll c:\myapp\
copy c:\OSGeo4W\bin\libcurl.dll c:\myapp\
copy c:\OSGeo4W\bin\zlib1.dll c:\myapp\
copy c:\OSGeo4W\bin\openjp2.dll c:\myapp\
copy c:\OSGeo4W\bin\spatialindex1.dll c:\myapp\
copy c:\OSGeo4W\bin\qwt5.dll c:\myapp\

copy c:\OSGeo4W\apps\qt4\plugins\iconengines\qsvgicon4.dll c:\myapp\iconengines\

copy C:\Progra~1\Git\bin\libiconv-2.dll c:\myapp\
copy C:\Progra~1\Git\bin\libintl-8.dll c:\myapp\

copy c:\OSGeo4W\apps\qgis-dev\bin\qgis_Core.dll c:\myapp\
copy c:\OSGeo4W\apps\qgis-dev\bin\qgis_gui.dll c:\myapp\
copy c:\OSGeo4W\apps\qgis-dev\bin\msvcp90.dll c:\myapp\

copy c:\windows\system32\msvcp100.dll c:\myapp\
copy c:\windows\system32\msvcr100.dll c:\myapp\

copy C:\OSGeo4W\apps\qgis-dev\resources\* c:\myapp\qgis\resources
copy C:\OSGeo4W\apps\qgis-dev\plugins\* c:\myapp\qgis\plugins
</pre>
<p>To be able to run the app, on a fresh windows XP, I had to install:</p>
<ul>
<li><a href="http://www.microsoft.com/en-us/download/details.aspx?id=29">Microsoft Visual C++ 2008 Redistributable Package (x86)</a></li>
<li><a href="http://www.microsoft.com/en-us/download/confirmation.aspx?id=3387">Microsoft Visual C++ 2005 Redistributable Package (x86)</a></li>
<li>
<p style="display: inline !important;"><a href="http://www.microsoft.com/en-us/download/confirmation.aspx?id=26347">Microsoft Visual C++ 2005 Service Pack 1 Redistributable Package MFC Security Update</a></p>
</li>
</ul>
<p>And copy the whole folder c:\myapp from the building machine to the target machine.</p>
<p>It seems that from Vista, the 2005 redistributable package is included. So, no need to install it.</p>
<p>And voilà!</p>
