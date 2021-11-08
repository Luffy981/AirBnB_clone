class FileStorage:
    """Class to serializes instances to a JSON file
    and deserializes JSON file to instances"""
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """returns the dictionary __objects"""
        return self.__objects

    def new(self, obj):
        if obj is not None:
            key = obj.__class__.__name__ + "." + obj.id
            self.__objects[key] = obj
