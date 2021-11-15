#!/usr/bin/python3
"""File Storage module"""
import json
import models
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


classes = {"BaseModel": BaseModel, "User": User, "State": State,
           "Amenity": Amenity, "Place": Place, "City": City, "Review": Review}


class FileStorage:
    """Class to serializes instances to a JSON file
    and deserializes JSON file to instances"""
    # string - path to the JSON file
    __file_path = "file.json"
    #  dictionary - empty but will store all objects
    __objects = {}

    def all(self):
        """returns the dictionary __objects"""
        return self.__objects

    def new(self, obj):
        """sets in __objects the obj with key <obj class name>.id"""
        if obj is not None:
            key = obj.__class__.__name__ + "." + obj.id
            self.__objects[key] = obj

    def save(self):
        """serializes __objects to the JSON file (path: __file_path)"""
        list_objects = {}
        for key in self.__objects:
            list_objects[key] = self.__objects[key].to_dict()
        with open(self.__file_path, 'w', encoding='UTF-8') as file:
            json.dump(list_objects, file)

    def reload(self):
        """deserializes the JSON file to __objects
        - only if the JSON file (__file_path) exists
        - otherwise, do nothing.
        - If the file doesn’t exist, no exception should be raised
        """
        try:
            with open(self.__file_path, 'r', encoding='UTF-8') as file:
                js = json.load(file)
            for key, value in js.items():
                reloadobj = classes[js[key]["__class__"]](**js[key])
                self.__objects[key] = reloadobj
        except FileNotFoundError:
            pass
