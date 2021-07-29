# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Login.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import pymysql
from Tampilan import Ui_Form1
from Daftar import  Ui_Form2
class Ui_Form(object):
    def messagebox(self, title, message):
        mess = QtWidgets.QMessageBox()

        mess.setWindowTitle(title)
        mess.setText(message)
        mess.setStandardButtons(QtWidgets.QMessageBox.Ok)
        mess.exec_()

    def warning(self, title, message):
        mess = QtWidgets.QMessageBox()

        mess.setWindowTitle(title)
        mess.setText(message)
        mess.setStandardButtons(QtWidgets.QMessageBox.Ok)
        mess.exec_()
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(421, 484)
        Form.setStyleSheet("QWidget#Form{\n"
"background-color: qconicalgradient(cx:0.5, cy:0.5, angle:45, stop:0 rgba(144, 0, 0, 255), stop:1 rgba(255, 0, 0, 255))\n"
"}")
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(170, 40, 91, 91))
        font = QtGui.QFont()
        font.setPointSize(17)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setStyleSheet("color: rgb(255, 255, 255);")
        self.label.setObjectName("label")
        self.lineEdit = QtWidgets.QLineEdit(Form)
        self.lineEdit.setGeometry(QtCore.QRect(110, 190, 241, 20))
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(Form)
        self.lineEdit_2.setGeometry(QtCore.QRect(110, 240, 241, 20))
        self.lineEdit_2.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(50, 190, 61, 16))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(50, 240, 61, 16))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_3.setObjectName("label_3")
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(160, 330, 101, 31))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet("background-color: rgb(68, 68, 68);\n"
"color: rgb(255, 255, 255);")
        self.pushButton.clicked.connect(self.login)
        self.pushButton.setObjectName("pushButton")
        self.label_4 = QtWidgets.QLabel(Form)
        self.label_4.setGeometry(QtCore.QRect(90, 400, 181, 20))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_4.setObjectName("label_4")
        self.pushButton_2 = QtWidgets.QPushButton(Form)
        self.pushButton_2.setGeometry(QtCore.QRect(270, 400, 75, 21))
        self.pushButton_2.setStyleSheet("background-color: rgb(68, 68, 68);\n"
"color: rgb(255, 255, 255);")
        self.pushButton_2.clicked.connect(self.daftar)
        self.pushButton_2.setObjectName("pushButton_2")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)
    def daftar(self):
        self.Form = QtWidgets.QDialog()
        self.ui = Ui_Form2()
        self.ui.setupUi(self.Form)
        self.Form.show()
        Form.hide()

    def login(self):
        username = self.lineEdit.text()
        password = self.lineEdit_2.text()
        conn = pymysql.connect(host="localhost", user="root", password="", db="gui_tubes", port=3306, autocommit=True)
        cur = conn.cursor()
        query = "select * from pembeli where NickName=%s and Password=%s"
        data = cur.execute(query, (username, password))
        if (len(cur.fetchall()) > 0):
            self.messagebox("Berhasil", "Anda telah Login")
            self.Form = QtWidgets.QDialog()
            self.ui = Ui_Form1()
            self.ui.setupUi(self.Form)
            self.Form.show()
            Form.hide()


        else:
            self.warning("Gagal", "Masukkan Username dan Password yang benar")
    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", "LOGIN"))
        self.label_2.setText(_translate("Form", "Nickname"))
        self.label_3.setText(_translate("Form", "Password"))
        self.pushButton.setText(_translate("Form", "Masuk"))
        self.label_4.setText(_translate("Form", "Anda belum mempunyai akun ? "))
        self.pushButton_2.setText(_translate("Form", "Daftar"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())

