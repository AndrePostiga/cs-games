from pplay.window import Window
from pplay.sprite import Sprite
from helpers.path_helper import asset_path
from core.observer import Observable
from components.button import DifficultyMenuAction, ReturnMenuAction

class EndlessLevel(Observable):
    def __init__(self, window: Window, difficulty: DifficultyMenuAction) -> None:
        super().__init__()
        self.window : Window = window
        self.difficulty : int = difficulty.value
        
        self.ball = Sprite(asset_path("images", "ball.png"))
        self.ball.x = (self.window.width - self.ball.width) / 2
        self.ball.y = (self.window.height - self.ball.height) / 2

    def update(self, delta_time: float) -> None:
        keyboard = self.window.get_keyboard()
        if keyboard.key_pressed("esc"):
            self._notify_observers(ReturnMenuAction.RETURN)

    def draw(self) -> None:
        self.ball.draw()
        