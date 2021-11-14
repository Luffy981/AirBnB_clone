#!/usr/bin/python3
"""module for testing amenity class"""

import unittest
from models.amenity import Amenity
import pycodestyle
# import pep8


class Test_Amenity(unittest.TestCase):
    """test Amenity"""

    def test_pep8_state(self):
        """test pep8 style"""
        pep8style = pycodestyle.StyleGuide(quiet=True)
        result = pep8style.check_files(['models/amenity.py'])
        self.assertEqual(result.total_errors, 0,
                        "Found code style errors (and warnings).")

if __name__ == '__main__':
    unittest.main()