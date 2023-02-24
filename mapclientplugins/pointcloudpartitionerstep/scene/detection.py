"""
Created on Jun 22, 2015

@author: hsorby
"""
from opencmiss.zinc.field import Field
from opencmiss.zinc.glyph import Glyph


class DetectionScene(object):
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
        iso_scalar_field = self._model.getIsoScalarField()
        scene = region.getScene()
        material = _createMaterial(scene)
        self._surface_graphic = _createContourGraphics(scene, coordinate_field, iso_scalar_field, material)


#         self._temp_points = _createPointsGraphics(scene, coordinate_field, None)
#         self._temp_lines = _createLinesGraphics(scene, coordinate_field)

def _createMaterial(scene):
    materialmodule = scene.getMaterialmodule()
    material = materialmodule.createMaterial()
    material.setAttributeReal3(material.ATTRIBUTE_AMBIENT, [0.25, 1.0, 0.33])
    material.setAttributeReal3(material.ATTRIBUTE_DIFFUSE, [0.0, 0.4, 0.0])

    return material


def _createContourGraphics(scene, finite_element_field, iso_scalar_field, material):
    scene.beginChange()
    # Create a surface graphic and set it's coordinate field
    # to the finite element coordinate field.
    graphic = scene.createGraphicsContours()
    graphic.setCoordinateField(finite_element_field)
    graphic.setIsoscalarField(iso_scalar_field)
    graphic.setListIsovalues(0.0)

    graphic.setMaterial(material)
    #         graphic.setSelectedMaterial(material)
    #         graphic.setSubgroupField(subgroup_field)
    scene.endChange()

    return graphic


def _createLinesGraphics(scene, finite_element_field):
    scene.beginChange()
    # Create a surface graphic and set it's coordinate field
    # to the finite element coordinate field.
    graphic = scene.createGraphicsLines()
    graphic.setCoordinateField(finite_element_field)
    #         graphic.setMaterial(material)
    #         graphic.setSelectedMaterial(material)
    #         graphic.setSubgroupField(subgroup_field)
    scene.endChange()

    return graphic


def _createPointsGraphics(scene, finite_element_field, label_field):
    scene.beginChange()
    # Create a surface graphic and set it's coordinate field
    # to the finite element coordinate field.
    graphic = scene.createGraphicsPoints()
    graphic.setCoordinateField(finite_element_field)
    graphic.setFieldDomainType(Field.DOMAIN_TYPE_MESH_HIGHEST_DIMENSION)
    graphic.setCoordinateField(finite_element_field)
    #         graphic.setSubgroupField(subgroup_field)
    attributes = graphic.getGraphicspointattributes()
    if label_field is not None:
        attributes.setLabelField(label_field)
    attributes.setGlyphShapeType(Glyph.SHAPE_TYPE_SPHERE)
    attributes.setBaseSize([1.0])
    #         graphic.setMaterial(material)
    #         graphic.setSelectedMaterial(material)
    #         graphic.setSubgroupField(subgroup_field)
    scene.endChange()

    return graphic
