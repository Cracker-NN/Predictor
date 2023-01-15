# _*_ utf-8 _*_
# @uthor : Aman Raj
# Filename : local (panel.py)
# File Modified : 09/01/2023
#!/usr/bin/env python3

from PyQt6 import QtCore, QtGui, QtWidgets
import os
import requests
import sys
from gui.panel import Panel
from gui.crawler import Crawler

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1023, 700)
        MainWindow.setStyleSheet("background-color: rgb(255, 255, 255);")
        MainWindow.setWindowTitle("Launcher Panel")
        MainWindow.setWindowIcon(QtGui.QIcon(os.path.join("assets", "launcher.ico")))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.main_frame = QtWidgets.QFrame(self.centralwidget)
        self.main_frame.setGeometry(QtCore.QRect(-30, -141, 1421, 681))
        self.main_frame.setStyleSheet("background-color: rgb(4, 122, 237);\n"
                                      "font-family: Segoe, Tahoma, Geneva, Verdana, sans-serif;\n"
                                      "color: rgb(255, 255, 255);\n"
                                      "line-height: 1.6;")
        self.main_frame.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.main_frame.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.main_frame.setObjectName("main_frame")
        self.logo = QtWidgets.QLabel(self.main_frame)
        self.logo.setGeometry(QtCore.QRect(60, 160, 281, 71))
        self.logo.setStyleSheet("font-weight: 300;\n"
                                "line-height: 1.2;\n"
                                "margin: 10px 0;\n"
                                "color: rgb(255, 255, 255);\n"
                                "font-size: 35pt;\n"
                                "font-family: Segoe UI, Tahoma, Geneva, Verdana, sans-serif;")
        self.logo.setObjectName("logo")
        self.home_logo = QtWidgets.QLabel(self.main_frame)
        self.home_logo.setGeometry(QtCore.QRect(70, 350, 121, 61))
        self.home_logo.setStyleSheet("font-size: 40px;\n"
                                     "color: rgb(255, 255, 255);\n"
                                     "font-weight: 300;\n"
                                     "line-height: 1.2;\n"
                                     "margin: 10px 0;\n"
                                     "font-family: Segoe UI, Tahoma, Geneva, Verdana, sans-serif;")
        self.home_logo.setObjectName("home_logo")
        self.info = QtWidgets.QLabel(self.main_frame)
        self.info.setGeometry(QtCore.QRect(70, 440, 411, 111))
        self.info.setStyleSheet("margin: 20px 0;\n"
                                "font-size: 12pt;")
        self.info.setObjectName("info")
        self.documentation_button = QtWidgets.QPushButton(self.main_frame)
        self.documentation_button.setGeometry(QtCore.QRect(100, 580, 191, 51))
        self.documentation_button.setCursor(
            QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.documentation_button.setStyleSheet("QPushButton{\n"
                                                "     padding: 10px 30px;\n"
                                                "    background-color: transparent;\n"
                                                "    border: 1px solid #fff;\n"
                                                "    display: inline-block;\n"
                                                "    background: #047aed;\n"
                                                "    color: #fff;\n"
                                                "    border-radius: 5px;\n"
                                                "    font-size: 13pt;\n"
                                                "    font-weight: 500;\n"
                                                "    cursor: pointer;\n"
                                                "}\n"
                                                "QPushButton:hover{\n"
                                                "    background-color: #fff;\n"
                                                "    color: #000;\n"
                                                "}")
        self.documentation_button.setObjectName("documentation_button")
        self.card_widget = QtWidgets.QWidget(self.main_frame)
        self.card_widget.setGeometry(QtCore.QRect(700, 290, 271, 291))
        self.card_widget.setStyleSheet("background-color: rgb(255, 255, 255);\n"
                                       "color: #333;\n"
                                       "border-radius: 10px;\n"
                                       "box-shadow: 0 3px 10px rgb(0 0 0 / 20%);\n"
                                       "padding: 20px;\n"
                                       "margin: 10px;\n"
                                       "position: relative;\n"
                                       "top: 60px;\n"
                                       "height: 350px;\n"
                                       "width: 400px;\n"
                                       "padding: 40px;\n"
                                       "z-index: 100;")
        self.card_widget.setObjectName("card_widget")
        self.suggetion_logo = QtWidgets.QLabel(self.card_widget)
        self.suggetion_logo.setGeometry(QtCore.QRect(-30, 20, 251, 51))
        self.suggetion_logo.setStyleSheet("background-color:none;\n"
                                          "font-weight: 300;\n"
                                          "line-height: 1.2;\n"
                                          "margin: 10px 0;\n"
                                          "font-size: 20pt;")
        self.suggetion_logo.setObjectName("suggetion_logo")
        self.suggetion_info = QtWidgets.QLabel(self.card_widget)
        self.suggetion_info.setGeometry(QtCore.QRect(-20, 40, 311, 241))
        self.suggetion_info.setStyleSheet("font-size: 10pt;\n"
                                          "color: grey;\n"
                                          "background-color:none;")
        self.suggetion_info.setObjectName("suggetion_info")
        self.break_widget = QtWidgets.QWidget(self.centralwidget)
        self.break_widget.setGeometry(QtCore.QRect(-70, 540, 1151, 80))
        self.break_widget.setStyleSheet("QWidget{\n"
                                        "    content: \' \';;\n"
                                        "    position: absolute;\n"
                                        "    height: 100px;\n"
                                        "    bottom: -70px;\n"
                                        "    right: 0;\n"
                                        "    left: 0;\n"
                                        "    background: #9acd32;\n"
                                        "    transform: skewY(-1deg);\n"
                                        "}")
        self.break_widget.setObjectName("break_widget")
        self.bottom_frame = QtWidgets.QLabel(self.centralwidget)
        self.bottom_frame.setGeometry(QtCore.QRect(-164, 650, 1311, 61))
        self.bottom_frame.setObjectName("bottom_frame")
        self.model_launcher = QtWidgets.QPushButton(self.centralwidget, clicked=lambda: self.download_launcher())
        self.model_launcher.setGeometry(QtCore.QRect(810, 650, 151, 41))
        self.model_launcher.setCursor(QtGui.QCursor(
            QtCore.Qt.CursorShape.PointingHandCursor))
        self.model_launcher.setStyleSheet("QPushButton{\n"
                                          "    border: 2px solid #fea44c;\n"
                                          "    color: #fea44c;\n"
                                          "    box-shadow: inset 0 0 0 0.15em #fea44c, 0 2px 20px #563719;\n"
                                          "    text-shadow: 0 2px 5px #563719;\n"
                                          "    border-radius: 10px;\n"
                                          "    transform-style: preserve-3d;\n"
                                          "    transform-box: 13px;\n"
                                          "    font: 12pt MS Shell Dlg 2;\n"
                                          "    font-weight: 500;\n"
                                          "}\n"
                                          "QPushButton:hover{\n"
                                          "    background-color: #fea44c;\n"
                                          "    color: #fff;\n"
                                          "    box-shadow: inset 0 0 0 0.15em #fea44c, 0 2px 20px #563719;\n"
                                          "}")
        self.model_launcher.setObjectName("model_launcher")
        self.image_launcher = QtWidgets.QPushButton(self.centralwidget, clicked=lambda: self.image_crawler())
        self.image_launcher.setGeometry(QtCore.QRect(600, 650, 161, 41))
        self.image_launcher.setCursor(QtGui.QCursor(
            QtCore.Qt.CursorShape.PointingHandCursor))
        self.image_launcher.setStyleSheet("QPushButton{\n"
                                          "    border: 2px solid cyan;\n"
                                          "    color: cyan;\n"
                                          "    box-shadow: inset 0 0 0 0.15em cyan, 0 2px 20px #563719;\n"
                                          "    text-shadow: 0 2px 5px cyan;\n"
                                          "    border-radius: 10px;\n"
                                          "    transform-style: preserve-3d;\n"
                                          "    transform-box: 13px;\n"
                                          "    font: 12pt MS Shell Dlg 2;\n"
                                          "    font-weight: 500;\n"
                                          "}\n"
                                          "QPushButton:hover{\n"
                                          "    background-color: cyan;\n"
                                          "    color: #fff;\n"
                                          "    box-shadow: inset 0 0 0 0.15em #fea44c, 0 2px 20px #563719;\n"
                                          "}")
        self.image_launcher.setObjectName("image_launcher")
        self.internet_connection = QtWidgets.QLabel(self.centralwidget)
        self.internet_connection.setGeometry(QtCore.QRect(10, 650, 211, 41))
        self.internet_connection.setStyleSheet("color: black;\n"
                                               "background: none;\n"
                                               "border-radius: 10px;\n"
                                               "font: 75 12pt \"MS Shell Dlg 2\";\n"
                                               "borde-bottomr: 2px solid rgb(0, 0, 0);\n"
                                               "")
        self.internet_connection.setObjectName("internet_connection")
        self.on_off = QtWidgets.QLabel(self.centralwidget)
        self.on_off.setGeometry(QtCore.QRect(160, 656, 29, 31))
        self.on_off.setStyleSheet("background-color: rgb(0, 170, 0);\n"
                                  "font: 500 12pt \"MS Shell Dlg 2\";\n"
                                  "border-radius: 10px;")
        self.on_off.setObjectName("on_off")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def download_launcher(self):
        self.window = QtWidgets.QMainWindow()
        self.gui = Panel("Panel", os.path.join("assets", "panel.ico"))
        self.gui.setupUi(self.window)
        self.window.show()

    def image_crawler(self):
        self.crwaler = QtWidgets.QMainWindow()
        self.ui = Crawler(os.path.join("assets", "crawler.ico"))
        self.ui.setupUi(self.crwaler)
        self.crwaler.show()


    def documentation(self):
        print("Documentation Comming Soon....")

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.logo.setText(_translate("MainWindow", "The Predictor"))
        self.home_logo.setText(_translate("MainWindow", "Home"))
        self.info.setText(_translate("MainWindow", "Hello, User, Thank\'s For Downloading Our Software 🎉.\n"
                                     "It is make easy the deep/machine learning task\'s.\n"
                                     "I hope, It will make your Job Easier🙏."))
        self.documentation_button.setText(
            _translate("MainWindow", "Documentation"))
        self.suggetion_logo.setText(_translate("MainWindow", "Suggetions"))
        self.suggetion_info.setText(_translate("MainWindow", "Configure Json File For \n"
                                               "Cutomizing the Download Panel.\n"
                                               "and change download \n"
                                               "auto save path to \n"
                                               "your destination\n"
                                               "`Setting & Configuration`."))
        self.bottom_frame.setText(_translate("MainWindow", "TextLabel"))
        self.model_launcher.setText(_translate("MainWindow", "Model Launcher"))
        self.image_launcher.setText(_translate("MainWindow", "Image Launcher"))
        self.internet_connection.setText(
            _translate("MainWindow", "Internet Connection"))
        try:
            r = requests.get("https://google.com")
            if r.status_code == 200:
                self.on_off.setStyleSheet("background-color: rgb(0, 170, 0);\n"
                                  "font: 500 12pt \"MS Shell Dlg 2\";\n"
                                  "border-radius: 10px;")
                self.on_off.setText(_translate("MainWindow", "✔️"))
            else:
                self.on_off.setStyleSheet("background-color: rgb(170, 0, 0);\n"
                                  "font: 500 12pt \"MS Shell Dlg 2\";\n"
                                  "border-radius: 10px;")
                self.on_off.setText(_translate("MainWindow", "❌"))
        except:
            self.on_off.setStyleSheet("background-color: rgb(170, 0, 0);\n"
                                  "font: 500 12pt \"MS Shell Dlg 2\";\n"
                                  "border-radius: 10px;")
            self.on_off.setText(_translate("MainWindow", ""))
        # self.on_off.setText(_translate("MainWindow", "ON"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())
