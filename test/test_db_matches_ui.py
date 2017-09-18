
def test_group_list(app, db):
    ui_groups = app.group.get_group_list()
    db_groups = db.get_group_list()
    assert sorted(ui_groups) == sorted(db_groups)

def test_contact_list(app, db):
    ui_contacts = app.contact.get_contact_list()
    db_contacts = db.get_contact_list()
    assert sorted(ui_contacts) == sorted(db_contacts)
