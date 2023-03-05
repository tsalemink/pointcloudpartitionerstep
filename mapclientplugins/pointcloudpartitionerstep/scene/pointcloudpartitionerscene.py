"""
Created on Jun 22, 2015

@author: tsalemink
"""
from opencmiss.zinc.field import Field
from opencmiss.zinc.glyph import Glyph


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
        selection_field = self._model.get_selection_field()
        region = self._model.getRegion()
        scene = region.getScene()
        materialmodule = scene.getMaterialmodule()
        red = materialmodule.findMaterialByName('red')
        blue = materialmodule.findMaterialByName('blue')
        self._node_graphics = self._createPointGraphics(scene, coordinate_field, red, None)
        self._selection_graphics = self._createPointGraphics(scene, coordinate_field, blue, selection_field)

    def _createPointGraphics(self, scene, finite_element_field, material, subgroup_field):
        scene.beginChange()
        # Create a surface graphic and set it's coordinate field to the finite element coordinate field.
        graphic = scene.createGraphicsPoints()
        graphic.setFieldDomainType(Field.DOMAIN_TYPE_NODES)
        graphic.setCoordinateField(finite_element_field)
        graphic.setMaterial(material)
        graphic.setSelectedMaterial(material)
        if subgroup_field:
            graphic.setSubgroupField(subgroup_field)
        attributes = graphic.getGraphicspointattributes()
        attributes.setGlyphShapeType(Glyph.SHAPE_TYPE_SPHERE)
        # TODO: Update this to depend on point cloud size.
        attributes.setBaseSize([0.02])
        # Make selected Nodes slightly bigger for testing.
        # This can be avoided if we can prevent the selected points from being drawn twice.
        if subgroup_field:
            attributes.setBaseSize([0.03])

        #         surface = scene.createGraphicsSurfaces()
        #         surface.setCoordinateField(finite_element_field)
        scene.endChange()

        return graphic
