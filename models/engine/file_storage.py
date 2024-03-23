#!/usr/bin/python3
"""
    File storage system
"""
import json


class FileStorage:
    """File storage system definition"""
    __file_path = "file.json"
    __objects = {}

    def __init__(self):
        """Initialisation of the class instance"""

    def all(self):
        """Returns the dictionary of objects"""
        return self.__objects

    def new(self, obj):
        """Set the object from list of objects"""
        id = "{}.{}".format(obj.__class__.__name__, obj.id)
        self.__objects[id] = obj

    def save(self):
        """Save all the objects in the file"""
        try:
            with open(self.__file_path, "w", encoding="utf-8") as file:
                list_obj = {}
                for x in self.__objects.keys():
                    list_obj[x] = self.__objects[x].to_dict()
                data = json.dumps(list_obj)
                file.write(data)
        except Exception:
            pass

    def reload(self):
        """Reload objects from file"""
        try:
            from models.base_model import BaseModel
            from models.user import User
            from models.place import Place
            from models.state import State
            from models.city import City
            from models.amenity import Amenity
            from models.review import Review
            with open(self.__file_path, "r", encoding="utf-8") as file:
                file_data = file.read()
                data = json.loads(file_data)
                for x in data:
                    if data[x]["__class__"] in ["BaseModel", "User", "State",
                                                "City", "Amenity", "Place",
                                                "Review"]:
                        exec("self.new({}(**{}))".format(data[x]["__class__"],
                                                         data[x]))
        except Exception:
            pass

    def delete(self, key):
        """Remove an instance"""
        del self.__objects[key]
