from abc import ABC, abstractmethod
from pathlib import Path
from typing import Any

class Serializer(ABC):
    
    @abstractmethod
    def serialize(self, obj: Any, save_path: Path) -> None:
        pass

    @abstractmethod
    def deserialize(self, load_path: Path) -> Any:
        pass


if __name__ == "__main__":
    ser = Serializer()