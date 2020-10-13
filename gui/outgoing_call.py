# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/Users/rwardrup/Projects/RadioTerm/gui/outgoing_call.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(400, 91)
        self.gridLayout = QtWidgets.QGridLayout(Dialog)
        self.gridLayout.setObjectName("gridLayout")
        self.outgoingCallButtons = QtWidgets.QDialogButtonBox(Dialog)
        self.outgoingCallButtons.setOrientation(QtCore.Qt.Vertical)
        self.outgoingCallButtons.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.outgoingCallButtons.setObjectName("outgoingCallButtons")
        self.gridLayout.addWidget(self.outgoingCallButtons, 0, 2, 3, 1)
        self.outgoingCallLabel = QtWidgets.QLabel(Dialog)
        self.outgoingCallLabel.setObjectName("outgoingCallLabel")
        self.gridLayout.addWidget(self.outgoingCallLabel, 0, 0, 1, 1)
        self.callDigipeatersInput = QtWidgets.QLineEdit(Dialog)
        self.callDigipeatersInput.setObjectName("callDigipeatersInput")
        self.gridLayout.addWidget(self.callDigipeatersInput, 1, 1, 1, 1)
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 1, 0, 1, 1)
        self.outgoingCallInput = QtWidgets.QComboBox(Dialog)
        self.outgoingCallInput.setObjectName("outgoingCallInput")
        self.gridLayout.addWidget(self.outgoingCallInput, 0, 1, 1, 1)

        self.retranslateUi(Dialog)
        self.outgoingCallButtons.accepted.connect(Dialog.accept)
        self.outgoingCallButtons.rejected.connect(Dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.outgoingCallLabel.setText(_translate("Dialog", "Outgoing Call: "))
        self.label.setText(_translate("Dialog", "Digipeaters: "))

