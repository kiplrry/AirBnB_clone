#!/usr/bin/env python3
"""
class User that inherits from BaseModel
"""
from models.base_model import BaseModel


class User(BaseModel):
    """class User that inherits from BaseModel"""
    email = ""
    password = ""
    first_name = ""
    last_name = ""

    def __init__(self, *args, **kwargs):
        print("user created")
        super().__init__(*args, **kwargs)

    def __str__(self):
        return f"[User] ({self.id}) {self.__dict__}"