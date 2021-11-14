#!/usr/bin/python3
"""module for testing city class"""

import unittest
from models.city import City
import pycodestyle
# import pep8


class Test_City(unittest.TestCase):
    """test City"""

    def test_pep8_state(self):
        """test pep8 style"""
        pep8style = pycodestyle.StyleGuide(quiet=True)
        result = pep8style.check_files(['models/city.py'])
        self.assertEqual(result.total_errors, 0,
                        "Found code style errors (and warnings).")

if __name__ == '__main__':
    unittest.main()