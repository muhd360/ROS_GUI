# # -*- coding: utf-8 -*-

# # Form implementation generated from reading ui file 'science.ui'
# #
# # Created by: PyQt5 UI code generator 5.14.1
# #
# # WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QLabel
from pyqtgraph import PlotWidget
import rospy
from std_msgs.msg import String,Float32,Float64
import sys

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(4095, 4095)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.lc1 = PlotWidget(self.centralwidget)

        self.x_data = []  # Initialize x_data list
        self.y_data = []

        self.x1_data = []  # Initialize x_data list
        self.y1_data = []

        self.x2_data = []  # Initialize x_data list
        self.y2_data = []


        self.lc1.setGeometry(QtCore.QRect(60, 269, 1361, 191))
        self.lc1.setObjectName("lc1")
        label_text="DHT(Humidity(%))"
        self.label = QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(60,200,1361,100))  # Adjust the position as needed
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setStyleSheet("font-size: 14pt; font-weight: bold;")
        self.label.setText(label_text)







        self.sht1 = PlotWidget(self.centralwidget)
        self.sht1.setGeometry(QtCore.QRect(60, 500, 650, 350))
        self.sht1.setObjectName("sht1")
        label_text="sht1(C)"
        self.label = QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(60, 850, 650, 30))  # Adjust the position as needed
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setStyleSheet("font-size: 14pt; font-weight: bold;")
        self.label.setText(label_text)


        self.sht2 = PlotWidget(self.centralwidget)
        self.sht2.setGeometry(QtCore.QRect(770, 500, 650, 350))
        self.sht2.setObjectName("sht2")
        label_text="sht2(T)"
        self.label = QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(770, 850, 650, 30))  # Adjust the position as needed
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setStyleSheet("font-size: 14pt; font-weight: bold;")
        self.label.setText(label_text)





        self.layoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget.setGeometry(QtCore.QRect(60, 30, 1361, 27))
        self.layoutWidget.setObjectName("layoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.layoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.pushButton = QtWidgets.QPushButton(self.layoutWidget)
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout.addWidget(self.pushButton)
        self.pushButton_2 = QtWidgets.QPushButton(self.layoutWidget)
        self.pushButton_2.setObjectName("pushButton_2")
        self.horizontalLayout.addWidget(self.pushButton_2)
        self.pushButton_3 = QtWidgets.QPushButton(self.layoutWidget)
        self.pushButton_3.setObjectName("pushButton_3")
        self.horizontalLayout.addWidget(self.pushButton_3)
        self.textBrowser = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser.setGeometry(QtCore.QRect(260, 100, 481, 131))
        self.textBrowser.setFrameShape(QtWidgets.QFrame.Box)
        self.textBrowser.setLineWidth(8)
        self.textBrowser.setObjectName("textBrowser")
        self.textBrowser_2 = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser_2.setGeometry(QtCore.QRect(930, 100, 491, 131))
        self.textBrowser_2.setFrameShape(QtWidgets.QFrame.Box)
        self.textBrowser_2.setLineWidth(8)
        self.textBrowser_2.setObjectName("textBrowser_2")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(70, 110, 191, 101))
        self.label.setStyleSheet("font: 75 italic 25pt \"Quicksand Medium\";")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(770, 110, 191, 101))
        self.label_2.setStyleSheet("font: 75 italic 25pt \"Quicksand Medium\";")
        self.label_2.setObjectName("label_2")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)



        self.ros_listener = ROSListener(self)
        #rospy.init_node('ros_gui_subscriber')
        self.subscriber1= rospy.Subscriber('numbers2', Float32, self.receive_data)
        self.subscriber2= rospy.Subscriber('numbers3', Float32, self.receive_data1)
        self.subscriber3= rospy.Subscriber('numbers4', Float32, self.receive_data2)
        self.retranslateUi(MainWindow)
        self.pushButton.clicked.connect(self.lc1.show)
        self.pushButton_2.clicked.connect(self.sht1.show)
        self.pushButton_3.clicked.connect(self.sht2.show)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)


    def receive_data(self,msg):
        data1=msg.data
        x = len(self.x_data) + 1
        self.x_data.append(x)
        self.y_data.append(data1)
        self.lc1.plot(self.x_data, self.y_data, pen=(1, 3))   

    def receive_data1(self,msg):
        data3=msg.data
        x = len(self.x1_data) + 1
        self.x1_data.append(x)
        self.y1_data.append(data3)
        self.sht1.plot(self.x1_data, self.y1_data, pen=(1, 3))   

    def receive_data2(self,msg):
        data2=msg.data
        x = len(self.x2_data) + 1
        self.x2_data.append(x)
        self.y2_data.append(data2)
        self.sht2.plot(self.x2_data, self.y2_data, pen=(1, 3))   



    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton.setText(_translate("MainWindow", "LOADCELL1"))
        self.pushButton_2.setText(_translate("MainWindow", "SHT_10.1"))
        self.pushButton_3.setText(_translate("MainWindow", "SHT_10.2"))
        self.label.setText(_translate("MainWindow", "LONGITUDE"))
        self.label_2.setText(_translate("MainWindow", "LATITUDE"))

    def update_text_browser(self, text):
        # Call the Ui_MainWindow method to update the text browser
        self.textBrowser.setText(text)

    def update_text_browser_2(self, text):
        # Call the Ui_MainWindow method to update the text browser
        self.textBrowser_2.setText(text)




