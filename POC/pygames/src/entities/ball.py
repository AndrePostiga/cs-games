from pplay.sprite import Sprite
from helper.paths import asset_path
from helper.positions import get_center_x, get_center_y

class Ball(Sprite):
    def __init__(self, window, x=None, y=None, speed_x=None, speed_y=None):
        image = asset_path("images", "ball.png")
        super().__init__(image)
        
        self.x = x if x is not None else get_center_x(window.width, self.width)
        self.y = y if y is not None else get_center_y(window.height, self.height)
        
        self.speed_x = speed_x if speed_x is not None else 200
        self.speed_y = speed_y if speed_y is not None else 200
        self.window = window

    def update(self, dt):
        self.move_x(self.speed_x * dt)
        self.move_y(self.speed_y * dt)

    def draw(self):
        super().draw()

    def handle_wall_collision(self, direction: str):
        """
        Decide what to do when the ball collides with a wall.
        """
        if direction == "left" or direction == "right":
            self.speed_x *= -1  # Inverts the horizontal direction of the ball
        elif direction == "top" or direction == "bottom":
            self.speed_y *= -1  # Inverts the vertical direction of the ball

    def on_collision(self, other):
        """
        Colisão com qualquer outro objeto. Inverte a direção horizontal da bola.
        """
        self.speed_x *= -1  # Inverte a direção horizontal da bola ao colidir com qualquer objeto

