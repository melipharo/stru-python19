import allure


def test_group_list(app, db):
    with allure.step("Given a group list from the web interface"):
        ui_groups = app.group.get_group_list()

    with allure.step("When I get group list from the database"):
        db_groups = db.get_group_list()

    with allure.step("Then the group list from the web interface is equal to the group list from the database"):
        assert sorted(ui_groups) == sorted(db_groups)

def test_contact_list(app, db):
    with allure.step("Given a contact list from the web interface"):
        ui_contacts = app.contact.get_contact_list()

    with allure.step("When I get contact list from the database"):
        db_contacts = db.get_contact_list()

    with allure.step("Then the contact list from the web interface is equal to the contact list from the database"):
        assert sorted(ui_contacts) == sorted(db_contacts)
