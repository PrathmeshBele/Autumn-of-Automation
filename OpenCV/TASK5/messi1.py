import cv2
vid = cv2.VideoCapture('/home/prathmesh/Desktop/UMIC/Autumn-of-Automation/OpenCV/TASK5/Record Breaking Sprint Speeds in Football.mp4') 
  
while(True): 
    ret, frame = vid.read()
    img_gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    ret, img_thresh = cv2.threshold(img_gray, 240, 255, cv2.THRESH_BINARY)
    contours, _ = cv2.findContours(img_thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    for cnt in contours:
	    if cv2.contourArea(cnt)>100:
	        approx = cv2.approxPolyDP(cnt, 0.01*cv2.arcLength(cnt, True), closed = True)
	        M = cv2.moments(cnt)
	        cX = int(M['m10']/M['m00'])
	        cY = int(M['m01']/M['m00'])
	        Centroid = (cX, cY) 
	        x, y = approx[0][0]
	        if len(approx) >=20:
	            cv2.drawContours(frame, cnt, -1, (0, 255, 0), 5)
    cv2.imshow('video', frame)
    if cv2.waitKey(1) == 27:     #ESC to end
        break 
vid.release() 
cv2.destroyAllWindows() 