---
source: "blog"
title: "Using QGIS from Conda"
date: "2019-05-29T22:46:23+0000"
link: "https://gisunchained.wordpress.com/2019/05/29/using-qgis-from-conda/"
draft: "false"
showcase: "planet"
subscribers: ["alexandre_netos_blog"]
author: "Alexandre Neto's blog"
tags: ["sem categoria", "conda", "qgis"]
---

<p>QGIS recipes have been available on Conda for a while, but now, that they work for the three main operating systems, getting QGIS from Conda is s starting to become a reliable alternative to other QGIS distributions. Anyway, let&#8217;s rewind a bit&#8230;</p>
<p>What is Conda?</p>
<blockquote><p>Conda is an open source package management system and environment management system that runs on Windows, macOS and Linux. Conda quickly installs, runs and updates packages and their dependencies. Conda easily creates, saves, loads and switches between environments on your local computer. It was created for Python programs, but it can package and distribute software for any language.</p></blockquote>
<p>Why is that of any relevance?</p>
<p>Conda provides a similar way to build, package and install QGIS (or any other software) in Linux, Windows, and Mac.</p>
<p>As a user, it&#8217;s the installation part that I enjoy the most. I am a Linux user, and one of the significant limitations is not having an easy way to install more than one version of QGIS on my machine (for example the latest stable version and the Long Term Release). I was able to work around that limitation by compiling QGIS myself, but with Conda, I can install as many versions as I want in a very convenient way.</p>
<p>The following paragraphs explain how to install QGIS using Conda. The instructions and Conda commands should be quite similar for all the operating systems.</p>
<h2>Anaconda or miniconda?</h2>
<p>First thing you need to do is to install the Conda packaging system. Two distributions install Conda: Anaconda and Miniconda.</p>
<p><strong>TL;DR</strong> Anaconda is big (3Gb?) and installs the packaging system and a lot of useful tools, python packages, libraries, etc&#8230; . Miniconda is much smaller and installs just the packaging system, which is the bare minimum that you need to work with Conda and will allow you to selectively install the tools and packages you need. I prefer the later.</p>
<p>For more information, check this stack exchange answer on <a href="https://stackoverflow.com/a/45421527/1918685">anaconda vs miniconda.</a></p>
<p>Download <a href="https://www.anaconda.com/distribution/">anaconda</a> or <a class="" href="https://docs.conda.io/en/latest/miniconda.html">miniconda</a> installers for your system and follow the instructions to install it.</p>
<p>Windows installer is an executable, you should run it as administrator. The OSX and Linux installers are bash scripts, which means that, once downloaded, you need to run something like this to install:</p>
<pre>bash Miniconda3-latest-Linux-x86_64.sh</pre>
<h2>Installing QGIS</h2>
<p>Notice that the Conda tools are used in a command line terminal. Besides, on Windows, you need to use the command prompt that is installed with miniconda.</p>
<h3>Using environments</h3>
<p>Conda works with environments, which are similar to <a href="https://virtualenv.pypa.io/en/latest/">Python virtual environments</a> but not limited only to python. Basically, it allows isolating different installations or setups without interfering with the rest of the system. I recommend that you always use environments. If, like me, you want to have more that one version of QGIS installed, then the use of environments is mandatory.</p>
<p>Creating an environment is as easy as entering the following command on the terminal:</p>
<pre>conda create --name &lt;name_of_the_environment&gt;</pre>
<p>For example,</p>
<pre>conda create --name qgis_stable</pre>
<p>You can choose the version of python to use in your environment by adding the option <code>python=&lt;version&gt;</code>. Currently versions of QGIS run on python 3.6, 3.7, 3.8 and 3.9.</p>
<p>conda create &#8211;name qgis_stable python=3.7</p>
<p>To use an environment, you need to activate it.</p>
<pre>conda activate qgis_stable</pre>
<p>Your terminal prompt will show you the active environment.</p>
<pre>(qgis_stable) aneto@oryx:~/miniconda3$</pre>
<p>To deactivate the current environment, you run</p>
<pre>conda deactivate</pre>
<h3>Installing packages</h3>
<p>Installing packages using Conda is as simples as:</p>
<pre>conda install &lt;package_name&gt;</pre>
<p>Because conda packages can be stored in different channels, and because the default channels (from the anaconda service) do not contain QGIS, we need to specify the channel we want to get the package from. <a href="https://conda-forge.org/">conda-forge</a> is a community-driven repository of conda recipes and includes updated QGIS packages.</p>
<pre>conda install qgis --channel conda-forge</pre>
<p>Conda will download the latest available version of QGIS and all its dependencies installing it on the active environment.</p>
<p>Note: Because conda always try to install the latest version, if you want to use the QGIS LTR version, you must specify the QGIS version.</p>
<p><code>conda install qgis=3.10.12 --channel conda-forge</code></p>
<h3>Uninstalling packages</h3>
<p>Uninstalling QGIS is also easy. The quickest option is to delete the entire environment where QGIS was installed. Make sure you deactivate it first.</p>
<p><code>conda deactivate<br />
conda env remove --name qgis_stable</code></p>
<p>Another option is to remove QGIS package manually. This is useful if you have other packages installed that you want to keep.</p>
<pre>conda activate qgis_stable
conda remove qgis -c conda-forge</pre>
<p>This only removes the QGIS package and will leave all other packages that were installed with it. Note that you need to specify the conda-forge channel. Otherwise, Conda will try to update some packages from the default channels during the removal process, and things may get messy.</p>
<h2><strong>Running QGIS</strong></h2>
<p>To run QGIS, in the terminal, activate the environment (if not activated already) and run the qgis command</p>
<pre>conda activate qgis_stable
qgis

</pre>
<h2>Updating QGIS</h2>
<p>To update QGIS to the most recent version, you need to run the following command with the respective environment active</p>
<pre>conda update qgis -c conda-forge</pre>
<p>To update a patch release for the QGIS LTR version you run the install command again with the new version:</p>
<pre>conda install qgis=3.10.13 -c conda-forge</pre>
<h2>Some notes and caveats</h2>
<p>Please be aware that QGIS packages on Conda do not provide the same level of user experience as the official Linux, Windows, and Mac installer from the QGIS.org distribution. For example, there are no desktop icons or file association, it does not include GRASS and SAGA, etc &#8230;</p>
<p>On the other hand, QGIS installations on Conda it will share user configurations, installed plugins, with any other QGIS installations on your system.</p>
