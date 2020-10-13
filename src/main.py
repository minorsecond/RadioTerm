import sys
from src import mainwindow

if __name__ == '__main__':
    app = mainwindow.QtWidgets.QApplication(sys.argv)
    window = mainwindow.MainWindow()
    window.show()
    sys.exit(app.exec_())
