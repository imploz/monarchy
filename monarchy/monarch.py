from collections import namedtuple
from datetime import datetime

BareMonarch = namedtuple("Monarch", ('id', 'name', 'country', 'house', 'since', 'to'))


class Monarch(BareMonarch):

    def has_ruled_in(self, year):
        to = self.to if self.to is not None else datetime.now().year
        return year in range(self.since, to + 1)
