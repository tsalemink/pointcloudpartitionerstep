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
        self._field_module = self._model.getRegion().getFieldmodule()

        self._point_group_dict = {}     # Key is label, value is Group.
        self._check_box_dict = {}       # Key is label, value is Button.
        self._button_group = QtWidgets.QButtonGroup()

        self._ui.widgetZinc.set_context(model.getContext())
        self._ui.widgetZinc.register_handler(SceneManipulation())
        self._ui.widgetZinc.register_handler(SceneSelection(QtCore.Qt.Key.Key_S))
        self._ui.widgetZinc.setModel(model)

        # self._ui.widgetZinc.setSelectionfilter(model.getSelectionfilter())

        self._makeConnections()

    def _makeConnections(self):
        self._ui.pushButtonContinue.clicked.connect(self._continueExecution)
        self._ui.pushButtonViewAll.clicked.connect(self._viewAllButtonClicked)
        self._ui.widgetZinc.graphics_initialized.connect(self._zincWidgetReady)
        self._ui.pushButtonCreateGroup.clicked.connect(self.create_point_group)
        self._ui.pushButtonAddToGroup.clicked.connect(self.add_points_to_group)

    def getLandmarks(self):
        return self._model.getLandmarks()

    def load(self, file_location):
        self._model.load(file_location)

    def create_unique_label(self):
        label = "Group_"
        i = len(self._point_group_dict) + 1
        while not self.label_is_unique(label + str(i)):
            i += 1
        return label + str(i)

    def label_is_unique(self, label):
        for key in self._point_group_dict.keys():
            if key == label:
                return False
        return True

    def create_point_group(self):
        name = self.create_unique_label()

        label = QtWidgets.QLabel(name)
        label.setTextInteractionFlags(QtCore.Qt.TextInteractionFlag.TextSelectableByMouse | QtCore.Qt.TextInteractionFlag.TextEditable)

        check_box = QtWidgets.QCheckBox()
        check_box.setSizePolicy(QtWidgets.QSizePolicy.Policy.Maximum, QtWidgets.QSizePolicy.Policy.Maximum)
        self._button_group.addButton(check_box)
        check_box.setChecked(True)

        group = self._field_module.createFieldGroup()
        group.setName(name)

        horizontal_layout = QtWidgets.QHBoxLayout()
        horizontal_layout.addWidget(check_box)
        horizontal_layout.addWidget(label)
        self._ui.verticalLayout_5.addLayout(horizontal_layout)

        self._check_box_dict[label.text()] = check_box
        self._point_group_dict[label.text()] = group

    # TODO: Implement.
    def add_points_to_group(self):
        pass

    # TODO: Create a pop-up if the label-text is not unique.
    def change_group_name(self):
        pass

    def registerDoneExecution(self, done_exectution):
        self._callback = done_exectution

    def _zincWidgetReady(self):
        self._ui.widgetZinc.set_selectionfilter(self._model.getSelectionfilter())

    def _viewAllButtonClicked(self):
        self._ui.widgetZinc.viewAll()

    def _continueExecution(self):
        self._callback()
