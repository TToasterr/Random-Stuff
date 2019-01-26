from PIL import Image
from mss import mss
import time as t
import numpy as np
import cv2
import win32api
import win32con

mon = {'top': 680, 'left': 1240, 'width': 80, 'height': 80}

sct = mss()

print("starting...")

# if vc.isOpened(): # try to get the first frame
#     rval, frame = vc.read()
# else:
#     rval = False

while(True):
    sct.get_pixels(mon)
    imgBytes = Image.frombytes('RGB', (sct.width, sct.height), sct.image)
    img = np.array(imgBytes)

    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    circles = cv2.HoughCircles(gray, cv2.HOUGH_GRADIENT, 1, 100, param1=10, param2=25, minRadius=5, maxRadius=20)

    if circles is None:
        continue

    print (circles, "ya yeet theres a circle")

    # win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
    # win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)

    for i in circles[0,:]:
       cv2.circle(gray,(i[0],i[1]),i[2],(0,255,0),1) # draw the outer circle
       cv2.circle(gray,(i[0],i[1]),2,(0,0,255),3) # draw the center of the circle

    cv2.imshow('video', gray)
    if cv2.waitKey(1)==27:# esc Key
        break

cv2.destroyAllWindows()