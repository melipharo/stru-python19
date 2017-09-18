from random import randrange
from generator import ContactGenerator


def test_check_fields_on_home_page(app, db):
    contacts_from_database = db.get_contact_list()

    if len(contacts_from_database) == 0:
        app.contact.create(ContactGenerator().get_contact())
        contacts_from_database = db.get_contact_list()

    contacts_from_home_page = sorted(app.contact.get_contact_list())
    contacts_from_database = sorted(contacts_from_database)

    for contact_from_home_page, contact_from_database in zip(contacts_from_home_page, contacts_from_database):
        assert contact_from_home_page == contact_from_database
        assert contact_from_home_page.all_phones_from_homepage == contact_from_database.merge_phones_like_on_home_page()
        assert contact_from_home_page.all_emails_from_homepage == contact_from_database.merge_emails_like_on_home_page()
