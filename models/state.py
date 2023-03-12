#!/usr/bin/env python3
"""
'State' class
"""

from models.base_model import BaseModel


class State(BaseModel):
    """
    class State inherited form Parent class 'BaseModel'

    Public class attrubute:
        name: Name of the state
    """
    name = ""

    def __init__(self, *args, **kwargs):
        """
        Initializes a new instance of User.
        """
        super().__init__(*args, **kwargs)
