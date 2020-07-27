import os
import cv2
path = '/home/prathmesh/Desktop/UMIC/Autumn-of-Automation/ML/UMIC'
for i in os.listdir(path):
	pth = path + '/' + i
	obj = os.listdir(pth)
	for j in obj:
		img = cv2.imread(pth + '/' + j)
		cv2.imwrite('{}.jpg'.format(j.replace('.pgm','')), img)