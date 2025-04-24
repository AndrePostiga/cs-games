from Game import Game
import sys


def main():
    game = Game()
    game.start()

if __name__ == "__main__":
    sys.exit(int(main() or 0))