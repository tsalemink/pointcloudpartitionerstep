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
        self.setFocusPolicy(QtCore.Qt.FocusPolicy.ClickFocus)

        self._ui = Ui_PointCloudPartitionerWidget()
        self._ui.setupUi(self)

        self._callback = None

        self._model = model
        self._scene = PointCloudPartitionerScene(model)
        self._field_module = self._model.getRegion().getFieldmodule()

        # TODO: Not sure if these would be best defined here or in the ZincWidget.
        self._label_dict = {}           # Key is CheckBox, value is Label.
        self._point_group_dict = {}     # Key is CheckBox, value is Group.
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
        i = len(self._label_dict) + 1
        while not self.label_is_unique(label + str(i)):
            i += 1
        return label + str(i)

    def label_is_unique(self, label):
        for value in self._label_dict.values():
            if value.get_label().text() == label:
                return False
        return True

    def validate_label(self):
        label = self.sender()
        if label.get_label().text() == label.get_line_edit().text() or self.label_is_unique(label.get_line_edit().text()):
            label.update_text()
        else:
            label.duplicate_warning()

    def check_box_pressed(self):
        if self.sender().isChecked():
            self.sender().group().setExclusive(False)

    def check_box_released(self):
        if self.sender().isChecked():
            self.sender().setChecked(False)
        self.sender().group().setExclusive(True)

    def create_point_group(self):
        name = self.create_unique_label()

        label = EditableLabel(name)
        label.text_updated.connect(self.validate_label)

        check_box = QtWidgets.QCheckBox()
        check_box.setSizePolicy(QtWidgets.QSizePolicy.Policy.Maximum, QtWidgets.QSizePolicy.Policy.Maximum)
        self._button_group.addButton(check_box)
        check_box.setChecked(True)
        check_box.pressed.connect(self.check_box_pressed)
        check_box.released.connect(self.check_box_released)

        group = self._field_module.createFieldGroup()
        group.setName(name)

        horizontal_layout = QtWidgets.QHBoxLayout()
        horizontal_layout.addWidget(check_box)
        horizontal_layout.addWidget(label)
        self._ui.verticalLayout_5.addLayout(horizontal_layout)

        self._label_dict[check_box] = label
        self._point_group_dict[check_box] = group

    # TODO: Implement.
    def add_points_to_group(self):
        pass

    def registerDoneExecution(self, done_exectution):
        self._callback = done_exectution

    def _zincWidgetReady(self):
        self._ui.widgetZinc.set_selectionfilter(self._model.getSelectionfilter())

    def _viewAllButtonClicked(self):
        self._ui.widgetZinc.viewAll()

    def _continueExecution(self):
        self._callback()


class EditableLabel(QtWidgets.QStackedWidget):
    """
    This widget contains a QLabel and a QLineEdit. This widget supports renaming of the QLabel but also ensures that the new label
    text is unique, otherwise we might write two FieldGroups with the same name when it comes to writing the Groups to a file.
    """
    text_updated = QtCore.Signal()

    def __init__(self, text):
        super().__init__()

        self._label = QtWidgets.QLabel(text)
        self._line_edit = CustomLineEdit(text)

        self.addWidget(self._label)
        self.addWidget(self._line_edit)

        self.setFocusPolicy(QtCore.Qt.FocusPolicy.StrongFocus)
        self.setSizePolicy(QtWidgets.QSizePolicy.Policy.Maximum, QtWidgets.QSizePolicy.Policy.Maximum)

        self._line_edit.editingFinished.connect(self.text_updated.emit)

    def get_label(self):
        return self._label

    def get_line_edit(self):
        return self._line_edit

    def mouseDoubleClickEvent(self, event):
        super().mouseDoubleClickEvent(event)
        self.setCurrentWidget(self._line_edit)
        self._line_edit.setFocus()

    def update_text(self):
        self._label.setText(self._line_edit.text())
        self.setCurrentIndex(0)

    # TODO: Give a small "pop-up" message warning that this group name is already in use.
    def duplicate_warning(self):
        print("DUPLICATE...")


class CustomLineEdit(QtWidgets.QLineEdit):
    """
    A Custom QLineEdit that emits the editingFinished signal on focusOutEvent even if there were no changes.
    """
    def focusOutEvent(self, event):
        super().focusOutEvent(event)
        self.editingFinished.emit()
