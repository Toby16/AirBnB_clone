#!/usr/bin/env python3

from models.base_model import BaseModel


class City(BaseModel):
    """
    class City inherited form Parent class 'BaseModel'

    Public class attrubute:
        state_id: The id of the state the city is in
        name: Name of the state
    """
    state_id = ""
    name = ""
