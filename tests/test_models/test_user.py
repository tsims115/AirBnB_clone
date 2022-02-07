#!/usr/bin/python3
"""Unit testing for User"""

from re import U
import unittest
from models.user import User
import pep8


class TestUserClass(unittest.TestCase):
    """ Class to test User """
    def setUp(self):
        """Set up"""

    def tearDown(self):
        """Tear down"""

    def test_pep8(self):
        """
        Testing pep8 compliance.
        """
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(['models/user.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")

    def test_documentation(self):
        """
        tests for module, class, & method documentation.
        """
        # Class docstring
        self.assertTrue(len(User.__doc__) >= 1)
        # Method docstrings
        self.assertTrue(len(User.__init__.__doc__) >= 1)

if __name__ == "__main__":
    unittest.main()
