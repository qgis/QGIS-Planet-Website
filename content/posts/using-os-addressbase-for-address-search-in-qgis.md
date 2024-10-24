---
source: "blog"
title: "Using OS AddressBase for Address Search in QGIS"
date: "2016-05-27T12:00:00-0500"
link: "https://lutraconsulting.co.uk/blog/2016/05/27/using-os-addressbase-for-address-search-in-qgis/"
draft: "false"
showcase: "planet"
subscribers: ["lutragis"]
author: "Lutra Consulting"
tags: []
---

<p>In this blog post we’ll learn how to use Ordnance Survey AddressBase data with the QGIS Discovery plugin for searching addresses.</p>

<p align="center"><img alt="Discovery Plugin for QGIS" src="https://www.lutraconsulting.co.uk/img/posts/discovery_small.png" /></p>

<!-- more -->

<h2 id="before_we_start">Before we start</h2>

<p>The AddressBase data will be loaded into a PostGIS table for Discovery to query. At this stage we should already have a functioning PostgreSQL / PostGIS installation.</p>

<p><a href="https://www.lutraconsulting.co.uk/blog/2016/04/25/Setting-up-Discovery-plugin/" target="_blank">A previous blog post</a> describes how to quickly set up such an environment.</p>

<h2 id="creating_the_addressbase_table">Creating the addressbase table</h2>

<p>Let’s now create a table for storing the addressbase data. In the example below we’ll create a table called <code class="highlighter-rouge">addressbase</code> in the <code class="highlighter-rouge">os_address</code> schema.</p>

<p>The script below can be executed through pgAdminIII.</p>

<p>To run the script:</p>

<ol>
  <li>Open pgAdminIII</li>
  <li>Connect to your destination database</li>
  <li>Select <em>Query tool</em> from the <em>Tools</em> menu</li>
  <li>Paste the code below into the <em>Query tool</em></li>
  <li>Press F5 to execute the query (it may take a few seconds to complete)</li>
</ol>

<p>When the query has finished you should see <em>Query returned successfully with no result in … seconds.</em> in the <em>Messages</em> panel:</p>

<p align="center"><img alt="pgAdminIII Messages Panel" src="https://www.lutraconsulting.co.uk/img/posts/pga_messages.png" /></p>

<p>At this point we should be able to locate the new <code class="highlighter-rouge">addressbase</code> table within the <code class="highlighter-rouge">os_address</code> schema:</p>

<p align="center"><img alt="addressbase Table" src="https://www.lutraconsulting.co.uk/img/posts/addressbase_table.png" /></p>

<p>If you can’t see the schema / table you probably need to refresh the schemas / tables views in pgAdminIII’s <em>Object browser</em> panel by hitting F5.</p>

<div class="highlighter-rouge"><div class="highlight"><pre class="highlight"><code>-- Create the destination schema if required
CREATE SCHEMA IF NOT EXISTS os_address;

