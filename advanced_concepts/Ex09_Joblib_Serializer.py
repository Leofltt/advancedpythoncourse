from pathlib import Path
from typing import Any
import joblib

from L05_pydantic import MusicAlbum
from L06_serializer_abstractclass import Serializer

class Joblib_Serializer(Serializer):

    def __init__(self,
                 compress: int = 9,
                 protocol: int = 5) -> None:
        self.compress = compress
        self.protocol = protocol

    def serialize(self, obj: Any, save_path: Path) -> None:
        joblib.dump(obj, save_path, compress=self.compress, protocol=self.protocol)

    def deserialize(self, load_path: Path) -> Any:
        return joblib.load(load_path)

if __name__ == "__main__":
    
    album_params = {
        "title": "The Dark Side of the Moon",
        "artist": "Pink Floyd",
        "year": 1973,
        "tracks": ["Speak to Me", "Breathe", "One More Time"]
    }

    album = MusicAlbum(**album_params)
    ser = Joblib_Serializer()

    ser.serialize(album, Path('./album.z'))
    album2 = ser.deserialize(Path('./album.z'))
    print(album2)