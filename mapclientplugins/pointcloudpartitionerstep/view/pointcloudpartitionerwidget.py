"""
Created on Jun 18, 2015

@author: tsalemink
"""
from PySide6 import QtGui, QtWidgets, QtCore

from opencmiss.zincwidgets.handlers.scenemanipulation import SceneManipulation
from opencmiss.zincwidgets.handlers.sceneselection import SceneSelection

from mapclientplugins.pointcloudpartitionerstep.view.ui_pointcloudpartitionerwidget import Ui_PointCloudPartitionerWidget
from mapclientplugins.pointcloudpartitionerstep.scene.pointcloudpartitionerscene import PointCloudPartitionerScene

ANGLE_RANGE = 50


class PointCloudPartitionerWidget(QtWidgets.QWidget):
    """
    classdocs
    """

    def __init__(self, model, parent=None):
        """
        Constructor
        """
        super(PointCloudPartitionerWidget, self).__init__(parent)
        self._ui = Ui_PointCloudPartitionerWidget()
        self._ui.setupUi(self)

        self._callback = None

        self._model = model
        self._scene = PointCloudPartitionerScene(model)

        self._ui.widgetZinc.set_context(model.getContext())
        self._ui.widgetZinc.register_handler(SceneManipulation())
        self._ui.widgetZinc.register_handler(SceneSelection(QtCore.Qt.KeyboardModifier.ControlModifier))
        self._ui.widgetZinc.setModel(model)

        # self._ui.widgetZinc.setSelectionfilter(model.getSelectionfilter())

        self._makeConnections()

    def _makeConnections(self):
        self._ui.pushButtonContinue.clicked.connect(self._continueExecution)
        self._ui.pushButtonViewAll.clicked.connect(self._viewAllButtonClicked)
        self._ui.widgetZinc.graphics_initialized.connect(self._zincWidgetReady)
        self._ui.pushButtonDeleteNode.clicked.connect(self._ui.widgetZinc.deleteSelectedNodes)

    def getLandmarks(self):
        return self._model.getLandmarks()

    def load(self, file_location):
        self._model.load(file_location)

    def registerDoneExecution(self, done_exectution):
        self._callback = done_exectution

    def _zincWidgetReady(self):
        self._ui.widgetZinc.set_selectionfilter(self._model.getSelectionfilter())

    def _viewAllButtonClicked(self):
        self._ui.widgetZinc.viewAll()

    def _continueExecution(self):
        self._callback()
