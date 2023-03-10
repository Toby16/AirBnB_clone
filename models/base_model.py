#!/usr/bin/python3
"""Basemodel class is defined here"""

from uuid import uuid4
import datetime
import models


class BaseModel:
    """This is basemodel class"""

    def __init__(self, *args, **kwargs):
        """Initialization of the instance
            Args:
                *args = argument variables
                **kwargs = keyword variables
            Raises:
                none        """
        my_dict = {}
        if kwargs is not None and len(kwargs) != 0:
            for key, value in kwargs.items():
                if key == "__class__":
                    continue
                if key == "created_at" or key == "updated_at":
                    self.__dict__[key] = datetime.datetime.fromisoformat(value)
                    # my_dict[key] = value
                else:
                    self.__dict__[key] = value
        else:
            self.id = str(uuid4())
            self.created_at = datetime.datetime.now()
            self.updated_at = datetime.datetime.now()
            # models.storage.new(self)

    def __str__(self):
        """This is the print model of the Basemodel"""
        cls_name = self.__class__.__name__
        str_result = ("[{}] ({}) {}".format(cls_name, self.id, self.__dict__))

        return(str_result)

    def save(self):
        """save(self): updates the public instance
        attribute updated_at with the current datetime
        """
        self.updated_at = datetime.datetime.now()
        models.storage.new(self)
        models.storage.save()

    def to_dict(self):
        """This returns a dictionary containing all keys/values of
        __dict__ of the instance: """
        dict_temp_file = self.__dict__.copy()
        dict_temp_file["created_at"] = self.created_at.isoformat()
        dict_temp_file["updated_at"] = self.updated_at.isoformat()
        dict_temp_file["__class__"] = self.__class__.__name__

        return(dict_temp_file)
