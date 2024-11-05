---
source: "blog"
title: "Importing CSV files into PostgreSQL using the DB Manager in QGIS"
date: "2015-02-08T06:04:40+0000"
link: "https://ieqgis.com/2015/02/08/importing-csv-files-into-postgresql-using-the-db-manager-in-qgis/"
draft: "false"
showcase: "planet"
subscribers: ["ireland_qgis_user_group_blog"]
author: "Ireland QGIS User Group Blog"
tags: ["uncategorized"]
---

<p>There is very useful tool in QGIS that can import very large CSV files into PostgreSQL rapidly and reliably. The DB Manager&#8217;s &#8220;Import Vector Layer&#8221; tool. Contrary to its highly misleading title it can import CSV files as well. Open the DB Manager (menu <em>Database &#8211; DB Manager</em>). Then select the database where you want to store your table and click the &#8220;Import layer/file&#8221; icon.</p>
<p><a href="https://ieqgis.files.wordpress.com/2015/02/icon_to_click.png"><img alt="Icon_to_Click" class="aligncenter size-full wp-image-695" src="https://ieqgis.files.wordpress.com/2015/02/icon_to_click.png?w=545" /></a>From the Import Vector Layer GUI, locate our CSV file on disk and enter the name of your new table in the Table box and click OK. Yes, it&#8217;s that simple. Proceeding this, you may need to select an text encoding scheme, files created on Windows often use ISO-8859-1 (Latin-1) instead of UTF-8 encoding. In my case, I was able to import a large statistical data set describing the energy efficiency of 525,500 Irish homes (432 megabytes) into PostgreSQL in ~15 minutes. After the CSV file is imported, you can optionally add it to your project using the DB Manager, right-click the table and select <em>Add to Canvas</em>. Don&#8217;t use the &#8220;Add PostGIS Layers&#8221; menu, it&#8217;s not a PostGIS layer.</p>
<p><a href="https://ieqgis.files.wordpress.com/2015/02/import_gui.png"><img alt="Import_Gui" class="aligncenter size-full wp-image-696" src="https://ieqgis.files.wordpress.com/2015/02/import_gui.png?w=545" /></a>And one more useful tip. You can convert Tab delimited text to CSV using QGIS. Load a Tab delimited text file into QGIS using the Add Delimited Text Layer GUI, then right click the imported file in the layer panel and save it as a CSV file.</p>
