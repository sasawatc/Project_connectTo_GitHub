__author__ = 'win.thitiwat'

from Person import Person

class Student(Person):
    def __init__(self, person_id, prefix, first_name, last_name, nick_name, thai_first_name, thai_last_name, birth_date,
                 nationality, shirt_size, photo_path, email, kmitl_id,  academic_year, department, faculty, password):

        Person.__init__(self, person_id, prefix, first_name, last_name, nick_name, thai_first_name,
                        thai_last_name, birth_date, nationality, shirt_size, photo_path, email)

        self.kmitl_id = kmitl_id
        self.person_id  = person_id
        self.academic_year = academic_year
        self.department = department
        self.faculty = faculty
        self.password = password
















# class Student(Person):
#     def __init__(self, stu_id=123,  firstName = None, lastName = None, nickName = None, prefix = None,
#          gender = None, thaiFirst = None, thaiLast = None, photo = None, role = None, shirtSize = None , birth_d = None):
#
#         Person.__init__(self, firstName, lastName, nickName, prefix, gender, thaiFirst, thaiLast, photo, role, shirtSize, birth_d)
#
#         self.studentID = stu_id
#
#     def printInfo(self):
#         return "In student:", self.studentID , Person.printInfo(self)
#
#
# print(Student("560900xx", "Thitiwat", "Wata").printInfo())