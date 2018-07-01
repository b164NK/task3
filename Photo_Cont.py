
import numpy as np
import cv2

def myfunc(i):
    pass # do nothing

cv2.namedWindow('title') # create win with win name

cv2.createTrackbar('value', # name of value
                   'title', # win name
                   1, # min
                   30, # max
                   myfunc) # callback func



cap = cv2.VideoCapture(0)
cap.set(cv2.CAP_PROP_FRAME_WIDTH,  640)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)


while(True):
    
    ret, frame = cap.read()
    if not ret: continue
    
    
    v = cv2.getTrackbarPos('value',  # get the value
                           'title')  # of the win
        
    ## do something by using v
    
    img = cv2.cvtColor(frame , cv2.COLOR_BGR2RGB)
    gray1 = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
    
    gamma = v * 0.1
    
    try:
        gray2 = 255 * (gray1 / 255)**(1/gamma)
    except ZeroDivisionError:
        print("ZeroDivisionError!!")
    
    cv2.imshow('title', gray2)  # show in the win
                           
    k = cv2.waitKey(1)
    if k == ord('q') or k == 27:
        break



cap.release()
cv2.destroyAllWindows()
# task2
# task2
