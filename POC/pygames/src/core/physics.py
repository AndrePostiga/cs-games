from pplay.sprite import Sprite
from typing import List

class PhysicsSystem:
    def __init__(self, screen_width: int, screen_height: int) -> None:
        self.screen_width = screen_width
        self.screen_height = screen_height

    def update(self, objects: List[Sprite]) -> None:
        for obj in objects:
            self._check_wall_collision(obj)
        self._check_object_collisions(objects)

    def _check_wall_collision(self, obj: Sprite) -> None:
        # Verifica colisão com a parede e notifica o objeto para reagir
        if obj.x <= 0:
            if hasattr(obj, "handle_wall_collision"):  # Verifica se o objeto tem esse método
                obj.handle_wall_collision("left")  # Notifica o objeto para reagir
        elif obj.x + obj.width >= self.screen_width:
            if hasattr(obj, "handle_wall_collision"):  # Verifica se o objeto tem esse método
                obj.handle_wall_collision("right")  # Notifica o objeto para reagir

        if obj.y <= 0:
            if hasattr(obj, "handle_wall_collision"):  # Verifica se o objeto tem esse método
                obj.handle_wall_collision("top")  # Notifica o objeto para reagir
        elif obj.y + obj.height >= self.screen_height:
            if hasattr(obj, "handle_wall_collision"):  # Verifica se o objeto tem esse método
                obj.handle_wall_collision("bottom")  # Notifica o objeto para reagir

    def _check_object_collisions(self, objects: List[Sprite]) -> None:
        for i in range(len(objects)):
            for j in range(i + 1, len(objects)):
                obj1 = objects[i]
                obj2 = objects[j]
                if self._collides(obj1, obj2):
                    if hasattr(obj1, "on_collision"):
                        obj1.on_collision(obj2)
                    if hasattr(obj2, "on_collision"):
                        obj2.on_collision(obj1)

    def _collides(self, a: Sprite, b: Sprite) -> bool:
        return (
            a.x < b.x + b.width and
            a.x + a.width > b.x and
            a.y < b.y + b.height and
            a.y + a.height > b.y
        )