# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'sign_in_up.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setEnabled(True)
        MainWindow.resize(466, 440)
        self.sign_in_up = QtWidgets.QWidget(MainWindow)
        self.sign_in_up.setObjectName("sign_in_up")
        self.create_new_accaunt = QtWidgets.QPushButton(self.sign_in_up)
        self.create_new_accaunt.setGeometry(QtCore.QRect(150, 300, 151, 23))
        self.create_new_accaunt.setObjectName("create_new_accaunt")
        self.label = QtWidgets.QLabel(self.sign_in_up)
        self.label.setGeometry(QtCore.QRect(150, 260, 161, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(20)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.sign_in_up)
        self.label_2.setGeometry(QtCore.QRect(140, 40, 161, 71))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(20)
        self.label_2.setFont(font)
        self.label_2.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.sign_in_up)
        self.label_3.setGeometry(QtCore.QRect(130, 100, 201, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.choose_file = QtWidgets.QPushButton(self.sign_in_up)
        self.choose_file.setGeometry(QtCore.QRect(130, 150, 191, 23))
        self.choose_file.setObjectName("choose_file")
        self.autorize = QtWidgets.QPushButton(self.sign_in_up)
        self.autorize.setGeometry(QtCore.QRect(130, 190, 191, 23))
        self.autorize.setObjectName("autorize")
        MainWindow.setCentralWidget(self.sign_in_up)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 466, 21))
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
        self.create_new_accaunt.setText(_translate("MainWindow", "Создать аккаунт"))
        self.label.setText(_translate("MainWindow", "Регистрация"))
        self.label_2.setText(_translate("MainWindow", "Авторизация"))
        self.label_3.setText(_translate("MainWindow", "Укажите путь к ключевому файлу"))
        self.choose_file.setText(_translate("MainWindow", "Выбрать файл"))
        self.autorize.setText(_translate("MainWindow", "Вход"))
