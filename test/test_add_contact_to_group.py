from generator import ContactGenerator, GroupGenerator
import random

def test_add_contact_to_group(app, db):
    groups = db.get_group_list()
    if len(groups) == 0:
        app.group.create(GroupGenerator().get_group())
        groups = db.get_group_list()

    group = random.choice(groups)
    contacts_in_group = db.get_contacts_in_group(group)
    contacts_not_in_group = db.get_contacts_not_in_group(group)

    if len(db.get_contact_list()) == 0 or len(contacts_not_in_group) == 0:
        app.contact.create(ContactGenerator().get_contact())
        contacts_not_in_group = db.get_contacts_not_in_group(group)

    contact = random.choice(contacts_not_in_group)
    app.contact.add_contact_to_group(contact, group)

    contacts_in_group.append(contact)
    assert sorted(contacts_in_group) == sorted(db.get_contacts_in_group(group))
