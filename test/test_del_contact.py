import random
from generator import ContactGenerator


def test_delete_some_contact(app, db, check_ui):
    old_contacts = db.get_contact_list()

    if len(old_contacts) == 0:
        app.contact.create(ContactGenerator().get_contact())
        old_contacts = db.get_contact_list()

    contact = random.choice(old_contacts)
    app.contact.delete_contact_by_id(contact.id)
    old_contacts.remove(contact)

    new_contacts = db.get_contact_list()
    assert sorted(old_contacts) == sorted(new_contacts)

    if check_ui:
        assert sorted(new_contacts) == sorted(app.contact.get_contact_list())
