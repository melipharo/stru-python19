import allure

def test_add_contact(app, db, check_ui, json_contacts):
    contact = json_contacts

    with allure.step("Given a contact list"):
        old_contacts = db.get_contact_list()

    with allure.step("When I add the contact {} to the list".format(contact)):
        app.contact.create(contact)

    with allure.step("Then the new contact list is equal to the old list with the added contact"):
        old_contacts.append(contact)
        new_contacts = db.get_contact_list()
        assert sorted(old_contacts) == sorted(new_contacts)
        if check_ui:
            assert sorted(new_contacts) == sorted(app.contact.get_contact_list())
