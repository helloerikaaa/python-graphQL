from sqlalchemy import Column, Integer, String, Float

from app.database.db_config import Base, db_session


class Artist(Base):
    __tablename__ = "artists"

    _id: Column(Integer, primary_key=True, index=True)
    name: Column(String)
    listeners: Column(Float)

    def create_artist(self, name: str, listeners: str):
        # check if the artist is already created
        artist = Artist.select().where(Artist.name == name.strip().lower())

        if artist.exists():
            return None

        artist = Artist(name=name, listeners=listeners)
        db_session.add(artist)
        db_session.commit()
        db_session.refresh(artist)

        return artist

    def get_artist(self, _id: int):
        return list(db_session.query(Artist).filter_by(Artist._id == _id).first())

    def list_artists(self):
        return db_session.query(Artist).all()
