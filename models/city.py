#!/usr/bin/env python3
"""
'city' class
"""
from models.base_model import BaseModel


class City(BaseModel):
    """
    class City inherited from Parent class 'BaseModel'

    Public class attrubute:
        state_id: The id of the state the city is in
        name: Name of the state
    """
    state_id = ""
    name = ""
