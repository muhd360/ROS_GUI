#!/usr/bin/python3

from PyQt5 import QtCore, QtGui, QtWidgets
from cam_feed import Ui_MainWindow  # Import the generated UI class
import subprocess
import sys
import webbrowser
import cv2
import urllib3
import numpy as np

class MyApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        # Add your application logic here

        self.pushButton.clicked.connect(self.launch_webpage)
        self.pushButton_2.clicked.connect(self.launch_webpage2)
        self.pushButton_3.clicked.connect(self.launch_webpage3)

    def launch_webpage(self):
        url = 'http://192.168.50.158:8080/photo.jpg'
        imgResp = urllib3.request.urlopen(url)  # Updated to urllib.request.urlopen for Python 3 compatibility
        imgNp = np.array(bytearray(imgResp.read()), dtype=np.uint8)
        img = cv2.imdecode(imgNp, -1)
        cv2.imshow('test', img)
        cv2.waitKey(10) 

    def launch_webpage2(self):
        url = 'https://www.youtube.com'
        try:
            # Open the specified URL in the default web browser
            webbrowser.open(url)
        except Exception as e:
            print(f"Error launching web page: {e}")

    def launch_webpage3(self):
        url = 'https://www.youtube.com'
        try:
            # Open the specified URL in the default web browser
            webbrowser.open(url)
        except Exception as e:
            print(f"Error launching web page: {e}")

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())
