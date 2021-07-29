# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Sell.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import pymysql
from DevBio import Ui_Form9
class Ui_Form8(object):
    def messagebox(self, title, message):
        mess = QtWidgets.QMessageBox()
        mess.setWindowTitle(title)
        mess.setText(message)
        mess.setStandardButtons(QtWidgets.QMessageBox.Ok)
        mess.exec_()
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(512, 515)
        Form.setStyleSheet("QWidget#Form {\n"
"background-color: qconicalgradient(cx:0.5, cy:0.5, angle:45, stop:0 rgba(144, 0, 0, 255), stop:1 rgba(255, 0, 0, 255));\n"
"}")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(200, 30, 181, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_2.setObjectName("label_2")
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(70, 100, 381, 361))
        self.label.setStyleSheet("background-color: rgb(67, 67, 67);")
        self.label.setText("")
        self.label.setObjectName("label")
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(160, 110, 181, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_3.setObjectName("label_3")
        self.label_12 = QtWidgets.QLabel(Form)
        self.label_12.setGeometry(QtCore.QRect(90, 140, 81, 21))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.label_12.setFont(font)
        self.label_12.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_12.setObjectName("label_12")
        self.lineEdit12 = QtWidgets.QLineEdit(Form)
        self.lineEdit12.setGeometry(QtCore.QRect(190, 140, 221, 20))
        self.lineEdit12.setStyleSheet(
                "background-color: qconicalgradient(cx:0.5, cy:0.5, angle:45, stop:0 rgba(144, 0, 0, 255), stop:1 rgba(255, 0, 0, 255));\n"
                "background-color: rgb(139, 139, 139);\n"
                "color: rgb(255, 255, 255);")
        self.lineEdit12.setObjectName("lineEdit12")
        self.label_4 = QtWidgets.QLabel(Form)
        self.label_4.setGeometry(QtCore.QRect(90, 170, 81, 21))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_4.setObjectName("label_4")
        self.lineEdit = QtWidgets.QLineEdit(Form)
        self.lineEdit.setGeometry(QtCore.QRect(190, 170, 221, 20))
        self.lineEdit.setStyleSheet("background-color: qconicalgradient(cx:0.5, cy:0.5, angle:45, stop:0 rgba(144, 0, 0, 255), stop:1 rgba(255, 0, 0, 255));\n"
"background-color: rgb(139, 139, 139);\n"
"color: rgb(255, 255, 255);")
        self.lineEdit.setObjectName("lineEdit")
        self.label_5 = QtWidgets.QLabel(Form)
        self.label_5.setGeometry(QtCore.QRect(90, 200, 81, 21))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_5.setObjectName("label_5")
        self.lineEdit_2 = QtWidgets.QLineEdit(Form)
        self.lineEdit_2.setGeometry(QtCore.QRect(190, 200, 221, 20))
        self.lineEdit_2.setStyleSheet("background-color: qconicalgradient(cx:0.5, cy:0.5, angle:45, stop:0 rgba(144, 0, 0, 255), stop:1 rgba(255, 0, 0, 255));\n"
"background-color: rgb(139, 139, 139);\n"
"color: rgb(255, 255, 255);")
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.label_6 = QtWidgets.QLabel(Form)
        self.label_6.setGeometry(QtCore.QRect(90, 230, 81, 21))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.label_6.setFont(font)
        self.label_6.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_6.setObjectName("label_6")
        self.lineEdit_3 = QtWidgets.QLineEdit(Form)
        self.lineEdit_3.setGeometry(QtCore.QRect(190, 230, 221, 20))
        self.lineEdit_3.setStyleSheet("background-color: qconicalgradient(cx:0.5, cy:0.5, angle:45, stop:0 rgba(144, 0, 0, 255), stop:1 rgba(255, 0, 0, 255));\n"
"background-color: rgb(139, 139, 139);\n"
"color: rgb(255, 255, 255);")
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.label_7 = QtWidgets.QLabel(Form)
        self.label_7.setGeometry(QtCore.QRect(90, 260, 91, 21))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.label_7.setFont(font)
        self.label_7.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_7.setObjectName("label_7")
        self.lineEdit_4 = QtWidgets.QLineEdit(Form)
        self.lineEdit_4.setGeometry(QtCore.QRect(190, 260, 221, 20))
        self.lineEdit_4.setStyleSheet("background-color: qconicalgradient(cx:0.5, cy:0.5, angle:45, stop:0 rgba(144, 0, 0, 255), stop:1 rgba(255, 0, 0, 255));\n"
"background-color: rgb(139, 139, 139);\n"
"color: rgb(255, 255, 255);")
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.label_8 = QtWidgets.QLabel(Form)
        self.label_8.setGeometry(QtCore.QRect(90, 300, 101, 21))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.label_8.setFont(font)
        self.label_8.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_8.setObjectName("label_8")
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(410, 480, 81, 23))
        self.pushButton.setStyleSheet("background-color: rgb(68, 68, 68);\n"
"color: rgb(255, 255, 255);\n"
"\n"
"font-color : rgb(255, 255, 255)")
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.jual)
        self.label_9 = QtWidgets.QLabel(Form)
        self.label_9.setGeometry(QtCore.QRect(70, 60, 491, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_9.setFont(font)
        self.label_9.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_9.setObjectName("label_9")
        self.lineEdit13 = QtWidgets.QLineEdit(Form)
        self.lineEdit13.setGeometry(QtCore.QRect(190, 300, 221, 121))
        self.lineEdit13.setStyleSheet("background-color: rgb(139, 139, 139);\n"
"color: rgb(255, 255, 255);")
        self.lineEdit13.setObjectName("lineEdit")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)
    def jual(self):
        GameID = self.lineEdit12.text()
        Nama_Game = self.lineEdit.text()
        Genre = self.lineEdit_2.text()
        Tahun_rilis = self.lineEdit_3.text()
        Harga = self.lineEdit_4.text()
        Deskripsi = self.lineEdit13.text()
        conn = pymysql.connect(host="localhost",user="root",password="",db="gui_tubes", port=3306,autocommit=True)
        cur = conn.cursor()
        query = ("insert into game(GameID,Nama_Game,Genre,Tahun_rilis,Harga,Deskripsi) values(%s,%s,%s,%s,%s,%s)")
        data = cur.execute(query, (GameID,Nama_Game,Genre,Tahun_rilis,Harga,Deskripsi))
        if(data):
            self.messagebox("Selamat", "Silahkan isi data Developer")
            self.Form = QtWidgets.QDialog()
            self.ui = Ui_Form9()
            self.ui.setupUi(self.Form)
            self.Form.show()
            Form.hide()
    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label_12.setText(_translate("Form","Kode Game"))
        self.label_2.setText(_translate("Form", "Sell your Game"))
        self.label_3.setText(_translate("Form", "Isi beberapa dokumen berikut ini"))
        self.label_4.setText(_translate("Form", "Nama Game "))
        self.label_5.setText(_translate("Form", "Genre"))
        self.label_6.setText(_translate("Form", "Tahun Rilis"))
        self.label_7.setText(_translate("Form", "Ajukan Harga"))
        self.label_8.setText(_translate("Form", "Deskripsi Game "))
        self.pushButton.setText(_translate("Form", "Berikutnya"))
        self.label_9.setText(_translate("Form", "Ajukan game game terbaik kalian untuk dikenal oleh dunia "))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form8()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())

