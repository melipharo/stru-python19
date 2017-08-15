from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import StaleElementReferenceException

class ContactHelper:
    def __init__(self, app):
        self.app = app

    def create(self, contact):
        wd = self.app.wd
        # click 'add new'
        wd.find_element_by_link_text("add new").click()
        self.set_contact_data(contact)
        # click 'enter'
        wd.find_element_by_name("submit").click()
        self.return_to_home_page()

    def set_contact_data(self, contact):
        wd = self.app.wd
        self.change_field("firstname", contact.firstname)
        self.change_field("lastname", contact.lastname)
        self.change_field("company", contact.company)
        self.change_field("home", contact.home_tel)
        self.change_field("notes", contact.note)

    def change_field(self, field, text):
        wd = self.app.wd
        if text is not None:
            wd.find_element_by_name(field).click()
            wd.find_element_by_name(field).clear()
            wd.find_element_by_name(field).send_keys(text)

    def delete_first(self):
        wd = self.app.wd
        self.open_contacts_page()
        # select first contact
        wd.find_element_by_name("selected[]").click()
        # click 'delete'
        wd.find_element_by_xpath("//div[@id='content']/form/div[@class='left']/input[@value='Delete']").click()
        # accept deletion
        wd.switch_to_alert().accept()
        # return to home page
        # there is autorefresh on page so wait until href is located
        # and try to open contact page
        wait = WebDriverWait(wd, 10)
        try:
            wait.until(EC.presence_of_element_located((By.LINK_TEXT, 'home'))).click()
        except StaleElementReferenceException:
            self.open_contacts_page()
        finally:
            self.open_contacts_page()

    def edit_first(self, contact):
        wd = self.app.wd
        self.open_contacts_page()
        # click 'edit' on first contact
        wd.find_element_by_xpath("//table[@id='maintable']/tbody/tr[2]/td[8]/a").click()
        self.set_contact_data(contact)
        # click 'update'
        wd.find_element_by_name("update").click()
        self.return_to_home_page()

    def return_to_home_page(self):
        self.app.wd.find_element_by_link_text("home page").click()

    def open_contacts_page(self):
        self.app.wd.find_element_by_link_text("home").click()