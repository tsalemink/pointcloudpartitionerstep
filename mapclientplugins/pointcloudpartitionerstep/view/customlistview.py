from PySide6 import QtCore, QtGui, QtWidgets


# TODO: This is all FUCKED.

# TODO: I think we're gonna have to use a delegate...

# TODO: OK.
#   What is we create a custom QStandardItem subclass.
#   Give it attributes for each of the widgets it needs...


class CustomListView(QtWidgets.QListView):
    # TODO: Emit signal for the PCPWidget.
    #   It needs to pass the source and target items.
    item_moved = QtCore.Signal(QtGui.QStandardItem, QtGui.QStandardItem)

    # TODO: The cleanup method isn't working...
    #   We might have to try using items instead of layouts and try updating the dict on signal from this method...??????
    #
    # TODO: This isn't working...
    #   When I move and item and then delete one of the OTHER items, the item I had moved gets re-named...?!?!?!?!?!?
    #   So this shit isn't working at all...
    #   ...
    #   WHAT IF I call the base implementation after copying the widget...???
    #   DOESN'T MAKE ANY DIFFERENCE!!!!!!!!!!!!!!!!!!!!!!
    #   ...
    #   I THINK IT'S BECAUSE IT HAS BEEN DELETED, SO IT'S PASSING THE WRONG ITEM THROUGH THE SIGNAL...
    #   SO, either we need to pass it AFTER creating the new item but BEFORE deleting the old one...
    #   OR, we just pass the new item through the signal and determine which item to replace based on which one is invalid/missing...
    #       Not quite sure how we would do this but that's OK... :)
    def dropEvent(self, event):
        source_index = self.selectedIndexes()[0]
        target_index = self.indexAt(event.pos())

        source_widget = self.indexWidget(source_index)
        source_layout = source_widget.layout()
        target_widget = QtWidgets.QWidget()
        target_widget.setLayout(source_layout)

        # # TODO: Call the base implementation...
        # super().dropEvent(event)
        # # TODO: Paste the widget into the new row...!!!
        # target_item = self.model().itemFromIndex(target_index)
        # self.setIndexWidget(target_index, target_widget)

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
