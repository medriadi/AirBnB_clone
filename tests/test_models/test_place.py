#!/usr/bin/python3
"""Place Class Unit Tests Module"""

import unittest
from datetime import datetime
from models.base_model import BaseModel
from models.place import Place


class TestPlace(unittest.TestCase):
    """TestPlace Class"""

    def setUp(self):
        """Method to setup test cases"""

        pass

    def tearDown(self):
        """Method to tear down the current environment"""

        pass

    def test_init(self):
        """Method to test no kwargs init of the class"""

        obj = Place()
        self.assertIsInstance(obj, Place)
        self.assertTrue(issubclass(type(obj), BaseModel))
        self.assertIsInstance(obj.id, str)
        self.assertIsInstance(obj.created_at, datetime)
        self.assertIsInstance(obj.updated_at, datetime)
        self.assertEqual(obj.city_id, "")
        self.assertEqual(obj.user_id, "")
        self.assertEqual(obj.name, "")
        self.assertEqual(obj.description, "")
        self.assertEqual(obj.number_rooms, 0)
        self.assertEqual(obj.number_bathrooms, 0)
        self.assertEqual(obj.max_guest, 0)
        self.assertEqual(obj.price_by_night, 0)
        self.assertEqual(obj.latitude, 0.0)
        self.assertEqual(obj.longitude, 0.0)
        self.assertEqual(obj.amenity_ids, [])

    def test_init_kwargs(self):
        """Method to test init with kwargs"""

        created_at = "2023-01-01T12:00:00.000001"
        updated_at = "2023-01-01T12:30:00.000002"
        city_id = "NYC"
        user_id = "123"
        name = "Cozy Apartment"
        description = "A cozy apartment in the heart of the city."
        number_rooms = 2
        number_bathrooms = 1
        max_guest = 4
        price_by_night = 100
        latitude = 40.7128
        longitude = -74.0060
        amenity_ids = ["wifi", "pool"]
        place = Place(
                created_at=created_at,
                updated_at=updated_at,
                city_id=city_id,
                user_id=user_id,
                name=name,
                description=description,
                number_rooms=number_rooms,
                number_bathrooms=number_bathrooms,
                max_guest=max_guest,
                price_by_night=price_by_night,
                latitude=latitude,
                longitude=longitude,
                amenity_ids=amenity_ids
        )
        self.assertEqual(place.created_at.isoformat(), created_at)
        self.assertEqual(place.updated_at.isoformat(), updated_at)
        self.assertEqual(place.city_id, city_id)
        self.assertEqual(place.user_id, user_id)
        self.assertEqual(place.name, name)
        self.assertEqual(place.description, description)
        self.assertEqual(place.number_rooms, number_rooms)
        self.assertEqual(place.number_bathrooms, number_bathrooms)
        self.assertEqual(place.max_guest, max_guest)
        self.assertEqual(place.price_by_night, price_by_night)
        self.assertEqual(place.latitude, latitude)
        self.assertEqual(place.longitude, longitude)
        self.assertEqual(place.amenity_ids, amenity_ids)


if __name__ == "__main__":
    unittest.main()
