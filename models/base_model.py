#!/usr/bin/python3
"""Module models.base_model with class BaseModel"""


from datetime import datetime
import uuid


class BaseModel:
    """Class BaseModel"""

    def __init__(self):
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def save(self):
        self.updated_at = datetime.now()

    def to_dict(self):
        self.__dict__['__class__'] = BaseModel.__name__
        self.created_at = datetime.isoformat(self.created_at)
        self.updated_at = datetime.isoformat(self.updated_at)
        return self.__dict__

    def __str__(self):
        return "[{}] ({}) {}".format(BaseModel.__name__, self.id, self.__dict__)
