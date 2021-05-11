#图像的几何变换，包括缩放、平移、旋转、镜像
import cv2
import numpy as np

# opencv读取图像文件
File_path = 'D:/Youxun/369.jpg'
img = cv2.imread(File_path)

#长、宽、通道
rows,cols,channels = img.shape

#指定任意尺寸缩放
new_img1 = cv2.resize(img ,(200,200))
cv2.imshow('new_img1',new_img1)
cv2.imshow('src',img)
cv2.waitKey(0)

#按比例缩放
new_img2 = cv2.resize(img, None, fx=2, fy=2)
cv2.imshow('new_img2',new_img2)
cv2.imshow('src',img)
cv2.waitKey(0)


#平移
M = np.array([[1, 0, 100], [0, 1, 100]], dtype = np.float32)
new_img_pan = cv2.warpAffine(img, M,(rows+100, cols+100))
cv2.imshow('new_img_pan',new_img_pan)
cv2.waitKey(0)

#平移（对点操作）
new_img_pan1 = np.zeros([rows+100, cols+100, channels], dtype=np.uint8)
for i in range(rows+100):
    for j in range (cols+100):
        if i>=100 and j>=100:
            new_img_pan1[i,j] = img[i-100,j-100]
        else:
            new_img_pan1[i,j] = 0
cv2.imshow('new_img_pan1',new_img_pan1)
cv2.waitKey(0)

#旋转
#旋转中心;旋转角度;缩放比例
M_Rotate = cv2.getRotationMatrix2D((cols/2,rows/2),45,0.6)
new_img_rotate = cv2.warpAffine(img, M_Rotate, (rows,cols))
cv2.imshow('new_img_rotate',new_img_rotate)
cv2.waitKey(0)

#镜像
img_mirror_x = cv2.flip(img, 1, dst = None)
img_mirror_y = cv2.flip(img, 0, dst = None)
cv2.imshow('img_mirror_x',img_mirror_x)
cv2.imshow('img_mirror_y',img_mirror_y)
cv2.waitKey(0)
