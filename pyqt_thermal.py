# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'PyQT_thermalGUI.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import (QThread, Qt, pyqtSignal)
#from PyQt5.QtGui import (QPixmap, QImage)
#from PyQt5.QtWidgets import QLabel
import cv2

'''
class Thread(QThread):
    changePixmap = pyqtSignal(QPixmap)

    def __init__(self, parent=None):
        QThread.__init__(self, parent=parent)

    def run(self):
        cap = cv2.VideoCapture(0)
        while True:
            ret, frame = cap.read()
            #frame = cv2.resize(frame,(800,600))
            convertToQtFormat = QImage(frame.data, frame.shape[1], frame.shape[0], QImage.Format_RGB888)
            convertToQtFormat = QPixmap.fromImage(convertToQtFormat)
            p = convertToQtFormat.scaled(800, 600, Qt.KeepAspectRatio)
            self.changePixmap.emit(p)
'''

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.graphicsView = QtWidgets.QGraphicsView(self.centralwidget)
        self.graphicsView.setObjectName("graphicsView")
        self.gridLayout.addWidget(self.graphicsView, 0, 0, 1, 3)
        self.startvideo = QtWidgets.QPushButton(self.centralwidget)
        self.startvideo.setObjectName("startvideo")
        self.gridLayout.addWidget(self.startvideo, 1, 0, 1, 1)
        self.stopvideo = QtWidgets.QPushButton(self.centralwidget)
        self.stopvideo.setObjectName("stopvideo")
        self.gridLayout.addWidget(self.stopvideo, 1, 1, 1, 1)
        self.captureimage = QtWidgets.QPushButton(self.centralwidget)
        self.captureimage.setObjectName("captureimage")
        self.gridLayout.addWidget(self.captureimage, 1, 2, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 593, 21))
        self.menubar.setObjectName("menubar")
        self.menuThermal_Camera = QtWidgets.QMenu(self.menubar)
        self.menuThermal_Camera.setObjectName("menuThermal_Camera")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionClose = QtWidgets.QAction(MainWindow)
        self.actionClose.setObjectName("actionClose")
        self.menuThermal_Camera.addSeparator()
        self.menuThermal_Camera.addAction(self.actionClose)
        self.menubar.addAction(self.menuThermal_Camera.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Thermal Camera"))
        self.startvideo.setText(_translate("MainWindow", "Start Video"))
        self.stopvideo.setText(_translate("MainWindow", "Stop Video"))
        self.captureimage.setText(_translate("MainWindow", "Capture Image"))
        self.menuThermal_Camera.setTitle(_translate("MainWindow", "File"))
        self.actionClose.setText(_translate("MainWindow", "Close"))
        
    


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

