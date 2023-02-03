import json

class CONFIG:
    def __init__(self, file) -> None:
        with open (file, 'r') as fp:
            self.content = json.load(fp)

    def get_highlighting(self, extension):
        fext = ""

        if '.' in extension:
            fext = extension.split('.')[1]

        for item in self.content['HIGHLIGHTING']:
            if item != fext:
                continue

            return item[0]

        return None