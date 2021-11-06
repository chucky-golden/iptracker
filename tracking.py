import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtGui import QIcon
from tracker.phonetrack import PhoneTrack
from tracker.iptrack import App

class Track(QWidget):

    def __init__(self):
        super().__init__()
        self.title = "SIMPLE TRACKING APP"
        self.left = 450
        self.top = 100
        self.width = 350
        self.height = 400
        self.w = None
        self.initUI()

    def initUI(self):
        self.setWindowIcon(QIcon("imgg.JPG"))
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)

        layout = QGridLayout()
        self.setStyleSheet("background-color: #660000; color: white;")

        button1 = QPushButton('GET PHONE NUMBER DETAILS', self)
        button1.setStyleSheet('QPushButton {background-color: #cc0000; color: white; padding: 10px;}')
        button1.move(100, 50)
        button1.clicked.connect(self.get_phone)
        layout.addWidget(button1)

        button3 = QPushButton('GET LOCATION WITH IP', self)
        button3.setStyleSheet('QPushButton {background-color: #cc0000; color: white; padding: 10px;}')
        button3.move(100, 50)
        button3.clicked.connect(self.get_ip)
        layout.addWidget(button3)

        self.setLayout(layout)
        self.show()

    @pyqtSlot()
    def get_phone(self):
        if self.w is None:
            self.w = PhoneTrack()
            self.w.show()
        else:
            # close the window is the button is clicked on again
            self.w.close()
            self.w = None


    def get_ip(self):
        if self.w is None:
            self.w = App()
            self.w.show()
        else:
            # close the window is the button is clicked on again
            self.w.close()
            self.w = None





if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Track()
    sys.exit(app.exec_())