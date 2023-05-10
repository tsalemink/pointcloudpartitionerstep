"""
Created on Jun 22, 2015

@author: tsalemink
"""
from cmlibs.zinc.field import Field
from cmlibs.zinc.glyph import Glyph
from cmlibs.zinc.graphics import Graphics
from cmlibs.zinc.scenecoordinatesystem import SCENECOORDINATESYSTEM_WINDOW_PIXEL_BOTTOM_LEFT

from cmlibs.utils.zinc.field import create_field_finite_element
from cmlibs.utils.zinc.finiteelement import create_nodes


def _set_graphic_point_size(graphic, size):
    attributes = graphic.getGraphicspointattributes()
    attributes.setBaseSize(size)


def _create_text_graphics(scene, coordinate_field):
    scene.beginChange()

    graphics_points = scene.createGraphicsPoints()
    graphics_points.setFieldDomainType(Field.DOMAIN_TYPE_NODES)
    graphics_points.setCoordinateField(coordinate_field)
    graphics_points.setScenecoordinatesystem(SCENECOORDINATESYSTEM_WINDOW_PIXEL_BOTTOM_LEFT)

    scene.endChange()

    return graphics_points


def setup_surface_graphics(region):
    surface_graphics_list = []
    child_region = region.getFirstChild()
    while child_region.isValid():
        mesh = child_region.getFieldmodule().findMeshByDimension(2)
        if mesh.getSize() != 0:
            surface_graphics_list.append(create_surface_graphics(child_region))
        child_region = child_region.getNextSibling()

    return surface_graphics_list


def create_surface_graphics(mesh_region):
    mesh_scene = mesh_region.getScene()
    field_module = mesh_region.getFieldmodule()
    mesh_coordinates = field_module.findFieldByName("coordinates")

    surfaces = mesh_scene.createGraphicsSurfaces()
    surfaces.setRenderPolygonMode(Graphics.RENDER_POLYGON_MODE_SHADED)
    surfaces.setCoordinateField(mesh_coordinates)
    surfaces.setVisibilityFlag(True)

    return surfaces


class PointCloudPartitionerScene(object):

    def __init__(self, model):
        self._model = model
        self._group_graphics_dict = {}
        self._label_graphics = None
        self._surface_graphics_list = None
        self._node_graphics = None
        self._selection_graphics = None
        self._not_field = None
        self._pixel_scale = 1
        self._data_point_base_size = 0.15
        self._setup_label_graphic()

    def setup_visualisation(self):
        if self._node_graphics is None and self._selection_graphics is None:
            region = self._model.get_region()
            scene = region.getScene()
            coordinate_field = self._model.get_coordinate_field()

            self._surface_graphics_list = setup_surface_graphics(region)

            self._node_graphics = self.create_point_graphics(scene, coordinate_field, None, None, Graphics.SELECT_MODE_DRAW_UNSELECTED)
            self._selection_graphics = self.create_point_graphics(scene, coordinate_field, None, None, Graphics.SELECT_MODE_DRAW_SELECTED)

    def _setup_label_graphic(self):
        normalised_region = self._model.get_region().createChild('normalised')
        normalised_scene = normalised_region.getScene()
        field_module = normalised_region.getFieldmodule()
        normalised_coordinate_field = create_field_finite_element(field_module, 'normalised', 2)
        create_nodes(normalised_coordinate_field, [[10.0, 10.0]])
        self._label_graphics = _create_text_graphics(normalised_scene, normalised_coordinate_field)

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
        _set_graphic_point_size(graphic, self._data_point_base_size * self._pixel_scale)

        scene.endChange()

        return graphic

    def update_graphics_name(self, old_name, new_name):
        self._group_graphics_dict[new_name] = self._group_graphics_dict[old_name]
        del self._group_graphics_dict[old_name]

    def delete_point_graphics(self, group_name):
        scene = self._model.get_region().getScene()
        scene.removeGraphics(self._group_graphics_dict[group_name])
        del self._group_graphics_dict[group_name]

    def set_pixel_scale(self, scale):
        self._pixel_scale = scale
        attributes = self._label_graphics.getGraphicspointattributes()
        attributes.setGlyphOffset([2.0 * scale, 0.0])
        font = attributes.getFont()
        font.setPointSize(int(font.getPointSize() * scale + 0.5))

        _set_graphic_point_size(self._node_graphics, self._data_point_base_size * scale)
        _set_graphic_point_size(self._selection_graphics, self._data_point_base_size * scale)
        for graphic in self._group_graphics_dict.values():
            _set_graphic_point_size(graphic, self._data_point_base_size * scale)

    def update_graphics_materials(self, materials):
        for (graphic, material) in zip(self._group_graphics_dict.values(), materials.values()):
            graphic.setMaterial(material)

    def update_label_text(self, handler_label):
        attributes = self._label_graphics.getGraphicspointattributes()
        attributes.setLabelText(1, handler_label)

    def set_node_graphics_subgroup_field(self, field):
        if self._node_graphics is not None:
            if field is not None:
                self._node_graphics.setSubgroupField(field)

    def set_surfaces_visibility(self, state):
        for graphics in self._surface_graphics_list:
            graphics.setVisibilityFlag(state != 0)

    def set_points_visibility(self, state):
        self._node_graphics.setVisibilityFlag(state != 0)
