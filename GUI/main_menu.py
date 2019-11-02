# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main_menu.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(500, 438)
        self.main_menu = QtWidgets.QWidget(MainWindow)
        self.main_menu.setObjectName("main_menu")
        self.label = QtWidgets.QLabel(self.main_menu)
        self.label.setGeometry(QtCore.QRect(20, 10, 71, 16))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.main_menu)
        self.label_2.setGeometry(QtCore.QRect(20, 40, 61, 16))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.main_menu)
        self.label_3.setGeometry(QtCore.QRect(20, 70, 101, 21))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(16)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.main_menu)
        self.label_4.setGeometry(QtCore.QRect(20, 120, 47, 13))
        self.label_4.setText("")
        self.label_4.setObjectName("label_4")
        self.recipient_addr = QtWidgets.QPlainTextEdit(self.main_menu)
        self.recipient_addr.setGeometry(QtCore.QRect(100, 100, 371, 31))
        self.recipient_addr.setObjectName("recipient_addr")
        self.txt_amount = QtWidgets.QPlainTextEdit(self.main_menu)
        self.txt_amount.setGeometry(QtCore.QRect(100, 150, 371, 31))
        self.txt_amount.setObjectName("txt_amount")
        self.label_5 = QtWidgets.QLabel(self.main_menu)
        self.label_5.setGeometry(QtCore.QRect(20, 110, 71, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.main_menu)
        self.label_6.setGeometry(QtCore.QRect(20, 160, 41, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.txt_your_account = QtWidgets.QLabel(self.main_menu)
        self.txt_your_account.setGeometry(QtCore.QRect(150, 10, 47, 13))
        self.txt_your_account.setObjectName("txt_your_account")
        self.txt_your_money = QtWidgets.QLabel(self.main_menu)
        self.txt_your_money.setGeometry(QtCore.QRect(150, 40, 47, 13))
        self.txt_your_money.setObjectName("txt_your_money")
        self.txt_logs = QtWidgets.QTextBrowser(self.main_menu)
        self.txt_logs.setGeometry(QtCore.QRect(100, 241, 371, 151))
        self.txt_logs.setObjectName("txt_logs")
        self.send_money = QtWidgets.QPushButton(self.main_menu)
        self.send_money.setGeometry(QtCore.QRect(100, 200, 371, 23))
        self.send_money.setObjectName("send_money")
        MainWindow.setCentralWidget(self.main_menu)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 500, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Ваш профиль "))
        self.label_2.setText(_translate("MainWindow", "Ваш баланс"))
        self.label_3.setText(_translate("MainWindow", "Отправка"))
        self.label_5.setText(_translate("MainWindow", "Получатель"))
        self.label_6.setText(_translate("MainWindow", "Сумма"))
        self.txt_your_account.setText(_translate("MainWindow", "TextLabel"))
        self.txt_your_money.setText(_translate("MainWindow", "TextLabel"))
        self.send_money.setText(_translate("MainWindow", "Отправить"))
