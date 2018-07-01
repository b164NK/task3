
import numpy as np
from matplotlib import pyplot as plt
import cv2
from skimage.color import rgb2gray, rgb2hsv

def myfunc(i):
    pass # do nothing

cv2.namedWindow('HSV') # create win with win name

cv2.createTrackbar('H', # name of value
                   'HSV', # win name
                   0, # min
                   179, # max
                   myfunc) # callback func

cv2.createTrackbar('S', # name of value
                   'HSV', # win name
                   0, # min
                   255, # max
                   myfunc) # callback func

cv2.createTrackbar('V', # name of value
                   'HSV', # win name
                   0, # min
                   255, # max
                   myfunc) # callback func


cap = cv2.VideoCapture(0)
cap.set(cv2.CAP_PROP_FRAME_WIDTH,  640)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)


while(True):
    
    ret, frame = cap.read()
    if not ret: continue
    
    H = cv2.getTrackbarPos('H',  # get the value
                           'HSV')  # of the win

    S = cv2.getTrackbarPos('S',  # get the value
                           'HSV')  # of the win
                           
    V = cv2.getTrackbarPos('V',  # get the value
                           'HSV')  # of the win
        
    ## do something by using v
    img = cv2.cvtColor(frame , cv2.COLOR_BGR2HSV)

    #cv2.imshow('HSV original', img)  # show in the win
    
    img[:,:,0] = img[:,:,0] + H
            
    img[:,:,1] = img[:,:,1] + S
            
    img[:,:,2] = img[:,:,2] + V

    cv2.imshow('HSV', img)  # show in the win
                           
    k = cv2.waitKey(1)
    if k == ord('q') or k == 27:
        break

cap.release()
cv2.destroyAllWindows()
