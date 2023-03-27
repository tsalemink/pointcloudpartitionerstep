"""
Created on Jun 18, 2015

@author: tsalemink
"""
import colorsys

from PySide6 import QtWidgets, QtCore

from opencmiss.zinc.material import Material
from opencmiss.zincwidgets.handlers.scenemanipulation import SceneManipulation
from opencmiss.zincwidgets.handlers.sceneselection import SceneSelection
from opencmiss.zincwidgets.definitions import SELECTION_GROUP_NAME

from mapclientplugins.pointcloudpartitionerstep.view.ui_pointcloudpartitionerwidget import Ui_PointCloudPartitionerWidget
from mapclientplugins.pointcloudpartitionerstep.scene.pointcloudpartitionerscene import PointCloudPartitionerScene

INVALID_STYLE_SHEET = 'background-color: rgba(239, 0, 0, 50)'
DEFAULT_STYLE_SHEET = ''


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
        self._field_module = self._model.get_region().getFieldmodule()

        self._check_box_dict = {}       # Key is LineEdit, value is CheckBox.
        self._point_group_dict = {}     # Key is CheckBox, value is Group.
        self._rgb_dict = {}             # Key is CheckBox, value is RGB-Value.
        self._button_group = QtWidgets.QButtonGroup()

        self._make_connections()

        self._ui.widgetZinc.set_context(model.get_context())
        self._ui.widgetZinc.register_handler(SceneManipulation())
        self._ui.widgetZinc.register_handler(SceneSelection(QtCore.Qt.Key.Key_S))
        self._ui.widgetZinc.set_model(model)

        # self._ui.widgetZinc.setSelectionfilter(model.get_selection_filter())

    def _make_connections(self):
        self._ui.pushButtonContinue.clicked.connect(self._continue_execution)
        self._ui.pushButtonViewAll.clicked.connect(self._view_all_button_clicked)
        self._ui.widgetZinc.graphics_initialized.connect(self._zinc_widget_ready)
        self._ui.pushButtonCreateGroup.clicked.connect(self.create_point_group)
        self._ui.pushButtonAddToGroup.clicked.connect(self.add_points_to_group)
        self._ui.pushButtonRemoveFromGroup.clicked.connect(self.remove_points_from_group)
        self._ui.widgetZinc.handler_updated.connect(self.update_label_text)

    def load(self, file_location):
        self._model.load(file_location)

    def create_unique_line_edit(self):
        i = len(self._check_box_dict) + 1
        line_edit = QtWidgets.QLineEdit("Group_" + str(i))
        while not self.line_edit_is_unique(line_edit):
            i += 1
            line_edit.setText("Group_" + str(i))
        return line_edit

    def line_edit_is_unique(self, line_edit):
        for value in self._check_box_dict.keys():
            if value.text() == line_edit.text() and value is not line_edit:
                return False
        return True

    def validate_line_edit(self):
        line_edit = self.sender()
        if self.line_edit_is_unique(line_edit):
            line_edit.setStyleSheet(DEFAULT_STYLE_SHEET)
            line_edit.setToolTip("")
        else:
            line_edit.setStyleSheet(INVALID_STYLE_SHEET)
            line_edit.setToolTip("Warning: group identifier is a duplicate.")

    def check_box_pressed(self):
        if self.sender().isChecked():
            self.sender().group().setExclusive(False)

    def check_box_released(self):
        if self.sender().isChecked():
            self.sender().setChecked(False)
        self.sender().group().setExclusive(True)

    def create_point_group(self):
        line_edit = self.create_unique_line_edit()
        line_edit.editingFinished.connect(self.validate_line_edit)

        check_box = QtWidgets.QCheckBox()
        check_box.setSizePolicy(QtWidgets.QSizePolicy.Policy.Maximum, QtWidgets.QSizePolicy.Policy.Maximum)
        check_box.setChecked(True)
        check_box.pressed.connect(self.check_box_pressed)
        check_box.released.connect(self.check_box_released)
        self._button_group.addButton(check_box)

        group = self._field_module.createFieldGroup()

        horizontal_layout = QtWidgets.QHBoxLayout()
        horizontal_layout.addWidget(check_box)
        horizontal_layout.addWidget(line_edit)
        self._ui.verticalLayout_5.addLayout(horizontal_layout)

        self._check_box_dict[line_edit] = check_box
        self._point_group_dict[check_box] = group
        self._rgb_dict[check_box] = None
        self._update_color_map()
        self._scene.update_graphics_materials(self._rgb_dict)
        material = self._rgb_dict[check_box]
        self._scene.create_point_graphics(self._model.get_region().getScene(), self._model.get_coordinate_field(), group, material)

    def _update_color_map(self):
        def get_distinct_colors(n):
            hue_partition = 1.0 / (n + 1)
            return [list(colorsys.hsv_to_rgb(hue_partition * value, 1.0, 1.0)) for value in range(0, n)]

        material_module = self._model.get_region().getScene().getMaterialmodule()
        colors = get_distinct_colors(len(self._rgb_dict) + 1)
        colors.pop(0)
        for i in range(len(colors)):
            material = material_module.createMaterial()
            material.setManaged(True)
            material.setAttributeReal3(Material.ATTRIBUTE_AMBIENT, colors[i])
            material.setAttributeReal3(Material.ATTRIBUTE_DIFFUSE, colors[i])
            material.setAttributeReal3(Material.ATTRIBUTE_SPECULAR, [0.1, 0.1, 0.1])
            self._rgb_dict[list(self._rgb_dict.keys())[i]] = material

    def add_points_to_group(self):
        selection_field = self._field_module.findFieldByName(SELECTION_GROUP_NAME).castGroup()
        selected_nodeset_group = self._get_selected_nodeset_group()
        nodeset_group = self._get_checked_nodeset_group()
        if not nodeset_group:
            return

        # Add the selected Nodes to the chosen Group.
        node_iter = selected_nodeset_group.createNodeiterator()
        node = node_iter.next()
        while node.isValid():
            nodeset_group.addNode(node)
            node = node_iter.next()
        selection_field.clear()

    def remove_points_from_group(self):
        selection_field = self._field_module.findFieldByName(SELECTION_GROUP_NAME).castGroup()
        selected_nodeset_group = self._get_selected_nodeset_group()
        nodeset_group = self._get_checked_nodeset_group()
        if not nodeset_group:
            return

        # Remove the selected Nodes from the chosen group.
        node_iter = selected_nodeset_group.createNodeiterator()
        node = node_iter.next()
        while node.isValid():
            nodeset_group.removeNode(node)
            node = node_iter.next()
        selection_field.clear()

    def _get_selected_nodeset_group(self):
        # Get the NodeSetGroup corresponding with the selected Nodes.
        selection_field = self._field_module.findFieldByName(SELECTION_GROUP_NAME).castGroup()
        selection_field_node_group = selection_field.getFieldNodeGroup(self._model.get_nodes())
        return selection_field_node_group.getNodesetGroup()

    def _get_checked_nodeset_group(self):
        checked_button = self._button_group.checkedButton()

        if len(self._point_group_dict) == 0:
            QtWidgets.QMessageBox.information(self, 'No Point Group Created', 'No point group created. Please create a point group first '
                                              'before attempting to add points.', QtWidgets.QMessageBox.StandardButton.Ok)
            return None
        elif not checked_button:
            dlg = GroupSelectionDialog(self, self._check_box_dict.keys())
            if dlg.exec_():
                checked_button = self._check_box_dict[dlg.get_line_edit()]
            else:
                return None

        # Get the NodeSetGroup corresponding with the chosen FieldGroup.
        checked_group = self._point_group_dict[checked_button]
        field_node_group = checked_group.getFieldNodeGroup(self._model.get_nodes())
        if not field_node_group.isValid():
            field_node_group = checked_group.createFieldNodeGroup(self._model.get_nodes())
        return field_node_group.getNodesetGroup()

    def update_label_text(self):
        handler_label_map = {SceneManipulation: "Mode: View", SceneSelection: "Mode: Selection"}
        handler_label = handler_label_map[type(self._ui.widgetZinc.get_active_handler())]
        self._scene.update_label_text(handler_label)

    def register_done_execution(self, done_exectution):
        self._callback = done_exectution

    def _zinc_widget_ready(self):
        self._ui.widgetZinc.set_selectionfilter(self._model.get_selection_filter())

    def _view_all_button_clicked(self):
        self._ui.widgetZinc.viewAll()

    def _continue_execution(self):
        self._remove_ui_region()
        self._clear_selection_group()
        self._model.write_model()
        self._callback()

    def _remove_ui_region(self):
        self._model.get_region().removeChild(self._model.get_region().findChildByName('normalised'))

    def _clear_selection_group(self):
        selection_field = self._field_module.findFieldByName(SELECTION_GROUP_NAME).castGroup()
        selection_field.clear()
        selection_field.setManaged(False)


