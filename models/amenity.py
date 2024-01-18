#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from os import getenv

if getenv('HBNB_TYPE_STORAGE')== 'db':

    class Amenity(BaseModel, Base):

        __tablename__ = 'amenities'

        name = Column(String(128), nullable=False)

        # place_amenities = 

else:
    class Amenity(BaseModel):
        name = ""
