__author__ = 'win.thitiwat'
import sys
import Resources
from PySide.QtGui import *
from PySide.QtUiTools import *

# from ViewSchedule_access import *
# from ViewBroadcast_access import *
# from ViewContacts_access import *
# from ViewCourses_access import *
# from ViewProfile_access import *

import ViewContacts_access
import ViewCourses_access
import ViewSchedule_access
import ViewProfile_access
import ViewBroadcast_access



class MainWindow(QWidget):
    def __init__(self, parent = None):
        QWidget.__init__(self, parent)

        loader = QUiLoader()

        # self.w = ViewProfile_access.ViewProfile_access()
        # self.w.show()
        self.form = loader.load("D:/Programming/SoftwarePrinciple/Project/UI/Main_page.ui", self)
        self.listWidget = self.form.findChild(QListWidget, "listWidget")
        self.pageWidget = self.form.findChild(QStackedWidget, "pageWidget")

        # self.pageWidget.addWidget(ViewBroadcast_access())
        # self.pageWidget.addWidget(ViewSchedule_access())
        # self.pageWidget.addWidget(ViewContacts_access())
        # self.pageWidget.addWidget(ViewCourses_access())
        # self.pageWidget.addWidget(ViewProfile_access())
        self.pageWidget.insertWidget(0, ViewBroadcast_access.ViewBroadcast_access())
        self.pageWidget.insertWidget(1, ViewSchedule_access.ViewSchedule_access())
        self.pageWidget.insertWidget(2, ViewContacts_access.ViewContacts_access())
        self.pageWidget.insertWidget(3, ViewCourses_access.ViewCourses_access())
        self.pageWidget.insertWidget(4, ViewProfile_access.ViewProfile_access())

        self.listWidget.setCurrentRow(0)
        self.listWidget.currentItemChanged.connect(self.changePage)
        self.pushBtt = self.form.findChild(QPushButton, "commit")
        self.pushBtt.clicked.connect(self.sListWidget)
        self.update()
    def sListWidget(self):
        print("in slistwidget")

    def changePage(self, current, previous):

        if not current:
            current = previous
        self.pageWidget.setCurrentIndex(self.listWidget.row(current))


    def mousePressEvent(self, event):
        print(event.x(), ", ", event.y())
        if 0 < event.x() < 180 and 0 < event.y() < 190:
            self.listWidget.setCurrentRow(-1)
            self.pageWidget.setCurrentIndex(4)

def main():
     app = QApplication(sys.argv)

     sample = MainWindow()
     sample.show()

     return app.exec_()
if __name__ == "__main__":
     sys.exit(main())


# self.listWidget.setViewMode(QListView.IconMode)
        # self.listWidget.setIconSize(QSize(96, 84))
        # self.listWidget.setMovement(QListView.Static)
        # self.listWidget.setMaximumWidth(128)
        # self.listWidget.setSpacing(12)
        #
        # self.course = QListWidgetItem(self.listWidget)
        # self.course.setIcon(QIcon('D:/Programming/SoftwarePrinciple/Project/images/course.png'))
        # self.course.setText("course")
        # self.course.setTextAlignment(Qt.AlignHCenter)
        # self.course.setFlags(Qt.ItemIsSelectable | Qt.ItemIsEnabled)
        #
        # self.setCentralWidget(self.form)


#     __author__ = 'win.thitiwat'
#
# import sys
# from PySide.QtCore import *
# from PySide.QtGui import *
# from PySide.QtUiTools import *
#
#
# class ViewBroadcast_access(QWidget):
#     def __init__(self, parent=None):
#         QWidget.__init__(self, parent)
#         loader = QUiLoader()
#         self.form = loader.load("D:/Programming/SoftwarePrinciple/Project/UI/Main_page.ui", self)
#
#         self.page = self.form.findChild(QLabel, "page1_2")
#         self.scrollArea = self.form.findChild(QScrollArea, "scrollArea_2")
#         self.pushBtt = self.form.findChild(QPushButton, "pushButton")
#         self.listWidget = self.form.findChild(QListWidget, "listWidget")
#
#         self.pushBtt.clicked.connect(self.sListWidget)
#         print("Init broad")
#
#     def sListWidget(self):
#         print("Hello world")
#         self.listWidget.addItem("helloworld")
