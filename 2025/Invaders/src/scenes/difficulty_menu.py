from pplay.sprite import Sprite
from pplay.window import Window
from helpers.path_helper import asset_path
from scenes.abstract_menu import AbstractMenu
from components.button import Button, DifficultyMenuAction

class DifficultyMenu(AbstractMenu):
    def __init__(self, window: Window) -> None:
        super().__init__(window, [
            Button(DifficultyMenuAction.EASY, Sprite(asset_path("images", "menu", "button_facil.png")), self._notify_observers),
            Button(DifficultyMenuAction.MEDIUM, Sprite(asset_path("images", "menu", "button_medio.png")), self._notify_observers),
            Button(DifficultyMenuAction.HARD, Sprite(asset_path("images", "menu", "button_dificil.png")), self._notify_observers)
        ])