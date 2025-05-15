from pplay.sprite import Sprite
from pplay.mouse import Mouse
from typing import Callable
from enum import Enum, auto
from typing import Union

class MainMenuAction(Enum):
    PLAY = auto()
    DIFFICULTY = auto()
    RANKING = auto()
    QUIT = auto()

class DifficultyMenuAction(Enum):
    EASY = 1
    MEDIUM = 2
    HARD = 3

class RankingMenuAction(Enum):
    CLEAR = auto()

class ReturnMenuAction(Enum):
    RETURN = auto()

ButtonAction = Union[MainMenuAction, DifficultyMenuAction, RankingMenuAction]

class Button:
    def __init__(self, action: ButtonAction, sprite: Sprite, callback: Callable[[ButtonAction], None]) -> None:
        self.sprite = sprite
        self.action = action
        self.callback = callback

    @property
    def x(self) -> float:
        return self.sprite.x
    @x.setter
    def x(self, value: float) -> None:
        self.sprite.x = value

    @property
    def y(self) -> float:
        return self.sprite.y
    @y.setter
    def y(self, value: float) -> None:
        self.sprite.y = value

    @property
    def width(self) -> float:
        return self.sprite.width
    
    @property
    def height(self) -> float:
        return self.sprite.height

    def _is_clicked(self, mouse: Mouse) -> bool:
        is_over = mouse.is_over_object(self.sprite)
        is_pressed = mouse.is_button_pressed(1)
        clicked = False

        if is_over and is_pressed and not self._was_pressed:
            clicked = True

        self._was_pressed = is_pressed
        return clicked 
       
    def _on_click(self) -> None:
        self.callback(self.action)

    def update(self, mouse: Mouse) -> None:
        if self._is_clicked(mouse):
            self._on_click()

    def draw(self) -> None:
        self.sprite.draw()