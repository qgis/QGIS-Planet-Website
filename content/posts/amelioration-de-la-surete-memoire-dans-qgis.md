---
source: "blog"
title: "Improving Memory Safety in QGIS"
date: "2026-11-02T11:38:19"
link: "https://oslandia.com/en/2026/11/06/amelioration-de-la-surete-memoire-dans-qgis/"
draft: "false"
showcase: "planet"
subscribers: ["qgis_oslandia"]
author: "QGIS Oslandia"
tags: ["qgis", "", "cybersecurity"]
languages: ["en_gb"]
available_languages: ["en_gb"]
---

<p class="part">As part of our <a href="https://pad.oslandia.net/_link?url=https%3A%2F%2Foslandia.com%2Fen%2F2025%2F03%2F25%2Fle-security-project-for-qgis-contribuez-maintenant%2F">Security project for QGIS</a> initiative, we identified a work package titled “Improve Memory Safety.”</p>
<p class="part">Having worked on this topic over the last few months, here is a summary of the issues involved and what has been accomplished so far.</p>
<p class="part">It’s not an easy thing to present this topic. I’ll try not to dive into too much technical details to focus instead on the broader objectives and implications.</p>
<h3 class="part" id="Once-upon-a-time-in-the-United-States…"><i class="fa fa-link"></i>Once upon a time, in the United States…</h3>
<p class="part">In November 2022, the NSA published a <a href="https://pad.oslandia.net/_link?url=https%3A%2F%2Fwww.nsa.gov%2FPress-Room%2FNews-Highlights%2FArticle%2FArticle%2F3215760%2Fnsa-releases-guidance-on-how-to-protect-against-software-memory-safety-issues%2F">report</a> on software security, in which it stated:</p>
<blockquote class="part"><p>Microsoft and Google have each stated that software memory safety issues are behind around 70 percent of their vulnerabilities. Poor memory management can lead to technical issues as well, such as incorrect program results, degradation of the program’s performance over time, and program crashes.</p></blockquote>
<p class="part">In other words: <strong>70% of software vulnerabilities stem from memory management issues.</strong></p>
<blockquote class="part"><p>NSA recommends that organizations use memory safe languages ​​when possible and bolster protection through code-hardening defenses such as compiler options, tool options, and operating system configurations.</p></blockquote>
<p class="part">The NSA recommends using “Memory Safe Languages” (MSLs) or “hardening” the code. QGIS consists of approximately 1.5 million lines of C++ code, a language not “memory safe” by default. I am therefore opting for the “harden the code” approach, rather than a rewrite which, I have to admit, would have had the “advantage” of keeping me employed until retirement.</p>
<h3 class="part" id="What’s-the-problem"><i class="fa fa-link"></i>What’s the problem?</h3>
<p class="part">C++ is not a “memory-safe” language by default, as it does not require the explicit management of the lifecycle of the memory segments it uses.</p>
<p> </p>
<p><img alt="" class="aligncenter size-full wp-image-10736" height="293" src="/img/subscribers/qgis_oslandia/amelioration-de-la-surete-memoire-dans-qgis/leonardo.webp" width="269"/></p>
<p class="part"><em>That sentence didn’t make any sense to you, don’t worry, it won’t hinder your understanding of what follows.</em></p>
<p class="part">C++ developers are expected to <strong>be careful</strong>: they must ensure they don’t forget to deallocate memory that was previously allocated, while also avoiding deallocating the same memory multiple times, errors that can lead respectively to memory bloat or program crashes.</p>
<p class="part">These memory management issues can be exploited by malicious actors to inject code into a program, potentially allowing them to steal passwords or gain unauthorized access.</p>
<p> </p>
<p><img alt="" class="aligncenter size-full wp-image-10737" height="700" src="/img/subscribers/qgis_oslandia/amelioration-de-la-surete-memoire-dans-qgis/hackerman.webp" width="700"/></p>
<p class="part"><em>A malicious actor</em></p>
<h3 class="part" id="Work-performed"><i class="fa fa-link"></i>Work performed</h3>
<p class="part">Fortunately, C++ offers control structures known as <em>smart pointers</em>, which help manage the memory lifecycle. Using them helps prevent memory leaks and crashes, while also limiting the attack surface.</p>
<p class="part">QGIS currently makes limited use of these. The goal, therefore, is to expand their adoption throughout the codebase and prevent the addition of any new code that fails to utilize them.</p>
<p class="part">To achieve this, I developed a program that rewrites the code to incorporate <em>smart pointers</em>, followed by an extensive review process to ensure no new errors were introduced.</p>
<p class="part"><em><img alt="" class="aligncenter size-full wp-image-10738" height="431" src="/img/subscribers/qgis_oslandia/amelioration-de-la-surete-memoire-dans-qgis/contributeur-qgis.webp" width="579"/></em></p>
<p class="part"><em>A QGIS contributor in the middle of reviewing a pull request</em></p>
<h4 class="part" id="Why-not-use-AI"><i class="fa fa-link"></i>Why not use AI?</h4>
<p class="part">Nowadays, it’s hard to discuss any software engineering topic without bringing up AI (at least we don’t hear about blockchain anymore!), so I feel compelled to answer the question: “Could AI have been used for this task?”—or, to use the terminology favored by “tech-bros,” could it have been “AI-powered”?</p>
<p class="part">The answer is <strong>YES</strong>. But also <strong>NO</strong>. For one thing, the QGIS project is still determining its policy regarding AI; for the time being, a moratorium is in place that prohibits its use within the QGIS <em>core</em>.</p>
<p class="part">Furthermore, it would have required a more thorough review. My migration program is deterministic—when it makes a mistake, it always does so in the same way. The same cannot easily be said for a probabilistic machine.</p>
<h3 class="part" id="So-does-this-mean-we’re-now-“memory-safe”"><i class="fa fa-link"></i>So, does this mean we’re now “memory safe”?</h3>
<p class="part">Not quite. We’ve reached a significant milestone, but there’s still more to do. This work will continue over the coming months.</p>
<p class="part">In parallel, I’ve also begun a related project, supported by a <a href="https://pad.oslandia.net/_link?url=https%3A%2F%2Fqgis.org%2Fcommunity%2Forganisation%2Fgrants%2Fqgis-grant-programme-2026-results%2F">QGIS.org grant</a>. The goal is to <a href="https://pad.oslandia.net/_link?url=https%3A%2F%2Fgithub.com%2Fqgis%2FQGIS-Enhancement-Proposals%2Fblob%2Fmaster%2Fqep-417-remove-sip-factory.md">replace</a> <code>SIP_FACTORY</code> annotations with <em>unique pointers</em>. Explaining the technical details of this, however, would likely scare off the few readers who have made it this far!</p>
<p class="part">This initiative is part of a <a href="https://pad.oslandia.net/_link?url=https%3A%2F%2Foslandia.com%2Fen%2Fsecurity-project-for-qgis%2F">broader effort</a>, as we believe that all security-related issues must be addressed simultaneously and with equal rigor. After all, what’s the point of installing a reinforced front door if you leave the garage door wide open?</p>
<h3 class="part" id="To-be-continued…">To be continued…</h3>
<p class="part">We are committed to a process of continuous improvement—both for the QGIS codebase itself and for the workflows surrounding how the software is contributed to and distributed. It is worth noting that this initiative is not just about security; it also helps to reduce software crashes and memory footprint.</p>
<p class="part">It requires financial support. If you would like to contribute, or if you have any other questions regarding QGIS, please do not hesitate to contact us at <a href="mailto:infos+qgis@oslandia.com">mailto:infos+qgis@oslandia.com</a>.</p>
<p class="part">You can stay informed by subscribing to our <a href="https://pad.oslandia.net/_link?url=https%3A%2F%2Foslandia.com%2Fnewsletter">newsletter</a> and following us on <a href="https://pad.oslandia.net/_link?url=https%3A%2F%2Fwww.linkedin.com%2Fcompany%2Foslandia">LinkedIn</a>.</p>
