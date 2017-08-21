# -*- coding: utf-8 -*-
from model import Contact


def test_add_contact(app):
    old_contacts = app.contact.get_contact_list()
    contact = Contact(
        firstname="John",
        lastname="Doe",
        company="test Co",
        home_tel="322223",
        note="test note"
    )
    app.contact.create(contact)
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) + 1 == len(new_contacts)
    old_contacts.append(contact)
    assert sorted(old_contacts) == sorted(new_contacts)

# def test_add_empty_contact(app):
#     app.contact.create(Contact(
#         "", "", "", "", ""
#     ))
