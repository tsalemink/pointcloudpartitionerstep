.. _mcp-pointcloudpartitioner-workflow-setup:

Workflow Setup
--------------

To setup a point cloud partitioner workflow, add a **File Chooser** step (or another step that provides a `Zinc` point-cloud EX file) and a
**Point Cloud Partitioner** step to the workflow area. Edit the **File Chooser** step configuration to specify the `Zinc` EX file that
contains the point cloud to be grouped. Once this step has been configured, connect its output port to the first input port of the
**Point Cloud Partitioner** step - as in :ref:`Fig. 1 <fig-point-cloud-partitioner-workflow>`. If you also have a `Zinc` mesh EX file
associated with the point-cloud, you can pass this to the partitioner plugin through its second input port. For this demonstration we have
chosen to use an additional **File Chooser** step to pass the mesh file. The partitioner step will be configured by default as it doesn't
have any configuration settings to be set. What you connect the **Point Cloud Partitioner** step output port to depends on your objective.
In :ref:`Fig. 1 <fig-point-cloud-partitioner-workflow>` we have connected the output port to a **File Location Sink** step - allowing us to
define a local directory where the output file will be saved.

.. _fig-point-cloud-partitioner-workflow:

.. figure:: _images/point-cloud-partitioner-workflow.png
   :figwidth: 100%
   :align: center

   **Point Cloud Partitioner** workflow connections.

Once we have the workflow set up, save it and click the `Execute` button to start the **Point Cloud Partitioner** GUI.
