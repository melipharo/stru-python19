class GroupHelper:
    def __init__(self, app):
        self.app = app

    def open_groups_page(self):
        self.app.wd.find_element_by_link_text("groups").click()

    def create(self, group):
        wd = self.app.wd
        self.open_groups_page()
        # click 'new group'
        wd.find_element_by_name("new").click()
        self.set_group_data(group)
        # click 'submit'
        wd.find_element_by_name("submit").click()
        self.return_to_groups_page()

    def edit_first(self, group):
        wd = self.app.wd
        self.open_groups_page()
        # select first group
        wd.find_element_by_name("selected[]").click()
        # click 'edit'
        wd.find_element_by_name("edit").click()
        self.set_group_data(group)
        # click 'update'
        wd.find_element_by_name("update").click()
        self.return_to_groups_page()

    def set_group_data(self, group):
        wd = self.app.wd
        wd.find_element_by_name("group_header").click()
        wd.find_element_by_name("group_name").click()
        wd.find_element_by_name("group_name").clear()
        wd.find_element_by_name("group_name").send_keys(group.name)
        wd.find_element_by_name("group_header").click()
        wd.find_element_by_name("group_header").clear()
        wd.find_element_by_name("group_header").send_keys(group.header)
        wd.find_element_by_name("group_footer").click()
        wd.find_element_by_name("group_footer").clear()
        wd.find_element_by_name("group_footer").send_keys(group.footer)

    def delete_first(self):
        wd = self.app.wd
        self.open_groups_page()
        # select first group
        wd.find_element_by_name("selected[]").click()
        # click 'delete'
        wd.find_element_by_name("delete").click()
        self.return_to_groups_page()

    def return_to_groups_page(self):
        self.app.wd.find_element_by_link_text("group page").click()
