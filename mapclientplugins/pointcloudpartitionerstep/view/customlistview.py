from PySide6 import QtCore, QtGui, QtWidgets


class GroupItem(object):
    def __init__(self, name):
        self.selected = False
        self.name = name


# TODO: Not sure if the delegate or the model should maybe handle unchecking other checkboxes...?
#   Ideally the model...?
# TODO: Implement TABLE model.
#   Make the PCPWidgets Add/Remove methods use this model.
#   Return any required values from the associated methods.
# TODO: Handle label uniqueness and emit a signal when group names are updated.
class GroupModel(QtCore.QAbstractTableModel):

    def __init__(self, parent=None):
        super().__init__(parent)

        self._groups = []
        self._selected_group = None

    def rowCount(self, parent=QtCore.QModelIndex()):
        return len(self._groups)

    def columnCount(self, parent=QtCore.QModelIndex()):
        return 3

    def data(self, index, role=QtCore.Qt.ItemDataRole.DisplayRole):
        item = self._get_group_from_index(index)

        if role == QtCore.Qt.ItemDataRole.DisplayRole:
            if index.column() == 1:
                return item.name

        return None

    def setData(self, index, value, role=QtCore.Qt.ItemDataRole.DisplayRole):
        item = self._get_group_from_index(index)

        if index.column() == 0:
            item.selected = value
            return True
        elif index.column() == 1:
            item.name = value
            return True

        return QtCore.QAbstractTableModel.setData(self, index, value, role)

    def add_group(self, name):
        group = GroupItem(name)
        self._groups.append(group)

    def remove_group(self):
        selected_group = self._selected_group
        self._groups.remove(selected_group)
        self._selected_group = None

        return selected_group.name

    def _get_group_from_index(self, index):
        return self._groups[index.row()]


class TableDelegate(QtWidgets.QStyledItemDelegate):
    button_clicked = QtCore.Signal(str)

    def createEditor(self, parent, option, index):
        if index.column() == 0:
            editor = QtWidgets.QCheckBox(parent)
        elif index.column() == 1:
            editor = QtWidgets.QLineEdit(parent)
        elif index.column() == 2:
            editor = QtWidgets.QPushButton("sel.", parent)
            editor.clicked.connect(lambda: self._button_clicked(index))
        else:
            editor = super().createEditor(parent, option, index)
        return editor

    def setEditorData(self, editor, index):
        if index.column() == 0:
            value = index.data(QtCore.Qt.ItemDataRole.CheckStateRole)
            editor.setChecked(value == QtCore.Qt.CheckState.Checked)
        elif index.column() == 1:
            editor.setText(index.data())

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

    def _button_clicked(self, index):
        name_index = index.model().index(index.row(), 1)
        name = name_index.data(QtCore.Qt.ItemDataRole.EditRole)
        self.button_clicked.emit(name)


#
#
#
#


# TODO: Get rid of this nonsense class.
class CustomListView(QtWidgets.QListView):
    # TODO: Emit signal for the PCPWidget.
    #   It needs to pass the source and target items.
    item_moved = QtCore.Signal(QtGui.QStandardItem, QtGui.QStandardItem)

    def dropEvent(self, event):
        source_index = self.selectedIndexes()[0]
        target_index = self.indexAt(event.pos())

        source_widget = self.indexWidget(source_index)
        source_layout = source_widget.layout()
        target_widget = QtWidgets.QWidget()
        target_widget.setLayout(source_layout)

        self.model().removeRow(source_index.row())
        target_item = self.create_row(target_widget, target_index.row())

        # TODO: Emit signal for the PCPWidget.
        source_item = self.model().itemFromIndex(source_index)
        self.item_moved.emit(source_item, target_item)

    def create_row(self, widget, index=None):
        if index is None:
            index = self.model().rowCount()

        item = QtGui.QStandardItem()
        item.setDropEnabled(False)
        item.setSizeHint(widget.sizeHint())
        self.model().insertRow(index, item)
        self.setIndexWidget(item.index(), widget)

        return item
