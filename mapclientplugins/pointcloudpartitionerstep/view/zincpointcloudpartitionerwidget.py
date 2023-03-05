"""
Created on Jun 18, 2015

@author: tsalemink
"""
from PySide6 import QtCore

from opencmiss.zincwidgets.basesceneviewerwidget import BaseSceneviewerWidget


class ZincPointCloudPartitionerWidget(BaseSceneviewerWidget):
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

    def deleteSelectedNodes(self):
        self._model.removeSelected()
