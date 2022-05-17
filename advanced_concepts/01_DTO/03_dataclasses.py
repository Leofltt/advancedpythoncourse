""" MusicAlbum -> title, artist, year, tracks :using @dataclass """

from dataclasses import dataclass
from typing import List

@dataclass
class MusicAlbum:
    title: str
    artist: str
    year: int
    tracks: List[str]

if __name__ == "__main__":
    album = MusicAlbum("The Dark Side of the Moon", "Pink Floyd", 1973, ["Speak to Me", "Breathe", "One More Time"])
    album2 = MusicAlbum("The Wall", "Pink Floyd", 1979, ["Whatever Happened to My Mother", "The Great Gig in the Sky", "Money"])
    album3 = MusicAlbum("The Dark Side of the Moon", "Pink Floyd", 1973, ["Speak to Me", "Breathe", "One More Time"])
    print(album == album3)