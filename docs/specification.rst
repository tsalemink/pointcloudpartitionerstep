.. _mcp-pointcloudpartitioner-specification:

Ports
-----

This plugin:

* **uses**:

  * *https://opencmiss.org/1.0/rdf-schema#file_location*
  * *https://opencmiss.org/1.0/rdf-schema#file_location*

and

* **provides**:

  * *https://opencmiss.org/1.0/rdf-schema#file_location*

The first **uses** port imports a `Zinc` EX file containing a point-cloud.
The second **uses** port imports a `Zinc` EX file containing a set of mesh surfaces.
Importing mesh surfaces is optional but will enable some additional selection features that can help with the point grouping stage.
The **provides** port outputs a `Zinc` EX file containing the point-cloud with the points separated into named groups.
