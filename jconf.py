import json
import os


class Jconf(object):
    def __init__(self, path):
        self._path = path
        self._content = {}
        self._raw_content = {}
        if os.path.exists(self._path):
            self.read()

    def read(self, path=''):
        # Custom path
        if not path:
            path = self._path

        with open(path, 'r') as file:
            self._raw_content = file.read()

        self.json_to_dict()

    def json_to_dict(self):
        try:
            self._content = json.loads(self._raw_content)
        except json.JSONDecodeError as e:
            print('Read Failed. Json decode error: {}'.format(e))

        for key, value in self._content.items():
            # Append leading '#' so num can be set as instance variable
            if key.isdigit():
                key = 'n' + str(key)

            # Wizzardry Harry
            setattr(self, key, value)

    def write(self, path=''):
        # Custom path
        if not path:
            path = self._path

        for key, value in self.__dict__.items():
            if not key.startswith('_'):
                self._content[key] = value

        with open(path, 'w') as file:
            file.write(json.dumps(self._content))

    def dict_to_json(self):
        try:
            self._content = json.dumps(self._raw_content)
        except json.JSONDecodeError as e:
            print('Json encode error:', e)

    def is_empty(self):
        for key, value in self.__dict__.items():
            if not key.startswith('_'):
                return False
        return True

    def keys(self):
        data = []
        if not self.is_empty():
            for key, value in self.__dict__.items():
                if not key.startswith('_'):
                    data.append(key)
            return data

    def items(self):
        if not self.is_empty():
            for key, value in self.__dict__.items():
                if not key.startswith('_'):
                    yield (key, value)
