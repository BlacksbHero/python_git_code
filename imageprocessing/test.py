import cv2
import numpy
from matplotlib import pyplot as plt

img = cv2.imread('D:\PythonCode\opencv\qiang.jpg')
# cv2.namedWindow("qiang", cv2.WINDOW_NORMAL)
cv2.imshow("qiang", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
