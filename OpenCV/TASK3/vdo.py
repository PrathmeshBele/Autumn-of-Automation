import cv2 as cv
vid = cv.VideoCapture(0) 
  
while(True): 
    ret, frame = vid.read()
    edges = cv.Canny(frame,0,200)
    edges = ~edges
    cv.imshow('video', edges)
    if cv.waitKey(1) == 27:     #ESC to end
        break 
vid.release() 
cv.destroyAllWindows() 