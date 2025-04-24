from PPlay.window import *
from PPlay.sprite import Sprite
from .Observer import Observer
from .Subject import Subject
from typing import List
import os

def colide_y_up(window : Window, sprite: Sprite) -> bool:  
    return sprite.y <= 0

def colide_x_right(window : Window, sprite: Sprite) -> bool:  
    return (window.width - sprite.width) - sprite.x <= 0

def colide_x_left(window : Window, sprite: Sprite) -> bool:  
    return sprite.x <= 0

def center_x(window : Window, sprite: Sprite) -> (int, int):
    return (window.width - sprite.width) / 2

def center_y(window : Window, sprite: Sprite) -> (int, int):
    return (window.height - sprite.height) / 2    

def center_x_y(window : Window, sprite: Sprite):
    sprite.set_position(center_x(window, sprite), center_y(window, sprite))

ACT_FLDR=os.path.dirname(os.path.abspath(__file__))    

class Gameplay(Subject):

    _state: int = None
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
        self.timer = 0
        self.shots : List[Sprite] = []
        self.shot_speed = 50
        self.ship_speed = 500
        self.ship = Sprite(os.path.join(ACT_FLDR, "..", "Assets", "Images", "ship.png"), 1)
        self.ship.set_position(center_x(self.game_window, self.ship), self.game_window.height - self.ship.height)

    def start(self):        
        self.loop()

    def check_inputs(self):
        keyboard = self.game_window.get_keyboard()

        # Movimentação
        if keyboard.key_pressed('LEFT'):
            self.ship.move_x(-1 * self.ship_speed * self.game_window.delta_time())
        elif keyboard.key_pressed('RIGHT'):
            self.ship.move_x(self.ship_speed * self.game_window.delta_time())

        # Patinação
        if colide_x_left(self.game_window, self.ship):
            self.ship.x = 0
        elif colide_x_right(self.game_window, self.ship):
            self.ship.x = self.game_window.width - self.ship.width

        # Tiros
        if keyboard.key_pressed('SPACE') and self.timer > 2:
            self.timer = 0
            shot = Sprite(os.path.join(ACT_FLDR, "..", "Assets", "Images", "shot.png"), 1)
            shot.set_position(self.ship.x, self.ship.y - self.ship.height - 5)
            self.shots.append(shot)


    def update_game_objects(self):
        self.timer += self.game_window.delta_time()
        print(self.shots)
        for shot in self.shots:            
            shot.move_y(-1 * self.shot_speed * self.game_window.delta_time())
            if colide_y_up(self.game_window, shot):
                self.shots.remove(shot)

    def draw(self):    
        self.game_window.set_background_color((0, 0, 0))
        self.ship.draw()
        for shot in self.shots:
            shot.draw()

    def loop(self):
        while(True):
            self.check_inputs()
            self.update_game_objects()
            self.draw()
            self.game_window.update()