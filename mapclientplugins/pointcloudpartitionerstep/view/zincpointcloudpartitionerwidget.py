"""
Created: April, 2023

@author: tsalemink
"""
from PySide6 import QtCore

from cmlibs.widgets.basesceneviewerwidget import BaseSceneviewerWidget
from cmlibs.widgets.handlers.sceneselection import SceneSelection


class ZincPointCloudPartitionerWidget(BaseSceneviewerWidget):
    selection_updated = QtCore.Signal()

    def __init__(self, parent=None):
        super(ZincPointCloudPartitionerWidget, self).__init__(parent)
        self._model = None
        self._active_button = QtCore.Qt.MouseButton.NoButton

    def set_model(self, model):
        self._model = model

    def mouse_enter_event(self, event):
        super().mouse_enter_event(event)
        self.setFocus()

    def mouse_release_event(self, event):
        super().mouse_release_event(event)
        if isinstance(self._active_handler, SceneSelection):
            self.selection_updated.emit()
