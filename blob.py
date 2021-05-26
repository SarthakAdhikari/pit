class Blob:
    oid = None

    def init(self, data):
        self.data = data

    def type(self):
        return "blob"

    def __str__(self):
        return self.data
