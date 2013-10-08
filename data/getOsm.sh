#!/bin/bash
mv data.osm data.osm.bak;
wget "http://overpass.osm.rambler.ru/cgi/xapi_meta?*[bbox=77.4811,12.857,77.7575,13.0751]" -O data.osm;
