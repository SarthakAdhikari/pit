import os

class WorkSpace:
    IGNORE = [".", "..", ".gits", "__pycache__", ".git"]

    def __init__(self, path_name):
        self.path_name = path_name

    def list_files(self):
        return list(set(os.listdir(self.path_name)) - set(self.IGNORE))

    def is_executable(self, path):
        return os.access(os.path.join(self.path_name, path), os.X_OK)

    def read_file(self, file_name):
        file = os.path.join(self.path_name, file_name)
        if os.path.isdir(file):
            return
        with open(file, 'r') as f:
            return f.read()
