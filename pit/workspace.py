import os

from pit.utils import deep_flatten

class WorkSpace:
    IGNORE = [".", "..", ".gits", "__pycache__", ".git"]

    def __init__(self, path_name):
        self.path_name = path_name

    def list_files(self, dir_name=None):
        if not dir_name:
            dir_name = self.path_name
        "Returns list of (all files - ignored files) recursively."
        file_names = list(set(os.listdir(dir_name)) - set(self.IGNORE))
        file_list = []
        for name in file_names:
            if os.path.isdir(name):
                directory_base = os.path.basename(name)
                file_list.append(
                    self.list_files(dir_name=directory_base)
                )
            else:
                file = os.path.join(dir_name, name)
                file_list.append(file)
        file_list = list(deep_flatten(file_list))
        return file_list

    def is_executable(self, path):
        return os.access(os.path.join(self.path_name, path), os.X_OK)

    def read_file(self, file_name):
        "Returns the content of file_name"
        file = os.path.join(self.path_name, file_name)

        if os.path.isdir(file):
            return
        with open(file, 'r') as f:
            return f.read()
