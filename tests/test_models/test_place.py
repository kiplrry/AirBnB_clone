#!/usr/bin/python3
"""
Defines class TestPlace
"""

import unittest
from models.base_model import BaseModel
from models.place import Place
from models import storage

class TestPlace(unittest.TestCase):
    """Tests for State."""

    def setUp(self):
        self.place = Place()

    def test_is_child(self):
        self.assertTrue(issubclass(Place, BaseModel))

    def test_instance(self):
        self.assertIsInstance(self.place, Place)
        self.assertIsInstance(self.place, BaseModel)

    def test_storage(self):
        key = f"{self.place.__class__.__name__}.{self.place.id}"
        self.assertTrue(key in storage.all())# stored with name "place"

    def test_types(self):
        self.assertIsInstance(self.place.city_id, str)
        self.assertIsInstance(self.place.user_id, str)
        self.assertIsInstance(self.place.name, str)
        self.assertIsInstance(self.place.description, str)
        self.assertIsInstance(self.place.number_rooms, int)
        self.assertIsInstance(self.place.number_bathrooms, int)
        self.assertIsInstance(self.place.max_guest, int)
        self.assertIsInstance(self.place.price_by_night, int)
        self.assertIsInstance(self.place.latitude, float)
        self.assertIsInstance(self.place.longitude, float)
        self.assertIsInstance(self.place.amenity_ids, list)
