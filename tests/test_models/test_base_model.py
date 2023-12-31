#!/usr/bin/python3
"""
test_base_model module
"""
from models.base_model import BaseModel
import pycodestyle
from time import sleep
from datetime import datetime
from uuid import uuid4
from unittest import TestCase


class TestBaseModel(TestCase):
    """
    Test cases for the BaseModel class
    """

    def test_str_doc(self):
        """test str functiom documentation"""
        doc = BaseModel.__str__.__doc__
        self.assertGreater(len(doc), 1)

    def test_save_doc(self):
        """test save method documentation"""
        doc = BaseModel.save.__doc__
        self.assertGreater(len(doc), 1)

    def test_init_doc(self):
        """test init method documentation"""
        doc = BaseModel.__init__.__doc__
        self.assertGreater(len(doc), 1)

    def test_class_doc(self):
        """test class documentation"""
        doc = BaseModel.__doc__
        self.assertGreater(len(doc), 1)

    def test_module_doc(self):
        """test module documentation"""
        doc = __import__("models.base_model").__doc__
        self.assertGreater(len(doc), 1)

    def test_pep(self):
        """test pep"""
        style = pycodestyle.StyleGuide(quiet=True)
        result = style.check_files(['models/base_model.py',
                                    'tests/test_models/test_base_model.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")

    def test_save(self):
        """test save method"""
        instance = BaseModel()
        sleep(1)

        now = datetime.now().replace(microsecond=0)
        instance.save()
        self.assertEqual(instance.updated_at.replace(microsecond=0), now)

    def test_to_dict_doc(self):
        """test to_dict method documentation"""
        doc = BaseModel.to_dict.__doc__
        self.assertGreater(len(doc), 1)

    def test_init(self):
        """test init method"""
        instance = BaseModel()

        self.assertIsInstance(instance, BaseModel)
        self.assertIsInstance(instance.id, str)
        self.assertIsInstance(instance.updated_at, datetime)
        self.assertIsInstance(instance.created_at, datetime)

    def test_to_dict(self):
        """test to_dict method"""
        instance = BaseModel()
        instance.name = "Holberton"
        instance.my_number = 89

        output = instance.to_dict()

        self.assertIsInstance(output, dict)

        o_id = output['id']
        updated_at = output['updated_at']
        created_at = output['created_at']
        class_name = output['__class__']
        name = output['name']
        my_number = output['my_number']

        self.assertIsInstance(o_id, str)
        self.assertIsInstance(updated_at, str)
        self.assertIsInstance(created_at, str)
        self.assertIsInstance(class_name, str)
        self.assertIsInstance(name, str)
        self.assertIsInstance(my_number, int)
