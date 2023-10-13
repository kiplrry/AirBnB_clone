#!/usr/bin/python3
"""
class Amenity
"""
from models.base_model import BaseModel

class Amenity(BaseModel):
    """Class Amenity inheriting BaseModel"""
    name = ""

    def __init__(self, *args, **kwargs):
        self.name = Amenity.name
        super().__init__(*args, **kwargs)
