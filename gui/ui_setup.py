# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/Users/rwardrup/Projects/RadioTerm/gui/ui_setup.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(400, 300)
        self.gridLayout = QtWidgets.QGridLayout(Dialog)
        self.gridLayout.setObjectName("gridLayout")
        self.portInput = QtWidgets.QLineEdit(Dialog)
        self.portInput.setObjectName("portInput")
        self.gridLayout.addWidget(self.portInput, 5, 1, 1, 1)
        self.beaconIntervalInput = QtWidgets.QSpinBox(Dialog)
        self.beaconIntervalInput.setMaximum(999)
        self.beaconIntervalInput.setObjectName("beaconIntervalInput")
        self.gridLayout.addWidget(self.beaconIntervalInput, 3, 1, 1, 1)
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 3, 0, 1, 1)
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 5, 0, 1, 1)
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 4, 0, 1, 1)
        self.digipeatersInput = QtWidgets.QLineEdit(Dialog)
        self.digipeatersInput.setObjectName("digipeatersInput")
        self.gridLayout.addWidget(self.digipeatersInput, 2, 1, 1, 1)
        self.callSignLabel = QtWidgets.QLabel(Dialog)
        self.callSignLabel.setObjectName("callSignLabel")
        self.gridLayout.addWidget(self.callSignLabel, 1, 0, 1, 1)
        self.callSignInput = QtWidgets.QLineEdit(Dialog)
        self.callSignInput.setObjectName("callSignInput")
        self.gridLayout.addWidget(self.callSignInput, 1, 1, 1, 1)
        self.digipeatersLabel = QtWidgets.QLabel(Dialog)
        self.digipeatersLabel.setObjectName("digipeatersLabel")
        self.gridLayout.addWidget(self.digipeatersLabel, 2, 0, 1, 1)
        self.hostIpInput = QtWidgets.QLineEdit(Dialog)
        self.hostIpInput.setObjectName("hostIpInput")
        self.gridLayout.addWidget(self.hostIpInput, 4, 1, 1, 1)
        self.label_4 = QtWidgets.QLabel(Dialog)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 6, 0, 1, 1)
        self.pacLenInput = QtWidgets.QLineEdit(Dialog)
        self.pacLenInput.setObjectName("pacLenInput")
        self.gridLayout.addWidget(self.pacLenInput, 6, 1, 1, 1)
        self.buttonBox = QtWidgets.QDialogButtonBox(Dialog)
        self.buttonBox.setOrientation(QtCore.Qt.Vertical)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.gridLayout.addWidget(self.buttonBox, 1, 2, 6, 1)

        self.retranslateUi(Dialog)
        self.buttonBox.accepted.connect(Dialog.accept)
        self.buttonBox.rejected.connect(Dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.portInput.setText(_translate("Dialog", "8000"))
        self.label.setText(_translate("Dialog", "Beacon Interval:"))
        self.label_3.setText(_translate("Dialog", "Port:"))
        self.label_2.setText(_translate("Dialog", "Host IP:"))
        self.callSignLabel.setText(_translate("Dialog", "Callsign: "))
        self.digipeatersLabel.setText(_translate("Dialog", "Digipeaters: "))
        self.hostIpInput.setText(_translate("Dialog", "localhost"))
        self.label_4.setText(_translate("Dialog", "Packet Length:"))

