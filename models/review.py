#!/usr/bin/python3
"""
class Review
"""
from models.base_model import BaseModel


class Review(BaseModel):
    """Class Review inheriting BaseModel"""
    place_id = ""
    user_id = ""
    text = ""

    def __init__(self, *args, **kwargs):
        self.place_id = Review.place_id
        self.user_id = Review.user_id
        self.text = Review.text
        super().__init__(*args, **kwargs)
