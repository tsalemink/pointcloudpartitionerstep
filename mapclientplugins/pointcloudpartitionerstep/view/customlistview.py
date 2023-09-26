from PySide6 import QtWidgets, QtGui


# TODO: Using a delegate may circumvent some of these issues, but would need some serious work...

# TODO: One issue I can see is that the PCPWidget keeps a handle to the QStandardItem so it can delete it later.
#   But this item may have been removed...
#   So, the Delete Group button won't work...?
#   ...
#   We could emit a signal when we move an row...?
#   ...
#   Ideally, we would just keep a handle to the layout as this stays constant...
#   Once the layout has been deleted, perhaps we could check if any of the item widgets are empty and delete those...?
class CustomListView(QtWidgets.QListView):
    """
    ???
    """

    def dropEvent(self, event):
        target_index = self.indexAt(event.pos())
        source_index = self.selectedIndexes()[0]

        source_widget = self.indexWidget(source_index)
        source_layout = source_widget.layout()
        target_widget = QtWidgets.QWidget()
        target_widget.setLayout(source_layout)

        self.model().removeRow(source_index.row())
        self.create_row(target_index.row(), target_widget)

    def create_row(self, index, widget):
        item = QtGui.QStandardItem()
        item.setDropEnabled(False)
        item.setSizeHint(widget.sizeHint())
        self.model().insertRow(index, item)
        self.setIndexWidget(item.index(), widget)
