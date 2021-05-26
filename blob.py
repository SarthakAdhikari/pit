class Blob:
    oid = None
    type = "blob"

    def __init__(self, data):
        self.data = data


    def __str__(self):
        return self.data
