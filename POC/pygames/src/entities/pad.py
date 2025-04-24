from pplay.sprite import Sprite
from helper.paths import asset_path
from pplay.window import Window

class Pad(Sprite):
    def __init__(self, x, y, width, height, window):
        image = asset_path("images", "pad.png")
        super().__init__(image)
        self.set_position(x, y)
        self.width = width
        self.height = height
        self.speed_x = 0  # O pad não se move horizontalmente
        self.speed_y = 200  # Velocidade do pad no eixo Y
        self.window = window

    def update(self, dt):
        pass  # A movimentação será feita externamente (no PlayerController ou AIController)

    def move_up(self, dt):
        if self.y > 0:
            self.move_y(-self.speed_y * dt)

    def move_down(self, dt):
        if self.y + self.height < self.window.height:
            self.move_y(self.speed_y * dt)

    def handle_wall_collision(self, direction: str):
        """
        Decide o que fazer quando o pad colide com uma parede.
        Impede que o pad ultrapasse os limites da tela.
        """
        if direction == "top":
            self.y = 0  # O pad ficou na borda superior
        elif direction == "bottom":
            self.y = self.window.height - self.height  # O pad ficou na borda inferior
        elif direction == "left":
            self.x = 0  # Impede que o pad ultrapasse a borda esquerda
        elif direction == "right":
            self.x = self.window.width - self.width  # Impede que o pad ultrapasse a borda direita

    def draw(self):
        super().draw()