from PIL import Image
from mss import mss
import time as t
import numpy as np
import cv2
import win32api
import win32con

mon = {'top': 680, 'left': 1240, 'width': 80, 'height': 80}

sct = mss()

while 1:
    sct.get_pixels(mon)
    img = Image.frombytes('RGB', (sct.width, sct.height), sct.image)
    imgTemp = np.array(img)

    lowBlue = np.array([60,30,0])
    # lowBlue = np.array([100,150,0])
    # lowBlue = np.array([0,115,35])
    highBlue = np.array([180,255,255])
    # highBlue = np.array([98,255,253])

    HSV = cv2.cvtColor(imgTemp, cv2.COLOR_BGR2HSV)
    RGB = cv2.cvtColor(imgTemp, cv2.COLOR_BGR2RGB)
    GRAY = cv2.cvtColor(imgTemp, cv2.COLOR_BGR2GRAY)

    HSVBlueMask = cv2.inRange(HSV, lowBlue, highBlue)
    MaskedRGB = cv2.bitwise_and(RGB, RGB, mask=HSVBlueMask)
    MaskedHSV = cv2.bitwise_and(HSV, HSV, mask=HSVBlueMask)

    cv2.imshow('HSV', np.array(HSV))
    cv2.imshow('RGB', np.array(RGB))
    cv2.imshow('GRAY', np.array(GRAY))
    cv2.imshow('MASK', np.array(HSVBlueMask))
    cv2.imshow('MASKEDRGB', np.array(MaskedRGB))
    cv2.imshow('MASKEDHSV', np.array(MaskedHSV))
    # cv2.imshow('RGBCircles', np.array(RGBcimb))

    # done = False
    #
    # for i in range(25):
    #     if i < 15 or done:
    #         print("nah fam")
    #     else:
    #         for x in range(25):
    #             if x < 15 or done:
    #                 print("nah fam")
    #             else:
    #                 if HSVBlueMask[i,x] == 255:
    #                     print("TRIGGERED")
    #                     win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
    #                     win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)
    #                     done = True

    if cv2.waitKey(25) & 0xFF == ord('q'):
        cv2.destroyAllWindows()
        break