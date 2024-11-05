---
source: "blog"
title: "OpenCL acceleration now available in QGIS"
date: "2018-09-03T15:33:50+0000"
link: "https://www.itopen.it/opencl-acceleration-now-available-in-qgis/"
draft: "false"
showcase: "planet"
subscribers: ["itopen"]
author: "ItOpen"
tags: ["qgis"]
---

<h2>What is OpenCL?</h2>
<p>From <a href="https://en.wikipedia.org/wiki/OpenCL">https://en.wikipedia.org/wiki/OpenCL:</a></p>
<blockquote>
<p><b>OpenCL</b> (<b>Open Computing Language</b>) is a <a href="https://en.wikipedia.org/wiki/Software_framework" title="Software framework">framework</a> for writing programs that execute across <a href="https://en.wikipedia.org/wiki/Heterogeneous_computing" title="Heterogeneous computing">heterogeneous</a> platforms consisting of <a href="https://en.wikipedia.org/wiki/Central_processing_unit" title="Central processing unit">central processing units</a> (CPUs), <a href="https://en.wikipedia.org/wiki/Graphics_processing_unit" title="Graphics processing unit">graphics processing units</a> (GPUs), <a href="https://en.wikipedia.org/wiki/Digital_signal_processor" title="Digital signal processor">digital signal processors</a> (DSPs), <a href="https://en.wikipedia.org/wiki/Field-programmable_gate_array" title="Field-programmable gate array">field-programmable gate arrays</a> (FPGAs) and other processors or <a class="mw-redirect" href="https://en.wikipedia.org/wiki/Hardware_accelerator" title="Hardware accelerator">hardware accelerators</a>. OpenCL specifies <a href="https://en.wikipedia.org/wiki/Programming_language" title="Programming language">programming languages</a> (based on <a href="https://en.wikipedia.org/wiki/C99" title="C99">C99</a> and <a href="https://en.wikipedia.org/wiki/C%2B%2B11" title="C++11">C++11</a>) for programming these <a class="mw-redirect" href="https://en.wikipedia.org/wiki/Personal_computer_hardware" title="Personal computer hardware">devices</a> and <a href="https://en.wikipedia.org/wiki/Application_programming_interface" title="Application programming interface">application programming interfaces</a> (APIs) to control the platform and execute programs on the <a class="mw-redirect" href="https://en.wikipedia.org/wiki/OpenCL_compute_devices" title="OpenCL compute devices">compute devices</a>. OpenCL provides a standard interface for <a href="https://en.wikipedia.org/wiki/Parallel_computing" title="Parallel computing">parallel computing</a> using <a href="https://en.wikipedia.org/wiki/Task_parallelism" title="Task parallelism">task-</a> and <a href="https://en.wikipedia.org/wiki/Data_parallelism" title="Data parallelism">data-based parallelism</a>.</p>
</blockquote>
<p>Basically, you write a program and you execute it on a GPU (or, less frequently, on a CPU or on a DSP) taking advantage of the huge parallel programming capabilities of the modern graphic cards.</p>
<p>Depending on many different factors, the speed gain can vary to a great extent, but it is typically around one order of magnitude.</p>
<h2>How QGIS benefits from OpenCL?</h2>
<p>The work I&#8217;ve done consisted in integrating OpenCL support into QGIS and writing all the utilities to load, build and run OpenCL programs.</p>
<p>For now, I&#8217;ve ported the following QGIS core algorithms, all of them are availabe in processing:</p>
<ul>
	<li>slope</li>
	<li>aspect</li>
	<li>hillshade</li>
	<li>ruggedness</li>
</ul>
<p>Since the framework to support OpenCL is now in place, I think that more algorithms will be ported over the time.</p>
<p>During this development, even if was not in scope, the hillshade renderer has been optimized for speed and it can also benefit of OpenCL acceleration.</p>
<h2>How to activate OpenCL support</h2>
<p>OpenCL support is optional and opt-in, to use it, you need to activate it into the QGIS options dialog like shown in the screenshot below:</p>
<h2><a class="thumbnail cboxElement" href="https://www.itopen.it/wp-content/uploads/2018/09/qigs_opencl_options.png"><img alt="" class="aligncenter wp-image-1913 size-full" height="911" src="https://www.itopen.it/wp-content/uploads/2018/09/qigs_opencl_options.png" width="1972" /></a></h2>
<h2>How much performance gain can I expect?</h2>
<p>Well, YMMV, but here are some figures for a big DEM raster, low values mean faster execution.</p>
<p>GDAL means CPU execution using the GDAL processing algorithm.</p>
<a class="thumbnail cboxElement" href="https://www.itopen.it/wp-content/uploads/2018/09/opencl_speed_comparison.png"><img alt="" class="aligncenter size-full wp-image-1915" height="913" src="https://www.itopen.it/wp-content/uploads/2018/09/opencl_speed_comparison.png" width="1259" /></a>
<h2>How to install the OpenCL drivers?</h2>
<p>Of course it depends on your specific hardware and on your O.S., AMD, NVidia and Intel have different distributions channels, in general the driver for your graphic card will also provide the OpenCL driver, if your GPU is compatible, if OpenCL is not available on your current machine, try to Google for OpenCL, your O.S. and graphic card.</p>
<p>If there is no OpenCL support for your graphic card, you might try to install a driver for your GPU (Intel for example provides them) and you will probably have a decent acceleration even if not as much as you can get on a real graphic card.</p>
<p>This fact worths some more explanation: you might ask your self why running and algorithm directly on the CPU and running it on the same CPU but using OpenCL would make any difference and the reason why it is generally faster by using OpenCL is that OpenCL will run the algorithm in parallel on all cores of your CPU, while a normal application (and QGIS does not make an exception here) will use a single core.</p>
<h2>How to build QGIS with OpenCL support on Ubuntu</h2>
<p>Just a quick note: you&#8217;ll need to install the OpenCL headers and the ICD library:</p>
<code>
sudo apt-get install opencl-headers ocl-icd-opencl-dev 
</code>
<p>&nbsp;</p>
<h2>Credits</h2>
<p>I started this work as a proof of concept in my spare time (that it is not much, lately) and when I realized that it was promising, I submitted a QGIS grant proposal in order to allocate some working time to port more algorithms, write tests and polish the implementation.</p>
<p>This work would not be possible without all the generous sponsors and donors that feed the QGIS grant program year after year, many thanks to the QGIS community for this amazing support!</p>
<p>Jürgen Fischer was as usual very helpful and took care of the windows builds, now available in OSGeo4W packages.</p>
<p>Nyall Dawson helped with the code review and with testing the implementation on different cards and machines.</p>
<p>Matthias Kuhn reviewed the code.</p>
<p>Even Rouault pointed me to some highly efficient GDAL algorithm optimizations that I&#8217;ve been able to integrate in QGIS.</p>
<p>&nbsp;</p>
<p>&nbsp;</p><p>The post <a href="https://www.itopen.it/opencl-acceleration-now-available-in-qgis/">OpenCL acceleration now available in QGIS</a> first appeared on <a href="https://www.itopen.it">Open Web Solutions, GIS & Python Development</a>.</p>
