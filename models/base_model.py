import uuid
from datetime import datetime
from models import storage
"""Air bnb proyect!!!"""
# Date format
date = "%Y-%m-%dT%H:%M:%S.%f"


class BaseModel:
    def __init__(self, *args, **kwargs):
        if kwargs is not None:
            for key in kwargs:
                if key != '__class__':
                    setattr(self, key, kwargs[key])
            if hasattr(self, 'created_at') and type(self.created_at) is str:
                self.created_at = datetime.strptime(kwargs["created_at"], date)
            if hasattr(self, 'updated_at') and type(self.updated_at) is str:
                self.updated_at = datetime.strptime(kwargs["updated_at"], date)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = self.created_at
            storage.new(self)

    def __str__(self):
        """ should print: [<class name>] (<self.id>) <self.__dict__>"""
        return "[{}] ({}) {}".format(self.__class__.__name__,
                                     self.id, self.__dict__)

    def save(self):
        """updates the public instance attribute
        updated_at with the current datetime"""
        self.update_at = datetime.now()
        storage.save()

    def to_dict(self):
        dictionary = self.__dict__.copy()
        if "created_at" in dictionary:
            dictionary["created_at"] = dictionary["created_at"].strftime(date)
        if "update_at" in dictionary:
            dictionary["updated_at"] = dictionary["updated_at"].strftime(date)
        dictionary[self.__class__.__name__] = self.__class__.__name__
        return dictionary
