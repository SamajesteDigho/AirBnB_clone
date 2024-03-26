#!/usr/bin/python3
"""
    Test file for the Base Model
"""
import unittest
from models.base_model import BaseModel
from datetime import datetime


class TestBaseModel(unittest.TestCase):
    """The base testing model"""
    def test_types(self):
        """Test the type of data saved"""
        obj = BaseModel()
        self.assertTrue(isinstance(obj.id, str))
        self.assertTrue(isinstance(obj.created_at, datetime))
        self.assertTrue(isinstance(obj.updated_at, datetime))

    def test_str_repr(self):
        """Testing the string representation of the object"""
        obj = BaseModel()
        string = "[{}] ({}) {}".format(obj.__class__.__name__, obj.id,
                                       obj.__dict__)
        self.assertEqual(obj.__str__(), string)

    def test_to_dict(self):
        obj = BaseModel()
        dict_repr = {
            "__class__": obj.__class__.__name__,
            "id": obj.id,
            "created_at": obj.created_at.isoformat(),
            "updated_at": obj.updated_at.isoformat()
        }
        self.assertTrue(isinstance(obj.to_dict(), dict))
        self.assertEqual(obj.to_dict(), dict_repr)
