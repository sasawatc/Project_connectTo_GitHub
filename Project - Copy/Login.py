import RegisterUIConnect

__author__ = 'win.thitiwat'

import sys

from PySide.QtGui import *
from PySide.QtUiTools import *
import RegisterUIConnect
import MainWindow


import Resources


class Login(QWidget):
    def __init__(self, parent = None):
        QWidget.__init__(self, parent)
        loader = QUiLoader()
        self.form = loader.load("D:/Programming/SoftwarePrinciple/Project/UI/Login.ui", self)
        self.background = self.form.findChild(QLabel, "background")
        self.symbol = self.form.findChild(QLabel, "symbol")
        self.create_acc = self.form.findChild(QPushButton, "createAcc")
        self.login = self.form.findChild(QPushButton, "login")


        self.create_acc.clicked.connect(self.goRegister)
        self.login.clicked.connect(self.check_Login)

    def goRegister(self):
        self.hide()
        self.registerPage = RegisterUIConnect.RegisterUIConnect()
        self.registerPage.show()
        pass

    def check_Login(self):
        return self.goMainPage()

    def goMainPage(self):
        self.hide()
        self.mainWin = MainWindow.MainWindow()
        self.mainWin.show()

def main():
    app = QApplication(sys.argv)
    sample = Login()
    sample.show()
    return app.exec_()

if __name__ == "__main__":
    sys.exit(main())

