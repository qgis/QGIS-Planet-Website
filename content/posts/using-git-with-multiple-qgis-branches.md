---
source: "blog"
title: "Using git With Multiple QGIS Branches"
date: "2011-11-14T09:03:15+0000"
link: "http://spatialgalaxy.net/2011/11/14/using-git-with-multiple-qgis-branches/"
draft: "false"
showcase: "planet"
subscribers: ["spatialgalaxy_net"]
author: "Spatial Galaxy"
tags: []
---

This post is for those of you that build QGIS on a regular basis and want to keep up with everything going on in the current release branches (1.7.2 and 1.8) as well as the master branch that will eventually become version 2.0.
While you can do all your work in one clone, this method has a couple of advantages, at the expense of a bit of disk space:
 Quicker compiles compared to branch switching, especially if you are using ccache Less likelihood of making a merge mess when switching branches  The basic steps are:
