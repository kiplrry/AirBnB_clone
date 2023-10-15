#!/usr/bin/python3
"""
Defines class TestUser
"""

import unittest
from models.base_model import BaseModel
from models.user import User
from models import storage


class TestUser(unittest.TestCase):
    """Tests for User."""

    def setUp(self):
        self.new_user = User()

    def test_is_child(self):
        self.assertTrue(issubclass(User, BaseModel))

    def test_instance(self):
        self.assertIsInstance(self.new_user, User)
        self.assertIsInstance(self.new_user, BaseModel)

    def test_storage(self):
        key = f"{self.new_user.__class__.__name__}.{self.new_user.id}"
        self.assertTrue(key in storage.all())  # stored with name "user"

    def test_types(self):
        self.assertIsInstance(self.new_user.password, str)
        self.assertIsInstance(self.new_user.email, str)
        self.assertIsInstance(self.new_user.first_name, str)
        self.assertIsInstance(self.new_user.last_name, str)
