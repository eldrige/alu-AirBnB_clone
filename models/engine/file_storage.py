import json
# from models.base_model import BaseModel


class FileStorage:

    def __init__(self):
        self.__file_path = "file.json"
        self.__objects = {}

    def all(self):
        return self.__objects

    def new(self, obj):
        key = obj.__class__.__name__ + '.' + obj.id
        self.__objects[key] = obj

    def save(self):
        obj_dict = {}
        for key, value in self.__objects.items():
            obj_dict[key] = value.to_dict()
        with open(self.__file_path, 'w') as file:
            json.dump(obj_dict, file)

    def reload(self):
        try:
            with open(self.__file_path, 'r') as file:
                obj_dict = json.load(file)
                from models.base_model import BaseModel
                for key, value in obj_dict.items():
                    self.__objects[key] = eval(
                        f"{value['__class__']}(**{value})")

        except FileNotFoundError:
            pass
