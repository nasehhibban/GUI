# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'DevBio.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import pymysql

class Ui_Form9(object):
    def messagebox(self, title, message):
        mess = QtWidgets.QMessageBox()
        mess.setWindowTitle(title)
        mess.setText(message)
        mess.setStandardButtons(QtWidgets.QMessageBox.Ok)
        mess.exec_()
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(508, 524)
        Form.setStyleSheet("QWidget#Form {\n"
"background-color: qconicalgradient(cx:0.5, cy:0.5, angle:45, stop:0 rgba(144, 0, 0, 255), stop:1 rgba(255, 0, 0, 255));\n"
"}")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(170, 30, 171, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(190, 90, 181, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(Form)
        self.label_4.setGeometry(QtCore.QRect(100, 150, 81, 21))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_4.setObjectName("label_4")
        self.lineEdit = QtWidgets.QLineEdit(Form)
        self.lineEdit.setGeometry(QtCore.QRect(200, 150, 221, 20))
        self.lineEdit.setStyleSheet("background-color: qconicalgradient(cx:0.5, cy:0.5, angle:45, stop:0 rgba(144, 0, 0, 255), stop:1 rgba(255, 0, 0, 255));\n"
"background-color: rgb(139, 139, 139);\n"
"color: rgb(255, 255, 255);")
        self.lineEdit.setObjectName("lineEdit")
        self.label_5 = QtWidgets.QLabel(Form)
        self.label_5.setGeometry(QtCore.QRect(100, 180, 81, 21))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(Form)
        self.label_6.setGeometry(QtCore.QRect(100, 210, 81, 21))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.label_6.setFont(font)
        self.label_6.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(Form)
        self.label_7.setGeometry(QtCore.QRect(100, 240, 91, 21))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.label_7.setFont(font)
        self.label_7.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_7.setObjectName("label_7")
        self.lineEdit_4 = QtWidgets.QLineEdit(Form)
        self.lineEdit_4.setGeometry(QtCore.QRect(200, 240, 221, 20))
        self.lineEdit_4.setStyleSheet("background-color: qconicalgradient(cx:0.5, cy:0.5, angle:45, stop:0 rgba(144, 0, 0, 255), stop:1 rgba(255, 0, 0, 255));\n"
"background-color: rgb(139, 139, 139);\n"
"color: rgb(255, 255, 255);")
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.lineEdit_2 = QtWidgets.QLineEdit(Form)
        self.lineEdit_2.setGeometry(QtCore.QRect(200, 180, 221, 20))
        self.lineEdit_2.setStyleSheet("background-color: qconicalgradient(cx:0.5, cy:0.5, angle:45, stop:0 rgba(144, 0, 0, 255), stop:1 rgba(255, 0, 0, 255));\n"
"background-color: rgb(139, 139, 139);\n"
"color: rgb(255, 255, 255);")
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.lineEdit_3 = QtWidgets.QLineEdit(Form)
        self.lineEdit_3.setGeometry(QtCore.QRect(200, 210, 221, 20))
        self.lineEdit_3.setStyleSheet("background-color: qconicalgradient(cx:0.5, cy:0.5, angle:45, stop:0 rgba(144, 0, 0, 255), stop:1 rgba(255, 0, 0, 255));\n"
"background-color: rgb(139, 139, 139);\n"
"color: rgb(255, 255, 255);")
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(70, 80, 381, 361))
        self.label.setStyleSheet("background-color: rgb(67, 67, 67);")
        self.label.setText("")
        self.label.setObjectName("label")
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(200, 460, 141, 41))
        self.pushButton.setStyleSheet("background-color: rgb(68, 68, 68);\n"
"color: rgb(255, 255, 255);\n"
"\n"
"font-color : rgb(255, 255, 255)")
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.ajukan)
        self.label.raise_()
        self.label_2.raise_()
        self.label_3.raise_()
        self.label_4.raise_()
        self.lineEdit.raise_()
        self.label_5.raise_()
        self.label_6.raise_()
        self.label_7.raise_()
        self.lineEdit_4.raise_()
        self.lineEdit_2.raise_()
        self.lineEdit_3.raise_()
        self.pushButton.raise_()

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def ajukan(self):
            DeveloperID = self.lineEdit.text()
            Nama = self.lineEdit_2.text()
            Email = self.lineEdit_3.text()
            Alamat = self.lineEdit_4.text()
            conn = pymysql.connect(host="localhost", user="root", password="", db="gui_tubes", port=3306,
                                   autocommit=True)
            cur = conn.cursor()
            query = ("insert into developer(DeveloperID,Nama,Email,Alamat) values(%s,%s,%s,%s)")
            data = cur.execute(query, (DeveloperID,Nama,Email,Alamat))
            if (data):
                    self.Form = QtWidgets.QDialog()
                    from Tampilan import Ui_Form1
                    self.ui = Ui_Form1()
                    self.ui.setupUi(self.Form)
                    self.Form.show()
                    Form.hide()
                    self.messagebox("Terkirim", "Silahkan tunggu verifikasi dari kami")
            else  :
                    self.messagebox("Gagal", "Isi Data terlebih dahulu")

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label_2.setText(_translate("Form", "DATA DEVELOPER"))
        self.label_3.setText(_translate("Form", "Isi biodata berikut "))
        self.label_4.setText(_translate("Form", "Kode Devlop"))
        self.label_5.setText(_translate("Form", "Nama"))
        self.label_6.setText(_translate("Form", "Email"))
        self.label_7.setText(_translate("Form", "Alamat"))
        self.pushButton.setText(_translate("Form", "Ajukan"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form9()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())

