#!/usr/bin/python3
"""Module containing class FileStorage"""


"""from models.base_model import BaseModel"""
import json
import os

class FileStorage:
    """Serializes instances to a
    JSON file and deserializes JSON file to instances"""
    def __init__(self):
        self.__file_path = 'file.json'
        self.__objects = {}
    
    def all(self):
        """Returns dictionary __objects"""
        return self.__objects

    def new(self, obj):
        """Sets in __objects the obj with key"""
        self.__objects[type(obj).__name__] = obj.to_dict()

    def save(self):
        """Serializes __objects to the JSON file"""
        json_string = json.dumps(self.__objects)
        with open(self.__file_path, 'w+') as f:
            data = f.read()
            f.seek(0)
            f.write(json_string)
            f.truncate()

    def reload(self):
        """Deserializes the JSON file to __objects"""
        if os.path.exists(self.__file_path):
            with open(self.__file_path, 'r') as f:
                self.__objects = json.load(f)
