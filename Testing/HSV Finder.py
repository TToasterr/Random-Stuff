from PIL import Image
from mss import mss
import time as t
import numpy as np
import cv2

mon = {'top': 300, 'left': 800, 'width': 700, 'height': 700}

sct = mss()

def nothing(x):
    pass
# Creating a window for later use
cv2.namedWindow('result')

# Starting with 100's to prevent error while masking
h,s,v = 100,100,100

# Creating track bar
cv2.createTrackbar('(low) h', 'result',0,179,nothing)
cv2.createTrackbar('(low) s', 'result',0,255,nothing)
cv2.createTrackbar('(low) v', 'result',0,255,nothing)
cv2.createTrackbar('(high) h', 'result',0,179,nothing)
cv2.createTrackbar('(high) s', 'result',0,255,nothing)
cv2.createTrackbar('(high) v', 'result',0,255,nothing)

while(1):
    sct.get_pixels(mon)
    img = Image.frombytes('RGB', (sct.width, sct.height), sct.image)
    imgTemp = np.array(img)

    RGB = cv2.cvtColor(imgTemp, cv2.COLOR_BGR2RGB)
    gray = cv2.cvtColor(imgTemp, cv2.COLOR_BGR2GRAY)

    #converting to HSV
    hsv = cv2.cvtColor(imgTemp, cv2.COLOR_BGR2HSV)

    # get info from track bar and appy to result
    hl = cv2.getTrackbarPos('(low) h','result')
    sl = cv2.getTrackbarPos('(low) s','result')
    vl = cv2.getTrackbarPos('(low) v','result')
    hh = cv2.getTrackbarPos('(high) h','result')
    sh = cv2.getTrackbarPos('(high) s','result')
    vh = cv2.getTrackbarPos('(high) v','result')

    # Normal masking algorithm
    lower = np.array([hl,sl,vl])
    upper = np.array([hh,sh,vh])

    HSVmask = cv2.inRange(hsv, lower, upper)
    RGBmask = cv2.inRange(RGB, lower, upper)
    # GRAYmask = cv2.inRange(gray, lower, upper)

    RGBResult = cv2.bitwise_and(RGB,RGB,mask = HSVmask)
    HSVResult = cv2.bitwise_and(hsv,hsv,mask=RGBmask)
    # GrayResult = cv2.bitwise_and(gray,gray,mask=graymask)

    cv2.imshow('RGB',RGBResult)
    cv2.imshow('HSV',HSVResult)
    # cv2.imshow('GRAY',GrayResult)

    k = cv2.waitKey(5) & 0xFF
    if k == 27:
        break

cap.release()

cv2.destroyAllWindows()