# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Main Window.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.

#import
from PyQt5 import QtCore, QtGui, QtWidgets

# membuat sebuah layout dengan widget dan ditambahkan komponen
class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(566, 614)
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(180, 40, 211, 20))
        font = QtGui.QFont()
        font.setFamily("Cooper Black")
        font.setPointSize(16)
        font.setBold(False)
        font.setWeight(50)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.textEdit = QtWidgets.QTextEdit(Form)
        self.textEdit.setGeometry(QtCore.QRect(60, 90, 441, 291))
        self.textEdit.setObjectName("textEdit")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(60, 400, 31, 16))
        font = QtGui.QFont()
        font.setFamily("Cooper Black")
        font.setPointSize(11)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.lineEdit = QtWidgets.QLineEdit(Form)
        self.lineEdit.setGeometry(QtCore.QRect(140, 400, 361, 20))
        self.lineEdit.setObjectName("lineEdit")
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(60, 430, 51, 16))
        font = QtGui.QFont()
        font.setFamily("Cooper Black")
        font.setPointSize(11)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.lineEdit_2 = QtWidgets.QLineEdit(Form)
        self.lineEdit_2.setGeometry(QtCore.QRect(140, 430, 361, 20))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.label_4 = QtWidgets.QLabel(Form)
        self.label_4.setGeometry(QtCore.QRect(60, 460, 71, 16))
        font = QtGui.QFont()
        font.setFamily("Cooper Black")
        font.setPointSize(11)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.lineEdit_3 = QtWidgets.QLineEdit(Form)
        self.lineEdit_3.setGeometry(QtCore.QRect(140, 460, 361, 20))
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.label_5 = QtWidgets.QLabel(Form)
        self.label_5.setGeometry(QtCore.QRect(60, 490, 71, 16))
        font = QtGui.QFont()
        font.setFamily("Cooper Black")
        font.setPointSize(11)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.lineEdit_4 = QtWidgets.QLineEdit(Form)
        self.lineEdit_4.setGeometry(QtCore.QRect(140, 490, 361, 20))
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(190, 520, 75, 23))
        font = QtGui.QFont()
        font.setFamily("Cooper Black")
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.pushButton_5 = QtWidgets.QPushButton(Form)
        self.pushButton_5.setGeometry(QtCore.QRect(270, 520, 75, 23))
        font = QtGui.QFont()
        font.setFamily("Cooper Black")
        self.pushButton_5.setFont(font)
        self.pushButton_5.setObjectName("pushButton_5")
        self.pushButton_6 = QtWidgets.QPushButton(Form)
        self.pushButton_6.setGeometry(QtCore.QRect(350, 520, 75, 23))
        font = QtGui.QFont()
        font.setFamily("Cooper Black")
        self.pushButton_6.setFont(font)
        self.pushButton_6.setObjectName("pushButton_6")
        self.pushButton_2 = QtWidgets.QPushButton(Form)
        self.pushButton_2.setGeometry(QtCore.QRect(430, 520, 75, 23))
        font = QtGui.QFont()
        font.setFamily("Cooper Black")
        self.pushButton_2.setFont(font)
        self.pushButton_2.setObjectName("pushButton_2")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", "DATA MAHASISWA"))
        self.label_2.setText(_translate("Form", "NIM"))
        self.label_3.setText(_translate("Form", "Nama"))
        self.label_4.setText(_translate("Form", "Jurusan"))
        self.label_5.setText(_translate("Form", "No. Telp"))
        self.pushButton.setText(_translate("Form", "TAMBAH"))
        self.pushButton_5.setText(_translate("Form", "EDIT"))
        self.pushButton_6.setText(_translate("Form", "CLEAR"))
        self.pushButton_2.setText(_translate("Form", "HAPUS"))

# untuk menampilkan layout widget yang tadi sudah dibuat dan menampilkan UInya
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())