
def test_add_group(app, db, check_ui, json_groups):
    group = json_groups

    old_groups = db.get_group_list()
    app.group.create(group)
    old_groups.append(group)

    new_groups = db.get_group_list()
    assert sorted(old_groups) == sorted(new_groups)

    if check_ui:
        assert sorted(new_groups) == sorted(app.group.get_group_list())
