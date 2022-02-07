#!/usr/bin/python3
"""Unit testing for FileStorage"""

import unittest
from models.engine.file_storage import FileStorage
import pep8


class TestBaseClass(unittest.TestCase):
    """ Class to test FileStorage """
    def setUp(self):
        """Set up"""

    def tearDown(self):
        """Tear down"""

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

if __name__ == "__main__":
    unittest.main()
