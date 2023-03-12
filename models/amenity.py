#!/usr/bin/env python3
"""
'Amenity' class
"""
from models.base_model import BaseModel


class Amenity(BaseModel):
    """
    class Amenity inherited from Parent class 'BaseModel'

    Public class attributes:
        name: name of the Anemity
    """
    name = ""

    def __init__(self, *args, **kwargs):
        """
        Initializes a new instance of User.
        """
        super().__init__(*args, **kwargs)
