from sys import maxsize


class Contact:
    def __init__(self, id=None, firstname=None, lastname=None, company=None, home_tel=None, note=None):
        self.id = id
        self.firstname = firstname
        self.lastname = lastname
        self.company = company
        self.home_tel = home_tel
        self.note = note

    def __repr__(self):
        return "{}:({} {})".format(self.id, self.firstname, self.lastname)

    def __eq__(self, other):
        return (
            (
                self.id == other.id
                or self.id is None
                or other.id is None
            )
            and self.firstname == other.firstname
            and self.lastname == other.lastname
        )

    def id_or_max(self):
        if self.id:
            return int(self.id)
        else:
            return maxsize

    def __lt__(self, other):
        return self.id_or_max() < other.id_or_max()
