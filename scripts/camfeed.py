import urllib
import cv2
import numpy as np

url = 'http://192.168.50.158:8080/photo.jpg'
imgResp = urllib.urlopen(url)  # Updated to urllib.request.urlopen for Python 3 compatibility
imgNp = np.array(bytearray(imgResp.read()), dtype=np.uint8)
img = cv2.imdecode(imgNp, -1)
cv2.imshow('test', img)
cv2.waitKey(10) 