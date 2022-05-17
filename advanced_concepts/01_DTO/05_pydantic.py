""" MusicAlbum -> title, artist, year, tracks :using pydantic """

from typing import List

from pydantic import BaseModel

CURRENT_YEAR = 2022

class MusicAlbum(BaseModel):
    title: str
    artist: str
    year: int
    tracks: List[str]
    years_from_publication: int = None

    def __init__(__pydantic_self__, **data) -> None:
        super().__init__(**data)
        __pydantic_self__.years_from_publication = CURRENT_YEAR - __pydantic_self__.year

if __name__ == "__main__":
    album_params = {
        "title": "The Dark Side of the Moon",
        "artist": "Pink Floyd",
        "year": 1973,
        "tracks": ["Speak to Me", "Breathe", "One More Time"]
    }

    album = MusicAlbum(title="The Dark Side of the Moon", artist="Pink Floyd", year=1973, tracks=["Speak to Me", "Breathe", "One More Time"])
    album2 = MusicAlbum(title="The Wall", artist="Pink Floyd", year=1979, tracks=["Whatever Happened to My Mother", "The Great Gig in the Sky", "Money"])
    album3 = MusicAlbum(**album_params)
    print(album == album3)