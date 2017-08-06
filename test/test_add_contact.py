# -*- coding: utf-8 -*-
from model import Contact


def test_add_contact(app):
    app.session.login(username="admin", password="secret")
    app.contact.create(Contact("John", "Doe", "test Co", "322223", "test note"))
    app.session.logout()


def test_add_empty_contact(app):
    app.session.login(username="admin", password="secret")
    app.contact.create(Contact("", "", "", "", ""))
    app.session.logout()
