#!/usr/bin/env python3
"""
'Place' class
"""

from models.base_model import BaseModel


class Place(BaseModel):
    """
    class State inherited form Parent class 'BaseModel'

    Public class attribute:
        city_id: it will be the City.id
        user_id: it will be the User.id
        name: name of the place.
        description: description of the place
        number_rooms: number of rooms in the place
        number_bathrooms: number of bathrooms in the place
        max_guest: maximum number of guests the place can contain
        price_by_night: price of the place at night
        latitude: latitude of the place
        longitude: longitude of the place
        amenity_ids: it will be the list of Amenity.id
    """
    city_id = ""
    user_id = ""
    name = ""
    description = ""
    number_rooms = 0
    number_bathrooms = 0
    max_guest = 0
    price_by_night = 0
    latitude = 0.0
    longitude = 0.0
    amenity_ids = []
