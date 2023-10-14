#!/usr/bin/python3
"""
class City
"""
from models.base_model import BaseModel


class City(BaseModel):
    """Class City inheriting BaseModel"""
    name = ""
    state_id = ""

    def __init__(self, *args, **kwargs):
        self.name = City.name
        self.state_id = City.state_id
        super().__init__(*args, **kwargs)
