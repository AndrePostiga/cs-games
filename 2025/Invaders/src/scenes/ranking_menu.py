from pplay.sprite import Sprite
from pplay.window import Window
from helpers.path_helper import asset_path
from scenes.abstract_menu import AbstractMenu
from components.button import Button, RankingMenuAction

class RankingMenu(AbstractMenu):
    def __init__(self, window: Window) -> None:
        super().__init__(window, [
            Button(RankingMenuAction.CLEAR, Sprite(asset_path("images", "menu", "button_limpar.png")), self._notify),
        ])
        