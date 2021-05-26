import os

class WorkSpace:
    IGNORE = [".", "..", ".git"]

    def __init__(self, path_name):
        self.path_name = path_name

    def list_files(self):
        return list(set(os.listdir(self.path_name)) - set(IGNORE))
