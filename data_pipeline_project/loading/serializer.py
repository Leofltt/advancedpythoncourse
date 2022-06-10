from abc import ABC, abstractmethod
from pathlib import Path
from typing import Any
import json

class Serializer(ABC):
    
    @abstractmethod
    def serialize(self, obj: Any, save_path: Path) -> None:
        pass

    @abstractmethod
    def deserialize(self, load_path: Path) -> Any:
        pass

class JSON_Serializer(Serializer):

    def __init__(self,
                 sort_keys: bool = True,
                 indent: int = 4) -> None:
        self.sort_keys = sort_keys
        self.indent = indent
    
    def serialize(self, obj: Any, save_path: Path) -> None:
        with open(save_path, 'w') as f:
            json.dump(obj, f, sort_keys=self.sort_keys, indent=self.indent) 

    def deserialize(self, load_path: Path) -> Any:
        with open(load_path, 'r') as f:
            return json.load(f)

class YAML_Serializer(Serializer):

    def __init__(self,
                 default_flow_style: bool = False) -> None:
        self.default_flow_style = default_flow_style

    def serialize(self, obj: Any, save_path: Path) -> None:
        with open(save_path, 'w') as f:
            yaml.dump(obj, f, default_flow_style=self.default_flow_style)

    def deserialize(self, load_path: Path) -> Any:
        with open(load_path, 'r') as f:
            return yaml.safe_load(f)
