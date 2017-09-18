import random
from generator import ContactGenerator


def test_edit_some_contact(app, db, check_ui):
    old_contacts = db.get_contact_list()
    if len(old_contacts) == 0:
        app.contact.create(ContactGenerator().get_contact())
        old_contacts = db.get_contact_list()

    contact = random.choice(old_contacts)
    new_contact_data = ContactGenerator().get_contact()
    new_contact_data.id = contact.id
    app.contact.edit_contact_by_id(contact.id, new_contact_data)
    old_contacts[old_contacts.index(contact)] = new_contact_data

    new_contacts = db.get_contact_list()
    assert sorted(old_contacts) == sorted(new_contacts)

    if check_ui:
        assert sorted(new_contacts) == sorted(app.contact.get_gcontact_list())
