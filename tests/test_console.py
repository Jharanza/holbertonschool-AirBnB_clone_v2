#!/usr/bin/python3
"""
Contains the class TestConsoleDocs
"""

import console
import inspect
import pep8
import unittest
HBNBCommand = console.HBNBCommand


class TestConsoleDocs(unittest.TestCase):
    """Class for testing documentation of the console"""
    def test_pep8_conformance_console(self):
        """Test that console.py conforms to PEP8."""

        # create a PEP8 StyleGuide instance with quiet mode enabled
        pep8s = pep8.StyleGuide(quiet=True)

        # use the instance of PEP8 to check console.py file
        result = pep8s.check_files(['console.py'])

        # Check if numbers of errors is equal to 0 or print message
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")

    def test_pep8_conformance_test_console(self):
        """Test that tests/test_console.py conforms to PEP8."""

        # create an instance of PEP8
        pep8s = pep8.StyleGuide(quiet=True)

        # Get information from the file test_console
        result = pep8s.check_files(['tests/test_console.py'])

        # Check if numbers of errors is 0 or print message
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")

    def test_console_module_docstring(self):
        """Test for the console.py module docstring"""

        # Check if doc is different of None or print message
        self.assertIsNot(console.__doc__, None,
                         "console.py needs a docstring")

        # Check if length of doc is mayor or equal to 1 or print message
        self.assertTrue(len(console.__doc__) >= 1,
                        "console.py needs a docstring")

    def test_HBNBCommand_class_docstring(self):
        """Test for the HBNBCommand class docstring"""

        # Check if exists doc or print message
        self.assertIsNot(HBNBCommand.__doc__, None,
                         "HBNBCommand class needs a docstring")

        # Check if length of doc is major or equal to 1 or print message
        self.assertTrue(len(HBNBCommand.__doc__) >= 1,
                        "HBNBCommand class needs a docstring")
