import os
import jsonpickle
import argparse
from model import Group
from model.utils import random_string


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
            for name in ["", random_string("name", self.name_max_len)]
            for header in ["", random_string("header", self.data_max_len)]
            for footer in ["", random_string("footer", self.data_max_len)]
        ]


if __name__ == "__main__":

    ap = argparse.ArgumentParser()
    ap.add_argument("-n", help="number of groups", default=5, type=int)
    ap.add_argument("-f", help="output filename", default="data/groups.json")
    args = ap.parse_args()

    datafile = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", args.f)
    with open(datafile, "w") as f:
        jsonpickle.set_encoder_options("json", indent=2)
        f.write(jsonpickle.encode(GroupGenerator().get_test_selection()))
