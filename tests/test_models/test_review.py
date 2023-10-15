#!/usr/bin/python3
"""
Defines class TestReview
"""

import unittest
from models.base_model import BaseModel
from models.review import Review
from models import storage


class TestReview(unittest.TestCase):
    """Tests for Review."""

    def setUp(self):
        self.review = Review()

    def test_is_child(self):
        self.assertTrue(issubclass(Review, BaseModel))

    def test_instance(self):
        self.assertIsInstance(self.review, Review)
        self.assertIsInstance(self.review, BaseModel)

    def test_storage(self):
        key = f"{self.review.__class__.__name__}.{self.review.id}"
        self.assertTrue(key in storage.all())  # stored with name "review"

    def test_types(self):
        self.assertIsInstance(self.review.place_id, str)
        self.assertIsInstance(self.review.user_id, str)
        self.assertIsInstance(self.review.text, str)
