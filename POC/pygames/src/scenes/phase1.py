from entities.ball import Ball
from entities.pad import Pad
from core.player_controller import PlayerController
from core.ia_controller import AIController
from pplay.window import Window
from core.physics import PhysicsSystem
from helper.positions import get_left_x, get_right_x, get_center_y

class Phase1:
    def __init__(self, window: Window):
        # Dimensões da tela para o sistema de física
        self.window = window
        screen_width, screen_height = Window.get_screen().get_size()
        self.physics = PhysicsSystem(screen_width, screen_height)

        # Objetos da fase
        self.game_objects = []

        # Cria uma bolinha
        self.ball = Ball(self.window)
        self.player_pad = Pad(x=get_left_x(window.width, 25), 
                              y=get_center_y(window.height, 100), 
                              width=25, 
                              height=100, 
                              window=window)
        
        self.ai_pad = Pad(x=get_right_x(window.width, 25), 
                          y=get_center_y(window.height, 100), 
                          width=25, 
                          height=100, 
                          window=window)

        self.player_controller = PlayerController(self.player_pad, self.window)
        self.ai_controller = AIController(self.ai_pad, self.ball)


        self.game_objects.extend([self.ball, self.player_pad, self.ai_pad])

    def update(self, dt: float) -> None:
        # Atualizando o controle do jogador e da IA
        self.player_controller.update(dt)
        self.ai_controller.update(dt)

        # Atualiza todos os objetos da cena
        for obj in self.game_objects:
            obj.update(dt)

        # Aplica física (colisão com bordas)
        self.physics.update(self.game_objects)

    def draw(self) -> None:
        self.window.set_background_color(self.window.get_background_color())
        for obj in self.game_objects:
            obj.draw()
