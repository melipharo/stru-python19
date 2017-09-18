import random
from generator import GroupGenerator


def test_delete_some_group(app, db, check_ui):
    old_groups = db.get_group_list()
    if len(old_groups) == 0:
        app.group.create(GroupGenerator().get_group())
        old_groups = db.get_group_list()

    group = random.choice(old_groups)
    app.group.delete_group_by_id(group.id)
    old_groups.remove(group)

    new_groups = db.get_group_list()
    assert sorted(old_groups) == sorted(new_groups)

    if check_ui:
        assert sorted(new_groups) == sorted(app.group.get_group_list())
