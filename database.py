import os
import zlib
import secrets
import string
import hashlib


class Database:
    def __init__(self, path_name):
        self.path_name = path_name

    def store(self, blob):
        content = f'{blob.type} {len(blob.data)}\0{blob.data}'.encode('utf-8')
        oid = hashlib.sha1(content).hexdigest()
        self.__write_object(oid, content)

    def __write_object(self, oid, content):
        # create dir struct like 8c/f19e34f5154ab264cc2ee71446309bd0302794
        object_dir = os.path.join(
            self.path_name,
            oid[:2]
        )
        os.makedirs(object_dir, exist_ok=True)
        object_file = os.path.join(
            object_dir,
            oid[2:]
        )
        temp_file_name = ''.join(
            secrets.choice(string.ascii_uppercase + string.digits) for _ in range(15)
        )
        temp_file_path = os.path.join(
            self.path_name,
            temp_file_name
        )
        with open(temp_file_path, "wb") as f:
            compressed = zlib.compress(content, level=zlib.Z_BEST_SPEED)
            f.write(compressed)
        os.rename(temp_file_path, object_file)
        print("Wrote to:", object_file)
