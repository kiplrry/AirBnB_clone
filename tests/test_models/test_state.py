#!/usr/bin/python3
"""
Defines class TestState
"""

import unittest
from models.base_model import BaseModel
from models.state import State
from models import storage

class TestState(unittest.TestCase):
    """Tests for State."""

    def setUp(self):
        self.state = State()

    def test_is_child(self):
        self.assertTrue(issubclass(State, BaseModel))

    def test_instance(self):
        self.assertIsInstance(self.state, State)
        self.assertIsInstance(self.state, BaseModel)

    def test_storage(self):
        key = f"{self.state.__class__.__name__}.{self.state.id}"
        self.assertTrue(key in storage.all())# stored with name "state"

    def test_types(self):
        self.assertIsInstance(self.state.name, str)
