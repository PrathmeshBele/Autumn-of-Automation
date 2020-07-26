import cv2 as cv
import numpy as np 

path = '/home/prathmesh/Desktop/UMIC/Autumn-of-Automation/OpenCV/TASK2/T.jpg'
img = cv.imread(path)
rows,cols = img.shape[0], img.shape[1]

#translations
M1 = np.float32([[1,0,100],[0,1,50]])
dst1 = cv.warpAffine(img,M1,(cols,rows))
cv.imwrite("T1.jpg", dst1)

M2 = np.float32([[1,0,50],[0,1,100]])
dst2 = cv.warpAffine(img,M2,(cols,rows))
cv.imwrite("T2.jpg", dst2)

M3= np.float32([[1,0,100],[0,1,100]])
dst3 = cv.warpAffine(img,M3,(cols,rows))
cv.imwrite("T3.jpg", dst3)

M4 = np.float32([[1,0,50],[0,1,50]])
dst4 = cv.warpAffine(img,M4,(cols,rows))
cv.imwrite("T4.jpg", dst4)

#rotation
M5 = cv.getRotationMatrix2D((cols/2,rows/2),90,1)
dst5 = cv.warpAffine(img,M5,(cols,rows))
cv.imwrite("T5.jpg", dst5)

M6 = cv.getRotationMatrix2D((cols/2,rows/2),180,1)
dst6 = cv.warpAffine(img,M6,(cols,rows))
cv.imwrite("T6.jpg", dst6)

M7 = cv.getRotationMatrix2D((cols/2,rows/2),280,1)
dst7 = cv.warpAffine(img,M7,(cols,rows))
cv.imwrite("T7.jpg", dst7)

M8 = cv.getRotationMatrix2D((cols/2,rows/2),354,1)
dst8 = cv.warpAffine(img,M8,(cols,rows))
cv.imwrite("T8.jpg", dst8)

#blurring
kernel1 = np.ones((3,3),np.float32)/9
dst9 = cv.filter2D(img,-1,kernel1)
cv.imwrite("T9.jpg", dst9)

blur = cv.GaussianBlur(img,(5,5),0)
cv.imwrite('T10.jpg', blur)