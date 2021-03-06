from sys import maxsize
from model.utils import trim_spaces, cleanup_email_string, cleanup_phone_string


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
        return "{}:({},{}):{}".format(self.id, self.firstname, self.lastname, self.address)

    def __eq__(self, other):
        def cleanup_contact_string(value):
            return "" if value is None else trim_spaces(value)

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

