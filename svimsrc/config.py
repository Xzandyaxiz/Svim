import json

class CONFIG:
    def __init__(self, file) -> None:
        with open (file, 'r') as fp:
            self.content = fp.read()

    def get_highlighting(self, extension):
        for item in self.content['HIGHLIGHTING']:
            if item != extension:
                continue

            return item[0]

        return "beans"