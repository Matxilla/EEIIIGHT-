# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\untitled.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        self.line = ""
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(250, 210)
        MainWindow.setMinimumSize(QtCore.QSize(250, 210))
        MainWindow.setMaximumSize(QtCore.QSize(250, 210))
        MainWindow.setStyleSheet("QPushButton{border-radius:0px;background-color:rgb(174,170,164)}")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.buttang1 = QtWidgets.QPushButton(self.centralwidget)
        self.buttang1.setEnabled(True)
        self.buttang1.setGeometry(QtCore.QRect(10, 50, 30, 30))
        self.buttang1.setObjectName("buttang1")
        self.buttang1.clicked.connect(lambda: self.getbutton(self.buttang1))
        self.buttang1.setProperty('value', "1")

        self.buttang2 = QtWidgets.QPushButton(self.centralwidget)
        self.buttang2.setEnabled(True)
        self.buttang2.setGeometry(QtCore.QRect(50, 50, 30, 30))
        self.buttang2.setObjectName("buttang2")
        self.buttang2.clicked.connect(lambda: self.getbutton(self.buttang2))
        self.buttang2.setProperty('value', "2")

        self.buttang3 = QtWidgets.QPushButton(self.centralwidget)
        self.buttang3.setEnabled(True)
        self.buttang3.setGeometry(QtCore.QRect(90, 50, 30, 30))
        self.buttang3.setObjectName("buttang3")
        self.buttang3.clicked.connect(lambda: self.getbutton(self.buttang3))
        self.buttang3.setProperty('value', "3")

        self.buttang4 = QtWidgets.QPushButton(self.centralwidget)
        self.buttang4.setEnabled(True)
        self.buttang4.setGeometry(QtCore.QRect(10, 90, 30, 30))
        self.buttang4.setObjectName("buttang4")
        self.buttang4.clicked.connect(lambda: self.getbutton(self.buttang4))
        self.buttang4.setProperty('value', "4")

        self.buttang5 = QtWidgets.QPushButton(self.centralwidget)
        self.buttang5.setEnabled(True)
        self.buttang5.setGeometry(QtCore.QRect(50, 90, 30, 30))
        self.buttang5.setObjectName("buttang5")
        self.buttang5.clicked.connect(lambda: self.getbutton(self.buttang5))
        self.buttang5.setProperty('value', "5")

        self.buttang6 = QtWidgets.QPushButton(self.centralwidget)
        self.buttang6.setEnabled(True)
        self.buttang6.setGeometry(QtCore.QRect(90, 90, 30, 30))
        self.buttang6.setObjectName("buttang6")
        self.buttang6.clicked.connect(lambda: self.getbutton(self.buttang6))
        self.buttang6.setProperty('value', "6")

        self.buttang7 = QtWidgets.QPushButton(self.centralwidget)
        self.buttang7.setEnabled(True)
        self.buttang7.setGeometry(QtCore.QRect(10, 130, 30, 30))
        self.buttang7.setObjectName("buttang7")
        self.buttang7.clicked.connect(lambda: self.getbutton(self.buttang7))
        self.buttang7.setProperty('value', "7")

        self.buttang8 = QtWidgets.QPushButton(self.centralwidget)
        self.buttang8.setEnabled(True)
        self.buttang8.setGeometry(QtCore.QRect(50, 130, 30, 30))
        self.buttang8.setObjectName("buttang8")
        self.buttang8.clicked.connect(lambda: self.getbutton(self.buttang8))
        self.buttang8.setProperty('value', "8")

        self.buttang9 = QtWidgets.QPushButton(self.centralwidget)
        self.buttang9.setEnabled(True)
        self.buttang9.setGeometry(QtCore.QRect(90, 130, 30, 30))
        self.buttang9.setObjectName("buttang9")
        self.buttang9.clicked.connect(lambda: self.getbutton(self.buttang9))
        self.buttang9.setProperty('value', "9")

        self.buttang10 = QtWidgets.QPushButton(self.centralwidget)
        self.buttang10.setEnabled(True)
        self.buttang10.setGeometry(QtCore.QRect(10, 170, 30, 30))
        self.buttang10.setObjectName("buttang10")
        self.buttang10.clicked.connect(lambda: self.getbutton(self.buttang10))
        self.buttang10.setProperty('value', ".")

        self.buttang11 = QtWidgets.QPushButton(self.centralwidget)
        self.buttang11.setEnabled(True)
        self.buttang11.setGeometry(QtCore.QRect(50, 170, 30, 30))
        self.buttang11.setObjectName("buttang11")
        self.buttang11.clicked.connect(lambda: self.getbutton(self.buttang11))
        self.buttang11.setProperty('value', "0")

        self.buttang12 = QtWidgets.QPushButton(self.centralwidget)
        self.buttang12.setEnabled(True)
        self.buttang12.setGeometry(QtCore.QRect(90, 170, 70, 30))
        self.buttang12.setObjectName("buttang12")
        self.buttang12.clicked.connect(lambda: self.getbutton(self.buttang12))
        self.buttang12.setProperty('value', "00")
        
        self.buttang13 = QtWidgets.QPushButton(self.centralwidget)
        self.buttang13.setEnabled(True)
        self.buttang13.setGeometry(QtCore.QRect(130, 50, 30, 30))
        self.buttang13.setObjectName("buttang13")
        self.buttang13.clicked.connect(lambda: self.getbutton(self.buttang13))
        self.buttang13.setProperty('value', "+")

        self.buttang14 = QtWidgets.QPushButton(self.centralwidget)
        self.buttang14.setEnabled(True)
        self.buttang14.setGeometry(QtCore.QRect(130, 90, 30, 30))
        self.buttang14.setObjectName("buttang14")
        self.buttang14.clicked.connect(lambda: self.getbutton(self.buttang14))
        self.buttang14.setProperty('value', "-")

        self.buttang15 = QtWidgets.QPushButton(self.centralwidget)
        self.buttang15.setEnabled(True)
        self.buttang15.setGeometry(QtCore.QRect(130, 130, 30, 30))
        self.buttang15.setObjectName("buttang15")
        self.buttang15.clicked.connect(lambda: self.getbutton(self.buttang15))
        self.buttang15.setProperty('value', "*")

        self.buttang16 = QtWidgets.QPushButton(self.centralwidget)
        self.buttang16.setEnabled(True)
        self.buttang16.setGeometry(QtCore.QRect(170, 50, 70, 30))
        self.buttang16.setObjectName("buttang16")
        self.buttang16.clicked.connect(lambda: self.getbutton(self.buttang16))
        self.buttang16.setProperty('value', "C")

        self.buttang17 = QtWidgets.QPushButton(self.centralwidget)
        self.buttang17.setEnabled(True)
        self.buttang17.setGeometry(QtCore.QRect(170, 90, 70, 110))
        self.buttang17.setObjectName("buttang17")
        self.buttang17.clicked.connect(lambda: self.getbutton(self.buttang17))
        self.buttang17.setProperty('value', "=")

        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(10, 10, 230, 30))
        self.lineEdit.setObjectName("lineEdit")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.buttang1.setText(_translate("MainWindow", "1"))
        self.buttang2.setText(_translate("MainWindow", "2"))
        self.buttang3.setText(_translate("MainWindow", "3"))
        self.buttang4.setText(_translate("MainWindow", "4"))
        self.buttang5.setText(_translate("MainWindow", "5"))
        self.buttang6.setText(_translate("MainWindow", "6"))
        self.buttang7.setText(_translate("MainWindow", "7"))
        self.buttang8.setText(_translate("MainWindow", "8"))
        self.buttang9.setText(_translate("MainWindow", "9"))
        self.buttang10.setText(_translate("MainWindow", "."))
        self.buttang11.setText(_translate("MainWindow", "0"))
        self.buttang12.setText(_translate("MainWindow", "00"))
        self.buttang13.setText(_translate("MainWindow", "+"))
        self.buttang14.setText(_translate("MainWindow", "-"))
        self.buttang15.setText(_translate("MainWindow", "*"))
        self.buttang16.setText(_translate("MainWindow", "C"))
        self.buttang17.setText(_translate("MainWindow", "="))

    def getbutton(self, butt):
        data = butt.property('value')
        print(data)
        if data == "10000-10000":
            from main import eighth
            print("CCC")
            eighth()
        if not data == "=":
            self.line += data
        if data == "C":
            self.line = ""
        elif data == "=":
            print(self.line)
            if self.line == "10000-10000":
                from main import eighth
                print("CCC")
                eighth()
            else:
                self.line = str(eval(self.line))
        self.lineEdit.setText(self.line)
        