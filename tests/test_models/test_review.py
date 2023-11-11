#!/usr/bin/python3
"""
test_city module
"""
import pycodestyle
from unittest import TestCase
from models.city import City


class TestReview(TestCase):
    """
    TestReview class
    """

    def test_pep(self):
        """test pep"""
        style = pycodestyle.StyleGuide(quiet=True)
        result = style.check_files(['models/review.py',
                                    'tests/test_models/test_review.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")

    def test_class_doc(self):
        """test class documentation"""
        doc = Review.__doc__
        self.assertGreater(len(doc), 1)

    def test_module_doc(self):
        """test module documentation"""
        doc = __import__('models.review').__doc__
        self.assertGreater(len(doc), 1)
