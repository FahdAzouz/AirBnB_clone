#!/usr/bin/python3
"""
place module
"""
from models.base_model import BaseModel


class Place(BaseModel):
    """
    Place class
    """

    city_id = ""
    user_id = ""
    name = ""
    price_by_night = 0
    latitude = 0.0
    longitude = 0.0
    amenity_ids = []
    description = ""
    number_rooms = 0
    number_bathrooms = 0
    max_guest = 0

    def __init__(self, *args, **kwargs):
        """Overriding constructor"""
        super().__init__(*args, **kwargs)