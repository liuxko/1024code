# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'test.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(869, 450)
        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(310, 380, 241, 41))
        self.pushButton.setObjectName("pushButton")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(20, 250, 91, 17))
        self.label.setObjectName("label")
        self.txtConsole = QtWidgets.QTextBrowser(Dialog)
        self.txtConsole.setGeometry(QtCore.QRect(560, 0, 311, 451))
        self.txtConsole.setObjectName("txtConsole")
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(20, 300, 91, 17))
        self.label_3.setObjectName("label_3")
        self.label_5 = QtWidgets.QLabel(Dialog)
        self.label_5.setGeometry(QtCore.QRect(20, 350, 91, 17))
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(Dialog)
        self.label_6.setGeometry(QtCore.QRect(310, 300, 81, 17))
        self.label_6.setObjectName("label_6")
        self.txtBaseCode = QtWidgets.QLineEdit(Dialog)
        self.txtBaseCode.setGeometry(QtCore.QRect(100, 240, 191, 31))
        self.txtBaseCode.setPlaceholderText("")
        self.txtBaseCode.setObjectName("txtBaseCode")
        self.label_7 = QtWidgets.QLabel(Dialog)
        self.label_7.setGeometry(QtCore.QRect(310, 350, 81, 20))
        self.label_7.setObjectName("label_7")
        self.txtVerfityCd = QtWidgets.QLineEdit(Dialog)
        self.txtVerfityCd.setGeometry(QtCore.QRect(390, 340, 161, 31))
        self.txtVerfityCd.setPlaceholderText("")
        self.txtVerfityCd.setObjectName("txtVerfityCd")
        self.txtSeed = QtWidgets.QLineEdit(Dialog)
        self.txtSeed.setGeometry(QtCore.QRect(100, 340, 191, 31))
        self.txtSeed.setPlaceholderText("")
        self.txtSeed.setObjectName("txtSeed")
        self.txtOffset = QtWidgets.QLineEdit(Dialog)
        self.txtOffset.setGeometry(QtCore.QRect(100, 390, 191, 31))
        self.txtOffset.setPlaceholderText("")
        self.txtOffset.setObjectName("txtOffset")
        self.label_8 = QtWidgets.QLabel(Dialog)
        self.label_8.setGeometry(QtCore.QRect(20, 400, 91, 17))
        self.label_8.setObjectName("label_8")
        self.txtCdNow = QtWidgets.QTextBrowser(Dialog)
        self.txtCdNow.setGeometry(QtCore.QRect(100, 290, 191, 31))
        self.txtCdNow.setObjectName("txtCdNow")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(400, 280, 141, 41))
        self.label_2.setMidLineWidth(1)
        self.label_2.setText("")
        self.label_2.setObjectName("label_2")
        self.label_9 = QtWidgets.QLabel(Dialog)
        self.label_9.setGeometry(QtCore.QRect(310, 250, 221, 17))
        font = QtGui.QFont()
        font.setFamily("文泉驿正黑")
        font.setPointSize(12)
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "1024邀请码"))
        self.pushButton.setText(_translate("Dialog", "开始验证"))
        self.label.setText(_translate("Dialog", "邀请码拼接："))
        self.label_3.setText(_translate("Dialog", "当前拼接码："))
        self.label_5.setText(_translate("Dialog", "随机数种子："))
        self.label_6.setText(_translate("Dialog", "验证码图片："))
        self.txtBaseCode.setText(_translate("Dialog", "????"))
        self.label_7.setText(_translate("Dialog", "验证码文本："))
        self.txtSeed.setText(_translate("Dialog", "0123456789abcdef"))
        self.txtOffset.setText(_translate("Dialog", "0"))
        self.label_8.setText(_translate("Dialog", "拼接偏移量："))
        self.label_9.setText(_translate("Dialog", "(‘?’作为随机数占位符)"))

