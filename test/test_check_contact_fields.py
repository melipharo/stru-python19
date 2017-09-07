from random import randrange
from generator import ContactGenerator


def test_check_fields_on_home_page(app):
    if app.contact.count() == 0:
        app.contact.create(ContactGenerator().get_contact())
    index = randrange(len(app.contact.get_contact_list()))
    contact_from_home_page = app.contact.get_contact_list()[index]
    contact_from_edit_page = app.contact.get_contact_info_from_edit_page(index)
    assert contact_from_home_page == contact_from_edit_page
    assert contact_from_home_page.all_phones_from_homepage == contact_from_edit_page.merge_phones_like_on_home_page()
    assert contact_from_home_page.all_emails_from_homepage == contact_from_edit_page.merge_emails_like_on_home_page()
