#!/usr/bin/python3
"""Module models.city with class City"""


from models.base_model import BaseModel


class City(BaseModel):
    """Class City inherits from BaseModel"""
    state_id = ""
    name = ""
