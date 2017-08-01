# -*- coding: utf-8 -*-
from selenium.webdriver.firefox.webdriver import WebDriver
import unittest
from group import Group
from contact import Contact

def is_alert_present(wd):
    try:
        wd.switch_to_alert().text
        return True
    except:
        return False

class tests(unittest.TestCase):
    def setUp(self):
        self.wd = WebDriver(
            firefox_binary="C:\\Program Files\\Mozilla Firefox\\firefox.exe"
        )
        self.wd.implicitly_wait(60)
    
    def test_add_group(self):
        self.open_addressbook()
        self.login(username="admin", password="secret")
        self.open_groups()
        self.create_group(Group(name="autotest group", header="test", footer="toor"))
        self.return_to_group_page()
        self.logout()

    def test_add_empty_group(self):
        self.open_addressbook()
        self.login(username="admin", password="secret")
        self.open_groups()
        self.create_group(Group(name="", header="", footer=""))
        self.return_to_group_page()
        self.logout()

    def test_add_contact(self):
        self.open_addressbook()
        self.login(username="admin", password="secret")
        self.add_contact(Contact("John", "Doe", "test Co", "322223", "test note"))
        self.return_to_contacts_page()
        self.logout()

    def test_add_empty_contact(self):
        self.open_addressbook()
        self.login(username="admin", password="secret")
        self.add_contact(Contact("", "", "", "", ""))
        self.return_to_contacts_page()
        self.logout()

    def add_contact(self, contact):
        wd = self.wd
        # click 'add new'
        wd.find_element_by_link_text("add new").click()
        # fill contact data
        wd.find_element_by_name("firstname").click()
        wd.find_element_by_name("firstname").clear()
        wd.find_element_by_name("firstname").send_keys(contact.firstname)
        wd.find_element_by_name("lastname").click()
        wd.find_element_by_name("lastname").clear()
        wd.find_element_by_name("lastname").send_keys(contact.lastname)
        wd.find_element_by_name("company").click()
        wd.find_element_by_name("company").clear()
        wd.find_element_by_name("company").send_keys(contact.company)
        wd.find_element_by_name("home").click()
        wd.find_element_by_name("home").clear()
        wd.find_element_by_name("home").send_keys(contact.home_tel)
        wd.find_element_by_name("notes").click()
        wd.find_element_by_name("notes").clear()
        wd.find_element_by_name("notes").send_keys(contact.note)
        # click 'enter'
        wd.find_element_by_xpath("//div[@id='content']/form/input[21]").click()

    def return_to_group_page(self):
        self.wd.find_element_by_link_text("group page").click()

    def return_to_contacts_page(self):
        self.wd.find_element_by_xpath("//div/div[4]/div/i/a[2]").click()

    def create_group(self, group):
        wd = self.wd
        # click 'new group'
        wd.find_element_by_name("new").click()
        # enter group data
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
        # click 'submit'
        wd.find_element_by_name("submit").click()

    def open_groups(self):
        self.wd.find_element_by_link_text("groups").click()

    def login(self, username, password):
        wd = self.wd
        wd.find_element_by_id("LoginForm").click()
        wd.find_element_by_name("user").click()
        wd.find_element_by_name("user").clear()
        wd.find_element_by_name("user").send_keys(username)
        wd.find_element_by_name("pass").click()
        wd.find_element_by_name("pass").clear()
        wd.find_element_by_name("pass").send_keys(password)
        wd.find_element_by_xpath("//form[@id='LoginForm']/input[3]").click()

    def logout(self):
        self.wd.find_element_by_link_text("Logout").click()

    def open_addressbook(self):
        self.wd.get("http://localhost/addressbook/")

    def tearDown(self):
        self.wd.quit()

if __name__ == '__main__':
    unittest.main()