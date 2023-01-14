#!/usr/bin/env python3
# _*_ utf-8 _*_
# @uthor : Aman Raj
# Filename : local (panel.py)
# File Modified : 09/01/2023



import os
import time
import joblib
from PyQt6 import QtCore, QtGui, QtWidgets
import local
import cv2
import sys
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'
import keras.utils

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setWindowTitle("Predictor Panel")
        MainWindow.setWindowIcon(QtGui.QIcon(os.path.join("assets", "panel.ico")))
        MainWindow.setObjectName("MainWindow")
        MainWindow.setWindowModality(QtCore.Qt.WindowModality.ApplicationModal)
        MainWindow.resize(800, 600)
        MainWindow.setStyleSheet("color: rgb(255, 255, 255);\n"
                                 "                border-color: rgb(0, 170, 255);\n"
                                 "                font: 75 italic 14pt \"Consolas\";\n"
                                 "                alternate-background-color: rgb(26, 26, 26);\n"
                                 "                background-color: rgb(26, 26, 26)")

        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.logo = QtWidgets.QLabel(self.centralwidget)
        self.logo.setGeometry(QtCore.QRect(10, 10, 281, 61))
        self.logo.setCursor(QtGui.QCursor(
            QtCore.Qt.CursorShape.PointingHandCursor))
        self.logo.setStatusTip("")
        self.logo.setStyleSheet("font: 75 24pt \"MS Shell Dlg 2\";\n"
                                "                        font: 36pt \"Edwardian Script ITC\";\n"
                                "                        font-weight: 500;\n"
                                "                        border-radius:15px;\n"
                                "                        background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0, stop:0\n"
                                "                        rgba(0, 0, 0, 255), stop:0.05 rgba(14, 8, 73, 255), stop:0.36 rgba(28, 17,\n"
                                "                        145, 255), stop:0.6 rgba(126, 14, 81, 255), stop:0.75 rgba(234, 11, 11,\n"
                                "                        255), stop:0.79 rgba(244, 70, 5, 255), stop:0.86 rgba(255, 136, 0, 255),\n"
                                "                        stop:0.935 rgba(239, 236, 55, 255));")
        self.logo.setObjectName("logo")
        self.clock = QtWidgets.QLabel(self.centralwidget)
        self.clock.setGeometry(QtCore.QRect(630, 10, 55, 40))
        self.clock.setStatusTip("")
        self.clock.setStyleSheet("border-radius:12px;\n"
                                 "                        font: 75 bolder 18pt \"MS Sans Serif\";\n"
                                 "                        background-color: rgb(85, 85, 255);\n"
                                 "margin: 8px;\n")
        self.clock.setObjectName("clock")
        self.list_of_classes = QtWidgets.QListWidget(self.centralwidget)
        self.list_of_classes.setGeometry(QtCore.QRect(10, 140, 201, 451))
        self.list_of_classes.setStatusTip("")
        self.list_of_classes.setStyleSheet("border-radius: 10px;\n"
                                           "                        background-color: rgb(0, 0, 0);\n"
                                           "                        color: rgb(255, 255, 255);\n"
                                           "                        font: 75 8pt \"MS Shell Dlg 2\";\n"
                                           "                        font: 75 12pt \"MS Shell Dlg 2\";\n"
                                           "                        /*background-color: rgb(85, 170, 255);*/\n"
                                           "                        font: 18pt \"Jokerman\";")
        self.list_of_classes.setObjectName("list_of_classes")
        item = QtWidgets.QListWidgetItem()
        icon = QtGui.QIcon.fromTheme("grey")
        item.setIcon(icon)
        self.list_of_classes.addItem(item)
        self.prediction_result_window = QtWidgets.QLabel(self.centralwidget)
        self.prediction_result_window.setGeometry(
            QtCore.QRect(250, 380, 411, 51))
        self.prediction_result_window.setStatusTip("")
        self.prediction_result_window.setStyleSheet("border-radius: 10px;\n"
                                                    "                        border: 5px solid black;\n"
                                                    "                        font: 14pt \"Lucida Handwriting\";\n"
                                                    "                        background-color: rgb(62, 166, 255);\n"
                                                    "                        color: rgb(0, 0, 0)")
        self.prediction_result_window.setObjectName("prediction_result_window")
        self.verticalScrollBar = QtWidgets.QScrollBar(self.centralwidget)
        self.verticalScrollBar.setGeometry(QtCore.QRect(190, 160, 13, 411))
        self.verticalScrollBar.setCursor(QtGui.QCursor(
            QtCore.Qt.CursorShape.PointingHandCursor))
        self.verticalScrollBar.setStatusTip("")
        self.verticalScrollBar.setStyleSheet("border-radius: 10px;\n"
                                             "                        background-color: rgb(255, 255, 255);\n"
                                             "                        color: rgb(0, 0, 0);\n"
                                             "                        selection-background-color: rgb(0, 170, 255);")
        self.verticalScrollBar.setOrientation(QtCore.Qt.Orientation.Vertical)
        self.verticalScrollBar.setObjectName("verticalScrollBar")
        self.model_path_entry = QtWidgets.QLineEdit(self.centralwidget)
        self.model_path_entry.setGeometry(QtCore.QRect(370, 470, 381, 31))
        self.model_path_entry.setStatusTip("")
        self.model_path_entry.setStyleSheet("QLineEdit{border-radius: 10px;\n"
                                            "border: 1px solid black;\n"
                                            "background-color: rgb(255, 255, 255);\n"
                                            "border-color: rgb(0, 170, 255);\n"
                                            "font: 10pt \"MS Shell Dlg 2\";\n"
                                            "color: black;}\n"
                                            "\n"
                                            "QLineEdit:hover{\n"
                                            "    background-color: rgb(170, 255, 255);\n"
                                            "}")
        self.model_path_entry.setObjectName("model_path_entry")
        self.class_path_entry = QtWidgets.QLineEdit(self.centralwidget)
        self.class_path_entry.setGeometry(QtCore.QRect(370, 510, 381, 31))
        self.class_path_entry.setStatusTip("")
        self.class_path_entry.setStyleSheet("QLineEdit{border-radius: 10px;\n"
                                            "border: 1px solid black;\n"
                                            "background-color: rgb(255, 255, 255);\n"
                                            "border-color: rgb(0, 170, 255);\n"
                                            "font: 10pt \"MS Shell Dlg 2\";\n"
                                            "color: black;}\n"
                                            "\n"
                                            "QLineEdit:hover{\n"
                                            "    background-color: rgb(170, 255, 255);\n"
                                            "}")
        self.class_path_entry.setObjectName("class_path_entry")
        self.path_area = QtWidgets.QListView(self.centralwidget)
        self.path_area.setGeometry(QtCore.QRect(240, 450, 521, 141))
        self.path_area.setStatusTip("")
        self.path_area.setObjectName("path_area")
        self.path_input = QtWidgets.QLabel(self.centralwidget)
        self.path_input.setGeometry(QtCore.QRect(450, 440, 101, 21))
        self.path_input.setStatusTip("")
        self.path_input.setObjectName("path_input")
        self.model_path = QtWidgets.QLabel(self.centralwidget)
        self.model_path.setGeometry(QtCore.QRect(250, 470, 101, 31))
        self.model_path.setStatusTip("")
        self.model_path.setStyleSheet("font: 15pt \"MS Shell Dlg 2\";\n"
                                      "                    ")
        self.model_path.setObjectName("model_path")
        self.class_path = QtWidgets.QLabel(self.centralwidget)
        self.class_path.setGeometry(QtCore.QRect(250, 510, 101, 31))
        self.class_path.setStatusTip("")
        self.class_path.setStyleSheet("font: 15pt \"MS Shell Dlg 2\";\n"
                                      "                    ")
        self.class_path.setObjectName("class_path")
        self.predict_button = QtWidgets.QPushButton(self.centralwidget)
        self.predict_button.setGeometry(QtCore.QRect(680, 380, 111, 41))
        self.predict_button.setCursor(QtGui.QCursor(
            QtCore.Qt.CursorShape.PointingHandCursor))
        self.predict_button.setStatusTip("")
        self.predict_button.setStyleSheet("QPushButton{font: 120 15pt \"MS Shell Dlg 2\";\n"
                                          "                        border-radius:15px;\n"
                                          "                        background-color: orangered;\n"
                                          "                        }\n"
                                          "                        QPushButton:hover{\n"
                                          "                        background-color: orange;\n"
                                          "                        }")
        self.predict_button.setObjectName("predict_button")
        self.predict_button.clicked.connect(self.path)

        self.class_path_entry_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.class_path_entry_2.setGeometry(QtCore.QRect(370, 550, 381, 31))
        self.class_path_entry_2.setStatusTip("")
        self.class_path_entry_2.setStyleSheet("QLineEdit{border-radius: 10px;\n"
                                              "border: 1px solid black;\n"
                                              "background-color: rgb(255, 255, 255);\n"
                                              "border-color: rgb(0, 170, 255);\n"
                                              "font: 10pt \"MS Shell Dlg 2\";\n"
                                              "color: black;}\n"
                                              "\n"
                                              "QLineEdit:hover{\n"
                                              "    background-color: rgb(170, 255, 255);\n"
                                              "}")
        self.class_path_entry_2.setObjectName("class_path_entry_2")
        self.class_path_2 = QtWidgets.QLabel(self.centralwidget)
        self.class_path_2.setGeometry(QtCore.QRect(250, 550, 111, 31))
        self.class_path_2.setStatusTip("")
        self.class_path_2.setStyleSheet("font: 15pt \"MS Shell Dlg 2\";\n"
                                        "                    ")
        self.class_path_2.setObjectName("class_path_2")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(250, 90, 411, 251))
        self.label.setStyleSheet("border-radius: 10px;\n"
                                 "                        border: 2px solid white;")
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap(
            "img.png"))
        self.label.setObjectName("label")
        self.path_area.raise_()
        self.logo.raise_()
        self.clock.raise_()
        self.list_of_classes.raise_()
        self.prediction_result_window.raise_()
        self.verticalScrollBar.raise_()
        self.class_path_entry.raise_()
        self.model_path_entry.raise_()
        self.path_input.raise_()
        self.model_path.raise_()
        self.class_path.raise_()
        self.predict_button.raise_()
        self.class_path_entry_2.raise_()
        self.class_path_2.raise_()
        self.label.raise_()
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)



    def path(self):
        self.paths = {'Model' : str(self.model_path_entry.text()),
                      'Class': str(self.class_path_entry.text()),
                      'Image': str(self.class_path_entry_2.text())}
        try:
            self.t0 = time.strftime('%S')
            self.img = self.paths['Image']
            self.file = cv2.imread(self.img)
            self.file = cv2.resize(self.file, (410, 253))
            self.file = keras.utils.array_to_img(self.file)
            self.file.save("img.png")
            self.x = joblib.load( self.paths['Class'] )
            self.item.setText("\n".join(self.x))
            self.result = local.img_decoder(model_path=self.paths['Model'],
                                            img_path=self.img,
                                            classes=self.paths['Class'])
            self.prediction_result_window.setText(f"Predicted Result : {str(self.result)}")
            self.clock.setText(str(int(time.strftime('%S')) - int(self.t0)) + 's')
        except FileNotFoundError and Exception:
            pass

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Predict Panel"))
        self.logo.setWhatsThis(_translate("MainWindow", "\n"
                                          "                        <html><head/><body><p><br/></p></body></html>"))
        self.logo.setText(_translate("MainWindow", "Predictor Panel"))
        self.clock.setText(_translate("MainWindow", "⏰"))
        __sortingEnabled = self.list_of_classes.isSortingEnabled()
        self.list_of_classes.setSortingEnabled(False)
        self.item = self.list_of_classes.item(0)
        self.item.setText(_translate("MainWindow", "Items"))
        self.list_of_classes.setSortingEnabled(__sortingEnabled)
        self.prediction_result_window.setText(
            _translate("MainWindow", "Predicted Result : "))
        self.path_input.setText(_translate("MainWindow", "Path Input"))
        self.model_path.setText(_translate("MainWindow", "Model Path"))
        self.class_path.setText(_translate("MainWindow", "Class Path"))
        self.predict_button.setText(_translate("MainWindow", "Predict"))
        self.class_path_2.setText(_translate("MainWindow", "Image Path"))


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())
