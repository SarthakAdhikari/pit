from datetime import datetime


class Author:
    TIME_FORMAT = "%s %z"

    def __init__(self, name, email, time):
        self.name = name
        self.email = email
        self.time = time

    def __str__(self):
        timestamp = datetime.strftime(self.time, self.TIME_FORMAT)
        return f'{self.name} <{self.email}> {timestamp}'
