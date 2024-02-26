# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'LAUNCH.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import subprocess

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1051, 582)
        MainWindow.setStyleSheet("\n"
"background-color: rgb(0, 0, 0);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.layoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget.setGeometry(QtCore.QRect(0, -70, 621, 701))
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.roslaunch = QtWidgets.QPushButton(self.layoutWidget)
        self.roslaunch.setMinimumSize(QtCore.QSize(0, 50))
        self.roslaunch.setStyleSheet("background-color: rgb(49, 12, 74);\n"
"font: 75 23pt \"C059\";\n"
"color:rgb(255,255,255);\n"
"border:2px solid white;")
        self.roslaunch.setObjectName("roslaunch")
        self.verticalLayout.addWidget(self.roslaunch)
        self.science_plot = QtWidgets.QPushButton(self.layoutWidget)
        self.science_plot.setEnabled(True)
        self.science_plot.setMinimumSize(QtCore.QSize(0, 50))
        self.science_plot.setStyleSheet("background-color: rgb(49, 12, 74);\n"
"font: 75 23pt \"C059\";\n"
"color:rgb(255,255,255);\n"
"border:2px solid white;")
        self.science_plot.setObjectName("science_plot")
        self.verticalLayout.addWidget(self.science_plot)
        self.science_plot2 = QtWidgets.QPushButton(self.layoutWidget)
        self.science_plot2.setMinimumSize(QtCore.QSize(0, 50))
        self.science_plot2.setStyleSheet("background-color: rgb(49, 12, 74);\n"
"font: 75 23pt \"C059\";\n"
"color:rgb(255,255,255);\n"
"border:2px solid white;")
        self.science_plot2.setObjectName("science_plot2")
        self.verticalLayout.addWidget(self.science_plot2)
        self.cam_view = QtWidgets.QPushButton(self.layoutWidget)
        self.cam_view.setMinimumSize(QtCore.QSize(0, 50))
        self.cam_view.setStyleSheet("background-color: rgb(49, 12, 74);\n"
"font: 75 23pt \"C059\";\n"
"color:rgb(255,255,255);\n"
"border:2px solid white;")
        self.cam_view.setObjectName("cam_view")
        self.verticalLayout.addWidget(self.cam_view)
        self.KILL_X = QtWidgets.QPushButton(self.layoutWidget)
        self.KILL_X.setMinimumSize(QtCore.QSize(0, 50))
        self.KILL_X.setStyleSheet("background-color: rgb(49, 12, 74);\n"
"font: 75 23pt \"C059\";\n"
"color:rgb(255,255,255);\n"
"border:2px solid white;")
        self.KILL_X.setObjectName("KILL_X")
        self.verticalLayout.addWidget(self.KILL_X)
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(630, 10, 411, 341))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("./img.png"))
        self.label.setObjectName("label")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.roslaunch.setText(_translate("MainWindow", "ROSCORE"))
        self.science_plot.setText(_translate("MainWindow", "SCIENCE"))
        self.science_plot2.setText(_translate("MainWindow", "SCIENCE-2"))
        self.cam_view.setText(_translate("MainWindow", "CAM VIEW"))
        self.KILL_X.setText(_translate("MainWindow", "KILL ALL PROCESS"))
        self.roslaunch.clicked.connect(self.roslauncher)
        self.science_plot.clicked.connect(self.science_ls)
        self.science_plot2.clicked.connect(self.science_ls1)
        self.cam_view.clicked.connect(self.CAM)
        self.KILL_X.clicked.connect(self.kill_all)

    def roslauncher(self):
        try:
            subprocess.Popen(['roscore'])
        except Exception as e:
            print(f"Error launching roscore: {e}")

    def science_ls(self):
        path_n = '/home/muhd/Desktop/WAS/catkin_ws_gui/src/my_gui/scripts/guiattempt1.py'
        try:
            subprocess.Popen(['python3', path_n])
        except Exception as e:
            print("F")

    def science_ls1(self):
        path_n1 = '/home/muhd/Desktop/WAS/catkin_ws_gui/src/my_gui/scripts/science.py'
        try:
            subprocess.Popen(['python3', path_n1])
        except Exception as e:
            print("F")

    def CAM(self):
        path_n2 = '/home/muhd/Desktop/WAS/catkin_ws_gui/src/my_gui/scripts/main.py'
        try:
            subprocess.Popen(['python3', path_n2])
            print("lol")
        except Exception as e:
            print("F")
    def kill_all(self):
        try:
            subprocess.Popen(['killall roscore'])
        except:
            print("laude lag gaye")


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
