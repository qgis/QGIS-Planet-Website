---
source: "blog"
title: "Use your android phone’s GPS in QGIS"
date: "2018-03-16T10:17:30+0000"
link: "https://www.itopen.it/use-your-android-phones-gps-in-qgis/"
draft: "false"
showcase: "planet"
subscribers: ["itopen"]
author: "ItOpen"
tags: ["qgis"]
---

Do you want to share your GPS data from your phone to QGIS?

Here is how:

&nbsp;

QGIS comes with a core plugin named <strong>GPS Tools</strong> that can be enabled in the Plugin installer dialog:

&nbsp;

<a class="thumbnail cboxElement" href="https://www.itopen.it/wp-content/uploads/2018/03/gps-connection-install.png"><img alt="" class="aligncenter size-large wp-image-1886" height="254" src="https://www.itopen.it/wp-content/uploads/2018/03/gps-connection-install-800x254.png" width="800" /></a>

There are several ways to forward data from your phone and most of them are very well described in the QGIS manual page: <a href="https://docs.qgis.org/testing/en/docs/user_manual/working_with_gps/plugins_gps.html">https://docs.qgis.org/testing/en/docs/user_manual/working_with_gps/plugins_gps.html</a>

What I&#8217;m going to describe here is mostly useful when your phone and your host machine running QGIS are on the same network (for example they are connected to the same WiFi access point) and it is based on the simple application <a href="https://play.google.com/store/apps/details?id=net.cajax.gps2net&amp;hl=it">GPS 2 NET</a>

&nbsp;

Once the application is installed and started on your phone, you need to know the IP address of the phone, on a linux box you can simply run a port scanner and it will find all devices connected to the port 6000 (the default port used by GPS 2 NET):

&nbsp;
<pre class="wp-code-highlight prettyprint"># Assuming your subnet is 192.168.9

nmap -p 6000 192.168.1.*

Nmap scan report for android-8899989888d02271.homenet.telecomitalia.it (192.168.99.50)
Host is up (0.0093s latency).
PORT STATE SERVICE
6000/tcp open X11

</pre>
&nbsp;

Now, in QGIS you can open the plugin dialog through <strong>Vector -&gt; GPS -&gt; GPS Tools</strong> and enter the IP address and port of your GPS device:

&nbsp;

<a class="thumbnail cboxElement" href="https://www.itopen.it/wp-content/uploads/2018/03/gps-connection-settings.png"><img alt="" class="aligncenter size-large wp-image-1890" height="800" src="https://www.itopen.it/wp-content/uploads/2018/03/gps-connection-settings-471x800.png" width="471" /></a>

Click on <strong>Connect</strong> button on the top right corner (mouse over the gray square for GPS status information)

&nbsp;

Start digitizing!

<a class="thumbnail cboxElement" href="https://www.itopen.it/wp-content/uploads/2018/03/gps-connection-fix.png"><img alt="" class="aligncenter size-large wp-image-1893" height="336" src="https://www.itopen.it/wp-content/uploads/2018/03/gps-connection-fix-800x336.png" width="800" /></a><p>The post <a href="https://www.itopen.it/use-your-android-phones-gps-in-qgis/">Use your android phone’s GPS in QGIS</a> first appeared on <a href="https://www.itopen.it">Open Web Solutions, GIS & Python Development</a>.</p>
