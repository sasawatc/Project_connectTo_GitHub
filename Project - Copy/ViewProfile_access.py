from PySide.QtGui import QLabel

__author__ = 'win.thitiwat'

import sys
from PySide.QtCore import *
from PySide.QtGui import *
from PySide.QtUiTools import *



class ViewProfile_access(QWidget):

    def __init__(self, parent=None):
        QWidget.__init__(self, parent)
        loader = QUiLoader()
        form = loader.load("D:/Programming/SoftwarePrinciple/Project/UI/profile_page.ui", self)
        layout = QVBoxLayout()
        self.setLayout(layout)
        layout.addWidget(form)
        self.scrollArea = form.findChild(QScrollArea, "scrollArea")
        self.temp = form.findChild(QPushButton, "temp")
        self.temp.clicked.connect(self.tempClicked)


        print("ViewProfile initialized")

    def tempClicked(self):
        print("in profile process UI")
    def view_name(self):
        return "name"

    def view_lastname(self):
        return "lastname"

    def view_gender(self):
        return "gender"

    def view_birthdate(self):
        return "birthdate"

    def view_email(self):
        return "email"

    def edit_profile(self):
        pass


def main():
    app = QApplication(sys.argv)

    sample = ViewProfile_access()
    sample.show()

    return app.exec_()
if __name__ == "__main__":
    sys.exit(main())