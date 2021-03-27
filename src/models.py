import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy import render_er
#inicio
Base = declarative_base()
#nueva clase
class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    nickname = Column(String(250), nullable=False)
    mail = Column(String(250), nullable=False)
    password = Column(String(250), nullable=False)
    mail = Column(String(250), nullable=False)
#nueva clase
class People(Base):
    __tablename__ = 'people'
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    height = Column(Integer, nullable=False)
    mass = Column(Integer, nullable=False)
    hair_color = Column(String(250), nullable=False)
    skin_color = Column(String(250), nullable=False)
    birth_year = Column(Integer, nullable=False)
    gender = Column(String(250), nullable=False)
    home_world = Column(String(250), nullable=False)
    planet_id = Column(Integer, nullable=False)
#nueva clase
class Planets(Base):
    __tablename__ = 'planets'
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    rotation_period = Column(Integer, nullable=False)
    orbital_period = Column(Integer, nullable=False)
    diameter = Column(Integer, nullable=False)
    climate = Column(String(250), nullable=False)
    gravity = Column(String(250), nullable=False)
    terrain = Column(String(250), nullable=False)
    surface_water = Column(String(250), nullable=False)
    population = Column(Integer, nullable=False)
    residents = Column(Integer, nullable=False)
#nueva clase
class Starships(Base):
    __tablename__ = 'starships'
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    model = Column(String(250), nullable=False)
    manufacturer = Column(String(250), nullable=False)
    cost_in_credits = Column(Integer, nullable=False)
    lenght = Column(Integer, nullable=False)
    max_atmospheric_speed = Column(Integer, nullable=False)
    crew = Column(String(250), nullable=False)
    passengers = Column(Integer, nullable=False)
    cargo_capacity = Column(Integer, nullable=False)
    consumables = Column(String(250), nullable=False)
    hyperdrive_rating = Column(Integer, nullable=False)
    MGLT = Column(Integer, nullable=False)
    starship_class = Column(String(250), nullable=False)
    pilots = Column(Integer, nullable=False)
#nueva clase
class Favorites(Base):
    __tablename__ = 'favorites'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user.id'))
    people_id = Column(Integer, ForeignKey('people.id'))
    planet_id = Column(Integer, ForeignKey('planets.id'))
    starships_id = Column(Integer, ForeignKey('starships.id'))
    user = relationship(User)
    people = relationship(People)
    planets = relationship(Planets)
    starships = relationship(Starships)

def to_dict(self):
        return {}

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')