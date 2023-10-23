#!/usr/bin/python3
"""Base Class for the other classes"""
import uuid
import datetime
from models import storage


class BaseModel:
    """class basemodel, base class for all other classes"""

    def __init__(self, *args, **kwargs):
        """initializing the baseclass"""
        fields = ["__class__", "created_at", "updated_at", "id"]
        if kwargs:
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
        """How the instance is to be printed"""
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        """Saves the object in storage"""
        self.updated_at = datetime.datetime.now()
        storage.save()

    def to_dict(self):
        """returns a dictionary representation of the object"""
        dictionary = dict.copy(self.__dict__)
        dictionary["created_at"] = self.created_at.isoformat()
        dictionary["updated_at"] = self.updated_at.isoformat()
        dictionary["__class__"] = self.__class__.__name__
        return dictionary
