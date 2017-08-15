# -*- coding: utf-8 -*-
from model import Group


def test_add_group(app):
    app.group.create(Group(name="autotest group", header="test", footer="toor"))


def test_add_empty_group(app):
    app.group.create(Group(name="", header="", footer=""))
