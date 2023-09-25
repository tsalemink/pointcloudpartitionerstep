"""
Created: April, 2023

@author: tsalemink
"""
from PySide6 import QtCore

from cmlibs.widgets.basesceneviewerwidget import BaseSceneviewerWidget
from cmlibs.widgets.handlers.sceneselection import SceneSelection


class ZincPointCloudPartitionerWidget(BaseSceneviewerWidget):
    handler_updated = QtCore.Signal()
    selection_updated = QtCore.Signal()

    def __init__(self, parent=None):
        super(ZincPointCloudPartitionerWidget, self).__init__(parent)
        self._model = None
        self._active_button = QtCore.Qt.MouseButton.NoButton

    def set_model(self, model):
        self._model = model

    def get_active_handler(self):
        return self._active_handler

    def register_handler(self, handler):
        super().register_handler(handler)
        self.handler_updated.emit()

    def _activate_handler(self, handler):
        super()._activate_handler(handler)
        self.handler_updated.emit()

    def mouse_enter_event(self, event):
        super().mouse_enter_event(event)
        self.setFocus()

    def mouse_release_event(self, event):
        if isinstance(self.get_active_handler(), SceneSelection):
            super().mouse_release_event(event)
            self.selection_updated.emit()
