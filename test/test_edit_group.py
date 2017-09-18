import random
from generator import GroupGenerator


def test_edit_some_group(app, db, check_ui):
    old_groups = db.get_group_list()
    if len(old_groups) == 0:
        app.group.create(GroupGenerator().get_group())
        old_groups = db.get_group_list()

    group = random.choice(old_groups)
    new_group_data = GroupGenerator().get_group()
    new_group_data.id = group.id
    app.group.edit_group_by_id(group.id, new_group_data)
    old_groups[old_groups.index(group)] = new_group_data

    new_groups = db.get_group_list()
    assert sorted(old_groups) == sorted(new_groups)

    if check_ui:
        assert sorted(new_groups) == sorted(app.group.get_group_list())
