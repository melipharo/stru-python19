from generator import ContactGenerator, GroupGenerator
import random
import allure

def test_add_contact_to_group(app, db):
    with allure.step("Given a group list"):
        groups = db.get_group_list()
        if len(groups) == 0:
            app.group.create(GroupGenerator().get_group())
            groups = db.get_group_list()

    with allure.step("Given a contact list from the group"):
        # use only the groups with non-empty name
        group = random.choice(list(filter(lambda x: x.name != "", groups)))
        contacts_in_group = db.get_contacts_in_group(group)
        contacts_not_in_group = db.get_contacts_not_in_group(group)
        if len(db.get_contact_list()) == 0 or len(contacts_not_in_group) == 0:
            app.contact.create(ContactGenerator().get_contact())
            contacts_not_in_group = db.get_contacts_not_in_group(group)

    with allure.step("When I add the contact to the group"):
        contact = random.choice(contacts_not_in_group)
        app.contact.add_contact_to_group(contact, group)

    with allure.step("Then contact list in the group is equal to the old contact list from the group with the added contact"):
        contacts_in_group.append(contact)
        assert sorted(contacts_in_group) == sorted(db.get_contacts_in_group(group))
