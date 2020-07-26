import cv2 as cv
import sys
path = '/home/prathmesh/Desktop/UMIC/Autumn-of-Automation/OpenCV/TASK1/rsz_peacock-feather.jpg'
img = cv.imread(path)
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imwrite("gray.jpg", gray)
_,bw_binary = cv.threshold(gray,127,255,cv.THRESH_BINARY)
cv.imwrite("bw_binary.jpg", bw_binary)
bw_adaptive_mean = cv.adaptiveThreshold(gray ,255,cv.ADAPTIVE_THRESH_MEAN_C,\
            cv.THRESH_BINARY,11,2)
cv.imwrite("bw_adaptive_mean.jpg", bw_adaptive_mean)
bw_adaptive_gaussian = cv.adaptiveThreshold(gray,255,cv.ADAPTIVE_THRESH_GAUSSIAN_C,\
            cv.THRESH_BINARY,11,2)
cv.imwrite("bw_adaptive_gaussian.jpg", bw_adaptive_gaussian)
cv.waitKey(0)