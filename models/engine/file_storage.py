#!/usr/bin/python3
"""FileStorage Class Module"""

from datetime import datetime
import json
import os


class FileStorage:
    """FileStorage Class"""

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Method to return the dictionary __objects"""

        return FileStorage.__objects

    def new(self, obj):
        """Method to set in __objects the obj with key <obj class name>.id"""

        key = "{}.{}".format(type(obj).__name__, obj.id)
        FileStorage.__objects[key] = obj

    def save(self):
        """
        Method to serialize __objects to
        the JSON file (path: __file_path)
        """

        with open(FileStorage.__file_path, "w", encoding="utf-8") as file:
            my_dict = {key: value.to_dict() for key,
                       value in FileStorage.__objects.items()}
            json.dump(my_dict, file)

    def reload(self):
        """
        deserializes the JSON file to __objects
        (only if the JSON file (__file_path) exists;
        otherwise, do nothing. If the file doesn't exist,
        no exception should be raised)
        """

        if not os.path.isfile(FileStorage.__file_path):
            return

        with open(FileStorage.__file_path, "r", encoding="utf-8") as file:
            try:
                my_dict = json.load(file)
            except:
                return
            my_dict = {key: self.classes()[value["__class__"]](**value)
                       for key, value in my_dict.items()}
            FileStorage.__objects = my_dict

    def classes(self):
        """Method to return a dictionary of all acceptable classes"""

        from models.base_model import BaseModel
        from models.state import State
        from models.city import City
        from models.place import Place
        from models.review import Review
        from models.amenity import Amenity
        from models.user import User

        classes = {
            "BaseModel": BaseModel,
            "State": State,
            "City": City,
            "Amenity": Amenity,
            "Place": Place,
            "Review": Review,
            "User": User
        }

        return classes
