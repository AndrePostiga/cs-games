from dataclasses import dataclass
from dotenv import load_dotenv
import os


@dataclass
class Config:
    # Defaults
    WINDOW_WIDTH: int = 1024
    WINDOW_HEIGHT: int = 720
    FPS: int = 60
    WINDOW_TITLE: str = "Andre Felipe Brasil Postiga"

    @classmethod
    def load(cls) -> "Config":
        load_dotenv()
        return cls(
            WINDOW_WIDTH=int(os.getenv("WINDOW_WIDTH", Config.WINDOW_WIDTH)),
            WINDOW_HEIGHT=int(os.getenv("WINDOW_HEIGHT", Config.WINDOW_HEIGHT)),
            FPS=int(os.getenv("FPS", Config.FPS)),
            WINDOW_TITLE=os.getenv("WINDOW_TITLE", Config.WINDOW_TITLE),
        )