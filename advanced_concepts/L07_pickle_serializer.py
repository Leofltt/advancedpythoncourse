from pathlib import Path
import pickle
from typing import Any

from L05_pydantic import MusicAlbum
from L06_serializer_abstractclass import Serializer

class PickleSerializer(Serializer):

    def __init__(self, 
                 protocol: int = 5,
                 encoding: str = 'ASCII') -> None:
        self.protocol = protocol
        self.encoding = encoding
    
    def serialize(self, obj: Any, save_path: Path) -> None:
        with open(save_path, 'wb') as f:
            pickle.dump(obj, f, protocol=self.protocol)

    def deserialize(self, load_path: Path) -> Any:
        with open(load_path, 'rb') as f:
            return pickle.load(f, encoding=self.encoding)

if __name__ == "__main__":
    
    album_params = {
        "title": "The Dark Side of the Moon",
        "artist": "Pink Floyd",
        "year": 1973,
        "tracks": ["Speak to Me", "Breathe", "One More Time"]
    }

    album = MusicAlbum(**album_params)
    ser = PickleSerializer()
    
    ser.serialize(album, Path('./album.pkl'))
    album2 = ser.deserialize(Path('./album.pkl'))

    print(album2) 