-- Create a function which will populate the full_address and geom columns as
-- data are imported
CREATE OR REPLACE FUNCTION create_geom_and_address()
RETURNS trigger AS $$
BEGIN
  -- The geometry
  -- Set it based on the x_coord and y_coord fields
  NEW.geom = ST_SetSRID(ST_MakePoint(NEW.x_coordinate, NEW.y_coordinate), 27700);
  -- The full address
  -- Initialise it
  NEW.full_address = '';
  -- Build the full address by only including optional address components if they
  -- exist
  IF NEW.organisation_name IS NOT NULL AND length(NEW.organisation_name) &gt; 0 THEN
	NEW.full_address = NEW.full_address || NEW.organisation_name || ', ';
  END IF;
  IF NEW.department_name IS NOT NULL AND length(NEW.department_name) &gt; 0 THEN
	NEW.full_address = NEW.full_address || NEW.department_name || ', ';
  END IF;
  IF NEW.po_box_number IS NOT NULL AND length(NEW.po_box_number) &gt; 0 THEN
	NEW.full_address = NEW.full_address || NEW.po_box_number || ', ';
  END IF;
  IF NEW.sub_building_name IS NOT NULL AND length(NEW.sub_building_name) &gt; 0 THEN
	NEW.full_address = NEW.full_address || NEW.sub_building_name || ', ';
  END IF;
  IF NEW.building_name IS NOT NULL AND length(NEW.building_name) &gt; 0 THEN
	NEW.full_address = NEW.full_address || NEW.building_name || ', ';
  END IF;
  IF NEW.building_number IS NOT NULL THEN
	NEW.full_address = NEW.full_address || NEW.building_number || ', ';
  END IF;
  IF NEW.dependent_thoroughfare IS NOT NULL AND length(NEW.dependent_thoroughfare) &gt; 0 THEN
	NEW.full_address = NEW.full_address || NEW.dependent_thoroughfare || ', ';
  END IF;
  IF NEW.thoroughfare IS NOT NULL AND length(NEW.thoroughfare) &gt; 0 THEN
	NEW.full_address = NEW.full_address || NEW.thoroughfare || ', ';
  END IF;

  NEW.full_address = NEW.full_address || NEW.post_town || ', ';

  IF NEW.double_dependent_locality IS NOT NULL AND length(NEW.double_dependent_locality) &gt; 0 THEN
	NEW.full_address = NEW.full_address || NEW.double_dependent_locality || ', ';
  END IF;
  IF NEW.dependent_locality IS NOT NULL AND length(NEW.dependent_locality) &gt; 0 THEN
	NEW.full_address = NEW.full_address || NEW.dependent_locality || ', ';
  END IF;

  NEW.full_address = NEW.full_address || NEW.postcode;

  RETURN NEW;
END;
$$ LANGUAGE 'plpgsql';

-- Drop any existing addressbase table
DROP TABLE IF EXISTS os_address.addressbase CASCADE;
CREATE TABLE os_address.addressbase
(
  -- id will be the primary key, populated automatically
  id serial NOT NULL,
  uprn bigint NOT NULL,
  os_address_toid varchar(24) NOT NULL,
  -- os_address_toid bigint NOT NULL,
  udprn integer NOT NULL,
  organisation_name varchar(60),
  department_name varchar(60),
  po_box_number varchar(6),
  sub_building_name varchar(30),
  building_name varchar(50),
  building_number smallint,
  dependent_thoroughfare varchar(80),
  thoroughfare varchar(80),
  post_town varchar(30) NOT NULL,
  double_dependent_locality varchar(35),
  dependent_locality varchar(35),
  postcode varchar(8) NOT NULL,
  postcode_type char(1) NOT NULL,
  x_coordinate numeric(8,2) NOT NULL,
  y_coordinate numeric(9,2) NOT NULL,
  latitude numeric(9,7) NOT NULL,
  longitude numeric(8,7) NOT NULL,
  rpc char(1) NOT NULL,
  country char(1) NOT NULL,
  change_type char(1) NOT NULL,
  la_start_date date NOT NULL,
  rm_start_date date NOT NULL,
  last_update_date date NOT NULL,
  class char(1) NOT NULL,
  -- the next two fields are populated automatically on insert
  full_address text NOT NULL,
  geom geometry(Point,27700) NOT NULL,
  CONSTRAINT addressbase_pkey PRIMARY KEY (id)
)
WITH (
  OIDS=FALSE
);

-- Create a pg_trgm index on the full_address column
-- This will allow super-fast, case-insensitive search on the column
CREATE EXTENSION IF NOT EXISTS pg_trgm;
CREATE INDEX addressbase_full_address_gin_trgm
  ON os_address.addressbase
  USING gin
  ("full_address" gin_trgm_ops);

-- Spatial index for the geometry column
CREATE INDEX addressbase_geom_gist
  ON os_address.addressbase
  USING gist
  (geom);

-- trigger to create points and addresses
-- This trigger will be executed on each row inserted, calling the function defined above
CREATE TRIGGER tr_create_geom_and_address BEFORE INSERT
  ON os_address.addressbase
  FOR EACH ROW
  EXECUTE PROCEDURE create_geom_and_address();

