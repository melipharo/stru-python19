# -*- coding: utf-8 -*-
import pytest
from model import ContactGenerator

test_data = ContactGenerator().get_test_selection()

@pytest.mark.parametrize("contact", test_data, ids=[repr(x) for x in test_data])
def test_add_contact(app, contact):
    old_contacts = app.contact.get_contact_list()
    app.contact.create(contact)
    assert len(old_contacts) + 1 == app.contact.count()
    new_contacts = app.contact.get_contact_list()
    old_contacts.append(contact)
    assert sorted(old_contacts) == sorted(new_contacts)
