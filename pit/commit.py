import os

class Commit:
    type = "commit"

    def __init__(self, parent, tree, author, message):
        self.oid = None
        self.parent = parent
        self.tree = tree
        self.author = author
        self.message = message

    def __str__(self):
        lines = []
        lines.append(f"tree {self.tree}")
        if self.parent:
            lines.append(f"parent {self.parent}")
        lines.append(f"author {self.author}")
        lines.append(f"committer {self.author}")
        lines.append(f"message {self.message}")
        return "\n".join(lines)
