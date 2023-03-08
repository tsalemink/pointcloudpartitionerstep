"""
Created on Jun 18, 2015

@author: tsalemink
"""
from opencmiss.zinc.context import Context
from opencmiss.zincwidgets.definitions import SELECTION_GROUP_NAME

from mapclientplugins.pointcloudpartitionerstep.utils.zinc import createNodes, createElements, createFiniteElementField


class PointCloudPartitionerModel(object):
    """
    classdocs
    """

    def __init__(self):
        """
        Constructor
        """
        self._location = None
        self._file_location = None
        self._nodes = None
        self._selection_group = None

        self._context = Context("PointCloudPartitioner")
        self._region = self._context.getDefaultRegion()
        self._field_module = self._region.getFieldmodule()
        self._cache = self._field_module.createFieldcache()
        self._coordinate_field = createFiniteElementField(self._region)

        self.defineStandardMaterials()
        self.defineStandardGlyphs()

        self._selection_filter = self._createSelectionFilter()

    def getSelectionfilter(self):
        return self._selection_filter

    def load(self, file_location):
        self._region.readFile(file_location)
        self._nodes = self._field_module.findNodesetByName("nodes")

    def setLocation(self, location):
        self._location = location

    def getContext(self):
        return self._context

    def getCoordinateField(self):
        return self._coordinate_field

    def getRegion(self):
        return self._context.getDefaultRegion()

    def _createMesh(self, nodes, elements):
        """
        Create a mesh from data extracted from a VRML file.
        The nodes are given as a list of coordinates and the elements
        are given as a list of indexes into the node list..
        """
        # First create all the required nodes
        createNodes(self._coordinate_field, self._nodes)
        # then define elements using a list of node indexes
        # createElements(self._coordinate_field, self._elements)
        # Define all faces also
        fieldmodule = self._coordinate_field.getFieldmodule()
        fieldmodule.defineAllFaces()

    def _createSelectionFilter(self):
        m = self._context.getScenefiltermodule()
        # r1 = m.createScenefilterRegion(self._detection_model.getRegion())
        # r2 = m.createScenefilterRegion(self._marker_model.getRegion())
        o = m.createScenefilterOperatorOr()
        # o.appendOperand(r1)
        # o.appendOperand(r2)
        return o

    def defineStandardGlyphs(self):
        """
        Helper method to define the standard glyphs
        """
        glyph_module = self._context.getGlyphmodule()
        glyph_module.defineStandardGlyphs()

    def defineStandardMaterials(self):
        """
        Helper method to define the standard materials.
        """
        material_module = self._context.getMaterialmodule()
        material_module.defineStandardMaterials()


def _makeElementsOneBased(elements_list):
    """
    Take a list of a list of element node indexes and increment the
    node index by one.
    """
    updated_elements = []
    for el in elements_list:
        updated_elements.append([n + 1 for n in el])

    return updated_elements


def _convertToElementList(elements_list):
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


def _calculateExtents(values):
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
