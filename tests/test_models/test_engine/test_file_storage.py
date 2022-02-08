#!/usr/bin/python3
"""Unit testing for FileStorage"""

import unittest
from models.engine.file_storage import FileStorage
import pep8
import json
import sys
from models.base_model import BaseModel
from models import storage


class TestFileStorageClass(unittest.TestCase):
    """ Class to test FileStorage """
    def setUp(self):
        """Set up"""
        self.ex1 = FileStorage()
        self.model = BaseModel()
        storage.save()

    def tearDown(self):
        """Tear down"""
        del self.ex1
        del self.model

    def test_pep8(self):
        """
        Testing pep8 compliance.
        """
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(['models/engine/file_storage.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")

    def test_documentation(self):
        """
        tests for module, class, & method documentation.
        """
        # Class docstring
        self.assertTrue(len(FileStorage.__doc__) >= 1)
        # Method docstrings
        self.assertTrue(len(FileStorage.__init__.__doc__) >= 1)

    def test_file_storage_reload_all(self):
        """Tests reload method"""
        self.assertEqual(self.ex1.all(), {})
        self.ex1.reload()
        with open("file.json", 'r') as f:
            data = json.load(f)
        if data == {}:
            self.assertEqual(data, self.ex1.all())
        self.assertTrue(data.keys() == self.ex1.all().keys())
        num = "BaseModel" + "." + self.model.id
        self.assertTrue(num in data.keys())

if __name__ == "__main__":
    unittest.main()