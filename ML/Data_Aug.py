import cv2 as cv
import numpy as np 
import os
import cv2
pth = '/home/prathmesh/Desktop/UMIC/Autumn-of-Automation/ML/UMIC/Yes'
obj = os.listdir(pth)
for j in obj:
	img = cv2.imread(pth + '/' + j)
	img_flip_lr = cv2.flip(img, 1)
	cv2.imwrite('A{}.jpg'.format(j.replace('.jpg','')), img_flip_lr)
