#!/usr/bin/python3
""" Place Module for HBNB project """
from sqlalchemy.ext.declarative import declarative_base
from models.base_model import BaseModel, Base
from sqlalchemy import Column, Integer, String
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship
from models.place import Place


class Place(BaseModel, Base):
    """ A place to stay
    Attributes:
    city_id: city_id
    user_id: user_id
    name: name
    description: description
    number_rooms: 0
    number_bathrooms: 0
    max_guest: 0
    price_by_night: 0
    latitude = 0.0
    longitude: 0.0
    amenity_ids: []
    """
    __tablename__ = "cities"
    name = Column(String(128), nullable=False)
    state_id = Column(String(60), ForeignKey('states.id'), nullable=False)
    places = relationship("Place", cascade='all, delete, delete-orphan',
                          backref="cities")
    
