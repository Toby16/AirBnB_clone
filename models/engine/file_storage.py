#!/usr/bin/python3
import json
from models.base_model import BaseModel


class FileStorage:
    """Defines File storage class"""

    __file_path = 'file.json'
    __objects = {}

    def all(self):
        """returns the dictionary __objects"""
        return (FileStorage.__objects)

    def new(self, obj):
        """"sets in __objects the obj with key <obj class name>.id"""
        obj_name = obj.__class__.__name__
        my_key = f"{obj_name}.{obj.id}"
        FileStorage.__objects[my_key] = obj

    def save(self):
        """serializes __objects to the JSON file (path: __file_path)"""

# my_temp_dict = {k: v.to_dict() for k, v in FileStorage.__objects.items() }
        my_temp_dict = {}
        for key, value in FileStorage.__objects.items():
            my_temp_dict[key] = value.to_dict()

        with open(FileStorage.__file_path, "w") as fl:
            json.dump(my_temp_dict, fl)

    def reload(self):
        """deserializes the JSON file to __objects
        (only if the JSON file (__file_path) exists; otherwise, do nothing.
        If the file doesn’t exist, no exception should be raised)"""
        try:
            with open(FileStorage.__file_path, "r") as fl:
                my_obj = json.load(fl)
                for key, value in my_obj.items():
                    self.__objects[key] = BaseModel(**value)
        except FileNotFoundError:
            pass
