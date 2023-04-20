"""
Created on Jun 22, 2015

@author: tsalemink
"""
from cmlibs.zinc.field import Field
from cmlibs.zinc.glyph import Glyph
from cmlibs.zinc.graphics import Graphics
from cmlibs.zinc.scenecoordinatesystem import SCENECOORDINATESYSTEM_WINDOW_PIXEL_BOTTOM_LEFT

from mapclientplugins.pointcloudpartitionerstep.utils.zinc import create_finite_element_field, create_nodes


def _update_point_graphic_size(graphic, size):
    attributes = graphic.getGraphicspointattributes()
    attributes.setBaseSize(size)


class PointCloudPartitionerScene(object):

    def __init__(self, model):
        self._model = model
        self._group_graphics_dict = {}
        self._label_graphics = None
        self._setup_visualisation()

    def _setup_visualisation(self):
        region = self._model.get_region()
        scene = region.getScene()

        coordinate_field = self._model.get_coordinate_field()
        self._node_graphics = self.create_point_graphics(scene, coordinate_field, None, None, Graphics.SELECT_MODE_DRAW_SELECTED)
        self._selection_graphics = self.create_point_graphics(scene, coordinate_field, None, None, Graphics.SELECT_MODE_DRAW_UNSELECTED)

        normalised_region = region.createChild('normalised')
        normalised_scene = normalised_region.getScene()
        normalised_coordinate_field = create_finite_element_field(normalised_region, 2)
        create_nodes(normalised_coordinate_field, [[10.0, 10.0]])
        self.create_text_graphics(normalised_scene, normalised_coordinate_field)

    def create_point_graphics(self, scene, finite_element_field, subgroup_field, material, mode=Graphics.SELECT_MODE_DRAW_UNSELECTED):
        scene.beginChange()
        graphic = scene.createGraphicsPoints()
        graphic.setFieldDomainType(Field.DOMAIN_TYPE_NODES)
        graphic.setCoordinateField(finite_element_field)
        graphic.setSelectMode(mode)

        if subgroup_field:
            graphic.setSubgroupField(subgroup_field)
            graphic.setMaterial(material)
            self._group_graphics_dict[subgroup_field.getName()] = graphic

        attributes = graphic.getGraphicspointattributes()
        attributes.setGlyphShapeType(Glyph.SHAPE_TYPE_SPHERE)

        # TODO: Update this to depend on point cloud size.
        attributes.setBaseSize([0.02])
        # Temporarily increase size of grouped Nodes.
        if subgroup_field:
            attributes.setBaseSize([0.3])

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

        self._label_graphics = graphics_points

        scene.endChange()

    def set_pixel_scale(self, scale):
        attributes = self._label_graphics.getGraphicspointattributes()
        attributes.setGlyphOffset([2.0 * scale, 0.0])
        font = attributes.getFont()
        font.setPointSize(int(font.getPointSize() * scale + 0.5))
        data_point_base_size = 0.05
        _update_point_graphic_size(self._node_graphics, data_point_base_size * scale)
        _update_point_graphic_size(self._selection_graphics, data_point_base_size * scale * 1.05)

    def update_graphics_materials(self, materials):
        for (graphic, material) in zip(self._group_graphics_dict.values(), materials.values()):
            graphic.setMaterial(material)

    def update_label_text(self, handler_label):
        attributes = self._label_graphics.getGraphicspointattributes()
        attributes.setLabelText(1, handler_label)
