""" MusicAlbum -> title, artist, year, tracks :using @dataclass """

from dataclasses import dataclass, field, asdict
from typing import List

CURRENT_YEAR = 2022

@dataclass
class MusicAlbum:
    title: str
    artist: str
    year: int
    tracks: List[str]
    years_from_publication: int = field(init=False)

    def __post_init__(self) -> None:
        self.years_from_publication = CURRENT_YEAR - self.year

    def to_dict(self) -> dict:
        return asdict(self)

if __name__ == "__main__":
    album = MusicAlbum("The Dark Side of the Moon", "Pink Floyd", 1973, ["Speak to Me", "Breathe", "One More Time"])
    album2 = MusicAlbum("The Wall", "Pink Floyd", 1979, ["Whatever Happened to My Mother", "The Great Gig in the Sky", "Money"])
    album3 = MusicAlbum("The Dark Side of the Moon", "Pink Floyd", 1973, ["Speak to Me", "Breathe", "One More Time"])
    print(album == album3)
    print(album.years_from_publication)
    print(album.to_dict())