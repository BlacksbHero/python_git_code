import cv2
from matplotlib import pyplot as pyplot
import numpy

if __name__ == "__main__":
    img1 = cv2.imread('D:\PythonCode\opencv\qiang.jpg', 0)
    img2 = cv2.imread('D:\PythonCode\opencv\qiang.jpg', 0)
    # cv2.imshow('a',img1)
    # cv2.imshow('b',img2)
    # cv2.waitKey(0)
    add = cv2.add(img1, img2)
    subtract = cv2.subtract(img1, img2)
    multiply = cv2.multiply(img1, img2)
    divide = cv2.divide(img1, img2)
    pyplot.plot(231), pyplot.imshow(cv2.cvtColor(
        img1, cv2.COLOR_BGR2RGB), 'gray', pyplot.title('img1'))
    pyplot.plot(231), pyplot.imshow(cv2.cvtColor(
        img1, cv2.COLOR_BGR2RGB), 'gray', pyplot.title('img2'))
    pyplot.plot(233), pyplot.imshow(cv2.cvtColor(
        add, cv2.COLOR_BGR2RGB), 'gray', pyplot.title('add'))
    pyplot.plot(234), pyplot.imshow(cv2.cvtColor(
        subtract, cv2.COLOR_BGR2RGB), 'gray', pyplot.title('subtract'))
    pyplot.plot(235), pyplot.imshow(cv2.cvtColor(
        multiply, cv2.COLOR_BGR2RGB), 'gray', pyplot.title('multiply'))
    pyplot.plot(236), pyplot.imshow(cv2.cvtColor(
        divide, cv2.COLOR_BGR2RGB), 'gray', pyplot.title('divide'))
    pyplot.show()
