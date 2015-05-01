__author__ = 'win.thitiwat'

import sys
from PySide.QtCore import *
from PySide.QtGui import *
from PySide.QtUiTools import *


class ViewCourses_access(QWidget):
    def __init__(self, parent=None):
        QWidget.__init__(self, parent)
        loader = QUiLoader()
        self.form = loader.load("D:/Programming/SoftwarePrinciple/Project/UI/Course_page.ui", self)
        self.page = self.form.findChild(QLabel, "page4_2")
        print("ViewCourses initialized")
    def show_courses(self):
        # a = [1,2,3]

        pass

    def delete_course(self, course_title):
        pass
