#!/usr/bin/python3
"""
test_console module
"""
import pycodestyle
from console import HBNBCommand
from unitest import TestCase


class TestHBNBCommandd(TestCase):
    """
    class TestHBNBCommand
    """

    def test_pep(self):
        """
        test pep
        """
        style = pycodestyle.StyleGuide(quiet=True)
        result = style.check_files(['console.py',
                                    'tests/test_console.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")

    def test_class_doc(self):
        """test class documentation"""
        doc = HBNBCommand.__doc__
        self.assertGreater(len(doc), 1)

    def test_module_doc(self):
        """
        test module documentation
        """
        doc = __import__('console').__doc__
        self.assertGreater(len(doc), 1)
