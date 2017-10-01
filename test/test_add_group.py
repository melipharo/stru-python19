import allure

def test_add_group(app, db, check_ui, json_groups):
    group = json_groups

    with allure.step("Given a group list"):
        old_groups = db.get_group_list()

    with allure.step("When I add the group {} to the list".format(group)):
        app.group.create(group)

    with allure.step("Then the new group list is equal to the old list with the added group"):
        old_groups.append(group)
        new_groups = db.get_group_list()
        assert sorted(old_groups) == sorted(new_groups)
        if check_ui:
            assert sorted(new_groups) == sorted(app.group.get_group_list())
