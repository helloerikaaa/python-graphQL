from re import A
from sqlalchemy import Column, Integer, String, ForeignKey

from models.artist import Artist
from app.database.db_config import Base, db_session


class Album(Base):
    __tablename__ = "albums"

    _id: Column(Integer, primary_key=True, index=True)
    name: Column(String)
    artist: Column(Integer, ForeignKey(Artist._id), primary_key=True)
    year: Column(Integer)

    def create_album(self, name: str, artist: int, year: int):
        album = Artist(name=name, artist=artist, year=year)
        db_session.add(album)
        db_session.commit()
        db_session.refresh(album)

        return album

    def get_album(self, _id: int):
        return list(db_session.query(Album).filter_by(Album._id == _id).first())

    def list_albums(self):
        return db_session.query(Album).all()
