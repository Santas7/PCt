from PyQt6.QtCore import QSize
from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton, QLabel, QFileDialog, QGridLayout, QLineEdit, \
    QVBoxLayout, QTextEdit, QProgressBar
from PyQt6 import QtGui, QtWidgets, QtCore
import sys


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        # settings window MainWindow
        self.setWindowTitle("PCt")
        self.setFixedSize(QSize(800, 600)) # size window
        self.title = QLabel("PCt", self)

        # standart text
        font = QtGui.QFont()
        font.setFamily('CeraPro-Bold')  # font
        font.setPointSize(14)  # size of font

        # title text
        font_ = QtGui.QFont()
        font_.setFamily('CeraPro-Bold')  # font
        font_.setPointSize(27)  # size of font

        # change icon window
        app_icon = QtGui.QIcon()
        app_icon.addFile('icon/PCt.png', QtCore.QSize(256, 256))
        app.setWindowIcon(app_icon)

        # change for title
        self.title.setFont(font_)
        self.title.move(380, 50)

        # panel input user name
        self.input_user = QLineEdit('', self)
        self.input_user.move(200, 110)
        self.input_user.setFixedSize(QSize(400, 40))
        self.input_user.setFont(font)

        # panel input ip
        self.input_user = QLineEdit('', self)
        self.input_user.move(200, 160)
        self.input_user.setFixedSize(QSize(400, 40))
        self.input_user.setFont(font)

        # panel input password connect
        self.input_user = QLineEdit('', self)
        self.input_user.move(200, 210)
        self.input_user.setFixedSize(QSize(400, 40))
        self.input_user.setFont(font)
        
        self.show()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    app.exec()
