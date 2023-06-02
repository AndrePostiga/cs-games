from PPlay.window import *
from PPlay.sprite import *

def center_y(window : Window, sprite: Sprite) -> (int, int):
    return (window.height - sprite.height) / 2    

def center_x(window : Window, sprite: Sprite) -> (int, int):
    return (window.width - sprite.width) / 2

def colide_x_right(window : Window, sprite: Sprite) -> bool:  
    return (window.width - sprite.width) - sprite.x <= 0

def colide_x_left(window : Window, sprite: Sprite) -> bool:  
    return sprite.x <= 0

def colide_x(window : Window, sprite: Sprite) -> bool:        
    return colide_x_right(window, sprite) or colide_x_left(window, sprite)

def colide_y_up(window : Window, sprite: Sprite) -> bool:  
    return sprite.y <= 0

def colide_y_down(window : Window, sprite: Sprite) -> bool:  
    return (window.height - sprite.height) - sprite.y <=0

def colide_y(window : Window, sprite: Sprite) -> bool:        
    return colide_y_up(window, sprite) or colide_y_down(window, sprite)

def oposite_direction(speed : float) -> float:
    return speed * -1

def left_pad_key_up(keyboard) -> bool:
    return keyboard.key_pressed('W')

def right_pad_key_up(keyboard) -> bool:
    return keyboard.key_pressed('UP')

def left_pad_key_down(keyboard) -> bool:
    return keyboard.key_pressed('S')

def right_pad_key_down(keyboard) -> bool:
    return keyboard.key_pressed('DOWN')


# Inicializção 
game_window=Window(600, 600)
game_window.set_title("Jogo")
game_window.set_background_color((0,0,0))

ball = Sprite('assets\\images\\ball_2.png', 1)
ball.set_position(center_x(game_window, ball), center_y(game_window, ball))
horizontal_ball_speed = 200
vertical_ball_speed = 300

pad_left = Sprite('assets\\images\\pad.png', 1)
pad_left.set_position(0, center_y(game_window, pad_left))

pad_right = Sprite('assets\\images\\pad.png', 1)
pad_right.set_position(game_window.width - pad_right.width, center_y(game_window, pad_right))

vertical_pad_speed = 400

keyboard_input = game_window.get_keyboard()

placar = [0,0]

# Game Loop
while (True):
    # Entrada de dados
    if left_pad_key_up(keyboard_input):
        pad_left.move_y(-1 * vertical_pad_speed * game_window.delta_time())
    elif left_pad_key_down(keyboard_input):
        pad_left.move_y(vertical_pad_speed * game_window.delta_time())

    if right_pad_key_up(keyboard_input):
        pad_right.move_y(-1 * vertical_pad_speed * game_window.delta_time())
    elif right_pad_key_down(keyboard_input):
        pad_right.move_y(vertical_pad_speed * game_window.delta_time())        

    # Update de game objects        
    ball.move_x(horizontal_ball_speed * game_window.delta_time())
    ball.move_y(vertical_ball_speed * game_window.delta_time())

    # Detecta gol
    if colide_x_left(game_window, ball):
        placar[0] += 1
        ball.set_position(center_x(game_window, ball), center_y(game_window, ball))
    elif colide_x_right(game_window, ball):
        placar[1] += 1
        ball.set_position(center_x(game_window, ball), center_y(game_window, ball))


    # Colisões com o cenário
    if colide_y(game_window, ball):
        ball.y = 0 if colide_y_up(game_window, ball) else (game_window.height - ball.height) # patinação eixo y
        vertical_ball_speed = oposite_direction(vertical_ball_speed)

    if colide_y_up(game_window, pad_left):
        pad_left.y = 0
    elif colide_y_down(game_window, pad_left):
        pad_left.y = game_window.height - pad_left.height

    if colide_y_up(game_window, pad_right):
        pad_right.y = 0
    elif colide_y_down(game_window, pad_right):
        pad_right.y = game_window.height - pad_right.height

    # Colisões entre sprites
    if ball.collided(pad_left):
        ball.x = 0 + pad_left.width # patinação com o pad da esquerda
        horizontal_ball_speed = oposite_direction(horizontal_ball_speed)
    elif ball.collided(pad_right):
        ball.x = pad_right.x - ball.width # patinação pad da direita
        horizontal_ball_speed = oposite_direction(horizontal_ball_speed)

    # Desenho    
    game_window.set_background_color((0,0,0)) ## Limpar tela pode ser com bg_color, imagem de fundo
    pad_left.draw()
    pad_right.draw()
    ball.draw()
    game_window.draw_text(f'{placar[0]}', (game_window.width / 2) - 20 , 20, 20, color=(255,255,255))
    game_window.draw_text(f'{placar[1]}', (game_window.width / 2) + 20 , 20, 20, color=(255,255,255))
    game_window.update()


# Finalizações