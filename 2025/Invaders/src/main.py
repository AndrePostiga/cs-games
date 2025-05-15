from core.game import Game
from config.config import Config

def main() -> None:
    config = Config().load()
    game = Game(config)
    game.run()


if __name__ == "__main__":
    main()