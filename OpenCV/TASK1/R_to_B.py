import cv2 as cv
import sys
path = '/home/prathmesh/Desktop/UMIC/Autumn-of-Automation/OpenCV/TASK1/rsz_peacock-feather.jpg'
img = cv.imread(path)
new = cv.cvtColor(img, cv.COLOR_BGR2RGB)
cv.imwrite("R_to_B.jpg", new)