from gui import mainwindow
from PyQt5 import QtWidgets


class MainWindow(QtWidgets.QMainWindow, mainwindow.Ui_MainWindow):
    """
    Main UI class
    """

    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        mainwindow.Ui_MainWindow.__init__(self)
        self.setupUi(self)
