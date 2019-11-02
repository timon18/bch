import sys

from PyQt5 import QtWidgets
from GUI import main_menu

class AppMenu(QtWidgets.QMainWindow, main_menu.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

def main():
    app = QtWidgets.QApplication(sys.argv)
    window = AppMenu()
    window.show()
    app.exec_()


main()