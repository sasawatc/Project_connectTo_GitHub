__author__ = 'win.thitiwat'

import sys
from PySide.QtCore import *
from PySide.QtGui import *
from PySide.QtUiTools import *


class ViewSchedule_access(QWidget):
    def __init__(self, parent=None):
        QWidget.__init__(self, parent)
        loader = QUiLoader()
        self.form = loader.load("D:/Programming/SoftwarePrinciple/Project/UI/Calendar_page.ui", self)
        self.calendarWidget = self.form.findChild(QCalendarWidget, "calendarWidget")
        # painter = QPainter()
        # painter.begin()
        # rect1 = QRect(100,200,11,16)
        # rect2 = QRect(100,200,11,16)
        # image = QImage(":/images/schedule.png")
        # painter.drawImage(rect1, image, rect2)
        # self.calendarWidget.paintCell(painter, rect1, QDate().currentDate())

        print("ViewCourses initialized")


