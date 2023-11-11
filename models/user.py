#!/usr/bin/python3
"""
user module
"""
from models.base_model import BaseModel


class User(BaseModel):
    """
    User class
    """

    last_name = ""
    first_name = ""
    password = ""
    email = ""

    def __init__(self, *args, **kwargs):
        """Overriding constructor"""
        super().__init__(*args, **kwargs)
