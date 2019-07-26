# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'PyQT_thermalGUI.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.Qt import *

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(593, 440)
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

Ui_MainWindow()

