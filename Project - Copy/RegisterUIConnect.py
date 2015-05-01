__author__ = 'win.thitiwat'

from PySide.QtGui import *
from PySide.QtUiTools import *

import MainWindow

import Resources

class RegisterUIConnect(QWidget):
    def __init__(self, parent = None):
        QWidget.__init__(self, parent)
        loader = QUiLoader()
        self.form = loader.load("D:/Programming/SoftwarePrinciple/Project/UI/Register_desktop.ui", self)
        self.register_page = self.form.findChild(QStackedWidget, "stackedWidget")

        self.next_btt = self.form.findChild(QPushButton, "next")
        self.backBtt = self.form.findChild(QPushButton, "backBtt")
        self.finish_btt = self.form.findChild(QPushButton, "finish")

        self.next_btt.clicked.connect(self.change_Page)
        self.backBtt.clicked.connect(self.change_Page)
        self.finish_btt.clicked.connect(self.goMainPage)
        self.nextPage = 1
        # listBtt = QListWidget()
        # listBtt.addItem(self.next_btt)
        # listBtt.cu
    def change_Page(self):
        if self.register_page.currentIndex() == 0:
            self.register_page.setCurrentIndex(self.nextPage)
            self.nextPage = 0
        else:
            self.register_page.setCurrentIndex(self.nextPage)
            self.nextPage = 1

    def goMainPage(self):
        self.hide()
        self.mainWin = MainWindow.MainWindow()
        self.mainWin.show()

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




        # self.firstname.setReadOnly(0)






    def connectDB(self):
        pass

    def openPicture(self):
        fileName = QFileDialog.getOpenFileName(None,'Open File', '', 'Images( *.jpg, *,png)', None, QFileDialog.DontUseNativeDialog )


# def main():
#     app = QApplication(sys.argv)
#     sample = RegisterUIConnect()
#     sample.show()
#     return app.exec_()
#
# if __name__ == "__main__":
#     sys.exit(main())