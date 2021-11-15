#!/usr/bin/python3
"""
Unit tests for Base class
"""


import unittest
from models import storage
# import pep8
import pycodestyle
from models.base_model import BaseModel


class Test_Base(unittest.TestCase):
    """Base class tests"""

    def test_1(self):
        """  Test Dictionary """
        model = BaseModel()
        model.save()
        new_object = storage.all()
        self.assertEqual(dict, type(new_object))

    def test_pep8(self):
        """Test PEP8."""
        pep8style = pycodestyle.StyleGuide(quiet=True)
        result = pep8style.check_files(['models/engine/file_storage.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")

if __name__ == '__main__':
    unittest.main()