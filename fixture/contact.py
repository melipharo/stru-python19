from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import StaleElementReferenceException
from model import Contact

class ContactHelper:
    def __init__(self, app):
        self.app = app

    def create(self, contact):
        wd = self.app.wd
        # click 'add new'
        self.open_contacts_page()
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
        # hint: self.wd.implicitly_wait(5)
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
        wd = self.app.wd
        on_root_page = wd.current_url.endswith("/addressbook/") or wd.current_url.endswith("/index.php")
        maintable_exists = len(wd.find_elements_by_xpath("//table[@id='maintable']/tbody/tr")) > 0
        if not (on_root_page and maintable_exists):
            wd.find_element_by_link_text("home").click()

    def count(self):
        self.open_contacts_page()
        return len(self.app.wd.find_elements_by_xpath("//table[@id='maintable']/tbody/tr")) - 1

    def get_contact_list(self):
        wd = self.app.wd
        self.open_contacts_page()
        contacts = []
        for element in wd.find_elements_by_xpath("//table[@id='maintable']/tbody/tr")[1:]:
            contacts.append(
                Contact(
                    id=element.find_element_by_name("selected[]").get_attribute("value"),
                    firstname=element.find_elements_by_xpath("td")[2].text,
                    lastname=element.find_elements_by_xpath("td")[1].text
                )
            )
        return contacts
