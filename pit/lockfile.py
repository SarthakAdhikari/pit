import os


class LockFile:
    MissingParent = Exception()
    StaleLock = Exception()

    def __init__(self, path):
        self.file_path = self.path
        self.lock_path = path + ".lock"
        self.lock = None

    def hold_for_update(self):
        try:
            if not self.lock:
                with open(self.file_path, "x"):
                    self.lock = self.lock_path
                return True
            return False
        except FileExistsError:
            return False

        except FileNotFoundError:
            raise self.MissingParent

    def commit(self):
        self.raise_on_stale_lock()
        os.rename(self.lock_path, self.file_path)

    def write(self, string):
        self.raise_on_stale_lock()
        self.lock.write(string)

    def _raise_on_stale_lock(self):
        if not self.lock:
            raise self.StaleLock("Not holding lock on file: {self.lock_path}")
