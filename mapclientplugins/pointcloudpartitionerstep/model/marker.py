"""
Created on Jun 23, 2015

@author: hsorby
"""
from opencmiss.zinc.status import OK
from opencmiss.zinc.field import Field

from mapclientplugins.pointcloudpartitionerstep.utils.zinc import createFiniteElementField


class MarkerModel(object):
    """
    classdocs
    """

    def __init__(self, parent, region):
        """
        Constructor
        """
        self._parent = parent
        self._region = region
        self._setupRegion(region)

    def getNodeLocation(self, node):
        fieldmodule = self._region.getFieldmodule()
        fieldcache = fieldmodule.createFieldcache()
        fieldmodule.beginChange()
        fieldcache.setNode(node)
        result, location = self._coordinate_field.evaluateReal(fieldcache, 3)
        fieldmodule.endChange()

        if result == OK:
            return location

        return None

    def getNodeAngle(self, node):
        fieldmodule = self._region.getFieldmodule()
        fieldcache = fieldmodule.createFieldcache()
        fieldmodule.beginChange()
        fieldcache.setNode(node)
        result, angle = self._angle_field.evaluateReal(fieldcache, 1)
        fieldmodule.endChange()

        if result == OK:
            return angle

        return None

    def getPlaneDescription(self):
        return self._parent.getPlaneDescription()

    def getCoordinateField(self):
        return self._coordinate_field

    def getRegion(self):
        return self._region

    def getLandmarks(self):
        lm = {}
        fieldmodule = self._region.getFieldmodule()
        fieldmodule.beginChange()

        nodeset = fieldmodule.findNodesetByFieldDomainType(Field.DOMAIN_TYPE_NODES)
        ni = nodeset.createNodeiterator()
        node = ni.next()
        locations = {}
        while node.isValid():
            location = self.getNodeLocation(node)
            angle = self.getNodeAngle(node)
            angle_key = str(angle)
            if angle_key not in locations:
                locations[angle_key] = []
            locations[angle_key].append(location)

            lm[str(node.getIdentifier())] = {'pos': location, 'angle': angle}
            node = ni.next()

        fieldmodule.endChange()
        lm['locations'] = locations
        return lm

    def setNodeLocation(self, node, location):
        fieldmodule = self._region.getFieldmodule()
        fieldcache = fieldmodule.createFieldcache()
        fieldmodule.beginChange()
        fieldcache.setNode(node)
        self._coordinate_field.assignReal(fieldcache, location)
        fieldmodule.endChange()

    def setNodeAngle(self, node, angle):
        fieldmodule = self._region.getFieldmodule()
        fieldcache = fieldmodule.createFieldcache()
        fieldmodule.beginChange()
        fieldcache.setNode(node)
        self._angle_field.assignReal(fieldcache, angle)
        fieldmodule.endChange()

    def setSelected(self, node):
        self._selection_group.addNode(node)

    def clearSelected(self):
        self._selection_group_field.clear()

    def removeSelected(self):
        self._selection_group.destroyAllNodes()

    def createNode(self):
        """
        Create a node with the models coordinate field.
        """
        fieldmodule = self._region.getFieldmodule()
        fieldmodule.beginChange()

        nodeset = fieldmodule.findNodesetByFieldDomainType(Field.DOMAIN_TYPE_NODES)
        template = nodeset.createNodetemplate()
        template.defineField(self._coordinate_field)
        template.defineField(self._angle_field)

        scene = self._region.getScene()
        selection_field = scene.getSelectionField()
        if not selection_field.isValid():
            scene.setSelectionField(self._selection_group_field)

        self._selection_group_field.clear()

        node = nodeset.createNode(-1, template)
        self._selection_group.addNode(node)

        fieldmodule.endChange()

        return node

    def getSelectionGroupField(self):
        return self._selection_group_field

    def _setupRegion(self, region):
        self._coordinate_field = createFiniteElementField(region)

        fieldmodule = region.getFieldmodule()
        self._angle_field = fieldmodule.createFieldFiniteElement(1)
        nodeset = fieldmodule.findNodesetByName('nodes')

        # Setup the selection fields
        self._selection_group_field = fieldmodule.createFieldGroup()
        node_group = self._selection_group_field.createFieldNodeGroup(nodeset)
        self._selection_group = node_group.getNodesetGroup()
