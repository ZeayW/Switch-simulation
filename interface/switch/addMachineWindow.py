# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'addMachineWindow.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_addMachineWin(object):
    def setupUi(self, addMachineWin):
        addMachineWin.setObjectName("addMachineWin")
        addMachineWin.resize(197, 117)
        self.macEdit = QtWidgets.QLineEdit(addMachineWin)
        self.macEdit.setGeometry(QtCore.QRect(70, 10, 113, 21))
        self.macEdit.setObjectName("macEdit")
        self.linkEdit = QtWidgets.QLineEdit(addMachineWin)
        self.linkEdit.setGeometry(QtCore.QRect(70, 40, 113, 21))
        self.linkEdit.setText("")
        self.linkEdit.setObjectName("linkEdit")
        self.label = QtWidgets.QLabel(addMachineWin)
        self.label.setGeometry(QtCore.QRect(10, 10, 72, 15))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(addMachineWin)
        self.label_2.setGeometry(QtCore.QRect(30, 40, 72, 15))
        self.label_2.setObjectName("label_2")
        self.addBtn = QtWidgets.QPushButton(addMachineWin)
        self.addBtn.setGeometry(QtCore.QRect(82, 70, 101, 28))
        self.addBtn.setObjectName("addBtn")

        self.retranslateUi(addMachineWin)
        QtCore.QMetaObject.connectSlotsByName(addMachineWin)

    def retranslateUi(self, addMachineWin):
        _translate = QtCore.QCoreApplication.translate
        addMachineWin.setWindowTitle(_translate("addMachineWin", "Form"))
        self.label.setText(_translate("addMachineWin", "MAC地址"))
        self.label_2.setText(_translate("addMachineWin", "接入"))
        self.addBtn.setText(_translate("addMachineWin", "添加机器节点"))
