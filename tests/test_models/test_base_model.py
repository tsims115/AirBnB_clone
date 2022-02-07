#!/usr/bin/python3
"""Unit testing for BaseModel"""

import unittest
from models.base_model import BaseModel
import pep8
from datetime import datetime


class TestBaseClass(unittest.TestCase):
    """ Class to test BaseModel """
    def setUp(self):
        """Set up"""
        self.ex1 = BaseModel()

    def tearDown(self):
        """Tear down"""
        del self.ex1

    def test_pep8(self):
        """
        Testing pep8 compliance.
        """
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(['models/base_model.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")

    def test_documentation(self):
        """
        tests for module, class, & method documentation.
        """
        # Class docstring
        self.assertTrue(len(BaseModel.__doc__) >= 1)
        # Method docstrings
        self.assertTrue(len(BaseModel.__init__.__doc__) >= 1)

    def test_base_model_uuid(self):
        """Testing BaseModel UUID"""
        id = self.ex1.id
        self.assertEqual(id, self.ex1.id)
        self.assertEqual(type(id), str)

    def test_base_model_to_dict(self):
        """Testing to_dict method"""
        name = self.ex1.to_dict()["__class__"]
        self.assertEqual(name, "BaseModel")
        typ = type(self.ex1.updated_at)
        self.assertEqual(datetime, typ)
        typ = type(self.ex1.to_dict()["updated_at"])
        self.assertEqual(typ, str)
        typ = type(self.ex1.created_at)
        self.assertEqual(datetime, typ)
        typ = type(self.ex1.to_dict()["created_at"])
        self.assertEqual(typ, str)
        typ = type(self.ex1.to_dict())
        self.assertEqual(dict, typ)

    def test_base_model_str(self):
        """Testing __str__ method"""
        self.assertEqual(type(str(self.ex1)), str)

    def test_save_method(self):
        """Testing save method for time"""
        time = self.ex1.updated_at
        self.ex1.save()
        self.assertFalse(time == self.ex1.updated_at)

if __name__ == "__main__":
    unittest.main()
