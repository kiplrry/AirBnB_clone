#!/usr/bin/python3
"""
Defines class TestAmenity
"""

import unittest
from models.base_model import BaseModel
from models.amenity import Amenity
from models import storage

class TestAmenity(unittest.TestCase):
    """Tests for Amenity."""

    def setUp(self):
        self.amenity = Amenity()

    def test_is_child(self):
        self.assertTrue(issubclass(Amenity, BaseModel))

    def test_instance(self):
        self.assertIsInstance(self.amenity, Amenity)
        self.assertIsInstance(self.amenity, BaseModel)

    def test_storage(self):
        key = f"{self.amenity.__class__.__name__}.{self.amenity.id}"
        self.assertTrue(key in storage.all())# stored with name "amenity"

    def test_types(self):
        self.assertIsInstance(self.amenity.name, str)
