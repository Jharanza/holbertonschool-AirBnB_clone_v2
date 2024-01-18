#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from os import getenv

if getenv('HBNB_TYPE_STORAGE') == 'db':

    class Amenity(BaseModel, Base):
        ''' Class that create a table amenity'''
        __tablename__ = 'amenities'

        name = Column(String(128), nullable=False)

else:
    class Amenity(BaseModel):
        ''' Use this in case we use file_storage'''
        name = ""
