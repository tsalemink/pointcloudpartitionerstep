============================
Point Cloud Partitioner Step
============================

The **Point Cloud Partitioner** step is an interactive plugin for the MAP-Client.
The MAP Client is a workflow management application written in Python.
It can be found at https://github.com/MusculoskeletalAtlasProject/mapclient.

This tool takes a `Zinc` compatible point-cloud EX file as an input and provides a GUI that gives the user a number of tools
to help separate these points into groups. The **Point Cloud Partitioner** step outputs another `Zinc` compatible EX file with the
points separated into groups defined by the user.

Please refer to the plugin documentation for details on how to set up and run this tool.


Inputs
------
- **pointcloud** [nx3 NumPy Array] : source pointcloud

Outputs
-------
- **list[pointcloud]** [list] : output pointcloud-list
