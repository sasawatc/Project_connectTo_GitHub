__author__ = 'win.thitiwat'

import sys
from PySide.QtCore import *
from PySide.QtGui import *
from PySide.QtUiTools import *


class ViewContacts_access(QWidget):
    def __init__(self, parent=None):
        QWidget.__init__(self, parent)
        loader = QUiLoader()
        self.form = loader.load("D:/Programming/SoftwarePrinciple/Project/UI/Contact_page.ui", self)
        self.tableWidget = self.form.findChild(QTableWidget, "tableWidget")
        self.a = self.form.findChild(QPushButton, "addContact")

        self.a.clicked.connect(self.show_contacts)


        # image = QImage(":/images/course.png")
        # self.page.setPixmap(QPixmap().fromImage(image))
        #
        # scrollArea = QScrollArea()
        # scrollArea.setBackgroundRole(QPalette().Dark)
        # scrollArea.setWidget(self.page)
        temp = QTableWidgetItem("Hello world")
        temp2 = QTableWidgetItem("Hi")

        print("ViewContact initialized")

    def show_contacts(self):
        temp = QTableWidgetItem("Hello world")
        temp2 = QTableWidgetItem("Hi")
        for row in range (10):
            self.tableWidget.insertRow(row)
            self.tableWidget.setItem(row, 0, QTableWidgetItem("Hi ", row))
            self.tableWidget.setItem(row, 1, QTableWidgetItem("Hello world ", row))
        # for i in range (self.tableWidget.columnCount()):
        #     temp.setFlags(Qt.ItemIsEditable | Qt.ItemIsEnabled)
        #     self.tableWidget.setItem(row, i, temp2)



        # self.tableWidget.setItem(2, 0, temp2)
        # self.tableWidget.setItem(2, 1, temp)
        # self.tableWidget.setItem(3, 0, temp2)
        # self.tableWidget.setItem(3, 1, temp)