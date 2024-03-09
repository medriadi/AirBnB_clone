#!/usr/bin/python3
"""User Class Module"""

from models.base_model import BaseModel


class User(BaseModel):
    """User class that inherits from BaseModel parent class"""

    email = ""
    password = ""
    first_name = ""
    last_name = ""
