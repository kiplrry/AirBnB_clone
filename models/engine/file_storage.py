#!/usr/bin/python3
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
        """reurns the objects"""
        return self.__class__.__objects

    def new(self, obj: object):
        """saves a new object to object dict"""
        key = f"{obj.__class__.__name__}.{obj.id}"
        FileStorage.__objects[key] = obj

    def save(self):
        """saves the object dict to a file"""
        with open(FileStorage.__file_path, "w", encoding="utf-8") as fp:
            properdict = {}
            for key, obj in FileStorage.__objects.items():
                properdict[key] = obj.to_dict()
            json.dump(properdict, fp)

    def reload(self):
        """reloads objects from the file"""
        if not os.path.exists(FileStorage.__file_path):
            return
        if os.path.getsize(FileStorage.__file_path) == 0:
            return
        with open(FileStorage.__file_path, "+r", encoding="utf-8") as fp:
            try:
                objects = {}
                loadeddict = json.load(fp)
                if loadeddict:
                    for key, dic in loadeddict.items():
                        classname = key.split(".")[0]
                        classobj = self.classes()[classname]
                        objects[key] = classobj(**dic)

                FileStorage.__objects = objects
            except json.decoder.JSONDecodeError:
                raise ValueError(f"Inappropriate json file")

    @staticmethod
    def classes():
        """returns all valid classes"""
        from models.base_model import BaseModel
        from models.user import User
        from models.review import Review
        from models.amenity import Amenity
        from models.place import Place
        from models.state import State
        from models.city import City

        classes = {
            "BaseModel": BaseModel,
            "User": User,
            "City": City,
            "State": State,
            "Amenity": Amenity,
            "Review": Review,
            "Place": Place
            }
        return classes
