import uuid
from datetime import datetime
"""Air bnb proyect!!!"""


class BaseModel:
    def __init__(self):
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = self.created_at

    def __str__(self):
        return "[{}] ({}) {}".format(self.__class__.__name__, self.id, self.__dict__)

    def save(self):
        self.update_at = datetime.now()

    def to_dict(self):
        dictionary = self.__dict__
        dictionary[self.__class__.__name__] = s
        return dictionary
