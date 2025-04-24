from PPlay.sprite import *
from PPlay.window import *

class CustomSprite(Sprite):
    def __init__(self, image_file, game_window: Window, frames=1,):
        super().__init__(image_file, frames)
        self.position_x = 0
        self.position_y = 0
        self.width = 0
        self.height = 0
        self.game_window = game_window

    def center(self):
        self.__center_x_y()

    def __get_actual_center(self):
        x = (self.game_window.width - self.width) / 2
        y = (self.game_window.height - self.height) / 2  
        return (x, y)

    def __center_x_y(self):
        (x, y) = self.__get_actual_center()
        self.position_x = x
        self.position_y = y
        self.set_position(self.x, self.y)
