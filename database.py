import hashlib

class Database:
    def __init__(self, path_name):
        self.path_name = path_name

    def store(self, blob):
        content = f'{blob.type} {len(blob.data)}\0{blob.data}'.encode('utf-8')
        blob.oid = hashlib.sha1(content).hexdigest()

    def __write_object(self, oid, content):
        pass
