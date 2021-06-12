import os
import zlib
import secrets
import string
import hashlib


class Entry:
    REGULAR_MODE = "100644"
    EXECUTABLE_MODE = "100755"

    def __init__(self, name, oid, is_executable):
        self.name = name
        self.oid = oid
        self.is_executable = is_executable

    def mode(self):
        return self.REGULAR_MODE if self.is_executable else self.REGULAR_MODE
