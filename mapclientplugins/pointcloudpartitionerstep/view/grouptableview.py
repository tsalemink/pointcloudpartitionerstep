from PySide6 import QtCore, QtWidgets


INVALID_STYLE_SHEET = 'background-color: rgba(239, 0, 0, 50)'
DEFAULT_STYLE_SHEET = ''


class GroupItem(object):
    def __init__(self, name):
        self.selected = False
        self.name = name


class GroupTableView(QtWidgets.QTableView):

    def dropEvent(self, event):
        super().dropEvent(event)

        source_index = self.selectedIndexes()[0].row()
        target_index = self.indexAt(event.pos()).row()

        self.model().move_row(source_index, target_index)
        event.accept()


class GroupModel(QtCore.QAbstractTableModel):

    def __init__(self, parent=None):
        super().__init__(parent)

        self.groups = []
        self.selected_group = None

    def flags(self, index):
        if not index.isValid():
            return QtCore.Qt.ItemFlag.ItemIsDropEnabled
        if index.row() < len(self.groups):
            return QtCore.Qt.ItemFlag.ItemIsEnabled | QtCore.Qt.ItemFlag.ItemIsSelectable | QtCore.Qt.ItemFlag.ItemIsDragEnabled
        return QtCore.Qt.ItemFlag.ItemIsEnabled | QtCore.Qt.ItemFlag.ItemIsEditable

    def supportedDropActions(self):
        return QtCore.Qt.DropAction.MoveAction

    def rowCount(self, parent=QtCore.QModelIndex()):
        return len(self.groups)

    def columnCount(self, parent=QtCore.QModelIndex()):
        return 3

    def data(self, index, role=QtCore.Qt.ItemDataRole.DisplayRole):
        item = self.get_group_from_index(index)

        if role == QtCore.Qt.ItemDataRole.DisplayRole:
            if index.column() == 1:
                return item.name

        return None

    def setData(self, index, value, role=QtCore.Qt.ItemDataRole.DisplayRole):
        item = self.get_group_from_index(index)

        if index.column() == 0:
            item.selected = value
            return True
        elif index.column() == 1:
            item.name = value
            return True

        return QtCore.QAbstractTableModel.setData(self, index, value, role)

    def add_group(self, name, row=None):
        if row is None:
            row = self.rowCount()

        names_in_use = _names_in_use(self)
        name = _next_available_name(names_in_use, name)

        group = GroupItem(name)
        self.beginInsertRows(QtCore.QModelIndex(), row, row)
        self.groups.insert(row, group)
        self.endInsertRows()
        self.layoutChanged.emit()

        return name

    def remove_group(self, row=None):
        if row is None:
            if not self.selected_group:
                return None
            row = self.groups.index(self.selected_group)
            name = self.selected_group.name
        else:
            name = self.groups[row].name

        self.beginRemoveRows(QtCore.QModelIndex(), row, row)
        del self.groups[row]
        self.endRemoveRows()
        self.layoutChanged.emit()
        self.selected_group = None

        return name

    def move_row(self, source_row, target_row):
        name = self.remove_group(source_row)
        self.add_group(name, target_row)

    def get_group_from_index(self, index):
        if index:
            return self.groups[index.row()]
        return None


class TableDelegate(QtWidgets.QStyledItemDelegate):
    name_changed = QtCore.Signal(str, str)
    button_clicked = QtCore.Signal(str)

    def __init__(self, parent=None):
        super().__init__(parent)

        self._check_box_group = QtWidgets.QButtonGroup()
        self._check_box_group.setExclusive(True)

    def createEditor(self, parent, option, index):
        model = index.model()
        item = model.get_group_from_index(index)

        if index.column() == 0:
            editor = QtWidgets.QCheckBox(parent)
            editor.setSizePolicy(QtWidgets.QSizePolicy.Policy.Maximum, QtWidgets.QSizePolicy.Policy.Maximum)
            editor.clicked.connect(lambda: self._selection_changed(model, item))
            self._check_box_group.addButton(editor)
        elif index.column() == 1:
            editor = QtWidgets.QLineEdit(parent)
            editor.textEdited.connect(lambda: self._name_changed(model, item))
        elif index.column() == 2:
            editor = QtWidgets.QPushButton("sel.", parent)
            editor.clicked.connect(lambda: self._button_clicked(item))
        else:
            editor = super().createEditor(parent, option, index)
        return editor

    def setEditorData(self, editor, index):
        if index.column() == 0:
            value = index.data(QtCore.Qt.ItemDataRole.CheckStateRole)
            editor.setChecked(value == QtCore.Qt.CheckState.Checked)
        elif index.column() == 1:
            editor.setText(index.data())

        editor.setFocus(QtCore.Qt.FocusReason.OtherFocusReason)

    def setModelData(self, editor, model, index):
        if index.column() == 0:
            value = QtCore.Qt.CheckState.Checked if editor.isChecked() else QtCore.Qt.CheckState.Unchecked
            model.setData(index, value, QtCore.Qt.ItemDataRole.CheckStateRole)
        elif index.column() == 1:
            model.setData(index, editor.text())

    def paint(self, painter, option, index):
        if isinstance(self.parent(), QtWidgets.QAbstractItemView):
            self.parent().openPersistentEditor(index)
        QtWidgets.QStyledItemDelegate.paint(self, painter, option, index)

    def _selection_changed(self, model, item):
        if self._check_box_group.checkedButton():
            model.selected_group = item
        else:
            model.selected_group = None

    def _name_changed(self, model, item):
        new_name = self._validate_line_edit(model, item)
        previous_name = item.name
        item.name = new_name

        self.name_changed.emit(previous_name, new_name)

    def _validate_line_edit(self, model, item):
        index = model.index(model.groups.index(item), 1)
        line_edit = self.parent().indexWidget(index)

        name = line_edit.text()
        names_in_use = _names_in_use(model, item)

        if name in names_in_use:
            name = _next_available_name(names_in_use, name)
            line_edit.setText(name)
            line_edit.setStyleSheet(INVALID_STYLE_SHEET)
            line_edit.setToolTip("Warning: group identifier is a duplicate.")
        else:
            line_edit.setStyleSheet(DEFAULT_STYLE_SHEET)
            line_edit.setToolTip("")

        return name

    def _button_clicked(self, item):
        self.button_clicked.emit(item.name)


def _names_in_use(model, group_item=None):
    names = []
    for row in range(model.rowCount()):
        item = model.get_group_from_index(model.index(row, 1))
        if item is not group_item:
            names.append(item.name)
    return names


def _next_available_name(names_in_use, name=None):
    i = 1
    stem_name = "Group"
    unique_name = f"{stem_name}_1" if name is None else name
    name = stem_name if name is None else name

    while unique_name in names_in_use:
        unique_name = f"{name}_{i}"
        i += 1

    return unique_name
