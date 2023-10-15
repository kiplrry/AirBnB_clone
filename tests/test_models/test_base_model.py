#!/usr/bin/env python3
"""
a test for BaseModel
"""
import unittest
import datetime
from models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):
    """Test for BaseModel"""
    def setUp(self):
        """set up before each test"""
        self.model1 = BaseModel()
        self.model2 = BaseModel()

    def test_instances(self):
        """test that instances are diff"""
        self.assertIsInstance(self.model1, BaseModel)
        self.assertIsInstance(self.model2, BaseModel)
        self.assertNotEqual(self.model1, self.model2)

    def test_id(self):
        """Check the id attribute"""
        self.assertNotEqual(self.model1.id, self.model2.id)
        self.assertIsInstance(self.model1.id, str)
        self.assertIsInstance(self.model2.id, str)

    def test_time(self):
        """test the time attribute"""
        self.assertIsInstance(self.model1.created_at, datetime.datetime)
        self.assertIsInstance(self.model1.updated_at, datetime.datetime)
        self.assertNotEqual(self.model1.updated_at, self.model1.created_at)
        self.model1.save()
        self.assertIsInstance(self.model1.updated_at, datetime.datetime)
        self.assertNotEqual(self.model1.updated_at, self.model1.created_at)

    def test_str(self):
        """test the output of print function"""
        self.assertIsInstance(self.model1.__str__(), str)
        expected_str = f"[BaseModel] ({self.model1.id}) {self.model1.__dict__}"
        self.assertEqual(self.model1.__str__(), expected_str)

    def test_to_dict(self):
        """test the to_dict() method"""
        self.assertIsInstance(self.model1.to_dict(), dict)
        dic = self.model1.to_dict()
        for key, val in self.model1.to_dict().items():
            self.assertIsInstance(val, str)

    def test_fromdict(self):
        """Test the instance created from a dict"""
        model3 = BaseModel()
        dic1 = model3.to_dict()
        model4 = BaseModel(**dic1)
        dic2 = model4.to_dict()

        self.assertNotEqual(model4, model3)
        self.assertEqual(dic1, dic2)

    def test_from_fake_dict(self):
        """test case of using a fake dict"""
        model3 = BaseModel()
        dic1 = model3.to_dict()
        del dic1["id"]

        with self.assertRaises(NameError):
            BaseModel(**dic1)

    def test_invalid_iso(self):
        """test using a wrong time string"""
        model3 = BaseModel()
        dict1 = model3.to_dict()
        dict1["created_at"] = "20302lov"

        with self.assertRaises(ValueError):
            BaseModel(**dict1)
