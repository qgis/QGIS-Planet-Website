---
source: "blog"
title: "Vim and CMake Out-of-Source Builds"
date: "2010-03-30T19:48:18+0000"
link: "http://spatialgalaxy.net/2010/03/30/vim-and-cmake-out-of-source-builds/"
draft: "false"
showcase: "planet"
subscribers: ["spatialgalaxy_net"]
author: "Spatial Galaxy"
tags: []
---

If you use Vim you probably know you can use the make command to build your project. The make command looks for a Makefile in your current directory. If you are editing a file that is not in the current directory (meaning you use some Vim magic to change to the directory containing your edit buffer), make will start below the top-level of your build directory. This is often the case when doing an out-of-source build with CMake.
