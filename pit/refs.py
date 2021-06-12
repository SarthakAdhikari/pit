import os
from pit.lockfile import LockFile

class Refs:
    LockDenied = Exception()

    def __init__(self, path_name):
        self.path_name = path_name

    def _head_path(self):
        return os.path.join(self.path_name, 'HEAD')

    def read_head(self):
        head_path = self._head_path()
        try:
            with open(head_path, 'r') as f:
                content = f.read()
                return content.strip()
        except FileNotFoundError:
            pass

    def update_head(self, oid):
        head_path = self._head_path()
        lockfile = LockFile(head_path)

        if not lockfile.hold_for_update():
            raise self.LockDenied("Could not acquire lock on file {head_path}")
        lockfile.write(oid + "\n")
        lockfile.commit()