# # ... (unchanged imports)

# class ROSListener(QtCore.QObject):
#     def __init__(self, ui_mainwindow):
#         super().__init__()

#         # Create ROS subscribers
#         rospy.init_node('qt_ros_subscriber')  # Initialize ROS node
#         self.subscriber_aa = rospy.Subscriber('numbers', Float32, self.update_text_browser)
#         self.subscriber_aa2 = rospy.Subscriber('AA2', String, self.update_text_browser_2)

#         # Connect to the Ui_MainWindow to access its methods
#         self.ui_mainwindow = ui_mainwindow

#         # Start ROS spin in a separate thread
#         self.thread = QtCore.QThread()
#         self.moveToThread(self.thread)
#         self.thread.started.connect(self.start_ros_spin)  # Connect to a custom method

#     def start_ros_spin(self):
#         rospy.spin()

#     def update_text_browser(self, msg):
#         # Call the Ui_MainWindow method to update the text browser
#         self.ui_mainwindow.textBrowser.setText(str(msg.data))

#     def update_text_browser_2(self, msg):
#         # Call the Ui_MainWindow method to update the text browser
#         self.ui_mainwindow.textBrowser_2.setText(str(msg.data))




# if __name__ == "__main__":
#     import sys
#     app = QtWidgets.QApplication(sys.argv)
#     MainWindow = QtWidgets.QMainWindow()
#     ui = Ui_MainWindow()
#     ui.setupUi(MainWindow)
#     MainWindow.show()
#     sys.exit(app.exec_())

# ... (unchanged imports)

class ROSListener(QtCore.QObject):
    update_text_browser_signal = QtCore.pyqtSignal(str)
    update_text_browser_signal2 = QtCore.pyqtSignal(str)

    def __init__(self, ui_mainwindow):
        super().__init__()

        # Create ROS subscribers
        rospy.init_node('qt_ros_subscriber')  # Initialize ROS node
        self.subscriber_aa = rospy.Subscriber('longitude', Float32, self.update_text_browser)
        self.subscriber_aa2 = rospy.Subscriber('latitude', Float32, self.update_text_browser_2)

        # Connect to the Ui_MainWindow to access its methods
        self.ui_mainwindow = ui_mainwindow

        # Connect signal to slot in the main thread
        self.update_text_browser_signal.connect(ui_mainwindow.update_text_browser)
        self.update_text_browser_signal2.connect(ui_mainwindow.update_text_browser_2)

    def update_text_browser(self, msg):
        # Emit the signal to update the text browser in the main thread
        self.update_text_browser_signal.emit(str(msg.data))

    def update_text_browser_2(self, msg):
        # Emit the signal to update the text browser in the main thread
        self.update_text_browser_signal2.emit(str(msg.data))

    def start_ros_spin(self):
        rate = rospy.Rate(10)  # Adjust the rate as needed
        while not rospy.is_shutdown():
            #rospy.spinOnce()
            rate.sleep()
            QtCore.QCoreApplication.processEvents()

# ... (unchanged code)
if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()

    # Create ROSListener after the MainWindow is shown
    ros_listener = ROSListener(ui)

    # Start the thread after the MainWindow is shown
    ros_listener.thread = QtCore.QThread()
    ros_listener.moveToThread(ros_listener.thread)
    ros_listener.thread.started.connect(ros_listener.start_ros_spin)
    ros_listener.thread.start()

    sys.exit(app.exec_())