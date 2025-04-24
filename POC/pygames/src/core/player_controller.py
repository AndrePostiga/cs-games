from pplay.window import Window

class PlayerController:
    def __init__(self, pad, window: Window):
        self.pad = pad
        self.window = window
        self.keyboard = self.window.get_keyboard()

    def update(self, dt):
        if self.keyboard.key_pressed("UP"):
            self.pad.move_up(dt)
        if self.keyboard.key_pressed("DOWN"):
            self.pad.move_down(dt)