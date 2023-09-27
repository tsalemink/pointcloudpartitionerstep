from PySide6 import QtWidgets, QtGui


class CustomListView(QtWidgets.QListView):

    # TODO: The cleanup method isn't working...
    #   We might have to try using items instead of layouts and try updating the dict on signal from this method...??????
    def dropEvent(self, event):
        target_index = self.indexAt(event.pos())
        source_index = self.selectedIndexes()[0]

        source_widget = self.indexWidget(source_index)
        source_layout = source_widget.layout()
        target_widget = QtWidgets.QWidget()
        target_widget.setLayout(source_layout)

        self.model().removeRow(source_index.row())
        self.create_row(target_widget, target_index.row())

    def create_row(self, widget, index=None):
        if index is None:
            index = self.model().rowCount()

        item = QtGui.QStandardItem()
        item.setDropEnabled(False)
        item.setSizeHint(widget.sizeHint())
        self.model().insertRow(index, item)
        self.setIndexWidget(item.index(), widget)

    # TODO: ???
    def cleanup_items(self):
        for row in range(self.model().rowCount()):
            index = self.model().index(row, 0)

            # TODO: REMOVE:
            # print(f"Row: {row}")
            # print(f"Index: {index}")
            print(f"Layout: {self.indexWidget(index).layout()}")
            print(f"Size: {self.indexWidget(index).layout().count()}")

            # Check if the container widget's layout is empty (no child widgets)
            if not self.indexWidget(index).layout():

                # TODO: REMOVE:
                print("Removing...")

                self.model().removeRow(row)
                # Decrement row to account for the removed item
                row -= 1
