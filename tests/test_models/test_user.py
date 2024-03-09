#!/usr/bin/python3
"""User Class Unit Tests Module"""

import unittest
from datetime import datetime
from models.base_model import BaseModel
from models.user import User

import unittest


class TestUser(unittest.TestCase):
    """TestUser Class"""

    def setUp(self):
        """Method to setup test cases"""

        pass

    def tearDown(self):
        """Method to tear down the current environment"""

        pass

    def test_init(self):
        """Method to test no kwargs init of the class"""

        obj = User()
        self.assertIsInstance(obj, User)
        self.assertTrue(issubclass(type(obj), BaseModel))
        self.assertIsInstance(obj.id, str)
        self.assertIsInstance(obj.created_at, datetime)
        self.assertIsInstance(obj.updated_at, datetime)
        self.assertEqual(obj.email, "")
        self.assertEqual(obj.password, "")
        self.assertEqual(obj.first_name, "")
        self.assertEqual(obj.last_name, "")

    def test_init_kwargs(self):
        """Method to test init with kwargs"""

        created_at = "2023-01-01T12:00:00.000001"
        updated_at = "2023-01-01T12:30:00.000002"
        email = "email"
        password = "password"
        first_name = "first name"
        last_name = "last name"
        obj = User(created_at=created_at, updated_at=updated_at, email=email,
                   password=password, first_name=first_name,
                   last_name=last_name)

        self.assertEqual(obj.created_at.isoformat(), created_at)
        self.assertEqual(obj.updated_at.isoformat(), updated_at)
        self.assertEqual(obj.email, email)
        self.assertEqual(obj.password, password)
        self.assertEqual(obj.first_name, first_name)
        self.assertEqual(obj.last_name, last_name)


if __name__ == "__main__":
    unittest.main()
