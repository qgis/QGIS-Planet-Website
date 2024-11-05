---
source: "blog"
title: "Hepler modules for development of QGIS plugins"
date: "2013-05-16T12:55:11+0000"
link: "https://3nids.wordpress.com/2013/05/16/hepler-modules-for-qgis-plugins/"
draft: "false"
showcase: "planet"
subscribers: ["qgis_tips"]
author: "QGIS Tips"
tags: ["plugins", "setting"]
---

<p>There are two things I have coded, re-coded and re-re-coded through all my plugins: the management of the settings and the management of combo boxes associated to layers and their fields.</p>
<p>I have decided to write two generic python modules to solve these tasks to avoid reinventing the wheel every time.</p>
<p>The first one is called <a href="http://3nids.github.io/qgissettingmanager/"><strong>QGIS setting manager</strong></a>.<br />
This module allows you to:</p>
<ul>
<li>manage <strong>different types of settings</strong> (bool, string, color, integer, double, stringlist)</li>
<li><strong>read and write settings</strong> in QGIS application or in the QGIS project</li>
<li>automatically <strong>set widgets from corresponding setting</strong></li>
<li>automatically <strong>write settings from widgets of a dialog</strong></li>
</ul>
<p>This means that the class of a dialog dedicated to editing the plugins settings can be reduced to just a few lines.<br />
You just have to name widgets according to settings and the module automatically detect the widgets, sets/reads the value from the widget and read/write the settings accordingly.</p>
<p>A setting class would look like this</p>
<pre class="brush: python; title: ; wrap-lines: false; notranslate">
from qgissettingmanager import *

class MySettings(SettingManager):
    def __init__(self):
        SettingManager.__init__(self, myPluginName)
        self.addSetting(&quot;myVariable&quot;, &quot;bool&quot;, &quot;global&quot;, True)
</pre>
<p>reading and write settings are performed by doing</p>
<pre class="brush: python; title: ; wrap-lines: false; notranslate">
self.settings = MySettings()
self.settings.setValue(&quot;myVariable&quot;, False)
myVariable = self.settings.value(&quot;myVariable&quot;)
</pre>
<p>and a dialog looks like this</p>
<pre class="brush: python; title: ; wrap-lines: false; notranslate">
class MyDialog(QDialog, Ui_myDialog, SettingDialog):
    def __init__(self):
        QDialog.__init__(self)
        self.setupUi(self)
        self.settings = MySettings()
        SettingDialog.__init__(self, self.settings)
</pre>
<p>You can find a complete <strong><a href="http://3nids.github.io/qgissettingmanager/">howto here</a></strong> and look at the code on <a href="https://github.com/3nids/qgissettingmanager">github</a>.</p>
<p>The second module is called <a href="http://3nids.github.io/qgiscombomanager/"><strong>QGIS combo manager</strong></a>. This module autmatically manages combo box widgets for layers, fields of vector layers and bands of raster layers.<br />
You can associate a field combo to a layer combo: as soon as the layer has been modified, the fields are updated to the current layer.</p>
<p>Associating a combo box to layers and another one to its fields would look like this:</p>
<pre class="brush: python; title: ; wrap-lines: false; notranslate">
from qgiscombomanager import *

self.layerComboManager = VectorLayerCombo(self.layerComboWidget)
self.myFieldComboManager = FieldCombo(self.myFieldComboManager, self.layerComboManager)
</pre>
<p>You can find a complete <strong><a href="http://3nids.github.io/qgiscombomanager/">howto here</a></strong> and look at the code on <a href="https://github.com/3nids/qgiscombomanager">github</a>.</p>
