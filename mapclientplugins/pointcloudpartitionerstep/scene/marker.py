"""
Created on Jun 23, 2015

@author: hsorby
"""
from opencmiss.zinc.field import Field
from opencmiss.zinc.glyph import Glyph


class MarkerScene(object):
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
        materialmodule = scene.getMaterialmodule()
        green = materialmodule.findMaterialByName('green')
        self._selection_graphics = _createGraphics(scene, coordinate_field, green, self._model.getSelectionGroupField())


def _createGraphics(scene, finite_element_field, material, subgroup_field):
    scene.beginChange()
    # Create a surface graphic and set it's coordinate field
    # to the finite element coordinate field.
    graphic = scene.createGraphicsPoints()
    graphic.setFieldDomainType(Field.DOMAIN_TYPE_NODES)
    graphic.setCoordinateField(finite_element_field)
    graphic.setMaterial(material)
    #     graphic.setSelectedMaterial(material)
    #     graphic.setSubgroupField(subgroup_field)
    attributes = graphic.getGraphicspointattributes()
    attributes.setGlyphShapeType(Glyph.SHAPE_TYPE_SPHERE)
    attributes.setBaseSize([1.0])
    #         surface = scene.createGraphicsSurfaces()
    #         surface.setCoordinateField(finite_element_field)
    scene.endChange()

    return graphic
