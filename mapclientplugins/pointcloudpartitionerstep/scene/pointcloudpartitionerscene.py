"""
Created on Jun 22, 2015

@author: tsalemink
"""
from opencmiss.zinc.field import Field
from opencmiss.zinc.glyph import Glyph
from opencmiss.zinc.graphics import Graphics
from opencmiss.zinc.scenecoordinatesystem import SCENECOORDINATESYSTEM_WINDOW_PIXEL_BOTTOM_LEFT

from mapclientplugins.pointcloudpartitionerstep.utils.zinc import create_finite_element_field, create_nodes


class PointCloudPartitionerScene(object):
    """
    classdocs
    """

    def __init__(self, model):
        """
        Constructor
        """
        self._model = model
        self._group_graphics_dict = {}
        self._label_graphics = None
        self._setup_visualisation()

    def _setup_visualisation(self):
        region = self._model.get_region()
        scene = region.getScene()

        coordinate_field = self._model.get_coordinate_field()
        group = self.create_ungrouped_nodeset_group(coordinate_field)

        self._node_graphics = self.create_point_graphics(scene, coordinate_field, group, None, Graphics.SELECT_MODE_DRAW_SELECTED)
        self._selection_graphics = self.create_point_graphics(scene, coordinate_field, group, None, Graphics.SELECT_MODE_DRAW_UNSELECTED)

        normalised_region = region.createChild('normalised')
        normalised_scene = normalised_region.getScene()
        normalised_coordinate_field = create_finite_element_field(normalised_region, 2)
        create_nodes(normalised_coordinate_field, [[10.0, 10.0]])
        self.create_text_graphics(normalised_scene, normalised_coordinate_field)

    def create_ungrouped_nodeset_group(self, coordinate_field):
        group = self._model.get_region().getFieldmodule().createFieldGroup()
        group.setName("ungrouped")
        field_node_group = group.createFieldNodeGroup(self._model.get_nodes())
        field_node_group.getNodesetGroup().addNodesConditional(coordinate_field)

        return group

    def create_point_graphics(self, scene, finite_element_field, subgroup_field, material, mode=Graphics.SELECT_MODE_DRAW_UNSELECTED):
        scene.beginChange()
        graphic = scene.createGraphicsPoints()
        graphic.setFieldDomainType(Field.DOMAIN_TYPE_NODES)
        graphic.setCoordinateField(finite_element_field)
        graphic.setSelectMode(mode)

        if subgroup_field:
            graphic.setSubgroupField(subgroup_field)
            if material:
                graphic.setMaterial(material)
                self._group_graphics_dict[subgroup_field.getName()] = graphic

        attributes = graphic.getGraphicspointattributes()
        attributes.setGlyphShapeType(Glyph.SHAPE_TYPE_SPHERE)

        # TODO: Update this to depend on point cloud size.
        attributes.setBaseSize([0.02])

        scene.endChange()

        return graphic

    def delete_point_graphics(self, group_name):
        scene = self._model.get_region().getScene()
        scene.removeGraphics(self._group_graphics_dict[group_name])
        del self._group_graphics_dict[group_name]

    def create_text_graphics(self, scene, coordinate_field):
        scene.beginChange()

        graphics_points = scene.createGraphicsPoints()
        graphics_points.setFieldDomainType(Field.DOMAIN_TYPE_NODES)
        graphics_points.setCoordinateField(coordinate_field)
        graphics_points.setScenecoordinatesystem(SCENECOORDINATESYSTEM_WINDOW_PIXEL_BOTTOM_LEFT)

        attributes = graphics_points.getGraphicspointattributes()
        attributes.setGlyphOffset([2.0, 0.0])

        self._label_graphics = graphics_points

        scene.endChange()

    def update_graphics_materials(self, materials):
        for (graphic, material) in zip(self._group_graphics_dict.values(), materials.values()):
            graphic.setMaterial(material)

    def update_label_text(self, handler_label):
        attributes = self._label_graphics.getGraphicspointattributes()
        attributes.setLabelText(1, handler_label)
