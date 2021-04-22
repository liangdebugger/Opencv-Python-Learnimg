import cv2
File_path = 'D:/Youxun/369.jpg'
img = cv2.imread(File_path)            
b, g ,r =cv2.split(img)                 
merged = cv2.merge([b,g,r])

cv2.imshow('image',img)
cv2.imshow("Blue 1", b)
cv2.imshow("Green 1", g)
cv2.imshow("Red 1", r)
cv2.imshow("merged 1", merged)
cv2.waitKey(0)
