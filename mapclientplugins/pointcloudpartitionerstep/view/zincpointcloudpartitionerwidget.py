"""
Created on Jun 18, 2015

@author: tsalemink
"""
from PySide6 import QtCore

from cmlibs.widgets.basesceneviewerwidget import BaseSceneviewerWidget


class ZincPointCloudPartitionerWidget(BaseSceneviewerWidget):
    handler_updated = QtCore.Signal()

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
