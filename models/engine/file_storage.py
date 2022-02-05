#!/usr/bin/python3
"""Module containing class FileStorage"""


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
        self.__objects[obj.id] = obj

    def save(self):
        """Serializes __objects to the JSON file"""
        new_dict = {}
        for k, v in self.__objects.items():
            new_dict[k] = v.to_dict()
        json_string = json.dumps(new_dict)
        with open(self.__file_path, 'w+') as f:
            data = f.read()
            f.seek(0)
            f.write(json_string)
            f.truncate()

    def reload(self):
        """Deserializes the JSON file to __objects"""
        from models.base_model import BaseModel
        if os.path.exists(self.__file_path):
            with open(self.__file_path, 'r') as f:
                data = json.load(f)
            for k, v in data.items():
                self.__objects[k] = BaseModel(**v)
            
