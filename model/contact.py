from sys import maxsize
from model.utils import *


class Contact:
    def __init__(self,
                 id=None,
                 firstname=None,
                 lastname=None,
                 company=None,
                 home_tel=None,
                 mobile_tel=None,
                 work_tel=None,
                 sec_tel=None,
                 email=None,
                 email2=None,
                 email3=None,
                 note=None,
                 address=None,
                 homepage=None,
                 all_phones_from_homepage=None,
                 all_emails_from_homepage=None):
        self.id = id
        self.firstname = firstname
        self.lastname = lastname
        self.company = company
        self.home_tel = home_tel
        self.mobile_tel = mobile_tel
        self.work_tel = work_tel
        self.sec_tel = sec_tel
        self.email = email
        self.email2 = email2
        self.email3 = email3
        self.note = note
        self.address = address
        self.homepage = homepage
        self.all_phones_from_homepage = all_phones_from_homepage
        self.all_emails_from_homepage = all_emails_from_homepage

    def __repr__(self):
        return "{}:({} {})".format(self.id, self.firstname, self.lastname)

    def __eq__(self, other):
        def cleanup_contact_string(value):
            return "" if value is None or value == "" else trim_spaces(value)

        self_fields = list(map(
            lambda x: cleanup_contact_string(x),
            [self.firstname, self.lastname, self.address]
        ))
        other_fields = list(map(
            lambda x: cleanup_contact_string(x),
            [other.firstname, other.lastname, other.address]
        ))

        return (
            (
                self.id == other.id
                or self.id is None
                or other.id is None
            )
            and self_fields == other_fields
        )

    def id_or_max(self):
        if self.id:
            return int(self.id)
        else:
            return maxsize

    def __lt__(self, other):
        return self.id_or_max() < other.id_or_max()

    def merge_phones_like_on_home_page(self):
        return "\n".join(list(
            filter(
                lambda x: x != "",
                map(
                    lambda x: cleanup_phone_string(x),
                    [
                        self.home_tel,
                        self.mobile_tel,
                        self.work_tel,
                        self.sec_tel
                    ]
                )
            )
        ))

    def merge_emails_like_on_home_page(self):
        return "\n".join(list(
            filter(
                lambda x: x != "",
                map(
                    lambda x: cleanup_email_string(x),
                    [
                        self.email,
                        self.email2,
                        self.email3
                    ]
                )
            )
        ))


class ContactGenerator:
    def __init__(self, name_max_len=10, tel_max_len=10, email_max_len=15, data_max_len=15):
        self.name_max_len = name_max_len
        self.tel_max_len = tel_max_len
        self.email_max_len = email_max_len
        self.data_max_len = data_max_len

    def get_contacts_count(self, count):
        return [
            Contact(
                firstname=random_string("", self.name_max_len),
                lastname=random_string("", self.name_max_len),
                company=random_string("", self.data_max_len),
                home_tel=random_phone("", self.tel_max_len),
                mobile_tel=random_phone("", self.tel_max_len),
                work_tel=random_phone("", self.tel_max_len),
                sec_tel=random_phone("", self.tel_max_len),
                email=random_email("", self.email_max_len),
                email2=random_email("", self.email_max_len),
                email3=random_email("", self.email_max_len),
                note=random_string("", self.data_max_len),
                address=random_string("", self.data_max_len),
                homepage=random_string("", self.data_max_len),
            ) for _ in range(count)
        ]

    def get_contact(self):
        return self.get_contacts_count(1)[0]

    def get_test_selection(self):
        return [
                   Contact(
                       firstname=firstname,
                       lastname=lastname,
                       company=random_string("", self.data_max_len),
                       home_tel=random_phone("", self.tel_max_len),
                       mobile_tel=random_phone("", self.tel_max_len),
                       work_tel=random_phone("", self.tel_max_len),
                       sec_tel=random_phone("", self.tel_max_len),
                       email=random_email("", self.email_max_len),
                       email2=random_email("", self.email_max_len),
                       email3=random_email("", self.email_max_len),
                       note=random_string("", self.data_max_len),
                       address=address,
                       homepage=random_string("", self.data_max_len),
                   )
                   for firstname in ["", random_string("", self.name_max_len)]
                   for lastname in ["", random_string("", self.name_max_len)]
                   for address in ["", random_string("", self.data_max_len)]
               ]
