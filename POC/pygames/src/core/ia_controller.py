class AIController:
    def __init__(self, pad, ball):
        self.pad = pad
        self.ball = ball

    def update(self, dt):
        if self.ball.y < self.pad.y:
            self.pad.move_up(dt)
        elif self.ball.y > self.pad.y + self.pad.height:
            self.pad.move_down(dt)