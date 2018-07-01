import cv2
import numpy as np
from matplotlib import pyplot as plt

def myfunc(i):
    pass # do nothing

cv2.namedWindow('Filter') # create win with win name

cv2.createTrackbar('Value', # name of value
                   'Filter', # win name
                   1, # min
                   10, # max
                   myfunc) # callback func

cap = cv2.VideoCapture(0)
cap.set(cv2.CAP_PROP_FRAME_WIDTH,  640)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)


while(True):
    
    ret, frame = cap.read()
    if not ret: continue
    
    v = cv2.getTrackbarPos('Value',  # get the value
                           'Filter')  # of the win

    ## do something by using v
    img = cv2.cvtColor(frame , cv2.COLOR_BGR2RGB)
    gray1 = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
    
    if v % 2 == 0:
        imf = cv2.blur(gray1,(v+1,v+1))
    else:
        imf = cv2.blur(gray1,(v,v))
 
    cv2.imshow('Filter', imf)  # show in the win
                           
    k = cv2.waitKey(1)
    if k == ord('q') or k == 27:
        break



cap.release()
cv2.destroyAllWindows()
