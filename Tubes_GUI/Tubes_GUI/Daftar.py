# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Daftar.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import pymysql
from Tampilan import Ui_Form1
class Ui_Form2(object):
    def messagebox(self,title,message):
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
        Form.resize(408, 468)
        Form.setStyleSheet("QWidget#Form{\n"
"background-color: qconicalgradient(cx:0.5, cy:0.5, angle:45, stop:0 rgba(144, 0, 0, 255), stop:1 rgba(255, 0, 0, 255))\n"
"}")
        self.label_5 = QtWidgets.QLabel(Form)
        self.label_5.setGeometry(QtCore.QRect(150, 50, 131, 91))
        font = QtGui.QFont()
        font.setPointSize(17)
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(Form)
        self.label_6.setGeometry(QtCore.QRect(40, 140, 61, 16))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_6.setFont(font)
        self.label_6.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_6.setObjectName("label_6")
        self.lineEdit_3 = QtWidgets.QLineEdit(Form)
        self.lineEdit_3.setGeometry(QtCore.QRect(100, 140, 241, 20))
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.label_7 = QtWidgets.QLabel(Form)
        self.label_7.setGeometry(QtCore.QRect(40, 180, 61, 16))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_7.setFont(font)
        self.label_7.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_7.setObjectName("label_7")
        self.lineEdit_4 = QtWidgets.QLineEdit(Form)
        self.lineEdit_4.setGeometry(QtCore.QRect(100, 180, 241, 20))
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(40, 260, 61, 16))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_3.setObjectName("label_3")
        self.lineEdit_5 = QtWidgets.QLineEdit(Form)
        self.lineEdit_5.setGeometry(QtCore.QRect(100, 260, 241, 20))
        self.lineEdit_5.setEchoMode(QtWidgets.QLineEdit.Normal)
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.label_4 = QtWidgets.QLabel(Form)
        self.label_4.setGeometry(QtCore.QRect(40, 220, 61, 16))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_4.setObjectName("label_4")
        self.lineEdit_6 = QtWidgets.QLineEdit(Form)
        self.lineEdit_6.setGeometry(QtCore.QRect(100, 220, 241, 20))
        self.lineEdit_6.setEchoMode(QtWidgets.QLineEdit.Normal)
        self.lineEdit_6.setObjectName("lineEdit_6")
        self.label_8 = QtWidgets.QLabel(Form)
        self.label_8.setGeometry(QtCore.QRect(40, 300, 61, 16))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_8.setFont(font)
        self.label_8.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_8.setObjectName("label_8")
        self.lineEdit_7 = QtWidgets.QLineEdit(Form)
        self.lineEdit_7.setGeometry(QtCore.QRect(100, 300, 241, 20))
        self.lineEdit_7.setEchoMode(QtWidgets.QLineEdit.Normal)
        self.lineEdit_7.setObjectName("lineEdit_7")
        self.pushButton_3 = QtWidgets.QPushButton(Form)
        self.pushButton_3.setGeometry(QtCore.QRect(170, 360, 75, 21))
        self.pushButton_3.setStyleSheet("background-color: rgb(68, 68, 68);\n"
"color: rgb(255, 255, 255);")
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_3.clicked.connect(self.daftar)
        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)
    def daftar(self):
        PembeliID = self.lineEdit_3.text()
        NickName = self.lineEdit_4.text()
        Email = self.lineEdit_6.text()
        Password = self.lineEdit_5.text()
        NoTelp = self.lineEdit_7.text()
        conn = pymysql.connect(host="localhost",user="root",password="",db="gui_tubes", port=3306,autocommit=True)
        cur = conn.cursor()
        query = ("insert into pembeli(PembeliID,NickName,Email,Password,NoTelp) values(%s,%s,%s,%s,%s)")
        data = cur.execute(query, (PembeliID,NickName,Email,Password,NoTelp))
        if(data):
            self.messagebox("Selamat", "Data Berhasil Ditambahkan")
            self.Form = QtWidgets.QDialog()
            self.ui = Ui_Form1()
            self.ui.setupUi(self.Form)
            self.Form.show()
            Form.hide()

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label_5.setText(_translate("Form", "DAFTAR"))
        self.label_6.setText(_translate("Form", "ID User"))
        self.label_7.setText(_translate("Form", "Nickname"))
        self.label_3.setText(_translate("Form", "Password"))
        self.label_4.setText(_translate("Form", "Email"))
        self.label_8.setText(_translate("Form", "No Telp"))
        self.pushButton_3.setText(_translate("Form", "Daftar"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form2()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())

