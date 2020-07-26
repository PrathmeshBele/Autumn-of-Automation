import cv2 as cv
vid = cv.VideoCapture(0) 
  
while(True): 
    ret, frame = vid.read()
    cv.imshow('video', frame)
    if cv.waitKey(1) == 27:     #ESC to end
        break
vid.release() 
cv.destroyAllWindows() 