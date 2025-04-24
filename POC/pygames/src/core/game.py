from scenes.phase1 import Phase1
from pplay.window import Window

class Game:
    def __init__(self):
        self.window = Window(1024, 720)
        self.window.set_title("Pong Pro")
        self.running = True

        # Cena atual (inicialmente a Fase 1)
        self.scene = Phase1(self.window)

    def update(self, dt):
        self.scene.update(dt)

    def draw(self):
        self.scene.draw()

    def run(self):
        while self.running:
            dt = self.window.delta_time()

            self.update(dt)
            self.draw()

            self.window.update()

if __name__ == '__main__':
    game = Game()
    game.run()
