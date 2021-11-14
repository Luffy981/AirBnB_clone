#!/usr/bin/python3
"""module for testing user class"""
import unittest
from models.user import User
from models.base_model import BaseModel
import pycodestyle
# import pep8



class TestUser(unittest.TestCase):
    """test User"""

    def test_pep8_user(self):
        """test pep8 style"""
        pep8style = pycodestyle.StyleGuide(quiet=True)
        result = pep8style.check_files(['models/user.py'])
        self.assertEqual(result.total_errors, 0,
                        "Found code style errors (and warnings).")

    def test_type_user(self):
        "test the type of attribute"
        user = User()
        self.assertEqual(type(user.email), str)
        self.assertEqual(type(user.password), str)
        self.assertEqual(type(user.first_name), str)
        self.assertEqual(type(user.last_name), str)

    def test_docstrings(self):
        """test documentation"""
        self.assertIsNotNone(User.__doc__)

    def test_instance(self):
        """check if user is an instance of BaseModel"""
        user = User()
        self.assertIsInstance(user, User)
        self.assertTrue(issubclass(type(user), BaseModel))
        self.assertEqual(str(type(user)), "<class 'models.user.User'>")

if __name__ == '__main__':
    unittest.main()

    