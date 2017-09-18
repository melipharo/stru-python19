
def test_add_contact(app, db, check_ui, json_contacts):
    contact = json_contacts

    old_contacts = db.get_contact_list()
    app.contact.create(contact)
    old_contacts.append(contact)

    new_contacts = db.get_contact_list()
    assert sorted(old_contacts) == sorted(new_contacts)

    if check_ui:
        assert sorted(new_contacts) == sorted(app.contact.get_contact_list())
