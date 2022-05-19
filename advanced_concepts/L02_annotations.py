""" MusicAlbum -> title, artist, year, tracks : adding annotations into the mix! """

from __future__ import annotations
from typing import List, Optional

class MusicAlbum:

    def __init__(self, title: str, artist: str, year: int, songs: Optional[List[str]] = None) -> None:
        self.title = title
        self.artist = artist
        self.year = year
        self.songs = songs
    
    def __str__(self) -> str:
        return f"MusicAlbum: {self.title} by {self.artist} ({self.year})"
    
    def __eq__(self, other: MusicAlbum) -> bool:
        if self.title == other.title and self.artist == other.artist and self.year == other.year:
            return True
        return False     

if __name__ == "__main__":
    album = MusicAlbum("The Dark Side of the Moon", "Pink Floyd", 1973, ["Speak to Me", "Breathe", "One More Time"])
    album2 = MusicAlbum("The Wall", "Pink Floyd", 1979, ["Whatever Happened to My Mother", "The Great Gig in the Sky", "Money"])
    album3 = MusicAlbum("The Dark Side of the Moon", "Pink Floyd", 1973, ["Speak to Me", "Breathe", "One More Time"])
    print(album == album3)