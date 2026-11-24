---
source: "blog"
title: "How to effectively get things changed in QGIS"
date: "2016-08-09T00:07:40+0000"
link: "https://nyalldawson.net/2016/08/how-to-effectively-get-things-changed-in-qgis/"
draft: "false"
showcase: "planet"
subscribers: ["nyalldawson_net"]
author: "nyalldawson.net"
tags: ["qgis", "opensource", "osgeo", "qgis"]
languages: ["en_gb"]
available_languages: ["en_gb"]
---

<p>I’ve been heavily involved in the open source <a href="http://www.qgis.org/en/site/">QGIS</a> mapping project for a number of years now. During this time I’ve kept a close watch on the various mailing lists, issue trackers, stackexchange, tweets and other various means users have to provide feedback to the project. Recently, I’ve started to come to the conclusion that there’s a lot of fundamental confusion about how the project works and how users can get changes made to the project. Read on for these insights, but keep in mind that these are just my thoughts and not reflective of the whole community’s views!..</p>
<p>Firstly – QGIS is a community driven project. Unlike some open source projects (and unlike the proprietary GIS offerings) there is no corporate backer or singular organisation directing the project. This means two things:</p>
<ol>
<li><strong>The bad news:</strong> No-one will do your work for you. QGIS has been created through a mix of user-led contributions (ie, users who have a need to change something and dive in and do it themselves) and through commercially supported contributions (either organisations who offer commercial QGIS support pushing fixes because their customers are directly affected or because they’ve been contracted by someone to implement a particular change). There HAS been a number of volunteer contributions from developers who are just donating their time (for various reasons), but these contributions are very much the minority.</li>
<li><strong>The good news:</strong> YOU have the power to shape the project! (<em>And whenever I say “you” – I’m referring directly to the person reading this, or the company you work for. Just pretend it’s in 24 point bold red blinking text.</em>) Because QGIS is community driven (and not subject to the whims of any one particular enterprise) every user has the ability to implement changes and fixes in the program.</li>
</ol>
<p>So how exactly can users get changes implemented in QGIS? Well, let’s take a look at all the possible different ways that changes get made and how effective each one is:</p>
<ol>
<li>YOU can make the changes yourself. This implies that you have the c++/Python skills required to make the changes, are able to find your way around the source code, and push through the initial hurdles of setting up a build environment and navigating git. This can be a significant time investment, but the ultimate result is that you can make whatever changes you want, and so long as your pull request is accepted you’ll get your changes directly into QGIS. You’ll find the QGIS team is very open to new contributors and will readily lend a hand if you need assistance navigating the source or for advise on the best way to make these changes. Just ask!</li>
<li>YOU (or your employer) can pay (or “sponsor”) someone to make the changes on your behalf. Reinvesting some of those savings you’re making through using an open source program back into the program itself is a great idea, and everyone benefits. There’s <a href="https://www.qgis.org/en/site/forusers/commercial_support.html">numerous organisations</a> who specialise in QGIS development (eg… my own consultancy, <a href="http://north-road.com">North Road</a>). You can liaise with these organisations to get them to make the changes on your behalf. This is probably the most effective way of getting changes implemented. These organisations all have a history with QGIS development and this experience generally translates to much faster development then if you code it yourself. It’s also somewhat of a shortcut – if you hire a core QGIS developer to make your changes, then you can be confident that they are familiar with the coding style, policies, and long-term goals of the project and accordingly can get the changes accepted rapidly. The obvious down side of paying for changes is that, well, it costs money. Understandably, not everyone has the resources available to do this.</li>
<li>Following on from option 2 – if you can’t directly sponsor changes yourself, you could help indirectly raise funds to pay for the changes. This is a great way to get changes implemented, because everyone has the power to do this. You could seek out similar organisations/users who have the same need and pool your resources, get involved with the local QGIS user group and raise funds together, organise a crowd-funding campaign, etc.</li>
<li>Ask a developer to make the changes for you. This is not terribly effective – you’re basically asking someone to work for free, and take time away from their family/job/hobbies/social life to do work for you. That said, it <strong>does</strong> sometimes happen, and here’s a few reasons I can think of why:
<ul>
<li>You’ve build up enough “karma” within the project through other contributions. If someone has been heavily involved in the non-development side of the project (eg translations, documentation, helping users out on mailing lists/stackexchange, organising hackfests or user groups, etc) then developers are much more likely to want to help them out in turn.</li>
<li>You’ve got a fantastic idea which has just never occurred to anyone before. By bringing it to the attention of a developer you might trigger the “wow, I could really benefit from that too!” impulse which is hard-wired into some of us!</li>
<li>It’s a particularly interesting or challenging problem, and sometimes developers just like to extend themselves.</li>
</ul>
</li>
<li>(For bugs only) File a bug report, and hope it gets picked up in one of the pre-release bug fixing sprints. This is basically the same as option 2 – expect that in this case someone else (the QGIS steering committee) is paying for the development time. There’s no way of guaranteeing that your bug will get fixed during this time though, so it’s not a particularly reliable approach if the fix is critical for you.</li>
</ol>
<p>Finally, there’s two more very ineffective approaches:</p>
<ol start="6">
<li>File a bug report/feature request, and wait. This isn’t very effective, because what you’re doing is basically the same as 1-4 above, but just waiting for someone else to either do the work or sponsor the changes. This might happen in a week, or might take <a href="http://hub.qgis.org/issues/777">10 years</a>.</li>
<li>Complain about something and hope for the best. This is… not very effective. No-one is particularly motivated to help out someone who is being a jerk.</li>
</ol>
<p>That’s it. Those are the ONLY ways changes get made in QGIS. There’s no other magical short-cuts you can take. Some of these approaches are much more effective than others, and some require skills or resources which may not be available. If you want to see something change in QGIS, you need to take a look at these options and decide for yourself which best meets your needs. But please, just don’t choose option 7!</p>
<p><em>Update: a <a href="http://nyalldawson.net/2016/08/how-to-effectively-get-things-changed-in-qgis-a-follow-up/">follow up</a> to this article was published</em></p>
