# -*- coding: utf-8 -*-
from model import Contact


def test_add_contact(app):
    app.contact.create(Contact(
        firstname="John",
        lastname="Doe",
        company="test Co",
        home_tel="322223",
        note="test note"
    ))

def test_add_empty_contact(app):
    app.contact.create(Contact(
        "", "", "", "", ""
    ))
