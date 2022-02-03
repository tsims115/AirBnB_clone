#!/usr/bin/python3
"""Module models.base_model with class BaseModel"""


from datetime import datetime
import uuid
from models import storage


class BaseModel:
    """Class BaseModel"""

    def __init__(self, *args, **kwargs):
        """Instanciates with current time and unique ID"""
        if kwargs:
            for k, v in kwargs.items():
                if k == 'created_at' or k == 'updated_at':
                    v = datetime.fromisoformat(v)
                if k == '__class__':
                    continue
                setattr(self, k, v)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
        storage.new(self)

    def save(self):
        """Saves new time"""
        self.updated_at = datetime.now()
        storage.save()

    def to_dict(self):
        """Creates dictionary with key/values of __dict__ of
        instance"""
        new_dict = {}
        for key, value in self.__dict__.items():
            new_dict[key] = value
        new_dict['__class__'] = type(self).__name__
        new_dict['created_at'] = datetime.isoformat(self.created_at)
        new_dict['updated_at'] = datetime.isoformat(self.updated_at)
        return new_dict

    def __str__(self):
        """Return string format of Object"""
        return "[{}] ({}) {}".format(type(self).__name__, self.id, self.__dict__)
