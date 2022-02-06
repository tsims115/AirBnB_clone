#!/usr/bin/python3
"""Module models.user with class User"""


from models.base_model import BaseModel


class User(BaseModel):
    """Class user inherits from BaseModel"""
    email = ""
    password = ""
    first_name = ""
    last_name = ""
