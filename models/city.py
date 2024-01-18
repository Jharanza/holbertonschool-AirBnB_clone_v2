#!/usr/bin/python3
""" City Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey
from os import getenv
from sqlalchemy.orm import relationship

if getenv('HBNB_TYPE_STORAGE') == 'db':
    class City(BaseModel, Base):
        """ The city class, contains state ID and name """

        __tablename__ = 'cities'

        name = Column(String(128), nullable=False)

        state_id = Column(String(60), ForeignKey('states.id'), nullable=False)

        from models.place import Place
        # import in this place to avoid a circular import
        places = relationship('Place', backref='cities', cascade='all, delete')
else:
    class City(BaseModel):
        ''' We use this option if we use file_storage '''
        name = ''
        state_id = ''
