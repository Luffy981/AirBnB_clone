#!/usr/bin/python3
"""module for testing place class"""

import unittest
from models.place import Place
import pycodestyle
# import pep8


class Test_Place(unittest.TestCase):
    """test Place"""

    def test_pep8_state(self):
        """test pep8 style"""
        pep8style = pycodestyle.StyleGuide(quiet=True)
        result = pep8style.check_files(['models/place.py'])
        self.assertEqual(result.total_errors, 0,
                        "Found code style errors (and warnings).")

if __name__ == '__main__':
    unittest.main()