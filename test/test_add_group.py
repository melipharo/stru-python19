# -*- coding: utf-8 -*-
from model import Group


def test_add_group(app):
    old_groups = app.group.get_group_list()
    group = Group(
        name="autotest group",
        header="test",
        footer="toor"
    )
    app.group.create(group)
    assert len(old_groups) + 1 == app.group.count()
    new_groups = app.group.get_group_list()
    old_groups.append(group)
    assert sorted(old_groups) == sorted(new_groups)

#
# def test_add_empty_group(app):
#     old_groups = app.group.get_group_list()
#     group = Group(
#         name="",
#         header="",
#         footer=""
#     )
#     app.group.create(group)
#     new_groups = app.group.get_group_list()
#     assert len(old_groups) + 1 == len(new_groups)
#     old_groups.append(group)
#     assert sorted(old_groups) == sorted(new_groups)
