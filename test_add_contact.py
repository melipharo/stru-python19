# -*- coding: utf-8 -*-
import pytest
from contact import Contact
from application import Application

@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture

def test_add_contact(app):
    app.login(username="admin", password="secret")
    app.add_contact(Contact("John", "Doe", "test Co", "322223", "test note"))
    app.logout()

def test_add_empty_contact(app):
    app.login(username="admin", password="secret")
    app.add_contact(Contact("", "", "", "", ""))
    app.logout()
