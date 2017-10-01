from generator import ContactGenerator, GroupGenerator
import random

def test_del_contact_from_group(app, db):
    groups = db.get_group_list()
    if len(groups) == 0:
        app.group.create(GroupGenerator().get_group())
        groups = db.get_group_list()

    group = random.choice(groups)
    contacts = db.get_contacts_in_group(group)
    if contacts is None or len(contacts) == 0:
        print("no contacts in selected group {} found".format(group))
        contacts_not_in_group = db.get_contacts_not_in_group(group)
        print("contacts not in group {}: {}".format(group, contacts_not_in_group))
        if len(contacts_not_in_group) == 0:
            print("no contacts either/ adding one..")
            app.contact.create(ContactGenerator().get_contact())
            contacts_not_in_group = db.get_contacts_not_in_group(group)
        contact = random.choice(contacts_not_in_group)
        print("adding contact {} in group {}".format(contact, group))
        app.contact.add_contact_to_group(contact, group)
        contacts = db.get_contacts_in_group(group)

    print("contact list: {}".format(contacts))
    contact = random.choice(contacts)
    app.contact.del_contact_from_group(contact, group)
    contacts.remove(contact)
    assert sorted(contacts) == sorted(db.get_contacts_in_group(group))
