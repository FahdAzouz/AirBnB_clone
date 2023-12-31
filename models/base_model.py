#!/usr/bin/python3
"""
base_model module
"""
import datetime
import uuid
from models import storage


class BaseModel:
    """
    BaseModel class
    """

    def __init__(self, *args, **kwargs):
        """initialization"""
        if kwargs is not None and kwargs != {}:
            for key, value in kwargs.items():
                if key != "__class__":
                    if key in ('created_at', 'updated_at'):
                        setattr(self, key, datetime.datetime.fromisoformat(value))
                    else:
                        setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.datetime.now()
            self.updated_at = self.created_at
            storage.new(self)

    def save(self):
        """updates the public instance attribute
        updated_at with the current datetime"""
        self.updated_at = datetime.datetime.now()
        storage.save()

    def to_dict(self):
        """returns a dictionary containing all keys/vlues
        of __dict__ of the instance"""
        my_dict = self.__dict__.copy()
        my_dict["__class__"] = type(self).__name__
        my_dict["updated_at"] = my_dict["updated_at"].isoformat()
        my_dict["created_at"] = my_dict["created_at"].isoformat()
        return my_dict

    def __str__(self):
        """returns string representation"""
        return "[{}] ({}) {}".\
            format(type(self).__name__, self.id, self.__dict__)