</code></pre></div></div>

<p>The script above has:</p>

<ul>
  <li>Created a table</li>
  <li>Added any necessary indices</li>
  <li>Created two additional, derived columns, full_address and geom</li>
</ul>

<p><em>full_address</em> will be used to store various address components into a sensible, human readable address. <em>geom</em> will be used to store point geometry based on address eastings/northings.</p>

<p>See the script comments for more information / detail.</p>

<h2 id="loading_addressbase">Loading AddressBase</h2>

<p>At this point we have an empty table ready to accept our AddressBase data.  We will now import the data using pgAdminIII. Extract the CSV files for the addresses, you should end up seeing one or more CSV files, for example <em>AddressBase_FULL_2016-03-19_001.csv</em></p>

<p>In <em>pgAdminIII</em>:</p>

<ol>
  <li>Locate the <em>addressbase</em> table</li>
  <li>Right click it, select <em>Import</em></li>
</ol>

<p>An import dialog should appear. Select the first CSV file and set the settings in the <em>File Options</em> tab as shown here:</p>

<p align="center"><img alt="AddressBase Import Options 1" src="https://www.lutraconsulting.co.uk/img/posts/addressbase_import_1.png" /></p>

<p>Uncheck the <em>id</em>, <em>full_address</em> and <em>geom</em> columns in the <em>Columns</em> tab as shown here:</p>

<p align="center"><img alt="AddressBase Import Options 2" src="https://www.lutraconsulting.co.uk/img/posts/addressbase_import_2.png" /></p>

<p>Click <em>Import</em>. After a few seconds the dialog may report <em>(Not Responding)</em>. This is nothing to worry about, be patient.</p>

<p>When the import process completes, close the import dialog and repeat the above steps with any remaining CSV files.</p>

<p>At this stage the data has been imported and the <em>full_address</em> field should contain sensible, human-readable addresses.</p>

<h2 id="configuring_discovery">Configuring Discovery</h2>

<p>With the data loaded in QGIS, we can now configure Discovery to make use of it.</p>

<ol>
  <li>Install the <em>Discovery</em> plugin if not already installed</li>
  <li>Open Discovery’s settings using the <span><img src="https://www.lutraconsulting.co.uk/img/posts/discovery_icon.png" /></span> button</li>
  <li>Set the settings as follows, changing the <em>Scale Expression</em> if required</li>
</ol>

<p align="center"><img alt="Discovery Settings for OS AddressBase" src="https://www.lutraconsulting.co.uk/img/posts/discovery_addressbase_settings.png" /></p>

<p>Congratulations! QGIS should now be set up to search your AddressBase data.</p>

    <div class="input-promo">
    <h2>You may also like...</h2>
    <a href="https://merginmaps.com">Mergin Maps, a field data collection app based on QGIS</a>. Mergin Maps makes field work easy with its simple interface and cloud-based sync. Available on Android, iOS and Windows.
    <img alt="Screenshots of the Mergin Maps mobile app for Field Data Collection" src="https://lutraconsulting.co.uk/img/posts/input_app_for_field_data_collection.jpg" /><br />
    <a href="https://play.google.com/store/apps/details?id=uk.co.lutraconsulting&amp;utm_source=lutra-atom&amp;utm_medium=lutra-blog-footer&amp;utm_campaign=input">
      <img alt="Get it on Google Play" src="https://play.google.com/intl/en_us/badges/images/generic/en_badge_web_generic.png" width="180px" />
    </a>
    <a href="https://apps.apple.com/us/app/input/id1478603559?ls=1&amp;utm_source=lutra-atom&amp;utm_medium=lutra-blog-footer&amp;utm_campaign=input">
      <img alt="Get it on Apple store" src="https://www.lutraconsulting.co.uk/img/posts/App_Store.svg" style="padding-top: 0px;" width="144px" />
    </a>
  </div>
