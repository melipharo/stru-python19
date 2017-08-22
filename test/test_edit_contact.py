from model import Contact
from random import randrange


def test_edit_some_contact(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(firstname="test"))
    old_contacts = app.contact.get_contact_list()
    index = randrange(len(old_contacts))
    contact = Contact(
        id = old_contacts[index].id,
        firstname="Alice",
        lastname="Who",
        company="test Co",
        home_tel="42-999999",
        note="test note"
    )
    app.contact.edit_contact_by_index(index, contact)
    assert len(old_contacts) == app.contact.count()
    new_contacts = app.contact.get_contact_list()
    old_contacts[index] = contact
    assert sorted(old_contacts) == sorted(new_contacts)

#
# def test_edit_contact_name(app):
#     if app.contact.count() == 0:
#         app.contact.create(Contact(firstname="test"))
#     app.contact.edit_first(Contact(
#         firstname="Sam",
#     ))
