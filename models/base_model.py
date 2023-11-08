#!/usr/bin/python3
"""
base model module
"""
import uuid
import datetime
from models import storage


class BaseModel():
    """
    base class for all other classes
    """
    def __init__(self, *args, **kwargs):
        """
        initialization
        """
        if kwargs is not None and kwargs != {}:
            for key, value in kwargs.items():
                if key is not "__class__":
                    if key in ('created_at', 'updated_at'):
                        setattr(self, key,
                                datetime.datetime.fromisoformat(value))
                    else:
                        setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.datetime.now()
            self.updated_at = self.created_at
            storage.new(self)

    def save(self):
        """
        updates last change time
        """
        self.updated_at = datetime.datetime.now()
        storage.save()

    def __str__(self):
        """
        override str function
        """
        return "[{}] ({}) {}".\
            format(type(self).__name__, self.id, self.__dict__)

    def to_dict(self):
        """
        returns a dictionary containing all key/values of __dict__
        """
        my_dict = self.__dict__.copy()
        my_dict["__class__"] = type.(self).__name__
        my_dict["updated_at"] = my_dict["updated_at"].isoformat()
        my_dict["created_at"] = my_dict["created_at"].isoformat()
