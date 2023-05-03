"""
Created on Jun 18, 2015

@author: tsalemink
"""
from cmlibs.zinc.context import Context


class PointCloudPartitionerModel(object):

    def __init__(self):
        self._nodes = None
        self._selection_group = None

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
        self._nodes = self._field_module.findNodesetByName("nodes")

    def get_context(self):
        return self._context

    def get_coordinate_field(self):
        return self._field_module.findFieldByName("coordinates")

    def get_region(self):
        return self._region

    def get_nodes(self):
        return self._nodes

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
