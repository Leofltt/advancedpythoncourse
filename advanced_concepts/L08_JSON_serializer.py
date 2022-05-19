import json
from pathlib import Path
from typing import Any

from L05_pydantic import MusicAlbum
from L06_serializer_abstractclass import Serializer


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

if __name__ == "__main__":
    
    album_params = {
        "title": "The Dark Side of the Moon",
        "artist": "Pink Floyd",
        "year": 1973,
        "tracks": ["Speak to Me", "Breathe", "One More Time"]
    }

    album = MusicAlbum(**album_params)
    ser = JSON_Serializer()

    ser.serialize(album.dict(), Path('./album.json'))
    album2 = ser.deserialize(Path('./album.json'))
    print(album2)