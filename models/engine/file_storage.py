#!/usr/bin/env python3
"""
class File Storage
"""
import json
import os


class FileStorage:
    """class FileStorage"""
    __file_path = "file.json"
    __objects = {}

    def all(self):
        return self.__class__.__objects

    def new(self, obj: object):
        key = f"{obj.__class__.__name__}.{obj.id}"
        FileStorage.__objects[key] = obj.to_dict()            

    def save(self):
        with open(FileStorage.__file_path, "w", encoding="utf-8") as fp:
            json.dump(self.all(), fp)

    def reload(self):
        if not os.path.exists(FileStorage.__file_path)\
            or os.path.getsize(FileStorage.__file_path) == 0:
            self.save()
        with open(self.__class__.__file_path, "+r", encoding="utf-8") as fp:
            try:
                FileStorage.__objects = json.load(fp)
            except json.decoder.JSONDecodeError as je:
                raise ValueError(f"Inappropriate json file")
