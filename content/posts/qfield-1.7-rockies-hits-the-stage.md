---
source: "blog"
title: "QField 1.7 Rockies hits the stage"
date: "2020-10-20T07:26:08+0000"
link: "https://qfield.org/blog/2020/10/20/qfield-1.7-rockies-hits-the-stage/"
draft: "false"
showcase: "planet"
subscribers: ["qfield"]
author: "QField"
tags: ["android-qgis", "featured", "gis", "qfield", "highlights", "qgis.org"]
languages: ["en_gb"]
available_languages: ["en_gb"]
---

<p><strong>Be ready for the cold weather with a smooth coordinate search, filters in the value relation widget, fancy new QML and HTML widgets, enhanced geometry editing functionalities and an expandable legend. Right when Autumn starts, QField 1.7 Rockies hits the stage.</strong></p>
<p>As usual get it now on the <a href="https://play.google.com/store/apps/details?id=ch.opengis.qfield" rel="noopener" target="_blank">play store</a> or on <a href="https://github.com/opengisch/QField/releases" rel="noopener" target="_blank">github</a>!</p>
<p>The days are getting shorter and the wind blows colder. It’s always good to be in a good company outside while getting your mapping work done. QField will be your reliable companion.</p>
<p>We know, QField 1.6 Qinling has only been out two months and with its amount of new features and stability improvements, it would have deserved a longer primetime. But we just couldn’t withhold you all the new great stuff we’ve been building lately.</p>
<p>So let’s welcome QField 1.7 Rockies. And yes, we mean THE <a href="https://en.wikipedia.org/wiki/Rocky_Mountains" rel="noopener" target="_blank">Rockies</a>, where QField is looking for plenty of new buddies.</p>
<p>Let’s have a look.</p>
<h2 id="merging-features">Merging features</h2>
<p>Splitting of a feature has been possible for quite some time. Now the merging of features of multipolygon-layer is possible as well. Select them and merge them - easy like that. The first selected feature gets the new geometry and keeps its attributes.</p>
<figure class="figure text-center mb-4"><img alt="" class="figure-img img-fluid gallery-img" height="387" src="/img/subscribers/qfield/qfield-1.7-rockies-hits-the-stage/mergesmall-3.webp" width="774"/></figure>
<h2 id="filters-in-the-value-relation-widget">Filters in the Value Relation Widget</h2>
<p>The value relation widgets provide an easy selection of a related feature. Often it’s used for lookup tables but sometimes the related tables contain a lot of entries and the list of the possible values is long.</p>
<p>Using filters in the value relation drop-down can increase the efficiency in selecting the correct value. It can be configured by expressions in QGIS, so it’s possible to have the content of the drop down depend on the values entered previously in other fields.</p>
<figure class="figure text-center mb-4"><img alt="" class="figure-img img-fluid gallery-img" height="669" src="/img/subscribers/qfield/qfield-1.7-rockies-hits-the-stage/filtervaluerelation_trans_hu_5fb35e00879e65f8.webp" width="1200"/></figure>
<p>In the screenshot above there is a Map Value Widget with “forest” and “meadow” as values. On selecting “forest”, only the trees appear in the Field “Plant Species”. On selecting “meadow” there would be listed flowers instead.</p>
<h2 id="go-to-coordinates-in-the-search">Go to coordinates in the Search</h2>
<p>The search has not only been improved in its appearance, but it’s handling is much more comfortable with a button to clear the text and easy opening and closing.</p>
<p>Additionally, we added the possibility to jump to coordinates. Searching a place you know the coordinates of is now super simple. And this means that digitizing that precise geometry with known coordinates is finally possible.</p>
<figure class="figure text-center mb-4"><img alt="coordinates" class="figure-img img-fluid gallery-img" src="/img/subscribers/qfield/qfield-1.7-rockies-hits-the-stage/91524953-c144ba00-e900-11ea-97db-8f8b5a7f32a3.webp"/>
<figcaption class="figure-caption text-center">coordinates</figcaption></figure>
<h2 id="qml-and-html-widget">QML and HTML Widget</h2>
<p>You might remember when we introduced the <a href="https://qfield.org/de/2018/11/06/qml-widgets-qgis/">QML widget in QGIS</a>. Now it’s in QField as well. And it’s not alone. HTML widgets are supported too.</p>
<p>This provides a lot of possibilities to display information with texts, images and charts and it even allows you interaction.<br/>
Do you need help setting up complex forms? Don’t hesitate to <a href="https://qfield.org/qgis-support/">get in touch with us</a>!</p>
<div class="gallery-wrapper">
<figure class="figure text-center mb-4"><img alt="qml" class="figure-img img-fluid gallery-img" src="/img/subscribers/qfield/qfield-1.7-rockies-hits-the-stage/91524902-ad00bd00-e900-11ea-86e2-c44af84bb04a.webp"/>
<figcaption class="figure-caption text-center">qml</figcaption></figure>
<figure class="figure text-center mb-4"><img alt="" class="figure-img img-fluid gallery-img" height="1911" src="/img/subscribers/qfield/qfield-1.7-rockies-hits-the-stage/html-1.webp" width="1024"/></figure>
</div>
<h2></h2>
<p>Expandable legend icons</p>
<p>The legend items are now expandable and collapsible.</p>
<p>Wait a minute… Wasn’t this possible before? Yes. It was possible in earlier versions. But why it’s announced here as a new feature?</p>
<p>Because now it is built in a future proof manner thanks to all the people and organisations who care for QField and bought <a href="https://qfield.org/qgis-support/">a support contract with the sustainability initiative</a> or committed to a <a href="https://github.com/sponsors/opengisch" rel="noopener" target="_blank">recurring sponsorship</a>.</p>
<p>Some technical background: As you may be aware QField uses QGIS under the hood and QGIS uses Qt under the hood. Qt is currently used in version 5. Qt 5 is not that young any more and has a lot of functionality which is no longer supported by Qt. The old legend was based on the tree view, a deprecated module. Using it had some implications like the suboptimal support of HiDPI. Furthermore, these deprecated modules will disappear in the soon-to-come Qt 6.</p>
<p>As you can see, keeping QField at the quality we and you expect requires a lot of maintenance work. It is of utmost importance and only possible thanks to sponsoring since paying for fixing already existing features is less attractive for most people.</p>
<h2 id="what-will-the-future-bring">What will the future bring</h2>
<p>In the last weeks, we have been highly busy on coding, testing and promoting <a href="https://qfield.cloud/" rel="noopener" target="_blank">QFieldCloud</a> and we are very happy to be able to announce it very soon. So be prepared.</p>
<p>Also, keep an eye on the <a href="https://twitter.com/qfieldforqgis" rel="noopener" target="_blank">@QFieldForQgis</a> and <a href="https://twitter.com/qfieldcloud" rel="noopener" target="_blank">@QFieldCloud</a> twitter accounts to stay updated.</p>
<h2 id="open-source">Open Source</h2>
<p>QField is an open source project. This means that whatever is produced is available free of charge. To anyone. Forever. This also means that everyone has the chance to contribute. You can write code, but you don’t need to. You can also help <a href="https://www.transifex.com/opengisch/qfield-for-qgis/dashboard/" rel="noopener" target="_blank">translating the app to your language</a> or help out <a href="https://github.com/opengisch/QField-docs" rel="noopener" target="_blank">writing documentation or case studies</a> or by sponsoring a new feature.</p>
<h2 id="and-now">And now…</h2>
<p>… enjoy QField 1.7 Rockies and have a nice autumn!</p>
