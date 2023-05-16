"""
Created on Jun 18, 2015

@author: tsalemink
"""
from cmlibs.zinc.context import Context


class PointCloudPartitionerModel(object):

    def __init__(self):
        self._point_cloud_nodes = None
        self._selection_group = None
        self._mesh = None

        self._context = Context("PointCloudPartitioner")
        self._region = self._context.getDefaultRegion()
        self._field_module = self._region.getFieldmodule()

        self.define_standard_materials()
        self.define_standard_glyphs()

        self._selection_filter = self._create_selection_filter()

    def get_selection_filter(self):
        return self._selection_filter

    def load(self, file_location):
        self._region.readFile(file_location)

        nodes = self._field_module.findNodesetByName("nodes")
        point_cloud_group_field = self._field_module.createFieldNodeGroup(nodes)
        self._point_cloud_nodes = point_cloud_group_field.getNodesetGroup()
        self._point_cloud_nodes.addNodesConditional(self.get_point_cloud_coordinates())

        self._mesh = self._field_module.findMeshByDimension(2)

    def get_context(self):
        return self._context

    def get_point_cloud_coordinates(self):
        return self._field_module.findFieldByName("data_coordinates")

    def get_mesh_coordinates(self):
        return self._field_module.findFieldByName("mesh_coordinates")

    def get_region(self):
        return self._region

    def get_nodes(self):
        return self._point_cloud_nodes

    def get_mesh(self):
        return self._mesh

    def _create_selection_filter(self):
        m = self._context.getScenefiltermodule()
        # r1 = m.createScenefilterRegion(self._detection_model.get_region())
        # r2 = m.createScenefilterRegion(self._marker_model.get_region())
        o = m.createScenefilterOperatorOr()
        # o.appendOperand(r1)
        # o.appendOperand(r2)
        return o

    def define_standard_glyphs(self):
        """
        Helper method to define the standard glyphs
        """
        glyph_module = self._context.getGlyphmodule()
        glyph_module.defineStandardGlyphs()

    def define_standard_materials(self):
        """
        Helper method to define the standard materials.
        """
        material_module = self._context.getMaterialmodule()
        material_module.defineStandardMaterials()
