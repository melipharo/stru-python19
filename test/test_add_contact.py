# -*- coding: utf-8 -*-
import pytest

from fixture import Application
from model import Contact


@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture

def test_add_contact(app):
    app.session.login(username="admin", password="secret")
    app.contact.create(Contact("John", "Doe", "test Co", "322223", "test note"))
    app.session.logout()

def test_add_empty_contact(app):
    app.session.login(username="admin", password="secret")
    app.contact.create(Contact("", "", "", "", ""))
    app.session.logout()
