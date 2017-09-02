# -*- coding: utf-8 -*-
import pytest
from model import GroupGenerator

test_data = GroupGenerator().get_test_selection()

@pytest.mark.parametrize("group", test_data, ids=[repr(x) for x in test_data])
def test_add_group(app, group):
    old_groups = app.group.get_group_list()
    app.group.create(group)
    assert len(old_groups) + 1 == app.group.count()
    new_groups = app.group.get_group_list()
    old_groups.append(group)
    assert sorted(old_groups) == sorted(new_groups)
