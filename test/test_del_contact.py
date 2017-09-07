from random import randrange
from generator import ContactGenerator


def test_delete_some_contact(app):
    if app.contact.count() == 0:
        app.contact.create(ContactGenerator().get_contact())
    old_contacts = app.contact.get_contact_list()

    index = randrange(len(old_contacts))
    app.contact.delete_contact_by_index(index)

    assert len(old_contacts) - 1 == app.contact.count()
    new_contacts = app.contact.get_contact_list()
    del old_contacts[index]
    assert old_contacts == new_contacts
