from Scenes.Gameplay import Gameplay
from Scenes.Menu import Menu, MenuEnum
from Scenes.Subject import Subject
from Scenes.Observer import Observer
from PPlay.window import *

# Controla os menus e telas novas
class Game(Observer):

    def update(self, subject: Subject) -> None:
        if subject._state == MenuEnum.PLAY:
            self.actual_scene = Gameplay(self.window)
            self.actual_scene.attach(self)
            
        self.window.set_background_color((0,0,0))
        self.start()

    def __init__(self):
        self.window=Window(1080, 600)
        self.window.set_title("SpaceInvaders")
        self.window.set_background_color((0,0,0))
        self.actual_scene = Menu(self.window)
        self.actual_scene.attach(self)

    def start(self):
        self.actual_scene.start()

