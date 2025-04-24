from enum import Enum
from typing import List
import os
from PPlay.window import *
from PPlay.sprite import Sprite
from typing import List
from .Observer import Observer
from .Subject import Subject

def center_x(window : Window, sprite: Sprite) -> (int, int):
    return (window.width - sprite.width) / 2

def center_y(window : Window, sprite: Sprite) -> (int, int):
    return (window.height - sprite.height) / 2    

def center_x_y(window : Window, sprite: Sprite):
    sprite.set_position(center_x(window, sprite), center_y(window, sprite))

ACT_FLDR=os.path.dirname(os.path.abspath(__file__))

BUTTON_PLAY_PATH = \
    os.path.join(ACT_FLDR, "..", "Assets", "Images", "jogar.png")
BUTTON_DIFICULTY_PATH = \
    os.path.join(ACT_FLDR, "..", "Assets", "Images", "dificuldade.png")
BUTTON_RANKING_PATH = \
    os.path.join(ACT_FLDR, "..", "Assets", "Images", "ranking.png")
BUTTON_EXIT_PATH = \
    os.path.join(ACT_FLDR, "..", "Assets", "Images", "sair.png")

class MenuEnum(Enum):
    PLAY = 1
    RANKING = 2
    EXIT = 3
    DIFICULTY = 4

class Menu(Subject):

    _state: MenuEnum = None
    _observers: List[Observer] = []

    def attach(self, observer: Observer) -> None:
        self._observers.append(observer)

    def detach(self, observer: Observer) -> None:
        self._observers.remove(observer)

    #Trigger an update in each subscriber.    
    def notify(self) -> None:
        for observer in self._observers:
            observer.update(self)

    def __init__(self, game_window : Window):
        self.game_window = game_window
        self.btn_play = Sprite(BUTTON_PLAY_PATH, 1)
        self.btn_dificulty = Sprite(BUTTON_DIFICULTY_PATH, 1)
        self.btn_ranking = Sprite(BUTTON_RANKING_PATH, 1)
        self.btn_exit = Sprite(BUTTON_EXIT_PATH, 1)        

        self.btn_play.set_position(center_x(self.game_window, self.btn_play), 0)
        self.btn_dificulty.set_position(center_x(self.game_window, self.btn_play), self.btn_play.y + self.btn_play.height + 20)
        self.btn_ranking.set_position(center_x(self.game_window, self.btn_play), self.btn_dificulty.y + self.btn_dificulty.height + 20)
        self.btn_exit.set_position(center_x(self.game_window, self.btn_play), self.btn_ranking.y + self.btn_ranking.height + 20)

    def start(self):
        self.loop()

    def check_inputs(self):
        mouse = self.game_window.get_mouse()
        if (mouse.is_over_object(self.btn_play) and mouse.is_button_pressed(1)):
            self._state = MenuEnum.PLAY
            self.notify()

    def draw(self):
        self.game_window.set_background_color((0, 0, 0))
        self.btn_play.draw()
        self.btn_dificulty.draw()
        self.btn_ranking.draw()
        self.btn_exit.draw()

    def update(self):        
        pass

    def loop(self):
        while(True):
            self.check_inputs()
            self.draw()    
            self.game_window.update()