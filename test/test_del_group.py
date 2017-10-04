import random
from generator import GroupGenerator
import allure


def test_delete_some_group(app, db, check_ui):
    with allure.step("Given a group list"):
        old_groups = db.get_group_list()
        if len(old_groups) == 0:
            app.group.create(GroupGenerator().get_group())
            old_groups = db.get_group_list()

    with allure.step("When I remove the random group from the group list"):
        group = random.choice(old_groups)
        app.group.delete_group_by_id(group.id)

    with allure.step("Then the new group list is equal to the old group list with the removed group"):
        old_groups.remove(group)
        new_groups = db.get_group_list()
        assert sorted(old_groups) == sorted(new_groups)
        if check_ui:
            assert sorted(new_groups) == sorted(app.group.get_group_list())
