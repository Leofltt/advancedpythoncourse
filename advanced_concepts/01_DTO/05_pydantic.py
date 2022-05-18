""" MusicAlbum -> title, artist, year, tracks :using pydantic """

from typing import List

from pydantic import BaseModel, validator

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
    
    @validator('year')
    @classmethod
    def check_year_is_valid(cls, value: int) -> None:
        supported_years = range(1900, CURRENT_YEAR)
        if not value in supported_years:
            raise ValueError("Year must be less than or equal to current year and greater than or equal to 1900")
        return value

if __name__ == "__main__":
    album_params = {
        "title": "The Dark Side of the Moon",
        "artist": "Pink Floyd",
        "year": 1873,
        "tracks": ["Speak to Me", "Breathe", "One More Time"]
    }

    album = MusicAlbum(title="The Dark Side of the Moon", artist="Pink Floyd", year=1973, tracks=["Speak to Me", "Breathe", "One More Time"])
    album2 = MusicAlbum(title="The Wall", artist="Pink Floyd", year=1979, tracks=["Whatever Happened to My Mother", "The Great Gig in the Sky", "Money"])
    album3 = MusicAlbum(**album_params)
    # print(album == album3)
    print(album3)