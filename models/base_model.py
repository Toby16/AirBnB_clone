#!/usr/bin/env python3
"""
class BaseModel
"""

import uuid  # import uuid module
import datetime  # import datetime module


class BaseModel:
    """
    class BaseModel
    """
    def __init__(self):
        """
        init method
        """
        self.id = str(uuid.uuid4())
        self.created_at = datetime.datetime.now()
        self.updated_at = self.created_at

    def save(self):
        self.updated_at = datetime.datetime.now()

    def __str__(self):
        return "[{}] ({}) ({})".format(self.__class__.__name__,
                                       self.id, self.__dict__)

    def to_dict(self):
        dict_val = self.__dict__.copy()
        dict_val.update({"__class__": self.__class__.__name__})
        dict_val["updated_at"] = self.updated_at.isoformat()
        dict_val["created_at"] = self.created_at.isoformat()
        return dict_val


if __name__ == "__main__":
    my_model = BaseModel()
    my_model.name = "My First Model"
    my_model.my_number = 89
    print(my_model)
    my_model.save()
    print(my_model)
    my_model_json = my_model.to_dict()
    print(my_model_json)
    print("JSON of my_model:")
    for key in my_model_json.keys():
        print("\t{}: ({}) - {}".format(key, type(my_model_json[key]),
                                       my_model_json[key]))

    print()
    print(my_model)
