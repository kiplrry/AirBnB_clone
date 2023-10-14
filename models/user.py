#!/usr/bin/python3
"""class User that inherits from BaseModel"""
from models.base_model import BaseModel


class User(BaseModel):
    """class User that inherits from BaseModel"""
    email = ""
    password = ""
    first_name = ""
    last_name = ""

    def __init__(self, *args, **kwargs):
        self.email = User.email
        self.password = User.password
        self.first_name = User.first_name
        self.last_name = User.last_name

        super().__init__(*args, **kwargs)
