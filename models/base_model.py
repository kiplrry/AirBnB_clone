#!/usr/bin/python3
"""
Base Class
"""
import uuid
import datetime
from models import storage



class BaseModel:
    """class basemodel"""

    def __init__(self, *args, **kwargs):
        fields = ["__class__", "created_at", "updated_at", "id"]
        if kwargs:
            """checking if kwargs is valid"""
            for i in fields:
                if i not in kwargs:
                    raise NameError(f"{i} was not found")
            for key, val in kwargs.items():
                if key in ["created_at", "updated_at"]:
                    setattr(self, key, datetime.datetime.fromisoformat(val))
                elif key != "__class__":
                    setattr(self, key, val)

        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.datetime.now()
            self.updated_at = datetime.datetime.now()
            storage.new(self)

    def __str__(self) -> str:
        return f"[BaseModel] ({self.id}) {self.__dict__}"

    def save(self):
        self.updated_at = datetime.datetime.now()
        storage.save()

    def to_dict(self):
        dictionary = dict.copy(self.__dict__)
        dictionary["created_at"] = self.created_at.isoformat()
        dictionary["updated_at"] = self.updated_at.isoformat()
        dictionary["__class__"] = self.__class__.__name__
        return dictionary
