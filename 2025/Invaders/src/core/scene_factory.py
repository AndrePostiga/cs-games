from scenes.endless_level import EndlessLevel
from scenes.main_menu import MainMenu
from scenes.difficulty_menu import DifficultyMenu
from scenes.ranking_menu import RankingMenu
from components.button import MainMenuAction, DifficultyMenuAction, RankingMenuAction, ButtonAction, ReturnMenuAction
from core.scenes_enum import ScenesEnum 
from pplay.window import Window
import pygame

class SceneFactory:
    def __init__(self):
        self._scene = {
            ScenesEnum.MAIN_MENU: MainMenu,
            ScenesEnum.DIFFICULTY_MENU: DifficultyMenu,
            ScenesEnum.RANKING_MENU: RankingMenu,
            ScenesEnum.ENDLESS_LEVEL: EndlessLevel,
        }

    def create_scene(self, action: ButtonAction, window: Window) -> object:
        if action == MainMenuAction.PLAY:
            return self._scene[ScenesEnum.ENDLESS_LEVEL](window, DifficultyMenuAction.EASY)
        elif action == ReturnMenuAction.RETURN:
            return self._scene[ScenesEnum.MAIN_MENU](window)
        elif action == MainMenuAction.DIFFICULTY:
            return self._scene[ScenesEnum.DIFFICULTY_MENU](window)
        elif action == MainMenuAction.RANKING:
            #return self._scene[ScenesEnum.RANKING_MENU](window)
            return None
        elif action == MainMenuAction.QUIT:
            pygame.quit()
            exit()
        elif action == DifficultyMenuAction.EASY or DifficultyMenuAction.MEDIUM or DifficultyMenuAction.HARD:
            return self._scene[ScenesEnum.ENDLESS_LEVEL](window, action)
        else:
            raise ValueError(f"Unknown scene type: {action}")