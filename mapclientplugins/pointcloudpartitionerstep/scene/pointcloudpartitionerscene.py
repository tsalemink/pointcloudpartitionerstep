"""
Created on Jun 22, 2015

@author: tsalemink
"""
from opencmiss.zinc.field import Field
from opencmiss.zinc.glyph import Glyph

from mapclientplugins.pointcloudpartitionerstep.scene.detection import DetectionScene


class PointCloudPartitionerScene(object):
    """
    classdocs
    """

    def __init__(self, model):
        """
        Constructor
        """
        self._model = model
        self._detection_scene = DetectionScene(model.getDetectionModel())
        self._setupVisualisation()

    def _setupVisualisation(self):
        coordinate_field = self._model.getCoordinateField()
        region = self._model.getRegion()
        scene = region.getScene()
        materialmodule = scene.getMaterialmodule()
        red = materialmodule.findMaterialByName('red')
        self._node_graphics = self._createPointGraphics(scene, coordinate_field, red, None)  # self._model.getNodeGroupField())
        # self._selection_graphics = self._createPointGraphics(scene, coordinate_field, yellow, None) # self._model.getSelectionGroupField())

    def _createPointGraphics(self, scene, finite_element_field, material, subgroup_field):
        scene.beginChange()
        # Create a surface graphic and set it's coordinate field to the finite element coordinate field.
        graphic = scene.createGraphicsPoints()
        graphic.setFieldDomainType(Field.DOMAIN_TYPE_NODES)
        graphic.setCoordinateField(finite_element_field)
        graphic.setMaterial(material)
        graphic.setSelectedMaterial(material)
        #         graphic.setSubgroupField(subgroup_field)
        attributes = graphic.getGraphicspointattributes()
        attributes.setGlyphShapeType(Glyph.SHAPE_TYPE_SPHERE)
        attributes.setBaseSize([1.0])
        #         surface = scene.createGraphicsSurfaces()
        #         surface.setCoordinateField(finite_element_field)
        scene.endChange()

        return graphic
