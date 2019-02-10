from PIL import Image
from mss import mss
# from hackManager.hack import Hack
import time as t
import numpy as np
import cv2
import win32api
import win32con
import win32process
import win32ui
import pytesseract
import os
import imutils
import ctypes
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files (x86)\Tesseract-OCR\tesseract.exe"

# -----------------------------------------------------------------------------

center = {'top': 500, 'left': 920, 'width': 80, 'height': 80}
# text = {'top': 460, 'left': 580, 'width': 760, 'height': 400}
sct = mss()

# -----------------------------------------------------------------------------

Red = np.array([0, 0, 255])
Blue = np.array([255, 0, 0])
Cyan = np.array([185, 164, 0])
Purp = np.array([223, 0, 97])
Yell = np.array([0, 141, 132])
Gree = np.array([0, 255, 0])
colorArray = ["BLUE", "RED", "CYAN", "PURPLE", "YELLOW", "GREEN"]

# -----------------------------------------------------------------------------

while 1:
    sct.get_pixels(center)
    img = Image.frombytes('RGB', (sct.width, sct.height), sct.image)
    imgTemp = np.array(img)

    RGB = cv2.cvtColor(imgTemp, cv2.COLOR_BGR2RGB)

    print("\n" * 50)
    print(RGB[40,40])

    done = False

    color = "NONE"

    # -----------------------------------------------------------------------------

    for i in range(80):
        if done:
            do = "nothing"
        else:
            for x in range(80):
                if done:
                    do = "nothing"
                elif np.array_equal(RGB[i,x], Blue):
                    color = "BLUE"
                    done = True
                elif np.array_equal(RGB[i,x], Red):
                    color = "RED"
                    done = True
                elif np.array_equal(RGB[i,x], Cyan):
                    color = "CYAN"
                    done = True
                elif np.array_equal(RGB[i,x], Purp):
                    color = "PURPLE"
                    done = True
                elif np.array_equal(RGB[i,x], Yell):
                    color = "YELLOW"
                    done = True
                elif np.array_equal(RGB[i,x], Gree):
                    color = "GREEN"
                    done = True

    print(color)

    f = open("H:\\Misc\\Codes\\C++ Stuff\\OLDTV\\color.txt", "r+")
    valueString = f.read()
    print(valueString)
    sleepTime = 0.5
    if valueString == "CLICK":
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)
        sleepTime = 0
    elif valueString == color:
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)
    elif color != "NONE":
        win32api.mouse_event(win32con.MOUSEEVENTF_RIGHTDOWN,0,0)
        win32api.mouse_event(win32con.MOUSEEVENTF_RIGHTUP,0,0)
    # f.write(color)

    # -----------------------------------------------------------------------------

    # filename = "text.png"
    # cv2.imwrite(filename, TEXT)
    # flipped = False
    #
    # colortext = pytesseract.image_to_string(Image.open("H:\\Misc\\Codes\\Random Stuff\\Game Programs\\%s" % filename), lang="eng").upper().split("\n")
    # othertext = " ".join(colortext[len(colortext[0]) + 1:])
    # colortext = colortext[0]
    # os.remove(filename)
    #
    # if not (colortext in colorArray) and color != "NONE" and not ("INVERTED" in othertext) and not ("SWITCH" in othertext):
    #     flipped = True
    #     TEXT = imutils.rotate(TEXT, 180)
    #     TEXT = cv2.flip(TEXT, 1)
    #     TEXT = TEXT[200:400, 0:760]
    #
    #     cv2.imwrite(filename, TEXT)
    #     colortext = pytesseract.image_to_string(Image.open("H:\\Misc\\Codes\\Random Stuff\\Game Programs\\%s" % filename), lang="eng").upper().split("\n")
    #     othertext = " ".join(colortext[len(colortext[0]) + 1:])
    #     colortext = colortext[0]
    #     os.remove(filename)

    # -----------------------------------------------------------------------------

    # print("COLORTEXT - \"%s\"" % colortext)
    # print("OTHERTEXT - \"%s\"" % othertext)

    # -----------------------------------------------------------------------------

    # if colortext == color:
    #     if "INVERTED" in othertext:
    #         win32api.mouse_event(win32con.MOUSEEVENTF_RIGHTDOWN,0,0)
    #         win32api.mouse_event(win32con.MOUSEEVENTF_RIGHTUP,0,0)
    #     elif "SWITCH" in othertext:
    #         t.sleep(2)
    #     else:
    #         win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
    #         win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)
    #
    # elif color != "NONE" and colortext in colorArray:
    #     if "INVERTED" in othertext:
    #         win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
    #         win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)
    #     elif "SWITCH" in othertext:
    #         t.sleep(2)
    #     else:
    #         win32api.mouse_event(win32con.MOUSEEVENTF_RIGHTDOWN,0,0)
    #         win32api.mouse_event(win32con.MOUSEEVENTF_RIGHTUP,0,0)

    # -----------------------------------------------------------------------------

    # cv2.imshow('RGB', RGB)
    # cv2.imshow('TEXT', TEXT)

    # -----------------------------------------------------------------------------

    if cv2.waitKey(25) & 0xFF == ord('q'):
        cv2.destroyAllWindows()
        break

    t.sleep(sleepTime)