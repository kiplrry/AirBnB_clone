#!/usr/bin/env python3
from models.engine.file_storage import FileStorage
import unittest
import os

storagepath = FileStorage._FileStorage__file_path
fileobjects = FileStorage._FileStorage__objects

class TestFileStorage(unittest.TestCase):
    def setUp(self) -> None:
        self.filestorage = FileStorage()

    def tearDown(self) -> None:
        self.delfile()

    def delfile(self) -> None:
        if os.path.exists(storagepath):
            os.remove(storagepath)

    @staticmethod
    def noraises(func):
        """used to handle func that shouldnt raise an error"""
        try:
            j = func()
            return 1
        except NameError:
            print("error")
            return None

    def test_nofile(self):
        self.assertFalse(os.path.exists(storagepath))
        self.filestorage.reload()
        self.assertFalse(os.path.exists(storagepath))

    def test_emptyfile(self):
        self.delfile()
        with open(storagepath, "w") as fp:
            pass
        self.assertTrue(os.path.exists(storagepath))
        filesize = os.path.getsize(storagepath)
        self.assertEqual(filesize, 0)
        self.assertIsNotNone(self.noraises(self.filestorage.reload))
    
    def test_invalid_file(self):
        with open(storagepath, "w") as fp:
            fp.write("feiheihi")
        
        with self.assertRaises(ValueError):
            self.filestorage.reload()
    
    def test_invalid_obj(self):
        with self.assertRaises(AttributeError):
            self.filestorage.new("lll")

