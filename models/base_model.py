#!/usr/bin/env python3
"""
class BaseModel
"""

import uuid  # import uuid module
import datetime  # import datetime module
import models


class BaseModel:
    """
    class BaseModel.
    A base model class with attributes to track the creation
        and modification times.

    Attributes:
        id (str): A unique identifier for the model instance.

        created_at (datetime): A timestamp representing
            the time the model instance was created.

        updated_at (datetime): A timestamp representing
            the last time the model instance was updated.
    """
    def __init__(self, *args, **kwargs):
        """
        init method.
        Initializes a new BaseModel instance.

        Arguments:
            *args - variable number of arguments.
            **kwargs - variable number of key-worded arguments.
        """
        # check if any arguments were passed in
        if kwargs:
            for key, value in kwargs.items():
                if key == "__class__":
                    continue
                elif key in ["created_at", "updated_at"]:
                    self.__dict__[key] = datetime.datetime.fromisoformat(value)
                else:
                    self.__dict__[key] = value
        else:
            # create a new ID and set created_at
            #   and updated_at to the current datetime
            self.id = str(uuid.uuid4())
            self.created_at = datetime.datetime.now()
            self.updated_at = datetime.datetime.now()
            # add a call to the method new(self) on storage
            # models.storage.new(self)

    def save(self):
        """
        Updates the 'updated_at' timestamp to the current time.
        """
        self.updated_at = datetime.datetime.now()
        models.storage.new(self)
        # call save(self) method of storage
        models.storage.save()

    def __str__(self):
        """
        returns a string representation of the BaseModel instance.
        """
        return "[{}] ({}) {}".format(self.__class__.__name__,
                                     self.id, self.__dict__)

    def to_dict(self):
        """
        Returns a dictionary representation of the BaseModel instance.
        """
        # create a copy of the object's dictionary representation
        dict_val = self.__dict__.copy()
        # add the class name to the dictionary
        dict_val.update({"__class__": self.__class__.__name__})
        # convert created_at and updated_at to isoformat strings
        #   and add them to the dictionary
        dict_val["updated_at"] = self.updated_at.isoformat()
        dict_val["created_at"] = self.created_at.isoformat()
        # return the dictionary
        return dict_val


if __name__ == "__main__":
    my_model = BaseModel()
    my_model.name = "My_First_Model"
    my_model.my_number = 89
    print(my_model.id)
    print(my_model)
    print()
    print(my_model)
    print()
    print(type(my_model.created_at))
    print("--")
    my_model_json = my_model.to_dict()
    print(my_model_json)
    print("JSON of my_model:")
    for key in my_model_json.keys():
        print("\t{}: ({}) - {}".format(
            key, type(my_model_json[key]), my_model_json[key]))

    print("--")
    my_new_model = BaseModel(**my_model_json)
    print(my_new_model.id)
    print(my_new_model)
    print(type(my_new_model.created_at))

    print("--")
    print(my_model is my_new_model)
    print("--")
    print("MY MODEL:", my_model)
    print()
    print("MY NEW MODEL:", my_new_model)
