# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/Users/rwardrup/Projects/RadioTerm/gui/mainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.connectButton = QtWidgets.QPushButton(self.centralwidget)
        self.connectButton.setObjectName("connectButton")
        self.gridLayout.addWidget(self.connectButton, 0, 0, 1, 1)
        self.disconnectButton = QtWidgets.QPushButton(self.centralwidget)
        self.disconnectButton.setObjectName("disconnectButton")
        self.gridLayout.addWidget(self.disconnectButton, 0, 1, 1, 1)
        self.beaconButton = QtWidgets.QPushButton(self.centralwidget)
        self.beaconButton.setObjectName("beaconButton")
        self.gridLayout.addWidget(self.beaconButton, 0, 2, 1, 1)
        self.mheardButton = QtWidgets.QPushButton(self.centralwidget)
        self.mheardButton.setObjectName("mheardButton")
        self.gridLayout.addWidget(self.mheardButton, 0, 3, 1, 1)
        self.displayTextOutput = QtWidgets.QTextEdit(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.displayTextOutput.sizePolicy().hasHeightForWidth())
        self.displayTextOutput.setSizePolicy(sizePolicy)
        self.displayTextOutput.setReadOnly(True)
        self.displayTextOutput.setObjectName("displayTextOutput")
        self.gridLayout.addWidget(self.displayTextOutput, 1, 0, 1, 4)
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.gridLayout.addWidget(self.line, 2, 0, 1, 4)
        self.sendText = QtWidgets.QPlainTextEdit(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.sendText.sizePolicy().hasHeightForWidth())
        self.sendText.setSizePolicy(sizePolicy)
        self.sendText.setMaximumSize(QtCore.QSize(16777215, 100))
        self.sendText.setObjectName("sendText")
        self.gridLayout.addWidget(self.sendText, 3, 0, 1, 4)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusBar = QtWidgets.QStatusBar(MainWindow)
        self.statusBar.setObjectName("statusBar")
        MainWindow.setStatusBar(self.statusBar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "RadioTerm"))
        self.connectButton.setText(_translate("MainWindow", "Connect"))
        self.disconnectButton.setText(_translate("MainWindow", "Disconnect"))
        self.beaconButton.setText(_translate("MainWindow", "Beacon"))
        self.mheardButton.setText(_translate("MainWindow", "MHeard"))

