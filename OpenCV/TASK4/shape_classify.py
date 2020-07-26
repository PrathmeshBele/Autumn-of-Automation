import cv2
import numpy as np
img = cv2.imread("/home/prathmesh/Desktop/UMIC/Autumn-of-Automation/OpenCV/TASK3/shapes.jpg")
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
ret, img_thresh = cv2.threshold(img_gray, 240, 255, cv2.THRESH_BINARY)
contours, _ = cv2.findContours(img_thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
for cnt in contours:
    if cv2.contourArea(cnt)>5000:
        approx = cv2.approxPolyDP(cnt, 0.01*cv2.arcLength(cnt, True), closed = True)
        M = cv2.moments(cnt)
        cX = int(M['m10']/M['m00'])
        cY = int(M['m01']/M['m00'])
        Centroid = (cX, cY) 
        x, y = approx[0][0]

        if len(approx) == 3:
            cv2.drawContours(img, cnt, -1, (0, 255, 0), 5)
            cv2.circle(img, (cX, cY), 7, (255, 255, 255), -1)
            cv2.putText(img, 'triangle', (x,y), cv2.FONT_HERSHEY_SIMPLEX , 1, 0,2) 

        elif len(approx) == 4:
            (x, y, w, h) = cv2.boundingRect(approx)
            ratio = cv2.contourArea(cnt)*1.0 / (w*h)

            if 0.95<w*1.0/h<1.05: 
            	cv2.drawContours(img, cnt, -1, (0, 255, 0), 5)
            	cv2.circle(img, (cX, cY), 7, (255, 255, 255), -1)
            	cv2.putText(img, 'square', (x,y), cv2.FONT_HERSHEY_SIMPLEX , 1, 0,2) 

            elif w*1.0/h>=1.05 or w*1.0/h<=0.95 and ratio==1:
            	cv2.drawContours(img, cnt, -1, (0, 255, 0), 5)
            	cv2.circle(img, (cX, cY), 7, (255, 255, 255), -1)
            	cv2.putText(img, 'rectangle', (x,y), cv2.FONT_HERSHEY_SIMPLEX , 1, 0,2)

            else:
            	cv2.drawContours(img, cnt, -1, (0, 255, 0), 5)
            	cv2.circle(img, (cX, cY), 7, (255, 255, 255), -1)
            	cv2.putText(img, 'diamond', (x,y), cv2.FONT_HERSHEY_SIMPLEX , 1, 0,2)

        elif len(approx)<15:
            cv2.drawContours(img, cnt, -1, (0, 255, 0), 5)
            cv2.circle(img, (cX, cY), 7, (255, 255, 255), -1)
            cv2.putText(img, 'ellipse', (x,y), cv2.FONT_HERSHEY_SIMPLEX , 1, 0,2) 

        elif len(approx) >=14:
            cv2.drawContours(img, cnt, -1, (0, 255, 0), 5)
            cv2.circle(img, (cX, cY), 7, (255, 255, 255), -1)
            cv2.putText(img, 'circle', (x,y), cv2.FONT_HERSHEY_SIMPLEX , 1, 0,2) 

cv2.imwrite("contour.jpg", img)