__author__ = 'win.thitiwat'

import sys
from PySide.QtCore import *
from PySide.QtGui import *
from PySide.QtUiTools import *


class RegisterUIConnect(QWidget):
    def __init__(self):
        QWidget.__init__(self, parent=None)
        loader = QUiLoader()
        self.form = loader.load("D:/Programming/SoftwarePrinciple/Project/UI/Register_desktop.ui", self)
        self.ui = self.form.findChild(QStackedWidget, "stackedWidget")
        # self.page_1 = self.form.findChild(QStackedWidget, "page")
        # self.page_2 = self.form.findChild(QStackedWidget, "page_2")
        #
        # self.stackWidget = QStackedWidget()
        # self.stackWidget.addWidget(self.page_1)
        # self.stackWidget.addWidget(self.page_2)

        '''self.do_connectUI()'''

        # self.firstname = self.form.findChild(QLineEdit, "firstname")
        # self.surname = self.form.findChild(QLineEdit, "surname")
        # self.email_address = self.form.findChild(QLineEdit, "email_address")
        # self.gender = self.form.findChild(QGroupBox, "gender_groupbox")
        # temp_var = self.form.findChild(QDateEdit, "birth_date")
        #
        #
        # # self.month = self.form.findChild(QComboBox, "month")
        # # self.day = self.form.findChild(QComboBox, "day")
        # # self.year = self.form.findChild(QComboBox, "year")
        # self.address = self.form.findChild(QPlainTextEdit, "address")
        # self.username = self.form.findChild(QLineEdit, "username")
        # self.password = self.form.findChild(QLineEdit, "password")
        # self.repassword = self.form.findChild(QLineEdit, "confirm_password")


    #     self.do_placeHolderText()
    #
    # def do_placeHolderText(self):
    #     self.firstname.setPlaceholderText("First name")


        # self.firstname.setReadOnly(0)



    def connectDB(self):
        pass

    def openPicture(self):
        fileName = QFileDialog.getOpenFileName(None,'Open File', '', 'Images( *.jpg, *,png)', None, QFileDialog.DontUseNativeDialog )


def main():
    app = QApplication(sys.argv)

    sample = RegisterUIConnect()
    sample.show()

    return app.exec_()
if __name__ == "__main__":
    sys.exit(main())