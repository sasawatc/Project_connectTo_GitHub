__author__ = 'win.thitiwat'

import sys
from PySide.QtCore import *
from PySide.QtGui import *
from PySide.QtUiTools import *


class ViewBroadcast_access(QWidget):
    def __init__(self, parent=None):
        QWidget.__init__(self)
        loader = QUiLoader()
        self.form = loader.load("D:/Programming/SoftwarePrinciple/Project/UI/Broadcast_page.ui", self)

        self.pushBtt = self.form.findChild(QPushButton, "commit")
        self.myBatch = self.form.findChild(QListWidget, "page1_listWidget")

        self.pushBtt.clicked.connect(self.pushBttClicked)
        print("Init broad")

    def pushBttClicked(self):
        print("Hello world")
        #self.myBatch.addItem("Hello World"))
        itemN = QListWidgetItem()
        #Create widget
        widget = QWidget()
        widgetText =  QLabel("I love PyQt!")
        widgetButton =  QPushButton("Push Me")
        widgetLayout = QHBoxLayout()
        widgetLayout.addWidget(widgetText)
        widgetLayout.addWidget(widgetButton)
        widgetLayout.addStretch()

        widgetLayout.setSizeConstraint(QLayout.SetFixedSize)
        widget.setLayout(widgetLayout)
        itemN.setSizeHint(widget.sizeHint())

        #Add widget to QListWidget funList
        self.myBatch.addItem(itemN)
        self.myBatch.setItemWidget(itemN, widget)