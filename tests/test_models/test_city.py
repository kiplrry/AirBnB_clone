#!/usr/bin/python3
"""
Defines class TestCity
"""

import unittest
from models.base_model import BaseModel
from models.city import City
from models import storage

class TestCity(unittest.TestCase):
    """Tests for City."""

    def setUp(self):
        self.city = City()

    def test_is_child(self):
        self.assertTrue(issubclass(City, BaseModel))

    def test_instance(self):
        self.assertIsInstance(self.city, City)
        self.assertIsInstance(self.city, BaseModel)

    def test_storage(self):
        key = f"{self.city.__class__.__name__}.{self.city.id}"
        self.assertTrue(key in storage.all())# stored with name "city"

    def test_types(self):
        self.assertIsInstance(self.city.name, str)
        self.assertIsInstance(self.city.state_id, str)
