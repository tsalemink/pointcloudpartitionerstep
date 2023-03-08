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
        materialmodule = scene.getMaterialmodule()
        red = materialmodule.findMaterialByName('red')
        blue = materialmodule.findMaterialByName('blue')
        self._node_graphics = self._createPointGraphics(scene, coordinate_field, red, Graphics.SELECT_MODE_DRAW_SELECTED)
        self._selection_graphics = self._createPointGraphics(scene, coordinate_field, blue, Graphics.SELECT_MODE_DRAW_UNSELECTED)

    def _createPointGraphics(self, scene, finite_element_field, material, mode):
        scene.beginChange()
        # Create a surface graphic and set it's coordinate field to the finite element coordinate field.
        graphic = scene.createGraphicsPoints()
        graphic.setFieldDomainType(Field.DOMAIN_TYPE_NODES)
        graphic.setCoordinateField(finite_element_field)
        # graphic.setMaterial(material)
        # graphic.setSelectedMaterial(material)
        graphic.setSelectMode(mode)
        attributes = graphic.getGraphicspointattributes()
        attributes.setGlyphShapeType(Glyph.SHAPE_TYPE_SPHERE)
        # TODO: Update this to depend on point cloud size.
        attributes.setBaseSize([0.02])
        #         surface = scene.createGraphicsSurfaces()
        #         surface.setCoordinateField(finite_element_field)
        scene.endChange()

        return graphic
