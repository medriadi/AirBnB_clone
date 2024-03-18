#!/usr/bin/python3
"""FileStorage Class Unit Tests Module"""

import unittest
import os
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel


class TestFileStorage(unittest.TestCase):
    """TestFileStorage Class"""

    def setUp(self):
        """Method to setup test cases"""

        if os.path.exists(FileStorage._FileStorage__file_path):
            os.remove(FileStorage._FileStorage__file_path)
        self.storage = FileStorage()

    def tearDown(self):
        """Method to tear down the current environment"""

        self.reset_storage()
        pass

    def reset_storage(self):
        """Method to reset the storage's state back to empty"""

        FileStorage._FileStorage__objects = {}

        if os.path.exists(FileStorage._FileStorage__file_path):
            os.remove(FileStorage._FileStorage__file_path)

    def test_all(self):
        """Method to test all() functionality"""

        objs = self.storage.all()
        self.assertIsInstance(objs, dict)
        self.assertEqual(len(objs), 0)

    def test_new(self):
        """Method to test new() functionality"""

        obj = BaseModel()
        self.storage.new(obj)
        objs = self.storage.all()
        self.assertEqual(len(objs), 1)

    def test_save_reload(self):
        """Method to test both save() and reload() functionality"""

        self.reset_storage()
        obj = BaseModel()
        self.storage.new(obj)
        self.storage.save()
        new_storage = FileStorage()
        new_storage.reload()
        objs = new_storage.all()
        self.assertEqual(len(objs), 1)
        loaded_obj = list(objs.values())[0]
        self.assertIsInstance(loaded_obj, BaseModel)
        self.assertEqual(loaded_obj.id, obj.id)
        self.assertEqual(loaded_obj.created_at, obj.created_at)
        self.assertEqual(loaded_obj.updated_at, obj.updated_at)

    def test_save_file(self):
        """Method to test saving when the json file doesn't exist"""

        self.reset_storage()
        obj = BaseModel()
        self.storage.new(obj)
        self.storage.save()
        self.assertTrue(os.path.exists(FileStorage._FileStorage__file_path))

    def test_reload_file(self):
        """Method to test reloading when the json file doesn't exist"""

        self.reset_storage()
        self.storage.reload()
        objs = self.storage.all()
        self.assertEqual(len(objs), 0)

    def test_reload_invalid_json(self):
        """Method to test reloading invalid json data from the file"""

        self.reset_storage()
        with open(FileStorage._FileStorage__file_path,
                  "w", encoding="utf-8") as file:
            file.write("Invalid JSON Data")
        self.storage.reload()
        objs = self.storage.all()
        self.assertEqual(len(objs), 0)

    def test_classes(self):
        """Method to test the existence of a valid class in classes"""

        classes = self.storage.classes()
        self.assertIsInstance(classes, dict)
        self.assertIn("BaseModel", classes)
        self.assertIn("State", classes)
        self.assertIn("City", classes)
        self.assertIn("Amenity", classes)
        self.assertIn("Place", classes)
        self.assertIn("Review", classes)
        self.assertIn("User", classes)


if __name__ == '__main__':
    unittest.main()
