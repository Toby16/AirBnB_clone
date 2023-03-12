#!/usr/bin/env python3
"""
'Review' class
"""

from models.base_model import BaseModel


class Review(BaseModel):
    """
    class Review inherited from Parent class 'BaseModel'

    Public instance attributes:
        place_id: it will be the Place.id
        user_id: it will be the User.id
        text: review of place
    """
    place_id = ""
    user_id = ""
    text = ""

    def __init__(self, *args, **kwargs):
        """
        Initializes a new instance of User.
        """
        super().__init__(*args, **kwargs)
