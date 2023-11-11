#!/usr/bin/python3
"""
city module
"""
from models.base_model import BaseModel


class City(BaseModel):
    """
    City class
    """

    name = ""
    state_id = ""

    def __init__(self, *args, **kwargs):
        """Overriding constructor"""
        super().__init__(*args, **kwargs)
