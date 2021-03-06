from model import Group

class GroupHelper:
    def __init__(self, app):
        self.app = app
        self.group_cache = None

    def open_groups_page(self):
        wd = self.app.wd
        if not (wd.current_url.endswith("/group.php") and len(wd.find_elements_by_name("new")) > 0):
            wd.find_element_by_link_text("groups").click()

    def create(self, group):
        wd = self.app.wd
        self.open_groups_page()
        # click 'new group'
        wd.find_element_by_name("new").click()
        self.set_group_data(group)
        # click 'submit'
        wd.find_element_by_name("submit").click()
        self.return_to_groups_page()
        self.group_cache = None

    def edit_first_group(self, group):
        self.edit_group_by_index(0, group)

    def edit_group_by_index(self, index, group):
        wd = self.app.wd
        self.open_groups_page()
        self.select_group_by_index(index)
        # click 'edit'
        wd.find_element_by_name("edit").click()
        self.set_group_data(group)
        # click 'update'
        wd.find_element_by_name("update").click()
        self.return_to_groups_page()
        self.group_cache = None

    def edit_group_by_id(self, id, group):
        wd = self.app.wd
        self.open_groups_page()
        self.select_group_by_id(id)
        # click 'edit'
        wd.find_element_by_name("edit").click()
        self.set_group_data(group)
        # click 'update'
        wd.find_element_by_name("update").click()
        self.return_to_groups_page()
        self.group_cache = None

    def set_group_data(self, group):
        wd = self.app.wd
        self.change_field("group_name", group.name)
        self.change_field("group_header", group.header)
        self.change_field("group_footer", group.footer)

    def change_field(self, field, text):
        wd = self.app.wd
        if text is not None:
            wd.find_element_by_name(field).click()
            wd.find_element_by_name(field).clear()
            wd.find_element_by_name(field).send_keys(text)

    def delete_first_group(self):
        self.delete_group_by_index(0)

    def delete_group_by_index(self, index):
        self.open_groups_page()
        self.select_group_by_index(index)
        # click 'delete'
        self.app.wd.find_element_by_name("delete").click()
        self.return_to_groups_page()
        self.group_cache = None

    def delete_group_by_id(self, id):
        self.open_groups_page()
        self.select_group_by_id(id)
        # click 'delete'
        self.app.wd.find_element_by_name("delete").click()
        self.return_to_groups_page()
        self.group_cache = None

    def select_first_group(self):
        self.select_group_by_index(0)

    def select_group_by_index(self, index):
        self.app.wd.find_elements_by_name("selected[]")[index].click()

    def select_group_by_id(self, id):
        self.app.wd.find_element_by_css_selector("input[value='{}']".format(id)).click()

    def return_to_groups_page(self):
        self.app.wd.find_element_by_link_text("group page").click()

    def count(self):
        self.open_groups_page()
        return len(self.app.wd.find_elements_by_name("selected[]"))

    def get_group_list(self):
        if self.group_cache is None:
            wd = self.app.wd
            self.open_groups_page()
            self.group_cache = []
            for element in wd.find_elements_by_css_selector("span.group"):
                self.group_cache.append(
                    Group(
                        id=element.find_element_by_name("selected[]").get_attribute("value"),
                        name=element.text
                    )
                )
        return self.group_cache

