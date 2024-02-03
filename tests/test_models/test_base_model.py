#!/usr/bin/python3
""" """
from models import base_model
import inspect
import unittest
import datetime
from uuid import UUID
import json
import os
import pep8 as pycodestyle

# import and instanciar base model
BaseModel = base_model.BaseModel
module_doc = base_model.__doc__


class TestBaseModelDocs(unittest.TestCase):
    """  """
    
    @classmethod
    def setUpClass(self):
        """ Save the methods in 1 instance of the class """
        self.base_funcs = inspect.getmembers(BaseModel, inspect.isfunction)
        
    def test_pep8_conformance(self):
        """ chick if file conforms to PEP8 """
        
        # iterate over files base_model and test_base_model
        for path in ['models/base_model.py', 
                     'tests/tests_models/test_base_model.py']:
            # Execute subtests into the principal test
            with self.subTest(path=path):
                # save the found errors in a variable
                errors = pycodestyle.Checker(path).check_all()
                # check if the number of errors is zero
                self.assertEqual(errors, 0)
                
    def test_module_docstring(self):
        """Test for the existence of module docstring"""
        
        # check if doc is not None or print a message
        self.assertIsNot(module_doc, None,
                         "base_model.py needs a docstring")
        
        # check if the length of doc is bigger than 1 or print a message
        self.assertTrue(len(module_doc) > 1,
                        "base_model.py needs a docstring")
        
    def test_class_docstring(self):
        """Test for the BaseModel class docstring"""
        
        # check if doc is not None or print a message
        self.assertIsNot(BaseModel.__doc__, None,
                         "BaseModel class needs a docstring")
        
        # check if length of doc is bigger or equal than 1 or print a message
        self.assertTrue(len(BaseModel.__doc__) >= 1,
                        "BaseModel class needs a docstring")
        
    def test_func_docstrings(self):
        """Test for the presence of docstrings in BaseModel methods"""
        
        # iterate ove hte list base_funcs from the class BaseModel
        for func in self.base_funcs:
            # Execute subtest into the principal test
            with self.subTest(function=func):
                # check if docstring is not None or print message
                self.assertIsNot(
                    func[1].__doc__,
                    None,
                    "{:s} method needs a docstring".format(func[0])
                ) # Check that length of doc is bigger than 1
                self.assertTrue(
                    len(func[1].__doc__) > 1,
                    "{:s} method needs a docstring".format(func[0])
                )


class test_basemodel(unittest.TestCase):
    """ """

    def __init__(self, *args, **kwargs):
        """ """
        super().__init__(*args, **kwargs)
        self.name = 'BaseModel'
        self.value = BaseModel

    def setUp(self):
        """ """
        pass

    def tearDown(self):
        try:
            os.remove('file.json')
        except:
            pass

    def test_default(self):
        """ """
        i = self.value()
        self.assertEqual(type(i), self.value)

    def test_kwargs(self):
        """ """
        i = self.value()
        copy = i.to_dict()
        new = BaseModel(**copy)
        self.assertFalse(new is i)

    def test_kwargs_int(self):
        """ """
        i = self.value()
        copy = i.to_dict()
        copy.update({1: 2})
        with self.assertRaises(TypeError):
            new = BaseModel(**copy)

    def test_save(self):
        """ Testing save """
        i = self.value()
        i.save()
        key = self.name + "." + i.id
        with open('file.json', 'r') as f:
            j = json.load(f)
            self.assertEqual(j[key], i.to_dict())

    def test_str(self):
        """ """
        i = self.value()
        self.assertEqual(str(i), '[{}] ({}) {}'.format(self.name, i.id,
                         i.__dict__))

    def test_todict(self):
        """ """
        i = self.value()
        n = i.to_dict()
        self.assertEqual(i.to_dict(), n)

    def test_kwargs_none(self):
        """ """
        n = {None: None}
        with self.assertRaises(TypeError):
            new = self.value(**n)

    def test_kwargs_one(self):
        """ """
        n = {'Name': 'test'}
        with self.assertRaises(KeyError):
            new = self.value(**n)

    def test_id(self):
        """ """
        new = self.value()
        self.assertEqual(type(new.id), str)

    def test_created_at(self):
        """ """
        new = self.value()
        self.assertEqual(type(new.created_at), datetime.datetime)

    def test_updated_at(self):
        """ """
        new = self.value()
        self.assertEqual(type(new.updated_at), datetime.datetime)
        n = new.to_dict()
        new = BaseModel(**n)
        self.assertTrue(new.created_at == new.updated_at)
