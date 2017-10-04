import random
from generator import ContactGenerator
import allure


def test_delete_some_contact(app, db, check_ui):
    with allure.step("Given a contact list"):
        old_contacts = db.get_contact_list()
        if len(old_contacts) == 0:
            app.contact.create(ContactGenerator().get_contact())
            old_contacts = db.get_contact_list()

    with allure.step("When I remove the contact"):
        contact = random.choice(old_contacts)
        app.contact.delete_contact_by_id(contact.id)

    with allure.step("Then the new contact list is equal to the old contact list with the removed contact"):
        old_contacts.remove(contact)
        new_contacts = db.get_contact_list()
        assert sorted(old_contacts) == sorted(new_contacts)
        if check_ui:
            assert sorted(new_contacts) == sorted(app.contact.get_contact_list())
