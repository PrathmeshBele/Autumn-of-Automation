import numpy as np
import cv2 as cv
from matplotlib import pyplot as plt
img = cv.imread('/home/prathmesh/Desktop/UMIC/Autumn-of-Automation/OpenCV/TASK1/rsz_peacock-feather.jpg',0)
edges = cv.Canny(img,0,200)
edges = ~edges
plt.subplot(121),plt.imshow(img,cmap = 'gray')
plt.title('Original Image'), plt.xticks([]), plt.yticks([])
plt.subplot(122),plt.imshow(edges,cmap = 'gray')
plt.title('Edge Image'), plt.xticks([]), plt.yticks([])
plt.show()