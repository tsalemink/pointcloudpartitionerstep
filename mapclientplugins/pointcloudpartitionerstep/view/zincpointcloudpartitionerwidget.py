"""
Created on Jun 18, 2015

@author: tsalemink
"""
from PySide6 import QtCore

from opencmiss.zincwidgets.sceneviewerwidget import SceneviewerWidget


class ZincPointCloudPartitionerWidget(SceneviewerWidget):
    """
    classdocs
    """

    def __init__(self, parent=None):
        """
        Constructor
        """
        super(ZincPointCloudPartitionerWidget, self).__init__(parent)
        self._model = None
        self._active_button = QtCore.Qt.MouseButton.NoButton
        self._plane_angle = None
        self._active_plane = None
        self._active_node = None

    def setModel(self, model):
        self._model = model

    def setPlaneAngle(self, value):
        self._plane_angle = value

    def deleteSelectedNodes(self):
        self._model.removeSelected()

    def mousePressEvent(self, event):
        if self._active_button != QtCore.Qt.MouseButton.NoButton:
            return

        self._active_button = event.button()

        self._handle_mouse_events = False
        self._active_plane = None
        self._active_node = None
        # if (event.modifiers() & QtCore.Qt.Modifier.CTRL) and event.button() == QtCore.Qt.MouseButton.LeftButton:
        if (event.modifiers() & QtCore.Qt.KeyboardModifier.ControlModifier) and event.button() == QtCore.Qt.MouseButton.LeftButton:
            node_graphic = self.getNearestGraphicsNode(event.x(), event.y())
            nearest_graphics = self.getNearestGraphics()
            if node_graphic is None and nearest_graphics.isValid():
                point_on_plane = self._calculatePointOnPlane(event.x(), event.y())
                if point_on_plane is not None:
                    self._model.clearSelected()
                    node = self._model.createNode()
                    self._model.setNodeLocation(node, point_on_plane)
                    self._model.setNodeAngle(node, self._plane_angle)
                    self._active_node = node
            elif node_graphic is not None and node_graphic == nearest_graphics:
                self._model.clearSelected()
                node = self.getNearestNode(event.x(), event.y())
                self._model.setSelected(node)
                self._model.setNodeAngle(node, self._plane_angle)
                self._active_node = node
                self._active_plane = 'pending'
        else:
            super(ZincPointCloudPartitionerWidget, self).mousePressEvent(event)

    def mouseMoveEvent(self, event):
        if self._active_node is not None:
            point_on_plane = self._calculatePointOnPlane(event.x(), event.y())
            if point_on_plane is not None:
                #                 node_model = self._model.getNodeModel()
                self._model.setNodeLocation(self._active_node, point_on_plane)
        else:
            super(ZincPointCloudPartitionerWidget, self).mouseMoveEvent(event)

    def mouseReleaseEvent(self, event):
        if self._active_button != event.button():
            return

        if self._active_node is not None:
            self._active_plane = None
            self._active_node = None
        else:
            super(ZincPointCloudPartitionerWidget, self).mouseReleaseEvent(event)

        self._active_button = QtCore.Qt.MouseButton.NoButton
