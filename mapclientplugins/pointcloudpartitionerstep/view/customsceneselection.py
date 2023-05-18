"""
Created: May, 2023

@author: tsalemink
"""
from cmlibs.widgets.handlers.sceneselection import SceneSelection
from cmlibs.widgets.definitions import BUTTON_MAP, SelectionMode, GraphicsSelectionMode
from cmlibs.zinc.sceneviewerinput import Sceneviewerinput


MODE_MAP = {
    "Exclusive": SelectionMode.EXCLUSIVE,
    "Additive": SelectionMode.ADDITIVE,
}


TYPE_MAP = {
    "Surfaces": GraphicsSelectionMode.ELEMENTS,
    "Points": GraphicsSelectionMode.NODE,
}


class CustomSceneSelection(SceneSelection):

    def __init__(self, key_code):
        super().__init__(key_code)
        self._selection_mode = SelectionMode.NONE
        self._primary_selection_mode = SelectionMode.EXCLUSIVE

    def set_primary_selection_mode(self, mode):
        self._primary_selection_mode = mode

    def mouse_press_event(self, event):
        super().mouse_press_event(event)

        if BUTTON_MAP[event.button()] == Sceneviewerinput.BUTTON_TYPE_LEFT:
            self._selection_mode = self._primary_selection_mode
