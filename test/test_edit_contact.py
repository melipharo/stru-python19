from model import Contact


def test_edit_first_contact(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(firstname="test"))
    old_contacts = app.contact.get_contact_list()
    contact = Contact(
        id = old_contacts[0].id,
        firstname="Alice",
        lastname="Who",
        company="test Co",
        home_tel="42-999999",
        note="test note"
    )
    app.contact.edit_first(contact)
    assert len(old_contacts) == app.contact.count()
    new_contacts = app.contact.get_contact_list()
    old_contacts[0] = contact
    assert sorted(old_contacts) == sorted(new_contacts)

#
# def test_edit_contact_name(app):
#     if app.contact.count() == 0:
#         app.contact.create(Contact(firstname="test"))
#     app.contact.edit_first(Contact(
#         firstname="Sam",
#     ))
