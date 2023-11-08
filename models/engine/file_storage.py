#!/usr/bin/python3
"""
File storage class
"""
from models import BaseModel
import json
import datetime
import os


class FileStorage:
    """
    serializes instances to a JSON file and vice versa
    """
    __file_path = self.__name__ + ".json"
    __objects = {}

    def all(self):
        """
        returns the dictionary __objects
        """
        return self.__objects

    def new(self, obj):
        """
        sets in __objects the obj with key <obj class name>.id
        """
        self.__objects["{}.{}"
                       .format(type(obj).__name__, obj.id)] = obj

    def save(self):
        """
        serializes __objects to the JSON file
        """
        with open(self.__file_path, mode="w") as f:
            dict_storage = {k: v.to_dict() for k, v in self.__objects.items()}
            json.dump(dict_storage, f)
    
    def reload(self):
        """
        deserializes the JSON file to __objects
        """
        if not os.path.isfile(FileStorage.__file_path):
            return
        with open(FileStorage.__file_path, mode="r", encoding="utf-8") as f:
            obj_dict = json.load(f)
            obj_dict = {k: self.classes()[v["__class__"]]
                        (**v) for k, v in obj_dict.items()}
            FileStorage.__objects = obj_dict

    def classes(self):
        """
        Returns a dictionary of valid classes and their references.
        """
        

    
