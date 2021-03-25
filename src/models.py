import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy import render_er

Base = declarative_base()

class Favorites(Base):
    __tablename__ = 'favorites'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user.id'))
    planet_id = Column(Integer, ForeignKey('planet.id'))
    people_id = Column(Integer, ForeignKey('people.id'))
    planets = relationship(Planets)
    people = relationship(People)
    user = relationship(User)

class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    nickname = Column(String(250), nullable=False)
    mail = Column(String(250), nullable=False)
    password = Column(String(250), nullable=False)
  
class People(Base):
    __tablename__ = 'people'
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    height = Column(Integer(250), nullable=False)
    mass = Column(Integer(250), nullable=False)
    hair_color = Column(String(250), nullable=False)
    skin_color = Column(String(250), nullable=False)
    birth_year = Column(Integer(250), nullable=False)
    gender = Column(String(250), nullable=False)
    home_world = Column(String(250), nullable=False)
    planet_id = Column(Integer(250), nullable=False)

class Planets(Base):
    __tablename__ = 'planets'
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    rotation_period = Column(Integer(250), nullable=False)
    orbital_period = Column(Integer(250), nullable=False)
    diameter = Column(Integer(250), nullable=False)
    climate = Column(String(250), nullable=False)
    gravity = Column(String(250), nullable=False)
    terrain = Column(String(250), nullable=False)
    surface_water = Column(String(250), nullable=False)
    population = Column(Integer(250), nullable=False)
    residents = Column(Integer(250), nullable=False)

class Starships(Base):
    __tablename__ = 'starships'
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    model = Column(String(250), nullable=False)
    manufacturer = Column(String(250), nullable=False)
    cost_in_credits = Column(Integer(250), nullable=False)
    lenght = Column(Integer(250), nullable=False)
    max_atmospheric_speed = Column(Integer(250), nullable=False)
    crew = Column(String(250), nullable=False)
    passengers = Column(Integer(250), nullable=False)
    cargo_capacity = Column(Integer(250), nullable=False)
    consumables = Column(String(250), nullable=False)
    hyperdrive_rating = Column(Integer(250), nullable=False)
    MGLT = Column(Integer(250), nullable=False)
    starship_class = Column(String(250), nullable=False)
    pilots = Column(Integer(250), nullable=False)

def to_dict(self):
        return {}

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')