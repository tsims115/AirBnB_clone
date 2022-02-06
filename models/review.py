#!/usr/bin/python3
"""Module models.review with class Review"""


from models.base_model import BaseModel


class Review(BaseModel):
    """Class Review inherits from BaseModel"""
    place_id = ""
    user_id = ""
    text = ""
