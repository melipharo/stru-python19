from random import randrange
from model import ContactGenerator


def test_edit_some_contact(app):
    if app.contact.count() == 0:
        app.contact.create(ContactGenerator().get_contact())
    old_contacts = app.contact.get_contact_list()

    index = randrange(len(old_contacts))
    new_contact_data = ContactGenerator().get_contact()
    new_contact_data.id = old_contacts[index].id
    app.contact.edit_contact_by_index(index, new_contact_data)

    assert len(old_contacts) == app.contact.count()
    new_contacts = app.contact.get_contact_list()
    old_contacts[index] = new_contact_data
    assert sorted(old_contacts) == sorted(new_contacts)
