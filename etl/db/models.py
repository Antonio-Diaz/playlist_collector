from sqlalchemy import create_engine, Column, Integer, Float, String, Boolean, ForeignKey
from sqlalchemy.orm import sessionmaker, relationship
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm.exc import NoResultFound

Base = declarative_base()

class User(Base):
    __tablename__ = 'users'

    id = Column(String, primary_key=True)
    display_name = Column(String)
    email = Column(String)
    country = Column(String)
    product = Column(String)
    followers = Column(Integer)
    images = Column(String)  # Assuming the images are stored as a string (e.g., JSON) in the database


class Playlist(Base):
    __tablename__ = 'playlists'

    id = Column(String, primary_key=True)
    name = Column(String)
    description = Column(String)
    owner = Column(String, ForeignKey('users.id'))
    public = Column(Boolean)
    collaborative = Column(Boolean)
    tracks = relationship('Track', back_populates='playlist')


class Track(Base):
    __tablename__ = 'tracks'

    id = Column(String, primary_key=True)
    name = Column(String)
    artists = Column(String)  # Assuming the artists are stored as a string (e.g., JSON) in the database
    album = Column(String)
    duration_ms = Column(Integer)
    explicit = Column(Boolean)
    popularity = Column(Integer)
    origin_playlist = Column(String, ForeignKey('playlists.id'))
    audio = relationship('Audio', uselist=False, back_populates='track')


class Audio(Base):
    __tablename__ = 'audio'

    id = Column(String, primary_key=True)
    danceability = Column(Float)
    energy = Column(Float)
    key = Column(Integer)
    loudness = Column(Float)
    mode = Column(Integer)
    speechiness = Column(Float)
    acousticness = Column(Float)
    instrumentalness = Column(Float)
    liveness = Column(Float)
    valence = Column(Float)
    tempo = Column(Float)
    duration_ms = Column(Integer)
    time_signature = Column(Integer)
    track_id = Column(String, ForeignKey('tracks.id'))
    track = relationship('Track', back_populates='audio')