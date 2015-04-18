__author__ = 'win.thitiwat'

from Person import Person


class Student(Person):
    def __init__(self, stu_id=123,  firstName = None, lastName = None, nickName = None, prefix = None,
         gender = None, thaiFirst = None, thaiLast = None, photo = None, role = None, shirtSize = None , birth_d = None):

        Person.__init__(self, firstName, lastName, nickName, prefix, gender, thaiFirst, thaiLast, photo, role, shirtSize, birth_d)

        self.studentID = stu_id

    def printInfo(self):
        return "In student:", self.studentID , Person.printInfo(self)


print(Student("560900xx", "Thitiwat", "Wata").printInfo())