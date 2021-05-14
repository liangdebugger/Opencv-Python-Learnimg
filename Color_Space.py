'''图像直方图可以展示图像不同灰度的像素分布'''

import cv2
import numpy as np
from matplotlib import pyplot as plt

# 灰度图像全局直方图
File_path = '369.jpg'
img = cv2.imread(File_path,0)
hist = cv2.calcHist([img], [0], None, [256], [0,256])
plt.figure()
plt.title('Grayima Histgram')
plt.xlabel('Bins')
plt.ylabel('# of Pixels')
plt.plot(hist)
plt.xlim([0,256])
plt.show()
input()

#灰度图像局部直方图
mask = np.zeros(img.shape[:2],np.uint8)
mask[100:200,100:200] = 255
hist = cv2.calcHist([img], [0], mask, [256], [0,256])
plt.figure()
plt.title('Grayima Histgram')
plt.xlabel('Bins')
plt.ylabel('# of Pixels')
plt.plot(hist)
plt.xlim([0,256])
plt.show()
input()

#彩色图像
img1 = cv2.imread(File_path)
channels = cv2.split(img1)
colors = ('b','g','r')
plt.figure()
plt.title('Colorima Histgram')
plt.xlabel('Bins')
plt.ylabel('# of Pixels')
for channel in channels:
    hist = cv2.calcHist([channel], [0], None, [256], [0, 256])
    plt.plot(hist)
plt.show()
input()

#灰度图像直方图全局均衡
equal = cv2.equalizeHist(img)
cv2.imshow('equal',equal)
cv2.waitKey(0)

#灰度图像直方图局部均衡
clahe = cv2.createCLAHE(5, (3, 3))
new_img = clahe.apply(img)
cv2.imshow('new_img',new_img)
cv2.imshow('img',img)
cv2.waitKey(0)
