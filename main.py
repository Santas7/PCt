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
        self.setFixedSize(QSize(380, 500)) # size window
        self.title = QLabel("PCt", self)
        self.setStyleSheet("background-color : black")
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
        self.title.move(160, 50)
        self.title.setStyleSheet("color: white")

        # panel input user name
        self.input_user = QLineEdit('', self)
        self.input_user.move(10, 110)
        self.input_user.setFixedSize(QSize(360, 40))
        self.input_user.setFont(font)
        self.input_user.setStyleSheet("color: white")

        # panel input ip
        self.input_ip = QLineEdit('', self)
        self.input_ip.move(10, 160)
        self.input_ip.setFixedSize(QSize(360, 40))
        self.input_ip.setFont(font)
        self.input_ip.setStyleSheet("color: white")

        # panel input password connect
        self.input_pass = QLineEdit('', self)
        self.input_pass.move(10, 210)
        self.input_pass.setFixedSize(QSize(360, 40))
        self.input_pass.setFont(font)
        self.input_pass.setStyleSheet("color: white")

        # buttons
        self.start = QPushButton("CONNECT TO", self)
        self.start.setFixedSize(QSize(150, 50))
        self.start.move(10, 260)
        self.start.setFont(font)
        self.start.setStyleSheet("background-color : #ff5757; color: white")

        self.end = QPushButton("EXIT..", self)
        self.end.setFixedSize(QSize(150, 50))
        self.end.move(170, 260)
        self.end.setFont(font)
        self.end.setStyleSheet("background-color : #ff5757; color: white")

        self.show()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    app.exec()
