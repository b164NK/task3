import numpy as np
import cv2

def myfunc(i):
    pass

cv2.namedWindow('title')

cv2.createTrackbar('value',
                   'title',
                   0,
                   160,
                   myfunc)

cap = cv2.VideoCapture(0)

cap.set(cv2.CAP_PROP_FRAME_WIDTH,  400)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 400)

while(True):
    
    ret, frame = cap.read()
    ret1, frame1 = cap.read()


    v = cv2.getTrackbarPos('value',
                           'title')

    hsv = cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)

    low_color = np.array([v-20, 75, 75])
    upper_color = np.array([v+20, 255, 255])
    
    ex_img = cv2.inRange(hsv,low_color,upper_color)

    cv2.imshow("SHOW COLOR IMAGE",ex_img)
    
    vvec =  np.ones((ex_img.shape[1],1))
    
    hvec =  np.ones((1,ex_img.shape[0]))
    
    hvec = np.dot(hvec,ex_img)
    vvec = np.dot(ex_img,vvec)
    
    x = np.argmax(hvec)
    y = np.argmax(vvec)
    
    cv2.circle(frame,(x,y),100,(0,255,0),thickness=3)
    
    cv2.imshow('title',frame)

    key = cv2.waitKey(1) & 0xFF

    if key == ord('q'):
        break

    if key == ord('s'):
        path = "photo.jpg"
        cv2.imwrite(path,frame)

cap.release()
cv2.destroyAllWindows()
