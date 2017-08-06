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

    def delete_first(self):
        wd = self.app.wd
        # select first contact
        wd.find_element_by_name("selected[]").click()
        # click 'delete'
        wd.find_element_by_xpath("//div[@id='content']/form/div[@class='left']/input[@value='Delete']").click()
        # accept deletion
        wd.switch_to_alert().accept()
        # return to home page
        # there is autorefresh on page so wait until href is located
        wait = WebDriverWait(wd, 10)
        try:
            wait.until(EC.presence_of_element_located((By.LINK_TEXT, 'home'))).click()
        except StaleElementReferenceException:
            # try to click again
            wd.find_element_by_link_text("home").click()

    def edit_first(self, contact):
        wd = self.app.wd
        # click 'edit' on first contact
        wd.find_element_by_xpath("//table[@id='maintable']/tbody/tr[2]/td[8]/a").click()
        self.set_contact_data(contact)
        # click 'update'
        wd.find_element_by_name("update").click()
        self.return_to_home_page()

    def return_to_home_page(self):
        self.app.wd.find_element_by_link_text("home page").click()
