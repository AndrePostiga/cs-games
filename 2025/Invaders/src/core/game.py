from pplay.window import Window
from config.config import Config
from scenes.main_menu import MainMenu
from components.button import ButtonAction
from core.scene_factory import SceneFactory
from core.observer import Observer

class Game(Observer):
    def __init__(self, config : Config):
        super().__init__()
        self.window = Window(config.WINDOW_WIDTH, config.WINDOW_HEIGHT)
        self.running = True
        self._set_scene(MainMenu(self.window))
        self.scene_factory = SceneFactory()

    def on_notification(self, msg: ButtonAction) -> None:
        scene = self.scene_factory.create_scene(msg, self.window)
        if scene is None:
            return
        
        del self.current_scene
        self._set_scene(scene)
        
    def _set_scene(self, scene) -> None:
        self.current_scene = scene
        self.current_scene.add_observer(self)

    def run(self) -> None:
        while self.running:
            self.window.set_background_color(self.window.get_background_color())

            self.current_scene.update(self.window.delta_time())
            self.current_scene.draw()

            self.window.update()