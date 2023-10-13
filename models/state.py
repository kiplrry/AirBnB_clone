#!/usr/bin/python3
"""
class State
"""
from models.base_model import BaseModel

class State(BaseModel):
    """Class State inheriting BaseModel"""
    name = ""

    def __init__(self, *args, **kwargs):
        self.name = State.name
        super().__init__(*args, **kwargs)
