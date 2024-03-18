#!/usr/bin/python3
"""BaseModel Class Unit Tests Module"""

import unittest
import time
from datetime import datetime
from models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):
    """TestBaseModel Class"""

    def setUp(self):
        """Method to setup test cases"""

        pass

    def tearDown(self):
        """Method to tear down the current environment"""

        pass

    def test_init(self):
        """Method to test no kwargs init of the class"""

        obj = BaseModel()
        self.assertIsInstance(obj.id, str)
        self.assertIsInstance(obj.created_at, datetime)
        self.assertIsInstance(obj.updated_at, datetime)

    def test_init_kwargs(self):
        """Method to test init with kwargs"""

        created_at = "2023-01-01T12:00:00.000001"
        updated_at = "2023-01-01T12:30:00.000002"
        obj = BaseModel(created_at=created_at, updated_at=updated_at)

        self.assertEqual(obj.created_at.isoformat(), created_at)
        self.assertEqual(obj.updated_at.isoformat(), updated_at)

    def test_save(self):
        """Method to test the save functionality"""

        obj = BaseModel()
        old_time = obj.updated_at
        time.sleep(0.8)
        obj.save()
        new_time = obj.updated_at

        self.assertGreater(new_time, old_time)

    def test_to_dict(self):
        """Method to test the to_dict functionality"""

        obj = BaseModel()
        obj_dict = obj.to_dict()
        keys = ['id', 'created_at', 'updated_at', '__class__']

        for key in keys:
            self.assertIn(key, obj_dict)


if __name__ == '__main__':
    unittest.main()
