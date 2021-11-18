from binascii import unhexlify

class Tree:
    type = "tree"

    def __init__(self, entries):
        self.oid = 0
        self.entries = entries

    def __str__(self):
        entries = sorted(self.entries, key=lambda x: x.name)
        formatted = [
            (
                f"{entry.mode} {entry.name}\0" +
                f"{unhexlify(entry.oid)}"
            )
            for entry in entries
        ]
        return "".join(formatted)
