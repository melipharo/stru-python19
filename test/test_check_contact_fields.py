from generator import ContactGenerator
import allure


def test_check_fields_on_home_page(app, db):
    with allure.step("Given a contact list from database"):
        contacts_from_database = db.get_contact_list()
        if len(contacts_from_database) == 0:
            app.contact.create(ContactGenerator().get_contact())
            contacts_from_database = sorted(db.get_contact_list())

    with allure.step("When I get contact list from the home page"):
        contacts_from_home_page = sorted(app.contact.get_contact_list())

    with allure.step("Then the fields of the contacts from the database is equal to the fields of the contacts from the home page"):
        for contact_from_home_page, contact_from_database in zip(contacts_from_home_page, contacts_from_database):
            assert contact_from_home_page == contact_from_database
            assert contact_from_home_page.all_phones_from_homepage == contact_from_database.merge_phones_like_on_home_page()
            assert contact_from_home_page.all_emails_from_homepage == contact_from_database.merge_emails_like_on_home_page()
