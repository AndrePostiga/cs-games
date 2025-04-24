from PPlay.window import *
from PPlay.sprite import *
from typing import List
from enum import Enum
import random

class WallSide(Enum):
    LEFT = "left"
    RIGHT = "right"
    TOP = "top"
    BOTTOM = "bottom"

class PadColision(Enum):
    PAD = "pad"

class Physics:
    def __init__(self, window : Window) -> None:
        self.screen_width = window.width
        self.screen_height = window.height

    def update(self, objects: List[Sprite]) -> None:
        for obj in objects:
            self._check_wall_collision(obj)
        self._check_object_collisions(objects)

    def _check_wall_collision(self, sprite: Sprite) -> None:
        if sprite.x <= 0:
            sprite.on_wall_collision(WallSide.LEFT)
        elif sprite.x + sprite.width >= self.screen_width:
            sprite.on_wall_collision(WallSide.RIGHT)

        if sprite.y <= 0:
            sprite.on_wall_collision(WallSide.TOP)
        elif sprite.y + sprite.height >= self.screen_height:
            sprite.on_wall_collision(WallSide.BOTTOM)

    def _check_object_collisions(self, sprites: List[Sprite]) -> None:
        for i in range(len(sprites)):
            for j in range(i + 1, len(sprites)):
                obj1 = sprites[i]
                obj2 = sprites[j]

                if (obj1.collided(obj2)):
                    obj1.on_collision(obj2)
                    obj2.on_collision(obj1)

class Game:
    def __init__(self):
        self.window = Window(1024, 300)
        self.window.set_title("Andre Felipe Brasil Postiga")
        self.window.set_background_color((0,0,150))
        self.running = True
        self.scene = Scene(self.window)

    def update(self, dt):
        self.scene.update(dt)

    def draw(self):
        self.scene.draw()

    def run(self):
        while self.running:
            self.window.set_background_color(self.window.get_background_color())
            # manda a cena atualizar todos os objetos que ela controla (posições, interações e etc)
            self.update(self.window.delta_time())
            # manda a cena desenhar todos os objetos já atualizados
            self.draw()
            # faz swap do framebuffer limpando antes
            self.window.update()

class Score:
    def __init__(self, window: Window):
        self.player_score = 0
        self.ia_score = 0
        self.window = window

    def on_notification(self, message):
        if message == WallSide.RIGHT:
            self.ia_score += 1
        elif message == WallSide.LEFT:
            self.player_score += 1

    def _get_score(self):
        return f'Player: {self.player_score} | {self.ia_score} : IA'

    def draw(self):
        score = self._get_score()
        self.window.draw_text(score, 20, 20, 20, (255,255,255))

class Scene:
    def _create_ball(self):
        ball = Ball(self.window)
        ball.observe(self.score)
        ball.observe(self)
        self.game_objects.append(ball)
        return ball

    def _create_pad(self, x, width, height, speed_y):
        pad = Pad(self.window, x=x, width=width, height=height, speed_y=speed_y)
        self.game_objects.append(pad)
        return pad
    
    def _create_obstacle(self):
        obstacle = Obstacle(self.window)
        self.game_objects.append(obstacle)
        return obstacle

    def __init__(self, window : Window):
        self.window = window
        self._paused = True
        self.game_objects : List[Sprite] = []
        self.physics = Physics(window)
        
        self.score = Score(self.window)
        self.ball = self._create_ball()
        self.obstacle = None

        padWidth = 25
        padHeight = 100
        padSpeed = 200
        self.leftPad = self._create_pad(0, padWidth, padHeight, padSpeed)
        self.rightPad = self._create_pad(self.window.width - padWidth, padWidth, padHeight, padSpeed)

        self.playerController = PlayerController(self.leftPad, self, self.window) 
        self.iaController = IAController(self.rightPad, self.ball, self.window)

        self.countPadColisions = 0

    def is_paused(self):
        return self._paused

    def pause(self):
        self._paused = True

    def resume(self):
        self._paused = False

    def _reset_positions(self):
        self.ball.center()
        self.leftPad.center()
        self.rightPad.center()

    def on_notification(self, message):
        if message == WallSide.LEFT or message == WallSide.RIGHT:
            self.pause()
            self._reset_positions()

        if message == PadColision.PAD:
            self.countPadColisions += 1
            if self.countPadColisions == 6:
                self._create_obstacle()
                self.countPadColisions = 0

    def update(self, dt):   
        # Verifica controles do player
        self.playerController.update(dt)

        # Verifica se o jogo está pausado antes de atualizar toda a cena
        if self.is_paused():
            return

        self.iaController.update(dt)

        # Atualiza objetos da cena
        for obj in self.game_objects:
            obj.update(dt)
            if isinstance(obj, Obstacle):
                if obj.destroyed:
                    self.game_objects.remove(obj)
                    continue
            

        # Atualiza física do jogo
        self.physics.update(self.game_objects)

    def draw(self):
        for obj in self.game_objects:
            obj.draw()

        self.score.draw()

        if self.is_paused():
            self.window.draw_text(
                "PAUSED!", 
                self.window.width // 2 - 100,
                self.window.height // 2 - 50,
                size=50, 
                color=(255, 255, 255)
            )

