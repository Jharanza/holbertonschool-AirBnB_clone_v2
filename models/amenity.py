#!/usr/bin/python3
""" State Module for HBNB project """
from os import getenv
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from models.base_model import BaseModel, Base


if getenv('HBNB_TYPE_STORAGE') == 'db':

    class Amenity(BaseModel, Base):
        ''' Class that create a table amenity'''
        __tablename__ = 'amenities'

        name = Column(String(128), nullable=False)

        ''' From table many to many '''
        place_amenities = relationship(
            'Place', secondary='place_amenity', back_populates='amenities'
        )

else:
    class Amenity(BaseModel):
        ''' Use this in case we use file_storage'''
        name = ""
