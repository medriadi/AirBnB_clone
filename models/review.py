#!/usr/bin/python3
"""Review Class Module"""

from models.base_model import BaseModel


class Review(BaseModel):
    """Review class that inherits from BaseModel parent class"""

    place_id = ""
    user_id = ""
    text = ""
