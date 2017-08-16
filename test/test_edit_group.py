from model import Group


def test_edit_first_group(app):
    if app.group.count() == 0:
        app.group.create(Group(name="test"))
    app.group.edit_first(Group(
        name="changed name",
        header="changed header",
        footer="changed footer"
    ))


def test_edit_group_name(app):
    if app.group.count() == 0:
        app.group.create(Group(name="test"))
    app.group.edit_first(Group(
        name="changed single name"
    ))


def test_edit_group_header(app):
    if app.group.count() == 0:
        app.group.create(Group(name="test"))
    app.group.edit_first(Group(
        header="changed single header"
    ))
