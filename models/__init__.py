#!/usr/bin/python3
"""This module instantiates an object of class FileStorage or DBStorage"""
from models.engine.file_storage import FileStorage
from models.engine.db_storage import DBStorage
from os import getenv


if getenv('HBNB_TYPE_STORAGE') == 'db':
    ''' Use this option in case the type of the storage is db '''
    storage = DBStorage()
else:
    ''' Use this option in case the type of the storage is fileStorage '''
    storage = FileStorage()

storage.reload()
