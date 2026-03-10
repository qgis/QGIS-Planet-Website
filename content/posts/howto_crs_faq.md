---
source: "blog"
title: "QGISにおける座標系設定に関するよくあるトラブルと解決法 - QGIS LAB by MIERUNE"
date: "2025-02-07T02:27:01"
link: "https://qgis.mierune.co.jp/posts/howto_crs_faq"
draft: "false"
showcase: "planet"
subscribers: ["qgis_lab_by_mierune"]
author: "QGIS LAB by MIERUNE"
tags: ["qgis"]
languages: ["ja_jp"]
available_languages: ["ja_jp"]
---

はじめにQGISで地図データを扱う際、重要な設定の1つが「座標系」です。座標系が正しく設定されていないと、地図データがずれて表示されたり、期待した位置にレイヤが配置されなかったりといったトラブルが発生します。下記の図では、国土数値情報の湖沼データをOpenStreetMapの上に表示していますが、座標系が適切でないため、海の上に琵琶湖が表示されてしまっています。海の上に琵琶湖が表示されている（Op...
