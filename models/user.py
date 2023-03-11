#!/usr/bin/env python3

from models.base_model import BaseModel

class User(BaseModel):
    """
    class 'User' that inherits from parent class - BaseModel
    """
    email = password = first_name = last_name = ""
