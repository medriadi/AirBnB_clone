#!/usr/bin/python3
"""Console Entry Point Unit Tests Module"""

import os
import unittest
from unittest.mock import patch
from io import StringIO
from models.base_model import BaseModel
from models import storage
from console import HBNBCommand
from models.engine.file_storage import FileStorage


class TestHBNBCommand(unittest.TestCase):
    """TestHBNBCommand Class"""

    def setUp(self):
        """Method to setup test cases"""

        self.command = HBNBCommand()

    def tearDown(self):
        """Method to tear down the current environment"""

        del self.command
        self.reset_storage()
        pass

    def reset_storage(self):
        """Method to reset the storage's state back to empty"""
        FileStorage._FileStorage__objects = {}

        if os.path.exists(FileStorage._FileStorage__file_path):
            os.remove(FileStorage._FileStorage__file_path)

    def test_create(self):
        """Method to test do_create functionality"""

        with patch('sys.stdout', new=StringIO()) as f:
            self.command.onecmd("create BaseModel")
            self.assertTrue(f.getvalue().strip() != "")

    def test_show(self):
        """Method to test do_show functionality"""

        obj = BaseModel()
        key = "{}.{}".format(type(obj).__name__, obj.id)

        with patch('sys.stdout', new=StringIO()) as f:
            self.command.onecmd("show BaseModel {}".format(obj.id))
            self.assertTrue(f.getvalue().strip() != "")
            self.assertEqual(f.getvalue().strip(), str(obj))

    def test_destroy(self):
        """Method to test do_destroy functionality"""

        obj = BaseModel()
        key = "{}.{}".format(type(obj).__name__, obj.id)

        with patch('sys.stdout', new=StringIO()) as f:
            self.command.onecmd("destroy BaseModel {}".format(obj.id))
            self.assertTrue(key not in storage.all())

    def test_all(self):
        """Method to test do_all functionality"""

        with patch('sys.stdout', new=StringIO()) as f:
            self.command.onecmd("all")
            self.assertTrue(f.getvalue().strip() != "")

    def test_update(self):
        """Method to test do_update functionality"""

        obj = BaseModel()
        key = "{}.{}".format(type(obj).__name__, obj.id)

        with patch('sys.stdout', new=StringIO()) as f:
            self.command.onecmd("update BaseModel {} name test".format(obj.id))
            self.assertEqual(obj.name, "test")

    def test_count(self):
        """Method to test count functionality"""

        obj = BaseModel()

        with patch('sys.stdout', new=StringIO()) as f:
            self.command.onecmd("BaseModel.count()")
            self.assertEqual(int(f.getvalue().strip()), 1)


if __name__ == '__main__':
    unittest.main()
