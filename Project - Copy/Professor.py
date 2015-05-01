__author__ = 'win.thitiwat'

from Person import Person

class Professor(Person):
    def __init__(self, lect_id = None,  firstName = None, lastName = None, nickName = None, prefix = None, gender = None,
                 thaiFirst = None, thaiLast = None, photo = None, role = None, shirtSize = None, birth_d = None):
        Person.__init__(self, firstName, lastName, nickName, prefix, gender,
                        thaiFirst, thaiLast, photo, role, shirtSize, birth_d)

        self.lecturer_id = lect_id
