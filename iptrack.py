import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import pyqtSlot
from PyQt5 import QtGui
import phonenumbers
from phonenumbers import geocoder
import folium
import geocoder
import webbrowser


class App(QWidget):

    def __init__(self):
        super().__init__()
        self.setWindowTitle("IP Tracker")
        self.setGeometry(550, 200, 360, 430)
        self.setWindowIcon(QIcon("imgg.JPG"))
        self.setStyleSheet("background-color: #660000; color: white;")
        self.UiComponents()

        self.show()

    def UiComponents(self):
        self.phone = QLineEdit(self)
        self.phone.setGeometry(30, 10, 300, 40)
        self.phone.setStyleSheet("QLineEdit"
                                 "{"
                                 "background : white;"
                                 "color: #802000;"
                                 "font-weight: bold;"
                                 "}")
        self.phone.setPlaceholderText('enter valid phone number')

        self.ipa = QLineEdit(self)
        self.ipa.setGeometry(30, 90, 300, 40)
        self.ipa.setStyleSheet("QLineEdit"
                                 "{"
                                 "background : white;"
                                 "color: #802000;"
                                 "font-weight: bold;"
                                 "}")
        self.ipa.setPlaceholderText('enter IP Address')

        push1 = QPushButton("check Location", self)
        push1.setStyleSheet('QPushButton {color: white;'
                            ' font-size: 15px; '
                            'font-weight: bold;'
                            'background-color: #cc0000;}')
        push1.setGeometry(80, 200, 200, 40)
        push1.clicked.connect(self.get_details)

        self.labelResult = QLabel(self)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(25)
        self.labelResult.setFont(font)
        self.labelResult.setText("")
        self.labelResult.setGeometry(10, 250, 300, 90)

    @pyqtSlot()
    def get_details(self):
        self.phone = self.phone.text()
        self.ipa = self.ipa.text()
        try:
            self.ch_number = phonenumbers.parse(self.phone)
            self.yourLocation = phonenumbers.geocoder.description_for_number(self.ch_number, "en")

            self.g = geocoder.ip(self.ipa)

            self.myaddress = self.g.latlng

            self.mymap1 = folium.Map(location=self.myaddress, zoom_start=9)

            folium.CircleMarker(location=self.myaddress, radius=50, popup=self.yourLocation)\
                .add_to(self.mymap1)
            folium.Marker(self.myaddress, popup=self.yourLocation).add_to(self.mymap1)

            self.mymap1.save("mylocation.html")

            self.labelResult.setText("Processing......")

            webbrowser.open("mylocation.html")
        except:
            self.labelResult.setText("Please enter a valid IP Address \n"
                                     "eg. (192.168.42.34)")


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())
