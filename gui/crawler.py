# _*_ utf-8 _*_
# @uthor : Aman Raj
# Filename : local (panel.py)
# File Modified : 09/01/2023


import requests
from urllib.request import urlretrieve
from bs4 import BeautifulSoup
import time
import math
import os
from PyQt6 import QtCore, QtGui, QtWidgets


class Crawler(object):
    def __init__(self, icon) -> None:
        self.ICON = icon

    def setupUi(self, MainWindow):
        MainWindow.setWindowTitle("Image Crawler")
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 632)
        MainWindow.setStyleSheet("background-color: rgb(45, 45, 68);")
        MainWindow.setWindowIcon(QtGui.QIcon(self.ICON))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(30, 20, 721, 211))
        self.widget.setStyleSheet("border-radius: 20px;\n"
                                  "                              background-color: rgb(45, 45, 0);\n"
                                  "                              color: #fff;")
        self.widget.setObjectName("widget")
        self.url_input = QtWidgets.QLineEdit(self.widget)
        self.url_input.setGeometry(QtCore.QRect(240, 10, 461, 31))
        self.url_input.setStyleSheet("QLineEdit{border-radius: 10px;\n"
                                     "                                   border: 1px solid black;\n"
                                     "                                   background-color: rgb(255, 255, 255);\n"
                                     "                                   border-color: rgb(0, 170, 255);\n"
                                     "                                   font: 10pt \"MS Shell Dlg 2\";\n"
                                     "                                   color: black;}\n"
                                     "                                   QLineEdit:hover{\n"
                                     "                                   background-color: rgb(170, 255, 255);}")
        self.url_input.setObjectName("url_input")
        self.directory_input = QtWidgets.QLineEdit(self.widget)
        self.directory_input.setGeometry(QtCore.QRect(240, 50, 461, 31))
        self.directory_input.setStyleSheet("QLineEdit{border-radius: 10px;\n"
                                           "                                   border: 1px solid black;\n"
                                           "                                   background-color: rgb(255, 255, 255);\n"
                                           "                                   border-color: rgb(0, 170, 255);\n"
                                           "                                   font: 10pt \"MS Shell Dlg 2\";\n"
                                           "                                   color: black;}\n"
                                           "                                   QLineEdit:hover{\n"
                                           "                                   background-color: rgb(170, 255, 255);}")
        self.directory_input.setObjectName("directory_input")
        self.number_input = QtWidgets.QLineEdit(self.widget)
        self.number_input.setGeometry(QtCore.QRect(240, 100, 101, 31))
        self.number_input.setStyleSheet("QLineEdit{border-radius: 10px;\n"
                                        "                                   border: 1px solid black;\n"
                                        "                                   background-color: rgb(255, 255, 255);\n"
                                        "                                   border-color: rgb(0, 170, 255);\n"
                                        "                                   font: 10pt \"MS Shell Dlg 2\";\n"
                                        "                                   color: black;}\n"
                                        "                                   QLineEdit:hover{\n"
                                        "                                   background-color: rgb(170, 255, 255);}")
        self.number_input.setObjectName("number_input")
        self.name_input = QtWidgets.QLineEdit(self.widget)
        self.name_input.setGeometry(QtCore.QRect(590, 100, 101, 31))
        self.name_input.setStyleSheet("QLineEdit{border-radius: 10px;\n"
                                      "                                   border: 1px solid black;\n"
                                      "                                   background-color: rgb(255, 255, 255);\n"
                                      "                                   border-color: rgb(0, 170, 255);\n"
                                      "                                   font: 10pt \"MS Shell Dlg 2\";\n"
                                      "                                   color: black;}\n"
                                      "                                   QLineEdit:hover{\n"
                                      "                                   background-color: rgb(170, 255, 255);}")
        self.name_input.setObjectName("name_input")
        self.format_entry = QtWidgets.QComboBox(self.widget)
        self.format_entry.setGeometry(QtCore.QRect(240, 150, 111, 41))
        self.format_entry.setStyleSheet("QComboBox{\n"
                                        "                                   border-radius: 10px;\n"
                                        "                                   border: 1px solid black;\n"
                                        "                                   background-color: rgb(255, 255, 255);\n"
                                        "                                   border-color: rgb(0, 170, 255);\n"
                                        "                                   font: 10pt \"MS Shell Dlg 2\";\n"
                                        "                                   color: black\n"
                                        "                                   }\n"
                                        "                                   QLineEdit:hover{\n"
                                        "                                   background-color: rgb(170, 255, 255);}")
        self.format_entry.setObjectName("format_entry")
        self.format_entry.addItem("")
        self.format_entry.addItem("")
        self.format_entry.addItem("")
        self.format_entry.addItem("")
        self.url = QtWidgets.QLabel(self.widget)
        self.url.setGeometry(QtCore.QRect(160, 10, 51, 31))
        self.url.setStyleSheet("font: 15pt \"MS Shell Dlg 2\";\n"
                               "                                   color: #fff;\n"
                               "                                   padding-left: 5px;")
        self.url.setObjectName("url")
        self.directory = QtWidgets.QLabel(self.widget)
        self.directory.setGeometry(QtCore.QRect(130, 50, 101, 31))
        self.directory.setStyleSheet("font: 15pt \"MS Shell Dlg 2\";\n"
                                     "                                   color: #fff;\n"
                                     "                                   padding-left: 5px;")
        self.directory.setObjectName("directory")
        self.number = QtWidgets.QLabel(self.widget)
        self.number.setGeometry(QtCore.QRect(120, 100, 91, 31))
        self.number.setStyleSheet("font: 15pt \"MS Shell Dlg 2\";\n"
                                  "                                   color: #fff;\n"
                                  "                                   padding-left: 5px;")
        self.number.setObjectName("number")
        self.name = QtWidgets.QLabel(self.widget)
        self.name.setGeometry(QtCore.QRect(500, 100, 71, 31))
        self.name.setStyleSheet("font: 15pt \"MS Shell Dlg 2\";\n"
                                "                                   color: #fff;\n"
                                "                                   padding-left: 5px;")
        self.name.setObjectName("name")
        self.format = QtWidgets.QLabel(self.widget)
        self.format.setGeometry(QtCore.QRect(130, 150, 91, 31))
        self.format.setStyleSheet("font: 15pt \"MS Shell Dlg 2\";\n"
                                  "                                   color: #fff;\n"
                                  "                                   padding-left: 5px;")
        self.format.setObjectName("format")
        self.pushButton = QtWidgets.QPushButton(self.widget)
        self.pushButton.setGeometry(QtCore.QRect(550, 150, 151, 50))  # 41
        self.pushButton.setCursor(QtGui.QCursor(
            QtCore.Qt.CursorShape.PointingHandCursor))
        self.pushButton.setStyleSheet("QPushButton{\n"
                                      "                                   padding: 10px 30px;\n"
                                      "                                   background-color: transparent;\n"
                                      "                                   border: 1px solid #fff;\n"
                                      "                                   display: inline-block;\n"
                                      "                                   background: none;\n"
                                      "                                   color: #fff;\n"
                                      "                                   border-radius: 5px;\n"
                                      "                                   font-size: 13pt;\n"
                                      "                                   font-weight: 500;\n"
                                      "                                   transition: 2ms ease-in;\n"
                                      "                                   cursor: pointer;\n"
                                      "                                   }\n"
                                      "                                   QPushButton:hover{\n"
                                      "                                   background-color: #fff;\n"
                                      "                                   color: #000;\n"
                                      "                                   }")
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.trigger)
        self.terminal = QtWidgets.QScrollArea(self.centralwidget)
        self.terminal.setGeometry(QtCore.QRect(30, 260, 731, 341))
        self.terminal.setStyleSheet("background-color: rgb(45, 0, 0);\n"
                                    "                              border-radius: 5px;\n"
                                    "                              color: rgb(0, 255, 0);")
        self.terminal.setWidgetResizable(True)
        self.terminal.setObjectName("terminal")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 731, 341))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.verticalScrollBar = QtWidgets.QScrollBar(
            self.scrollAreaWidgetContents)
        self.verticalScrollBar.setGeometry(QtCore.QRect(720, 0, 11, 361))
        self.verticalScrollBar.setStyleSheet("QScrollBar:vertical {\n"
                                             "                                        border: none;\n"
                                             "                                        background: rgb(45, 45, 68);\n"
                                             "                                        width: 14px;\n"
                                             "                                        margin: 15px 0 15px 0;\n"
                                             "                                        border-radius: 0px;\n"
                                             "                                        }\n"
                                             "\n"
                                             "                                        /* HANDLE BAR VERTICAL */\n"
                                             "                                        QScrollBar::handle:vertical {\n"
                                             "                                        background-color: rgb(80, 80, 122);\n"
                                             "                                        min-height: 30px;\n"
                                             "                                        border-radius: 7px;\n"
                                             "                                        }\n"
                                             "                                        QScrollBar::handle:vertical:hover{\n"
                                             "                                        background-color: rgb(255, 0, 127);\n"
                                             "                                        }\n"
                                             "                                        QScrollBar::handle:vertical:pressed {\n"
                                             "                                        background-color: rgb(185, 0, 92);\n"
                                             "                                        }\n"
                                             "\n"
                                             "                                        /* BTN TOP - SCROLLBAR */\n"
                                             "                                        QScrollBar::sub-line:vertical {\n"
                                             "                                        border: none;\n"
                                             "                                        background-color: rgb(59, 59, 90);\n"
                                             "                                        height: 15px;\n"
                                             "                                        border-top-left-radius: 7px;\n"
                                             "                                        border-top-right-radius: 7px;\n"
                                             "                                        subcontrol-position: top;\n"
                                             "                                        subcontrol-origin: margin;\n"
                                             "                                        }\n"
                                             "                                        QScrollBar::sub-line:vertical:hover {\n"
                                             "                                        background-color: rgb(255, 0, 127);\n"
                                             "                                        }\n"
                                             "                                        QScrollBar::sub-line:vertical:pressed {\n"
                                             "                                        background-color: rgb(185, 0, 92);\n"
                                             "                                        }\n"
                                             "                                        /* RESET ARROW */\n"
                                             "                                        QScrollBar::up-arrow:vertical,\n"
                                             "                                        QScrollBar::down-arrow:vertical {\n"
                                             "                                        background: none;\n"
                                             "                                        }\n"
                                             "                                        QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical\n"
                                             "                                        {\n"
                                             "                                        background: none;\n"
                                             "                                        }\n"
                                             "\n"
                                             "                                        QScrollBar:vertical {\n"
                                             "                                        border: none;\n"
                                             "                                        background: rgb(56, 56, 85);}\n"
                                             "                                   ")
        self.verticalScrollBar.setOrientation(QtCore.Qt.Orientation.Vertical)
        self.verticalScrollBar.setObjectName("verticalScrollBar")
        self.label = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label.setGeometry(QtCore.QRect(10, 10, 691, 16))
        self.label.setObjectName("label")
        self.terminal.setWidget(self.scrollAreaWidgetContents)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.format_entry.setItemText(0, _translate("MainWindow", "jpeg"))
        self.format_entry.setItemText(1, _translate("MainWindow", "png"))
        self.format_entry.setItemText(2, _translate("MainWindow", "bmp"))
        self.format_entry.setItemText(3, _translate("MainWindow", "jpg"))
        self.url.setText(_translate("MainWindow", "Url"))
        self.directory.setText(_translate("MainWindow", "Directory"))
        self.number.setText(_translate("MainWindow", "Number"))
        self.name.setText(_translate("MainWindow", "Name"))
        self.format.setText(_translate("MainWindow", "Format"))
        self.pushButton.setText(_translate("MainWindow", "Crawling"))
        self.label.setText(_translate("MainWindow", ""))

    def trigger(self):
        try:
            self.URL = self.url_input.text()
            self.DIRECTORY = self.directory_input.text()
            self.NUMBER = int(self.number_input.text())
            self.NAME = str(self.name_input.text())
            self.FORMAT = self.format_entry.currentText()
            URL = str(self.URL)
            USER_AGENT = {
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.83 Safari/537.36',
                'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
                'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
                'Accept-Encoding': 'none',
                'Accept-Language': 'en-US,en;q=0.8',
                'Connection': 'keep-alive',
            }
            IMG_NUMBER = int(self.NUMBER)

            if os.path.isdir(self.DIRECTORY):
                SAVE_DIR = self.DIRECTORY
            else:
                os.mkdir(self.DIRECTORY)
                SAVE_DIR = self.DIRECTORY

            FORMAT = self.FORMAT
            PREFIX = self.NAME

            response = requests.get(URL, headers=USER_AGENT)
            soup = BeautifulSoup(response.text, 'html.parser')
            count = 0
            links = []
            for i in soup.findAll('img', {'class': 'rg_i Q4LuWd'}):
                try:
                    key = i['data-src']
                    links.append(key)
                    count += 1
                    if count >= IMG_NUMBER:
                        break
                except KeyError:
                    continue

            starting_time = int(time.strftime("%S"))
            self.label.setText("Downloading is Started...")
            img_count = 0
            for img in links:
                img_count += 1
                urlretrieve(img, os.path.join(
                    f"{SAVE_DIR}", f"{PREFIX}({img_count}).{FORMAT}"))

            self.label.setText("Images is Downloaded")
            final_time = int(int(time.strftime('%S'))-starting_time)
            self.label.setText(f"Total Time Taken : {math.gcd(final_time)}s")

        except Exception:
            pass
