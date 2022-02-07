#!/usr/bin/python3
"""Module containing class FileStorage"""


import json
import os


class FileStorage:
    """Serializes instances to a
    JSON file and deserializes JSON file to instances"""
    def __init__(self):
        """Instanciates FileStorage"""
        self.__file_path = 'file.json'
        self.__objects = {}

    def all(self):
        """Returns dictionary __objects"""
        return self.__objects

    def new(self, obj):
        """Sets in __objects the obj with key"""
        self.__objects[type(obj).__name__ + "." + obj.id] = obj

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

    def classes(self):
        from models.base_model import BaseModel
        from models.user import User
        from models.state import State
        from models.city import City
        from models.amenity import Amenity
        from models.place import Place
        from models.review import Review

        classes = {
            "BaseModel": BaseModel,
            "User": User,
            "State": State,
            "City": City,
            "Amenity": Amenity,
            "Place": Place,
            "Review": Review
            }
        return classes

    def reload(self):
        """Deserializes the JSON file to __objects"""
        classes = self.classes()
        if os.path.exists(self.__file_path):
            with open(self.__file_path, 'r') as f:
                data = json.load(f)
            for k, v in data.items():
                class_name = v["__class__"]
                self.__objects[k] = classes[class_name](**v)
