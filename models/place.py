#!/usr/bin/python3
""" Place Module for HBNB project """
from os import getenv
from sqlalchemy import Column, Integer, String, ForeignKey, Float, Table
from sqlalchemy.orm import relationship
from models.base_model import BaseModel, Base
from models.amenity import Amenity
from models import storage


if getenv('HBNB_TYPE_STORAGE') == 'db':
    place_amenity = Table('place_amenity', Base.metadata,
                          Column(
                              'place_id', String(60), ForeignKey('places.id'),
                              primary_key=True, nullable=False),
                          Column(
                              'amenity_id', String(60),
                              ForeignKey('amenities.id'), primary_key=True,
                              nullable=False)
                          )

    class Place(BaseModel, Base):
        """ A place to stay """

        __tablename__ = 'places'

        city_id = Column(String(60), ForeignKey('cities.id'), nullable=False)
        user_id = Column(String(60), ForeignKey('users.id'), nullable=False)
        name = Column(String(128), nullable=False)
        description = Column(String(1024), default='', nullable=True)
        number_rooms = Column(Integer, default=0, nullable=False)
        number_bathrooms = Column(Integer, default=0, nullable=False)
        max_guest = Column(Integer, default=0, nullable=False)
        price_by_night = Column(Integer, default=0, nullable=False)
        latitude = Column(Float, default=0.0, nullable=True)
        longitude = Column(Float, default=0.0, nullable=True)
        amenities = relationship(
            'Amenity', secondary='place_amenity',
            back_populates='place_amenities'
        )
        amenity_ids = []
else:
    class Place(BaseModel):
        """ Use this option to file_storage """
        city_id = ''
        user_id = ''
        name = ''
        description = ''
        number_rooms = 0
        number_bathrooms = 0
        max_guest = 0
        price_by_night = 0
        latitude = 0.0
        longitude = 0.0
        amenity_ids = []

        @property
        def amenities(self):
            '''Method that return a list of instances based in amenity_ids'''
            data_amenity = storage.all(Amenity)
            amenity_list = [
                data_amenity for data_amenity in data_amenity.values()
                if data_amenity.id in self.amenity_ids]
            return amenity_list

        @amenities.setter
        def amenities(self, obj):
            ''' Method that add Amenity.id to the attribute amenity_ids '''
            if obj.__class__.__name__ == "Amenity":
                self.amenity_ids.append(obj.id)
            else:
                pass
