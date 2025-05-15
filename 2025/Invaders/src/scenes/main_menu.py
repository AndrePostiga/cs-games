from pplay.sprite import Sprite
from pplay.window import Window
from helpers.path_helper import asset_path
from scenes.abstract_menu import AbstractMenu
from components.button import Button, MainMenuAction

class MainMenu(AbstractMenu):
    def __init__(self, window: Window) -> None:
        super().__init__(window, [
            Button(MainMenuAction.PLAY, Sprite(asset_path("images", "menu", "button_jogar.png")), self._notify_observers),
            Button(MainMenuAction.DIFFICULTY, Sprite(asset_path("images", "menu", "button_dificuldade.png")), self._notify_observers),
            Button(MainMenuAction.RANKING, Sprite(asset_path("images", "menu", "button_ranking.png")), self._notify_observers),
            Button(MainMenuAction.QUIT, Sprite(asset_path("images", "menu", "button_sair.png")), self._notify_observers)
        ])
        