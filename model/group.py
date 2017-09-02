from sys import maxsize
from model.utils import random_string, trim_spaces


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


class GroupGenerator:
    def __init__(self, name_max_len=10, data_max_len=20):
        self.name_max_len = name_max_len
        self.data_max_len = data_max_len

    def get_groups_count(self, count):
        return [
            Group(
                name=random_string("name", self.name_max_len),
                header=random_string("header", self.data_max_len),
                footer=random_string("footer", self.data_max_len)
            ) for _ in range(count)
        ]

    def get_group(self):
        return self.get_groups_count(1)[0]

    def get_test_selection(self):
        return [
            Group(
                name=name,
                header=header,
                footer=footer
            )
            for name in ["",random_string("name", self.name_max_len)]
            for header in ["", random_string("header", self.data_max_len)]
            for footer in ["", random_string("footer", self.data_max_len)]
        ]
