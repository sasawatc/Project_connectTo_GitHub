__author__ = 'win.thitiwat'


class Person():
    def __init__(self,  firstName , lastName , nickName = None, prefix = None, gender = None,
                  thaiFirst = None, thaiLast = None, photo = None, role = None, shirtSize = None, birth_d = None ):
        self.firstName = firstName
        self.lastName = lastName
        self.nickName = nickName
        self.prefix = prefix
        self.gender = gender
        self.thai_firstName = thaiFirst
        self.thai_lastName = thaiLast
        self.photo = photo
        self.role = role
        self.shirtSize = shirtSize
        self.birth_date = birth_d

    def printInfo(self):
        return "In person: ", self.firstName, ", ", self.lastName
