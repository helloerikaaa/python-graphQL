from sqlalchemy import Column, Integer, String, ForeignKey

from models.artist import Artist
from models.album import Album
from app.database.db_config import Base, db_session


class Song(Base):
    __tablename__ = "songs"

    _id: Column(Integer, primary_key=True, index=True)
    name: Column(String)
    artist: Column(Integer, ForeignKey(Artist._id), primary_key=True)
    album: Column(Integer, ForeignKey(Album._id), primary_key=True)
    duration: Column(Integer)

    def create_song(self, name: str, artist: int, album: int, duration: int):
        album = Artist(name=name, artist=artist, album=album, duration=duration)
        album.save()

        return album

    def get_song(self, _id: int):
        return list(db_session.query(Song).filter_by(Song._id == _id).first())

    def list_songs(self):
        return db_session.query(Song).all()
