'''怀旧风格滤镜模型为：
 new_r = 0.393 * r + 0.769 * g + 0.189 * b
 new_g = 0.349 * r + 0.686 * g + 0.168 * b
 new_b = 0.272 * r + 0.534 * g + 0.131 * b'''

import cv2
import numpy as np

src = cv2.imread('455.jpg')
img = cv2.resize(src, None, fx=0.5, fy=0.5)
rows, cols, channels = img.shape
new_img=np.zeros([rows,cols,channels],dtype=np.uint8)
for i in range (rows):
    for j in range(cols):
        b = img[i, j][0]
        g = img[i, j][1]
        r = img[i, j][2]
        new_b = int(0.272 * r + 0.534 * g + 0.131 * b)
        new_g = int(0.349 * r + 0.686 * g + 0.168 * b)
        new_r = int(0.393 * r + 0.769 * g + 0.189 * b)
        if new_b > 255:
            new_b = 255
        if new_g > 255:
            new_g = 255
        if new_r > 255:
            new_r = 255
        if new_b > 255:
            new_b = 255
        new_img[i, j][0] = new_b
        new_img[i, j][1] = new_g
        new_img[i, j][2] = new_r
cv2.imshow('img', np.hstack([img, new_img]))
cv2.waitKey(0)
