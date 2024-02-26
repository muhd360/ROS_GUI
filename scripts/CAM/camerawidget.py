from PyQt5.QtWidgets import QWidget
from PyQt5.QtGui import QImage, QPixmap
import cv2
from PyQt5 import QtCore, QtGui


class CameraWidget(QWidget):
    def __init__(self, parent=None):
        super(CameraWidget, self).__init__(parent)
        self.video_capture = cv2.VideoCapture(0)  # Change the argument if using a different camera index

        # Set up a timer to continuously update the displayed frame
        self.timer = QtCore.QTimer(self)
        self.timer.timeout.connect(self.update_frame)
        self.timer.start(100)  # Update every 100 milliseconds

    def update_frame(self):
        ret, frame = self.video_capture.read()
        if ret:
            # Convert the OpenCV frame to a QImage
            height, width, channel = frame.shape
            bytes_per_line = 3 * width
            q_image = QImage(frame.data, width, height, bytes_per_line, QImage.Format_RGB888).rgbSwapped()

            # Set the QImage as the pixmap for the QLabel
            self.setPixmap(QPixmap.fromImage(q_image))

    def closeEvent(self, event):
        # Release the video capture when the widget is closed
        self.video_capture.release()
        event.accept()
