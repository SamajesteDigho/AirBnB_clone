#!/usr/bin/python3
"""
    The Base Model File
    Here is the base model for all the classes
"""
from uuid import uuid4
from datetime import datetime
from models import storage


class BaseModel:
    """The base model for defining the base attributes for all the classes"""
    def __init__(self, *args, **kwargs):
        """The initialization of all the class"""
        if kwargs is None or len(kwargs.keys()) == 0:
            self.id = str(uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            storage.new(self)
        else:
            for x in kwargs.keys():
                if x in ["created_at", "updated_at"]:
                    self.__setattr__(x, datetime.fromisoformat(kwargs[x]))
                elif x != "__class__":
                    self.__setattr__(x, kwargs[x])

    def __str__(self):
        """Return the string representation of the object"""
        name = self.__class__.__name__
        id = self.id
        data = self.__dict__
        return "[{}] ({}) {}".format(name, id, data)

    def save(self):
        """Save an instance of the object concerned"""
        self.updated_at = datetime.now()
        storage.save()

    def to_dict(self):
        """Returns the dictionary representation of the objet"""
        obj = {"__class__": self.__class__.__name__}
        for x in self.__dict__.keys():
            if x in ["created_at", "updated_at"]:
                obj[x] = datetime.isoformat(self.__dict__[x])
            else:
                obj[x] = self.__dict__[x]
        return obj
