__author__ = 'win.thitiwat'





class Person:
    def __init__(self, person_id, prefix, first_name, last_name, nick_name, thai_first_name, thai_last_name, birth_date, nationality, shirt_size, photo_path, email):
        self.person_id = person_id
        self.prefix = prefix
        self.first_name = first_name
        self.last_name = last_name
        self.nick_name = nick_name
        self.thai_first_name = thai_first_name
        self.thai_last_name = thai_last_name
        self.birth_date = birth_date
        self.nationality = nationality
        self.shirt_size = shirt_size
        self.photo_path = photo_path
        self.email = email


# class Person():
#     def __init__(self,  firstName , lastName , nickName = None, prefix = None, gender = None,
#                   thaiFirst = None, thaiLast = None, photo = None, role = None, shirtSize = None, birth_d = None ):
#         self.firstName = firstName
#         self.lastName = lastName
#         self.nickName = nickName
#         self.prefix = prefix
#         self.gender = gender
#         self.thai_firstName = thaiFirst
#         self.thai_lastName = thaiLast
#         self.photo = photo
#         self.role = role
#         self.shirtSize = shirtSize
#         self.birth_date = birth_d
#
#     def printInfo(self):
#         return "In person: ", self.firstName, ", ", self.lastName