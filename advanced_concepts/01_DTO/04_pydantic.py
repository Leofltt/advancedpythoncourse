""" MusicAlbum -> title, artist, year, tracks :using pydantic """

from typing import List

from pydantic import BaseModel

class MusicAlbum(BaseModel):
    title: str
    artist: str
    year: int
    tracks: List[str]

if __name__ == "__main__":
    album = MusicAlbum(title="The Dark Side of the Moon", artist="Pink Floyd", year=1973, tracks=["Speak to Me", "Breathe", "One More Time"])
    album2 = MusicAlbum(title="The Wall", artist="Pink Floyd", year=1979, tracks=["Whatever Happened to My Mother", "The Great Gig in the Sky", "Money"])
    album3 = MusicAlbum(title="The Dark Side of the Moon", artist="Pink Floyd", year=1973, tracks=["Speak to Me", "Breathe", "One More Time"])
    print(album == album3)