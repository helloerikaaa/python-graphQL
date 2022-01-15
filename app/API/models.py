import strawberry

from typing import List
from pydantic import BaseModel


@strawberry.type
class Artist(BaseModel):
    name: str
    listeners: float
    active: bool


@strawberry.type
class Album:
    name: str
    year: int
    active: bool


@strawberry.type
class Song(BaseModel):
    name: str
    artist: Artist
    album: Album
    duration: int
    active: bool


@strawberry.type
class User(BaseModel):
    name: str
    country: str
    songs: List[Song]
    active: bool
