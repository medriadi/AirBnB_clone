#!/usr/bin/python3
"""Review Class Unit Tests Module"""

import unittest
from datetime import datetime
from models.base_model import BaseModel
from models.review import Review


class TestReview(unittest.TestCase):
    """TestReview Class"""

    def setUp(self):
        """Method to setup test cases"""

        pass

    def tearDown(self):
        """Method to tear down the current environment"""

        pass

    def test_init(self):
        """Method to test no kwargs init of the class"""

        obj = Review()
        self.assertIsInstance(obj, Review)
        self.assertTrue(issubclass(type(obj), BaseModel))
        self.assertIsInstance(obj.id, str)
        self.assertIsInstance(obj.created_at, datetime)
        self.assertIsInstance(obj.updated_at, datetime)
        self.assertEqual(obj.place_id, "")
        self.assertEqual(obj.user_id, "")
        self.assertEqual(obj.text, "")

    def test_init_kwargs(self):
        """Method to test init with kwargs"""

        created_at = "2023-01-01T12:00:00.000001"
        updated_at = "2023-01-01T12:30:00.000002"
        place_id = "pid"
        user_id = "uid"
        text = "text"
        obj = Review(created_at=created_at, updated_at=updated_at,
                     place_id=place_id, user_id=user_id, text=text)

        self.assertEqual(obj.created_at.isoformat(), created_at)
        self.assertEqual(obj.updated_at.isoformat(), updated_at)
        self.assertEqual(obj.place_id, place_id)
        self.assertEqual(obj.user_id, user_id)
        self.assertEqual(obj.text, text)


if __name__ == "__main__":
    unittest.main()
