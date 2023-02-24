"""
Created on Jun 18, 2015

@author: tsalemink
"""
from PySide6 import QtGui, QtWidgets

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

        self._ui.widgetZinc.setContext(model.getContext())
        self._ui.widgetZinc.setModel(model.getMarkerModel())
        # self._ui.widgetZinc.setSelectionfilter(model.getSelectionfilter())

        self._makeConnections()

    def _makeConnections(self):
        self._ui.pushButtonContinue.clicked.connect(self._continueExecution)
        self._ui.pushButtonViewAll.clicked.connect(self._viewAllButtonClicked)
        self._ui.widgetZinc.graphicsInitialized.connect(self._zincWidgetReady)
        self._ui.pushButtonDeleteNode.clicked.connect(self._ui.widgetZinc.deleteSelectedNodes)

    def getLandmarks(self):
        return self._model.getLandmarks()

    def load(self, file_location):
        self._model.load(file_location)

    def registerDoneExecution(self, done_exectution):
        self._callback = done_exectution

    def _zincWidgetReady(self):
        self._ui.widgetZinc.setSelectionfilter(self._model.getSelectionfilter())

    def _viewAllButtonClicked(self):
        self._ui.widgetZinc.viewAll()

    def _continueExecution(self):
        self._callback()
