#!/usr/bin/python3
"""module for testing state class"""

import unittest
from models.state import State
from models.base_model import BaseModel
from datetime import datetime
from uuid import UUID
import pep8


class Test_State(unittest.TestCase):
    """test State"""

    def test_pep8_state(self):
        """test pep8 style"""
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(['models/state.py'])
        self.assertEqual(result.total_errors, 0,
                        "Found code style errors (and warnings).")
    
    def test_instance(self):
        """check if state is an instance of BaseModel"""
        state = State()
        self.assertIsInstance(state, State)

    def test_docstrings(self):
        """test documentation"""
        self.assertIsNotNone(State.__doc__)

    def test_type_state(self):
        """Test the type of the attribute"""
        state = State()
        self.assertEqual(type(state.name), str)

    def test_hasattr(self):
        """Test if an object has an attribute"""
        state = State()
        self.assertTrue(hasattr(state, "name"))

    def test_subclass(self):
        """test if class is subclass"""
        self.assertEqual(issubclass(State, BaseModel), True)

    def test_normal_cases(self):
        """normal cases"""
        obj = State()
        obj.name = "Runspenstinski"
        obj.my_number = 29
        obj.save()
        obj_dict = obj.to_dict()
        self.assertEqual(obj.name, "Runspenstinski")
        self.assertEqual(obj.my_number, 29)
        self.assertEqual(obj.__class__.__name__, "State")
        self.assertEqual(isinstance(obj.created_at, datetime), True)
        self.assertEqual(isinstance(obj.updated_at, datetime), True)
        self.assertEqual(type(obj.__dict__), dict)

if __name__ == '__main__':
    unittest.main()