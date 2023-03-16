"""
Created on Jun 22, 2015

@author: tsalemink
"""
from opencmiss.zinc.field import Field
from opencmiss.zinc.glyph import Glyph
from opencmiss.zinc.graphics import Graphics


class PointCloudPartitionerScene(object):
    """
    classdocs
    """

    def __init__(self, model):
        """
        Constructor
        """
        self._model = model
        self._setupVisualisation()

    def _setupVisualisation(self):
        coordinate_field = self._model.getCoordinateField()
        region = self._model.getRegion()
        scene = region.getScene()
        self._node_graphics = self.create_point_graphics(scene, coordinate_field, None, Graphics.SELECT_MODE_DRAW_SELECTED)
        self._selection_graphics = self.create_point_graphics(scene, coordinate_field, None, Graphics.SELECT_MODE_DRAW_UNSELECTED)

    def create_point_graphics(self, scene, finite_element_field, subgroup_field, mode=Graphics.SELECT_MODE_DRAW_UNSELECTED):
        scene.beginChange()
        graphic = scene.createGraphicsPoints()
        graphic.setFieldDomainType(Field.DOMAIN_TYPE_NODES)
        graphic.setCoordinateField(finite_element_field)
        graphic.setSelectMode(mode)

        if subgroup_field:
            graphic.setSubgroupField(subgroup_field)

        attributes = graphic.getGraphicspointattributes()
        attributes.setGlyphShapeType(Glyph.SHAPE_TYPE_SPHERE)

        # TODO: Update this to depend on point cloud size.
        attributes.setBaseSize([0.02])
        # Temporarily increase size of grouped Nodes.
        if subgroup_field:
            attributes.setBaseSize([0.03])

        scene.endChange()

        return graphic
