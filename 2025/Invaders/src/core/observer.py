from abc import ABC, abstractmethod
from typing import List

class Observer(ABC):
    @abstractmethod
    def on_notification(self, msg: str):
        raise NotImplementedError("You should implement this method.")
    
class Observable(ABC):
    def __init__(self):
        self._observers : List[Observer] = []

    def add_observer(self, observer: Observer):
        if observer not in self._observers:
            self._observers.append(observer)

    def _notify_observers(self, msg: str):
        for observer in self._observers:
            observer.on_notification(msg)
