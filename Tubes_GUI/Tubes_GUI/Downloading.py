# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Downloading.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!
import sys
from PyQt5.QtCore import *
from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form7(object):
    def messagebox(self, title, message):
        mess = QtWidgets.QMessageBox()
        mess.setWindowTitle(title)
        mess.setText(message)
        mess.setStandardButtons(QtWidgets.QMessageBox.Ok)
        mess.exec_()

    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(650, 439)
        Form.setStyleSheet("QWidget#Form {\n"
"background-color: qconicalgradient(cx:0.5, cy:0.5, angle:45, stop:0 rgba(144, 0, 0, 255), stop:1 rgba(255, 0, 0, 255));\n"
"}")

        self.progressBar = QtWidgets.QProgressBar(Form)
        self.progressBar.setGeometry(QtCore.QRect(20, 250, 591, 16))
        self.progressBar.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(74, 74, 74);")
        self.progressBar.setObjectName("progressBar")
        self.progressBar.setValue(100)
        self.timer = QBasicTimer
        self.step = 0
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(20, 280, 75, 23))
        self.pushButton.setStyleSheet("background-color: rgb(68, 68, 68);\n"
"color: rgb(255, 255, 255);\n"
"\n"
"font-color : rgb(255, 255, 255)")
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.start)
        self.pushButton_2 = QtWidgets.QPushButton(Form)
        self.pushButton_2.setGeometry(QtCore.QRect(100, 280, 75, 23))
        self.pushButton_2.setStyleSheet("background-color: rgb(68, 68, 68);\n"
"color: rgb(255, 255, 255);\n"
"\n"
"font-color : rgb(255, 255, 255)")
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_2.clicked.connect(self.cancel)
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(20, 50, 261, 151))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap(":/header.jpg"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(290, 50, 441, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(290, 80, 221, 16))
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(Form)
        self.label_4.setGeometry(QtCore.QRect(290, 100, 121, 16))
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(False)
        font.setWeight(50)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(Form)
        self.label_5.setGeometry(QtCore.QRect(290, 120, 201, 16))
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(False)
        font.setWeight(50)
        self.label_5.setFont(font)
        self.label_5.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(Form)
        self.label_6.setGeometry(QtCore.QRect(290, 160, 201, 16))
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(False)
        font.setWeight(50)
        self.label_6.setFont(font)
        self.label_6.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(Form)
        self.label_7.setGeometry(QtCore.QRect(290, 140, 201, 16))
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(False)
        font.setWeight(50)
        self.label_7.setFont(font)
        self.label_7.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(Form)
        self.label_8.setGeometry(QtCore.QRect(20, 230, 201, 16))
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(False)
        font.setWeight(50)
        self.label_8.setFont(font)
        self.label_8.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_8.setObjectName("label_8")
        self.pushButton_3 = QtWidgets.QPushButton(Form)
        self.pushButton_3.setGeometry(QtCore.QRect(290, 190, 91, 31))
        self.pushButton_3.setStyleSheet("background-color: rgb(230, 0, 0);\n"
"color: rgb(0, 0, 0);\n"
"background-color: rgb(0, 184, 184);\n"
"\n"
"\n"
"")
        self.pushButton_3.setObjectName("pushButton_3")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)


    def cancel(self):
        self.step = 0
        self.progressBar.setValue(0)
        self.messagebox("Warning","Download dibatalkan")
        from Tampilan import Ui_Form1
        self.Form = QtWidgets.QDialog()
        self.ui = Ui_Form1()
        self.ui.setupUi(self.Form)
        self.Form.show()
        Form.hide()

    def timerEvent(self, event):
        if self.step >= 100:
            self.timer.stop()
            self.pushButton.setText('Selesai')
            return

        self.step += 1
        self.progressBar.setValue(self.step)
    def start(self, event):
        if self.timer.isActive():
            self.timer.stop()
            self.pushButton.setText('Start')
        else:
            self.timer.start(100, self)
            self.pushButton.setText('Stop')



    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.pushButton.setText(_translate("Form", "Start"))
        self.pushButton_2.setText(_translate("Form", "Cancel"))
        self.label_2.setText(_translate("Form", "Parakacuk "))
        self.label_3.setText(_translate("Form", "Genre : School, Fight and Adventure"))
        self.label_4.setText(_translate("Form", "Ukuran : 19 GB"))
        self.label_5.setText(_translate("Form", "Kebutuhan space kosong : 30 GB"))
        self.label_6.setText(_translate("Form", "Minimum RAM : 8 GB"))
        self.label_7.setText(_translate("Form", "Space kosong 48 GB"))
        self.label_8.setText(_translate("Form", "Proses downloading..."))
        self.pushButton_3.setText(_translate("Form", "Play Now"))

import haha

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form7()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())

