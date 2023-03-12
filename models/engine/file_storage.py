#!/usr/bin/env python3

import json
import os
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class FileStorage:
    """
    Class for storing and retrieving objects to/from a JSON file.
    """
    __classes = {
            "BaseModel": BaseModel,
            "User": User,
            "State": State,
            "City": City,
            "Amenity": Amenity,
            "Place": Place,
            "Review": Review
            }

    def __init__(self):
        """
        Initializes the file path and objects dictionary.
        """
        self.__file_path = "file.json"
        self.__objects = {}

    def all(self):
        """
        Returns the dictionary of objects.
        """
        return self.__objects

    def new(self, obj):
        """
        Adds a new object to the dictionary.
        Args:
            obj: An object to be added to the dictionary.
        """
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        self.__objects[key] = obj

    def save(self):
        """
        Saves the dictionary of objects to a JSON file.
        The objects are converted to dictionaries
            using their `to_dict` method before being saved.
        """
        with open(self.__file_path, "w", encoding="utf-8") as file:
            dict_value = {key: value.to_dict() for key,
                          value in self.__objects.items()}
            json.dump(dict_value, file)

    def reload(self):
        """
        Loads the dictionary of objects from a JSON file.
        The objects are created from dictionaries
            using their respective class constructors.
        """
        # check if the file path exists
        if os.path.exists(self.__file_path):
            with open(self.__file_path, "r", encoding="utf-8") as file:
                # load the json data into a dictionary
                object_dict = json.load(file)
                for key, value in object_dict.items():
                    class_name, obj_id = key.split(".")
                    obj_cls = self.__classes.get(class_name)
                    if obj_cls is not None:
                        self.__objects[key] = obj_cls(**value)
