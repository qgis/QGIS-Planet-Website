---
source: "blog"
title: "How to QGIS 4.2 on Linux Mint (Sept ’26)"
date: "2026-09-18T18:14:46+0000"
link: "https://anitagraser.com/2026/09/18/how-to-qgis-4-2-on-linux-mint-sept-26/"
draft: "false"
showcase: "planet"
subscribers: ["anita_graser"]
author: "Anita Graser"
tags: ["gis", "qgis"]
languages: ["en_gb"]
available_languages: ["en_gb"]
---

<p class="wp-block-paragraph">For a while now, my preferred way of installing QGIS has been from conda-forge. However, while we’re waiting for QGIS 4 to become available on conda-forge, there are alternatives: </p>
<p class="wp-block-paragraph"><strong>Option 1: Flatpak</strong></p>
<p class="wp-block-paragraph">In the Software Manager, you can find <a href="https://flathub.org/en/apps/org.qgis.qgis">QGIS from Flathub</a> in two different versions: stable and lts. And stable should give you 4.2 (even if the Software Manager preview shows an older one):</p>
<figure class="wp-block-image size-large"><a href="https://anitagraser.com/wp-content/uploads/2026/09/image-8.png"><img alt="" class="wp-image-9831" height="668" src="/img/subscribers/anita_graser/how-to-qgis-4-2-on-linux-mint-sept-26/image-8.webp" width="734"/></a></figure>
<p class="wp-block-paragraph"><strong>Option 2: Meet the <a href="https://github.com/qgis/qgis-docker">official QGIS Docker Images</a></strong></p>
<p class="wp-block-paragraph">First off, you’ll need Docker. If you haven’t installed it yet, it’s directly available from the Linux Mint Software Manager:</p>
<figure class="wp-block-image size-large"><a href="https://anitagraser.com/wp-content/uploads/2026/09/image-9.png"><img alt="" class="wp-image-9833" height="668" src="/img/subscribers/anita_graser/how-to-qgis-4-2-on-linux-mint-sept-26/image-9.webp" width="734"/></a></figure>
<p class="wp-block-paragraph">From there on, we just switch to the Terminal for the rest. </p>
<figure class="wp-block-image size-large"><a href="https://anitagraser.com/wp-content/uploads/2026/09/image-1.png"><img alt="" class="wp-image-9805" height="357" src="/img/subscribers/anita_graser/how-to-qgis-4-2-on-linux-mint-sept-26/image-1.webp" width="662"/></a></figure>
<p class="wp-block-paragraph">If you get “permission denied while trying to connect to the docker API” when running any of the following commands, you may have to add your user account to the <code>docker</code> group:</p>
<div class="wp-block-code">
<div class="cm-editor">
<div class="cm-scroller">
<pre>
<code class="language-shell"><div class="cm-line"><span class="tok-variableName">sudo</span> usermod <span class="tok-propertyName">-aG</span> docker <span class="tok-variableName tok-definition">$USER</span></div><div class="cm-line">newgrp docker <span class="tok-comment"># or just log out and back in</span></div><div class="cm-line"></div></code></pre>
</div>
</div>
</div>
<p class="wp-block-paragraph">Afterwards, it should be straightforward to get the image from <a href="https://hub.docker.com/r/qgis/qgis/tags">Docker Hub</a>, e.g.:</p>
<div class="wp-block-code">
<div class="cm-editor">
<div class="cm-scroller">
<pre>
<code class="language-shell"><div class="cm-line">docker pull qgis/qgis:4.2.2-questing</div><div class="cm-line"></div></code></pre>
</div>
</div>
</div>
<p class="wp-block-paragraph">And once it’s downloaded, we can launch QGIS:</p>
<div class="wp-block-code">
<div class="cm-editor">
<div class="cm-scroller">
<pre>
<code class="language-shell"><div class="cm-line">xhost <span class="tok-operator">+</span>local:docker</div><div class="cm-line">docker run <span class="tok-propertyName">--rm</span> <span class="tok-propertyName">-it</span> <span class="tok-propertyName">--name</span> qgis \ </div><div class="cm-line">  <span class="tok-propertyName">-v</span> /tmp/.X11-unix:/tmp/.X11-unix \ </div><div class="cm-line">  <span class="tok-propertyName">-e</span> <span class="tok-variableName tok-definition">DISPLAY</span><span class="tok-operator">=</span><span class="tok-variableName tok-definition">$DISPLAY</span> \ </div><div class="cm-line">  qgis/qgis:4.2.2-questing qgis</div><div class="cm-line">  </div></code></pre>
</div>
</div>
</div>
<p class="wp-block-paragraph"><strong>Voilá, QGIS 4!</strong></p>
<figure class="wp-block-image size-large"><a href="https://anitagraser.com/wp-content/uploads/2026/09/image-3.png"><img alt="" class="wp-image-9808" height="639" src="/img/subscribers/anita_graser/how-to-qgis-4-2-on-linux-mint-sept-26/image-3.webp" width="1024"/></a></figure>
<p class="wp-block-paragraph">To persist your QGIS profile/settings across container runs, mount a local folder to the config path, e.g.:</p>
<div class="wp-block-code">
<div class="cm-editor">
<div class="cm-scroller">
<pre>
<code class="language-shell"><div class="cm-line">docker run <span class="tok-propertyName">--rm</span> <span class="tok-propertyName">-it</span> <span class="tok-propertyName">--name</span> qgis \ </div><div class="cm-line">  <span class="tok-propertyName">-v</span> /tmp/.X11-unix:/tmp/.X11-unix \ </div><div class="cm-line">  <span class="tok-propertyName">-e</span> <span class="tok-variableName tok-definition">DISPLAY</span><span class="tok-operator">=</span><span class="tok-variableName tok-definition">$DISPLAY</span> \ </div><div class="cm-line">  <span class="tok-propertyName">-v</span> ~/.qgis-docker-profile:/root/.local/share/QGIS \ </div><div class="cm-line">  qgis/qgis:4.2.2-questing qgis</div><div class="cm-line">  </div></code></pre>
</div>
</div>
</div>
<p class="wp-block-paragraph">Of course, last but not least, we’ll also need access to our data, so let’s mount a data directory as well, e.g.:</p>
<div class="wp-block-code">
<div class="cm-editor">
<div class="cm-scroller">
<pre>
<code class="language-shell"><div class="cm-line">docker run <span class="tok-propertyName">--rm</span> <span class="tok-propertyName">-it</span> <span class="tok-propertyName">--name</span> qgis \</div><div class="cm-line">  <span class="tok-propertyName">-v</span> /tmp/.X11-unix:/tmp/.X11-unix \</div><div class="cm-line">  <span class="tok-propertyName">-e</span> <span class="tok-variableName tok-definition">DISPLAY</span><span class="tok-operator">=</span><span class="tok-variableName tok-definition">$DISPLAY</span> \</div><div class="cm-line">  <span class="tok-propertyName">-e</span> <span class="tok-variableName tok-definition">LIBGL_ALWAYS_SOFTWARE</span><span class="tok-operator">=</span><span class="tok-number">1</span> \</div><div class="cm-line">  <span class="tok-propertyName">-v</span> ~/.qgis-docker-profile:/root/.local/share/QGIS \</div><div class="cm-line">  <span class="tok-propertyName">-v</span> /mnt/ssd1/Geodata:/data \</div><div class="cm-line">  qgis/qgis:4.2.2-questing qgis</div><div class="cm-line">  </div></code></pre>
</div>
</div>
</div>
<p class="wp-block-paragraph">Fancy a bit of a stress test? I happened to find a project file written by QGIS 2.19 <img alt="🫢" class="wp-smiley" src="/img/subscribers/anita_graser/how-to-qgis-4-2-on-linux-mint-sept-26/1fae2.webp" style="height: 1em;"/></p>
<p class="wp-block-paragraph">Yes, my friend, this project file is indeed a litte bit older … but hey, that doesn’t look too bad at all! Some icons seem to be off but, otherwise, looks like winter is coming.</p>
<figure class="wp-block-image size-large"><a href="https://anitagraser.com/wp-content/uploads/2026/09/image-7.png"><img alt="" class="wp-image-9821" height="646" src="/img/subscribers/anita_graser/how-to-qgis-4-2-on-linux-mint-sept-26/image-7.webp" width="1024"/></a></figure>
<hr class="wp-block-separator has-alpha-channel-opacity"/>
<p class="wp-block-paragraph"><em>On a side note, whom do I need to ping to the QGIS logo in the System Package / Software Manager updated?</em></p>
<figure class="wp-block-image size-large"><a href="https://anitagraser.com/wp-content/uploads/2026/09/image-5.png"><img alt="" class="wp-image-9811" height="765" src="/img/subscribers/anita_graser/how-to-qgis-4-2-on-linux-mint-sept-26/image-5.webp" width="874"/></a></figure>
