"""
Created on Jun 18, 2015

@author: tsalemink
"""
import os

from opencmiss.zinc.context import Context

from mapclientplugins.pointcloudpartitionerstep.utils.zinc import create_nodes, create_elements, create_finite_element_field


class PointCloudPartitionerModel(object):
    """
    classdocs
    """

    def __init__(self, source_points):
        """
        Constructor
        """
        self._location = None
        self._file_location = None
        self._output_filename = None
        self._nodes = None
        self._selection_group = None

        self._context = Context("PointCloudPartitioner")
        self._region = self._context.getDefaultRegion()
        self._field_module = self._region.getFieldmodule()
        self._cache = self._field_module.createFieldcache()
        self._coordinate_field = create_finite_element_field(self._region, 3)

        self.load(source_points)
        self.define_standard_materials()
        self.define_standard_glyphs()

        self._selection_filter = self._create_selection_filter()

    def get_selection_filter(self):
        return self._selection_filter

    def load(self, file_location):
        self._file_location = file_location
        self._region.readFile(file_location)
        self._nodes = self._field_module.findNodesetByName("nodes")

    def write_model(self):
        temp_location = os.path.join(os.path.split(self._location)[0], "_temp")
        if not os.path.exists(temp_location):
            os.makedirs(temp_location)

        filename = os.path.basename(self._file_location).split('.')[0] + '-grouped.exf'
        self._output_filename = os.path.join(temp_location, filename)
        self._region.writeFile(self._output_filename)

    def get_output_filename(self):
        return self._output_filename

    def set_location(self, location):
        self._location = location

    def get_context(self):
        return self._context

    def get_coordinate_field(self):
        return self._coordinate_field

    def get_region(self):
        return self._context.getDefaultRegion()

    def get_cache(self):
        return self._cache

    def get_nodes(self):
        return self._nodes

    def _create_mesh(self, nodes, elements):
        """
        Create a mesh from data extracted from a VRML file.
        The nodes are given as a list of coordinates and the elements
        are given as a list of indexes into the node list..
        """
        # First create all the required nodes
        create_nodes(self._coordinate_field, nodes)
        # then define elements using a list of node indexes
        create_elements(self._coordinate_field, elements)
        # Define all faces also
        fieldmodule = self._coordinate_field.getFieldmodule()
        fieldmodule.defineAllFaces()

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


def _make_elements_one_based(elements_list):
    """
    Take a list of a list of element node indexes and increment the
    node index by one.
    """
    updated_elements = []
    for el in elements_list:
        updated_elements.append([n + 1 for n in el])

    return updated_elements


def _convert_to_element_list(elements_list):
    """
    Take a list of element node indexes deliminated by -1 and convert
    it into a list element node indexes list.
    """
    elements = []
    current_element = []
    for node_index in elements_list:
        if node_index == -1:
            elements.append(current_element)
            current_element = []
        else:
            # We also add one to the indexes to suit Zinc node indexing
            current_element.append(node_index + 1)

    return elements


def _calculate_extents(values):
    """
    Calculate the maximum and minimum for each coordinate x, y, and z
    Return the max's and min's as:
     [x_min, x_max, y_min, y_max, z_min, z_max]
    """
    x_min = 0
    x_max = 1
    y_min = 0
    y_max = 1
    z_min = 0
    z_max = 2
    if values:
        initial_value = values[0]
        x_min = x_max = initial_value[0]
        y_min = y_max = initial_value[1]
        z_min = z_max = initial_value[2]
        for coord in values:
            x_min = min([coord[0], x_min])
            x_max = max([coord[0], x_max])
            y_min = min([coord[1], y_min])
            y_max = max([coord[1], y_max])
            z_min = min([coord[2], z_min])
            z_max = max([coord[2], z_max])

    return [x_min, x_max, y_min, y_max, z_min, z_max]
