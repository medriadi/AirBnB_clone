#!/usr/bin/python3
"""City Class Module"""

from models.base_model import BaseModel


class City(BaseModel):
    """City class that inherits from BaseModel parent class"""

    state_id = ""
    name = ""
