from pathlib import Path
from typing import Any
import yaml

from L05_pydantic import MusicAlbum
from L06_serializer_abstractclass import Serializer

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

if __name__ == "__main__":
    
    album_params = {
        "title": "The Dark Side of the Moon",
        "artist": "Pink Floyd",
        "year": 1973,
        "tracks": ["Speak to Me", "Breathe", "One More Time"]
    }

    album = MusicAlbum(**album_params)
    ser = YAML_Serializer()

    ser.serialize(album.dict(), Path('./album.yaml'))
    album2 = ser.deserialize(Path('./album.yaml'))
    print(album2)