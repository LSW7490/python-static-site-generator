from pickle import NONE
import re
from yaml import load , FullLoader
from collections.abc import Mapping

class Content(Mapping):
    __delimeter = r"^(?:-|\+){3}\s*$"
    __regex = re.compile(__delimeter, re.MULTILINE)

    @classmethod
    def load(cls, string):
        _, fm, content = cls.__regex.split(string, 2)
        load(fm, Loader=FullLoader)

    def __init__(self, metadata, content):
        self.data = metadata
        self.data["content"] = content

    @property
    def body(self):
        return self.data["content"]

    @property
    def type(self):
        if self.data.has_key("type"):
            return self.data["type"]
        else:
            return NONE

    @type.setter
    def type(self, new_type):
        self.data["type"] = new_type
    
    def __getitem__(self, key) :
        return self.data[key]

    def __iter__(self):
        return self.data

    def __len__(self) :
        return len(self.data)
    
    def __repr__(self):
        data = []
        for key, value in self.data.items():
            if not key == "content":
                data[key] = value
        return str(data)
