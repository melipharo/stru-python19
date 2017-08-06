from model import Group

def test_delete_first_group(app):
    app.session.login(username="admin", password="secret")
    app.group.edit_first(Group(
        name="changed name",
        footer="changed footer",
        header="changed header"
    ))
    app.session.logout()
