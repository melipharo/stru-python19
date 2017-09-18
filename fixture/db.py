import pymysql.cursors
from model import Group
from model import Contact

class DBFixture:
    def __init__(self, host, database, user, password):
        self.host = host
        self.database = database
        self.user = user
        self.password = password
        self.connection = pymysql.connect(
            host = host,
            database = database,
            user = user,
            password = password
        )
        self.connection.autocommit(True)

    def get_group_list(self):
        list = []
        with (self.connection.cursor()) as cursor:
            cursor.execute(
                "select group_id, group_name, group_header, group_footer from group_list"
            )
            for row in cursor:
                id, name, header, footer = row
                list.append(
                    Group(
                        id=str(id),
                        name=name,
                        header=header,
                        footer=footer
                    )
                )
        return list

    def get_contact_list(self):
        list = []
        with (self.connection.cursor()) as cursor:
            cursor.execute(
                "select id, firstname, lastname, address from addressbook where deprecated='0000-00-00 00:00:00'"
            )
            for row in cursor:
                id, firstname, lastname, address = row
                list.append(
                    Contact(
                        id=str(id),
                        firstname=firstname,
                        lastname=lastname,
                        address=address
                    )
                )
        return list

    def destroy(self):
        self.connection.close()

    def do_something(self):
        contacts = self.get_contact_list()
        for contact in contacts:
            print(contact)
        print(len(contacts))
