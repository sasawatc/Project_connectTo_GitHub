__author__ = 'win.thitiwat'

import sys
from PySide.QtCore import *
from PySide.QtGui import *
from PySide.QtUiTools import *

class MainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self, None)
        loader = QUiLoader()
        self.form = loader.load("D:/Programming/SoftwarePrinciple/Project/Main_page.ui", self)
        self.setCentralWidget(self.form)



    def

