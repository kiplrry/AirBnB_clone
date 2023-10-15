#!/usr/bin/python3
"""
class Place
"""
from models.base_model import BaseModel


class Place(BaseModel):
    """Class Place inheriting BaseModel"""
    city_id = ""
    name = ""
    user_id = ""
    description = ""
    number_rooms = 0
    number_bathrooms = 0
    max_guest = 0
    price_by_night = 0
    latitude = 0.0
    longitude = 0.0
    amenity_ids = []

    def __init__(self, *args, **kwargs):
        self.city_id = Place.city_id
        self.name = Place.name
        self.user_id = Place.user_id
        self.description = Place.description
        self.number_rooms = Place.number_rooms
        self.number_bathrooms = Place.number_bathrooms
        self.max_guest = Place.max_guest
        self.price_by_night = Place.price_by_night
        self.latitude = Place.latitude
        self.longitude = Place.longitude
        self.amenity_ids = Place.amenity_ids

        super().__init__(*args, **kwargs)
