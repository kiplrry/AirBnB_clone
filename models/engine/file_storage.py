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
        FileStorage.__objects[key] = obj
        

    def save(self):
        with open(FileStorage.__file_path, "w", encoding="utf-8") as fp:
            properdict = {}
            for key, obj in FileStorage.__objects.items():
                properdict[key] = obj.to_dict()
            json.dump(properdict, fp)

    def reload(self):
        if not os.path.exists(FileStorage.__file_path)\
            or os.path.getsize(FileStorage.__file_path) == 0:
            self.save()
        with open(self.__class__.__file_path, "+r", encoding="utf-8")\
            as fp:
            try:
                objects = {}
                loadeddict = json.load(fp)
                if loadeddict:
                    for key, dic in loadeddict.items():
                        classname = key.split(".")[0]
                        classobj = self.classes()[classname]
                        objects[key] = classobj(**dic)
                print("reloaded")
                FileStorage.__objects = objects
            except json.decoder.JSONDecodeError as je:
                raise ValueError(f"Inappropriate json file")

    @staticmethod
    def classes():
        """returns all valid classes"""
        from models.base_model import BaseModel
        from models.user import User
        
        classes = {"BaseModel": BaseModel}
        return classes