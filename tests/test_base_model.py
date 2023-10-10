#!/usr/bin/env python3
"""
a test for BaseModel
"""
from models.base_model import BaseModel
import unittest
import datetime

class TestBaseModel(unittest.TestCase):
    def setUp(self):
        self.model1 = BaseModel()
        self.model2 = BaseModel()

    def test_instances(self):
        self.assertIsInstance(self.model1, BaseModel)
        self.assertIsInstance(self.model2, BaseModel)
        self.assertNotEqual(self.model1, self.model2)

    def test_id(self):
        self.assertNotEqual(self.model1.id, self.model2.id)
        self.assertIsInstance(self.model1.id, str)
        self.assertIsInstance(self.model2.id, str)
    
    def test_time(self):
        self.assertIsInstance(self.model1.created_at, datetime.datetime)
        self.assertIsInstance(self.model1.updated_at, datetime.datetime)
        self.assertNotEqual(self.model1.updated_at, self.model1.created_at)
        self.model1.save()
        self.assertIsInstance(self.model1.updated_at, datetime.datetime)
        self.assertNotEqual(self.model1.updated_at, self.model1.created_at)
    
    def test_str(self):
        self.assertIsInstance(self.model1.__str__(), str)
        expected_str = f"[BaseModel] ({self.model1.id}) {self.model1.__dict__}"
        self.assertEqual(self.model1.__str__(), expected_str)

    def test_to_dict(self):
        self.assertIsInstance(self.model1.to_dict(), dict)
        dic = self.model1.to_dict()
        for key, val in self.model1.to_dict().items():
            self.assertIsInstance(val, str)
        
