import os
import jsonpickle
import argparse
from model import Contact
from model.utils import random_phone, random_email, random_string

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


if __name__ == "__main__":

    ap = argparse.ArgumentParser()
    ap.add_argument("-n", help="number of contact", default=5, type=int)
    ap.add_argument("-f", help="output filename", default="data/contacts.json")
    args = ap.parse_args()

    datafile = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", args.f)
    with open(datafile, "w") as f:
        jsonpickle.set_encoder_options("json", indent=2)
        f.write(jsonpickle.encode(ContactGenerator().get_test_selection()))
