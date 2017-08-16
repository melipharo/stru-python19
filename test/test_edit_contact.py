from model import Contact


def test_edit_first_contact(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(firstname="test"))
    app.contact.edit_first(Contact(
        firstname="Alice",
        lastname="Who",
        company="test Co",
        home_tel="42-999999",
        note="test note"
    ))


def test_edit_contact_name(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(firstname="test"))
    app.contact.edit_first(Contact(
        firstname="Sam",
    ))
