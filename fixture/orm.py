from pony.orm import *
import datetime
from model import Group, Contact
from pymysql.converters import decoders, encoders, convert_mysql_timestamp


class ORMFixture:
    def __init__(self, host, database, user, password):
        conv = encoders
        conv.update(decoders)
        conv[datetime] = convert_mysql_timestamp

        self.db.bind(
            "mysql",
            host=host,
            database=database,
            user=user,
            password=password,
            conv=conv,
            autocommit=True
        )
        self.db.generate_mapping()

    db = Database()

    class ORMGroup(db.Entity):
        _table_ = "group_list"
        id = PrimaryKey(int, column="group_id")
        name = Optional(str, column="group_name")
        header = Optional(str, column="group_header")
        footer = Optional(str, column="group_footer")
        contacts = Set(
            lambda: ORMFixture.ORMContact,
            table="address_in_groups",
            column="id",
            reverse="groups",
            lazy=True
        )

    class ORMContact(db.Entity):
        _table_ = "addressbook"
        id = PrimaryKey(int, column="id")
        firstname = Optional(str, column="firstname")
        lastname = Optional(str, column="lastname")
        company = Optional(str, column="company")
        home_tel = Optional(str, column="home")
        mobile_tel = Optional(str, column="mobile")
        work_tel = Optional(str, column="work")
        sec_tel = Optional(str, column="phone2")
        email = Optional(str, column="email")
        email2 = Optional(str, column="email2")
        email3 = Optional(str, column="email3")
        note = Optional(str, column="notes")
        address = Optional(str, column="address")
        homepage = Optional(str, column="homepage")
        deprecated = Optional(datetime.datetime, column="deprecated")
        groups = Set(
            lambda: ORMFixture.ORMGroup,
            table="address_in_groups",
            column="group_id",
            reverse="contacts",
            lazy=True
        )

    @db_session
    def get_group_list(self):
        return self.convert_groups_to_model(select(g for g in ORMFixture.ORMGroup))

    @staticmethod
    def convert_groups_to_model(groups):
        def convert(group):
            return Group(
                id=str(group.id),
                name=group.name,
                footer=group.footer
            )
        return list(map(convert, groups))

    @db_session
    def get_contact_list(self):
        return self.convert_contacts_to_model(
            select(c for c in ORMFixture.ORMContact if c.deprecated is None)
        )

    @staticmethod
    def convert_contacts_to_model(contacts):
        def convert(contact):
            return Contact(
                id=str(contact.id),
                firstname=contact.firstname,
                lastname=contact.lastname,
                company=contact.company,
                home_tel=contact.home_tel,
                mobile_tel=contact.mobile_tel,
                work_tel=contact.work_tel,
                sec_tel=contact.sec_tel,
                email=contact.email,
                email2=contact.email2,
                email3=contact.email3,
                note=contact.note,
                address=contact.address,
                homepage=contact.homepage
            )
        return list(map(convert, contacts))

    @db_session
    def get_contact_group(self, group):
        return list(select(g for g in ORMFixture.ORMGroup if g.id == group.id))[0]

    @db_session
    def get_contacts_in_group(self, group):
        orm_group = self.get_contact_group(group)
        return self.convert_contacts_to_model(filter(lambda x: x.deprecated is None, orm_group.contacts))

    @db_session
    def get_contacts_not_in_group(self, group):
        orm_group = self.get_contact_group(group)
        contacts = select(
            c for c in ORMFixture.ORMContact
            if c.deprecated is None and orm_group not in c.groups
        )
        return self.convert_contacts_to_model(contacts)

    def do_something(self):
        l = self.get_contacts_in_group(Group(id="123"))
        print(l)
        for item in l:
            print(item)
        print(len(l))
