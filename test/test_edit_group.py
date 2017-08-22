from model import Group
from random import randrange


def test_edit_first_group(app):
    if app.group.count() == 0:
        app.group.create(Group(name="test"))
    old_groups = app.group.get_group_list()
    index = randrange(len(old_groups))
    group = Group(
        name="changed name",
        header="changed header",
        footer="changed footer",
        id = old_groups[index].id
    )
    app.group.edit_group_by_index(index, group)
    assert len(old_groups) == app.group.count()
    new_groups = app.group.get_group_list()
    old_groups[index] = group
    assert sorted(old_groups) == sorted(new_groups)

#
# def test_edit_group_name(app):
#     if app.group.count() == 0:
#         app.group.create(Group(name="test"))
#     old_groups = app.group.get_group_list()
#     app.group.edit_first(Group(
#         name="changed single name"
#     ))
#     new_groups = app.group.get_group_list()
#     assert len(old_groups) == len(new_groups)
#
#
# def test_edit_group_header(app):
#     if app.group.count() == 0:
#         app.group.create(Group(name="test"))
#     old_groups = app.group.get_group_list()
#     app.group.edit_first(Group(
#         header="changed single header"
#     ))
#     new_groups = app.group.get_group_list()
#     assert len(old_groups) == len(new_groups)
