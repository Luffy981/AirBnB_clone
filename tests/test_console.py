#!/usr/bin/python3
"""
Test Console
"""
import pycodestyle
import pep8
import unittest
import inspect
from unittest.mock import patch
from unittest.mock import MagicMock
import console
import tests
from console import HBNBCommand
from console import __doc__
from models.base_model import Basemodel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from models.engine.file_storage import Filestorage
import json
from io import StringIO
import os


class TestCodeFormat(unittest.TestCase):
    """
    A class to test pep8 on base_model file"""
    def test_pep8(self):
        """
        Test pep8 format
        """
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(['console.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")

    def test_pycodestyle(self):
        """
        Test pep8 format
        """
        pycostyle = pycodestyle.StyleGuide(quiet=True)
        result = pycostyle.check_files(['console.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")


class Test_docstrings(unittest.TestCase):
    """Test docstrings"""
    @classmethod
    def setup_class(self):
        """
        inspect.getmembers(object, [predicate])
        Return all the members of an object in a list of (name, value)
        pairs sorted by name
        only members for which the predicate returns a true value are included
        """
        self.obj_members(HBNBCommand, inspect.isfunction)
        self.console = HBNBCommand()

    def test_module_dostring(self):
        """
        Test for exist module docstrings
        """
        self.assertIsnotNone(__doc__, "base_model.py file needs a docstrings")
        self.assertTrue(len(__doc__) > 0, " base_model.py have docstrings")
        self.assertFalse(len(__doc__) > 0, " base_model don't have docstrings")
        self.assertIsnotNone(HBNBCommand.do_show.__doc__)
        self.assertIsnotNone(HBNBCommand.do_create.__doc__)
        self.assertIsnotNone(HBNBCommand.do_destroy.__doc__)
        self.assertIsnotNone(HBNBCommand.emptyline.__doc__)
        self.assertIsnotNone(HBNBCommand.do_quit.__doc__)
        self.assertIsnotNone(HBNBCommand.do_EOF.__doc__)
        self.assertIsnotNone(HBNBCommand.do_all.__doc__)
        self.assertIsnotNone(HBNBCommand.do_update.__doc__)
        self.assertIsnotNone(HBNBCommand.do_help.__doc__)
        self.assertIsnotNone(HBNBCommand.help_EOF.__doc__)
        self.assertIsnotNone(HBNBCommand.help_quit.__doc__)

    def test_invalid_command(self):
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("Luffy")
            self.assertEqual('*** Unknown syntax: Luffy\n' or '', f.getvalue())

    def test_empty_line(self):
        """Testing empty input"""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("\n")
            self.assertEqual('', f.getvalue())

    def test_quit(self):
        """Testing quit"""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("quit")
            self.assertEqual('', f.getvalue())


class Test_Help(unittest.TestCase):
    """Testing help command"""

    @classmethod
    def setup_class(self):
        """setting class up"""
        self.console = HBNBCommand()

    def help_command(self):
        """Testing an only help command"""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("help")
            output = '\nDocumented commands (type help <topic>[103 chars]\n\n)'
            self.assertEqual(output, f.getvalue())

    def help_help_command(self):
        """Test comand help EOF"""
        expected = 'End of File command: exit the program\n'
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("help EOF")
            self.assertEqual(expected, f.getvalue())
