from sys import maxsize
from model.utils import trim_spaces


class Group:
    def __init__(self, id=None, name=None, header=None, footer=None):
        self.id = id
        self.name = name
        self.header = header
        self.footer = footer

    def __repr__(self):
        return "{}:{}:{}:{}".format(self.id, self.name, self.header, self.footer)

    def __eq__(self, other):
        return (
            (
                self.id == other.id
                or self.id is None
                or other.id is None
            )
            and trim_spaces(self.name) == trim_spaces(other.name)
        )

    def id_or_max(self):
        if self.id:
            return int(self.id)
        else:
            return maxsize

    def __lt__(self, other):
        return self.id_or_max() < other.id_or_max()