class Ball(Sprite):
    def __init__(self, window: Window, x=50, y=50, speed_x=300, speed_y=300):
        super().__init__("images/ball.png") 
        self.x = (window.width - x)/2
        self.y = (window.height - y)/2
        self.speed_x = speed_x
        self.speed_y = speed_y
        self.window = window
        self.observers = []
        self._randomize_speed_direction()

    def _randomize_speed_direction(self):
        self.speed_x *= random.choice([-1, 1])
        self.speed_y *= random.choice([-1, 1])

    def observe(self, observer):
        self.observers.append(observer)
    
    def _notifyScore(self, message):
        for observer in self.observers:
            observer.on_notification(message)

    def _notifyPadColision(self):
        for observer in self.observers:
            observer.on_notification(PadColision.PAD)

    def center(self):
        self.x = (self.window.width - self.width)/2
        self.y = (self.window.height - self.height)/2

    def update(self, dt):
        self.move_x(self.speed_x * dt)
        self.move_y(self.speed_y * dt)

    def on_wall_collision(self, side: WallSide):
        if side == WallSide.LEFT:
            self.center()
            self._notifyScore(WallSide.LEFT)
        elif side == WallSide.RIGHT:
            self.center()
            self._notifyScore(WallSide.RIGHT)
        elif side == WallSide.TOP:
            self.y = 0
            self.speed_y *= (-1)
        elif side == WallSide.BOTTOM:
            self.y = self.window.height - self.height
            self.speed_y *= (-1)
    
    def on_collision(self, collidedSprite : Sprite):
        if self.speed_x > 0:
            self.x = collidedSprite.x - self.width 
        elif self.speed_x < 0: 
            self.x = collidedSprite.x + collidedSprite.width

        self.speed_x *= -1

        if isinstance(collidedSprite, Pad):
            self._notifyPadColision()

        if isinstance(collidedSprite, Obstacle):
            if (self.speed_x > 0):
                self.speed_x += 50 
            else:
                self.speed_x -= 50

            if (self.speed_y > 0):
                self.speed_y += 50
            else:
                self.speed_y -= 50

    def draw(self):
        self.window.draw_text(
            f'vel({self.speed_x:.2f},{self.speed_y:.2f})', 
            self.x, 
            self.y - 15, 
            size=15, 
            color=(255, 255, 255)
        )
        super().draw()

class Pad(Sprite):
    def __init__(self, window: Window, x=0, width=25, height=100, speed_y=400):
        super().__init__("images/pad.png")
        self.window = window
        self.width = width
        self.height = height
        self.x = x
        self.y = (self.window.height - self.height) / 2
        self.speed_x = 0
        self.speed_y = speed_y

    def center(self):
        self.y = (self.window.height - self.height) / 2

    def update(self, dt):
        pass # Não é necessário pois será controlado pelo player

    def move_up(self, dt):
        self.move_y(self.speed_y * dt * -1)
        # esse menos um significa que o zero começa em cima
        # portanto velocidade positiva vai pra baixo
        # velocidade negativa vai pra cima

    def move_down(self, dt):
        self.move_y(self.speed_y * dt)

    def on_collision(self, collidedSprite : Sprite):
        pass

    def on_wall_collision(self, side: WallSide):
        if side == WallSide.TOP:
            self.y = 0
        elif side == WallSide.BOTTOM:
            self.y = self.window.height - self.height
        elif side == WallSide.LEFT:
            self.x = 0
        elif side == WallSide.RIGHT:
            self.x = self.window.width - self.width

class PlayerController:
    def __init__(self, pad: Pad, scene: Scene, window: Window):
        self.pad = pad
        self.window = window
        self.scene = scene
        self.keyboard = self.window.get_keyboard()

    def update(self, dt):
        if self.scene.is_paused():
            if self.keyboard.key_pressed("space"):
                self.scene.resume()
            return
        
        if self.keyboard.key_pressed("p"):
            self.scene.pause()
            return

        if self.keyboard.key_pressed("UP"):
            self.pad.move_up(dt)
        if self.keyboard.key_pressed("DOWN"):
            self.pad.move_down(dt)

class IAController:
    def __init__(self, pad: Pad, ball: Ball, window: Window):
        self.pad = pad
        self.ball = ball
        self.window = window

    def update(self, dt):
        # Predict the ball's future y position
        future_ball_y = self.ball.y + (self.ball.speed_y * dt)

        # Center of the paddle
        pad_center_y = self.pad.y + (self.pad.height / 2)

        # Move the paddle towards the predicted position of the ball
        if future_ball_y < pad_center_y:
            self.pad.move_up(dt)
        elif future_ball_y > pad_center_y:
            self.pad.move_down(dt)

class Obstacle(Sprite):
    def __init__(self, window: Window):
        super().__init__("images/pad.png")
        self.window = window
        self.x = (self.window.width - self.width)/2
        
        # Igual pad Image
        self.width = 25
        self.height = 100

        self.y = random.randint(0, (int)(self.window.height - self.height))
        self.timer = 0
        self.ttl = random.randint(2, 4) #vide de 2 a 4 segundos
        self.destroyed = False

    def update(self, dt):
        self.timer += dt
        if self.timer >= self.ttl:
            self.destroyed = True

    def on_collision(self, collidedSprite : Sprite):
        pass
    
    def on_wall_collision(self, side: WallSide):
        pass

    def draw(self):
        timeleft = self.ttl - self.timer
        self.window.draw_text(
            f'TimeLeft:({timeleft:.2f}))', 
            self.x, 
            self.y - 15, 
            size=15, 
            color=(255, 255, 255)
        )
        super().draw()

def main():
    game = Game()
    game.run()

if __name__ == '__main__':
    main()