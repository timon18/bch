import sys

from PyQt5 import QtWidgets
from GUI import sign_in_up

class AppLogin(QtWidgets.QMainWindow, sign_in_up.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

def main():
    app = QtWidgets.QApplication(sys.argv)
    window = AppLogin()
    window.show()
    app.exec_()


main()