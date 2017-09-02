from random import randrange
from model import GroupGenerator


def test_edit_some_group(app):
    if app.group.count() == 0:
        app.group.create(GroupGenerator().get_group())
    old_groups = app.group.get_group_list()

    index = randrange(len(old_groups))
    new_group_data = GroupGenerator().get_group()
    new_group_data.id = old_groups[index].id
    app.group.edit_group_by_index(index, new_group_data)

    assert len(old_groups) == app.group.count()
    new_groups = app.group.get_group_list()
    old_groups[index] = new_group_data
    assert sorted(old_groups) == sorted(new_groups)
