from abc import ABC, abstractmethod
from pplay.window import Window
from typing import List
from components.button import Button, ButtonAction
from core.observer import Observable

class AbstractMenu(Observable, ABC):
    def __init__(self, window: Window, buttons : List[Button]) -> None:
        super().__init__()
        self.buttons : List[Button] = buttons
        self.window = window

    def _space_between(self) -> None:
        window_height = self.window.height
        button_height = self.buttons[0].sprite.height
        total_height = button_height * len(self.buttons)
        
        space_between = (window_height - total_height) / (len(self.buttons) + 1)
        for i, button in enumerate(self.buttons):
            button.y = space_between + i * (button_height + space_between)
            self._center_horizontally(button)

    def _center_horizontally(self, button: Button) -> None:
        button.x = (self.window.width - button.width) / 2

    def update(self, delta_time: float) -> None:
        mouse = self.window.get_mouse()
        for button in self.buttons:
            button.update(mouse)

    def draw(self) -> None:
        self._space_between()
        for button in self.buttons:
            button.draw()
