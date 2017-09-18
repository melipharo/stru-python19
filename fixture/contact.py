import re
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import StaleElementReferenceException
from model import Contact


class ContactHelper:
    def __init__(self, app):
        self.app = app
        self.contact_cache = None

    def create(self, contact):
        wd = self.app.wd
        self.open_contacts_page()
        # click 'add new'
        wd.find_element_by_link_text("add new").click()
        self.set_contact_data(contact)
        # click 'submit'
        wd.find_element_by_name("submit").click()
        self.return_to_home_page()
        self.contact_cache = None

    def set_contact_data(self, contact):
        self.change_field("firstname", contact.firstname)
        self.change_field("lastname", contact.lastname)
        self.change_field("company", contact.company)

        self.change_field("home", contact.home_tel)
        self.change_field("mobile", contact.mobile_tel)
        self.change_field("work", contact.work_tel)
        self.change_field("phone2", contact.sec_tel)

        self.change_field("email", contact.email)
        self.change_field("email2", contact.email2)
        self.change_field("email3", contact.email3)

        self.change_field("address", contact.address)
        self.change_field("homepage", contact.homepage)
        self.change_field("notes", contact.note)

    def change_field(self, field, text):
        wd = self.app.wd
        if text is not None:
            wd.find_element_by_name(field).click()
            wd.find_element_by_name(field).clear()
            wd.find_element_by_name(field).send_keys(text)

    def delete_first_contact(self):
        self.delete_contact_by_index(0)

    def delete_selected_contact(self):
        wd = self.app.wd
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
        self.contact_cache = None

    def select_contact_by_index(self, index):
        self.app.wd.find_elements_by_name("selected[]")[index].click()

    def select_contact_by_id(self, id):
        self.app.wd.find_element_by_css_selector("input[value='{}']".format(id)).click()

    def delete_contact_by_index(self, index):
        self.open_contacts_page()
        self.select_contact_by_index(index)
        self.delete_selected_contact()

    def delete_contact_by_id(self, id):
        self.open_contacts_page()
        self.select_contact_by_id(id)
        self.delete_selected_contact()

    def edit_first_contact(self, contact):
        self.edit_contact_by_index(0, contact)

    def update_contact_data(self, contact):
        self.set_contact_data(contact)
        # click 'update'
        self.app.wd.find_element_by_name("update").click()
        self.return_to_home_page()
        self.contact_cache = None

    def edit_contact_by_index(self, index, contact):
        self.open_contact_to_edit_by_index(index)
        self.update_contact_data(contact)

    def edit_contact_by_id(self, id, contact):
        self.open_contact_to_edit_by_id(id)
        self.update_contact_data(contact)

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
        if self.contact_cache is None:
            wd = self.app.wd
            self.open_contacts_page()
            self.contact_cache = []
            for element in wd.find_elements_by_xpath("//table[@id='maintable']/tbody/tr")[1:]:
                cells = element.find_elements_by_xpath("td")
                try:
                    homepage=cells[9].find_element_by_xpath("a/img").get_attribute("alt")
                except Exception:
                    homepage=""

                self.contact_cache.append(
                    Contact(
                        id=element.find_element_by_name("selected[]").get_attribute("value"),
                        firstname=cells[2].text,
                        lastname=cells[1].text,
                        address=cells[3].text,
                        homepage=homepage,
                        all_emails_from_homepage=cells[4].text,
                        all_phones_from_homepage=cells[5].text,
                    )
                )
        return self.contact_cache

    def open_contact_to_edit_by_index(self, index):
        self.open_contacts_page()
        self.app.wd.find_element_by_xpath("//table[@id='maintable']/tbody/tr[{}]/td[8]/a".format(index + 2)).click()

    def open_contact_to_edit_by_id(self, id):
        self.open_contacts_page()
        links = self.app.wd.find_elements_by_xpath("//table[@id='maintable']/tbody/tr/td[8]/a")
        for link in links:
            href = link.get_attribute("href")
            if re.findall("id={}".format(id), href):
                link.click()
                break
        else:
            assert False, "contact with id={} not found".format(id)


    def get_contact_info_from_edit_page(self, index):
        wd = self.app.wd
        self.open_contact_to_edit_by_index(index)

        return Contact(
            id=wd.find_element_by_name("id").get_attribute("value"),
            firstname=wd.find_element_by_name("firstname").get_attribute("value"),
            lastname=wd.find_element_by_name("lastname").get_attribute("value"),
            company=wd.find_element_by_name("company").get_attribute("value"),
            home_tel=wd.find_element_by_name("home").get_attribute("value"),
            mobile_tel=wd.find_element_by_name("mobile").get_attribute("value"),
            work_tel=wd.find_element_by_name("work").get_attribute("value"),
            sec_tel=wd.find_element_by_name("phone2").get_attribute("value"),
            note=wd.find_element_by_name("notes").get_attribute("value"),
            email=wd.find_element_by_name("email").get_attribute("value"),
            email2=wd.find_element_by_name("email2").get_attribute("value"),
            email3=wd.find_element_by_name("email3").get_attribute("value"),
            address=wd.find_element_by_name("address").get_attribute("value"),
            homepage=wd.find_element_by_name("homepage").get_attribute("value"),
        )

    def open_contact_view_page_by_index(self, index):
        self.open_contacts_page()
        self.app.wd.find_element_by_xpath("//table[@id='maintable']/tbody/tr[{}]/td[7]/a".format(index + 2)).click()

    def get_contact_from_view_page(self, index):
        wd = self.app.wd
        self.open_contact_view_page_by_index(index)
        content = wd.find_element_by_id("content").text
        return Contact(
            home_tel=re.search("H: (.*)", content).group(1),
            mobile_tel=re.search("M: (.*)", content).group(1),
            work_tel=re.search("W: (.*)", content).group(1)
        )