class GroupSelectionDialog(QtWidgets.QDialog):
    def __init__(self, parent, line_edits):
        super().__init__(parent)

        self.setMinimumSize(300, 200)
        self.setWindowTitle("Select Point Group")

        buttons = QtWidgets.QDialogButtonBox.StandardButton.Ok | QtWidgets.QDialogButtonBox.StandardButton.Cancel
        self.button_box = QtWidgets.QDialogButtonBox(buttons)
        self.button_box.button(QtWidgets.QDialogButtonBox.StandardButton.Ok).setEnabled(False)
        self.button_box.accepted.connect(self.accept)
        self.button_box.rejected.connect(self.reject)

        self.layout = QtWidgets.QVBoxLayout()
        self.button_group = QtWidgets.QButtonGroup()
        self.button_group.buttonClicked.connect(self._enable_button)

        message = QtWidgets.QLabel("Choose the group that you wish to add the selected points to:")
        self.layout.addWidget(message)

        self.line_edit_dict = {}
        for line_edit in line_edits:
            text = line_edit.text()
            check_box = QtWidgets.QCheckBox(text)
            self.button_group.addButton(check_box)
            self.layout.addWidget(check_box)
            self.line_edit_dict[text] = line_edit

        self.layout.addStretch()
        self.layout.addWidget(self.button_box)
        self.setLayout(self.layout)

    def _enable_button(self):
        self.button_box.button(QtWidgets.QDialogButtonBox.StandardButton.Ok).setEnabled(True)

    def get_line_edit(self):
        return self.line_edit_dict[self.button_group.checkedButton().text()]
