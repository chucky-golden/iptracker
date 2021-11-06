import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import pyqtSlot
from PyQt5 import QtGui
import phonenumbers
from phonenumbers import geocoder
from phonenumbers import carrier


class PhoneTrack(QWidget):

    def __init__(self):
        super().__init__()
        self.setWindowTitle("PHONE DETAILS")
        self.setGeometry(550, 200, 360, 400)
        self.setWindowIcon(QIcon("imgg.JPG"))
        self.setStyleSheet("background-color: #660000; color: white;")
        self.UiComponents()

        self.show()

    def UiComponents(self):
        self.phone = QLineEdit(self)
        self.phone.setGeometry(30, 10, 300, 50)
        self.phone.setStyleSheet("QLineEdit"
                                 "{"
                                 "background : white;"
                                 "color: #802000;"
                                 "font-weight: bold;"
                                 "}")
        self.phone.setPlaceholderText('enter phone number')

        push1 = QPushButton("check number", self)
        push1.setStyleSheet('QPushButton {color: white;'
                            ' font-size: 15px; '
                            'font-weight: bold;'
                            'background-color: #cc0000;}')
        push1.setGeometry(80, 100, 200, 40)
        push1.clicked.connect(self.get_details)

        self.labelResult = QLabel(self)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(25)
        self.labelResult.setFont(font)
        self.labelResult.setText("")
        self.labelResult.setGeometry(10, 250, 300, 60)

    @pyqtSlot()
    def get_details(self):
        self.phone = self.phone.text()
        try:
            self.ch_number = phonenumbers.parse(self.phone)
            self.yourLocation = phonenumbers.geocoder.description_for_number(self.ch_number, "en")

            self.service_number = phonenumbers.parse(self.phone)
            self.service_provider = carrier.name_for_number(self.service_number, "en")

            self.labelResult.setText("Location: " + self.yourLocation + "\n\n"
                                                                   "" + "Carrier: " + self.service_provider)
        except:
            self.labelResult.setText("Please enter a valid phone number \n"
                                     "eg. (+23492215432)")


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = PhoneTrack()
    sys.exit(app.exec_())
