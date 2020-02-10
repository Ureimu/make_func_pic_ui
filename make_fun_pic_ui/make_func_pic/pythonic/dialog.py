# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'dialog.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(400, 300)
        Dialog.setMinimumSize(QtCore.QSize(400, 300))
        Dialog.setMaximumSize(QtCore.QSize(400, 300))
        self.progressBar = QtWidgets.QProgressBar(Dialog)
        self.progressBar.setGeometry(QtCore.QRect(20, 220, 371, 23))
        self.progressBar.setProperty("value", 36)
        self.progressBar.setOrientation(QtCore.Qt.Horizontal)
        self.progressBar.setObjectName("progressBar")
        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(310, 260, 75, 23))
        self.pushButton.setObjectName("pushButton")
        self.plainTextEdit = QtWidgets.QPlainTextEdit(Dialog)
        self.plainTextEdit.setGeometry(QtCore.QRect(20, 20, 361, 181))
        self.plainTextEdit.setObjectName("plainTextEdit")

        self.retranslateUi(Dialog)
        self.pushButton.clicked.connect(Dialog.exec)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.pushButton.setText(_translate("Dialog", "OK"))
