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
    lower_blue = np.array([hl,sl,vl])
    upper_blue = np.array([hh,sh,vh])

    mask = cv2.inRange(hsv,lower_blue, upper_blue)

    result = cv2.bitwise_and(RGB,RGB,mask = mask)

    cv2.imshow('result',result)

    k = cv2.waitKey(5) & 0xFF
    if k == 27:
        break

cap.release()

cv2.destroyAllWindows()