#!/usr/bin/python3
"""module for testing review class"""

import unittest
from models.review import Review
import pycodestyle
# import pep8


class Test_Review(unittest.TestCase):
    """test Review"""

    def test_pep8_state(self):
        """test pep8 style"""
        pep8style = pycodestyle.StyleGuide(quiet=True)
        result = pep8style.check_files(['models/city.py'])
        self.assertEqual(result.total_errors, 0,
                        "Found code style errors (and warnings).")

if __name__ == '__main__':
    unittest.main()