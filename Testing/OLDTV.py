from PIL import Image
from mss import mss
import time as t
import numpy as np
import cv2
import win32api
import win32con
import pytesseract
import os
import imutils
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files (x86)\Tesseract-OCR\tesseract.exe"

# -----------------------------------------------------------------------------

center = {'top': 500, 'left': 920, 'width': 80, 'height': 80}
# toptext = {'top': 140, 'left': 580, 'width': 760, 'height': 320}
text = {'top': 460, 'left': 580, 'width': 760, 'height': 160}
# bottomtext = {'top': 620, 'left': 580, 'width': 760, 'height': 320}
sct = mss()

# -----------------------------------------------------------------------------

red = np.array([0, 0, 255])
blue = np.array([255, 0, 0])
cyan = np.array([185, 164, 0])
purple = np.array([223, 0, 97])
yellow = np.array([0, 141, 132])
green = np.array([0, 255, 0])
colorArray = ["BLUE", "RED", "CYAN", "PURPLE", "YELLOW", "GREEN"]

# -----------------------------------------------------------------------------

while 1:
    sct.get_pixels(center)
    img = Image.frombytes('RGB', (sct.width, sct.height), sct.image)
    imgTemp = np.array(img)

    # sct.get_pixels(toptext)
    # img = Image.frombytes('RGB', (sct.width, sct.height), sct.image)
    # topTextTemp = np.array(img)

    sct.get_pixels(text)
    img = Image.frombytes('RGB', (sct.width, sct.height), sct.image)
    textTemp = np.array(img)

    # sct.get_pixels(bottomtext)
    # img = Image.frombytes('RGB', (sct.width, sct.height), sct.image)
    # bottomTextTemp = np.array(img)

    RGB = cv2.cvtColor(imgTemp, cv2.COLOR_BGR2RGB)
    # TOPTEXT = cv2.cvtColor(topTextTemp, cv2.COLOR_BGR2GRAY)
    TEXT = cv2.cvtColor(textTemp, cv2.COLOR_BGR2GRAY)
    # BOTTOMTEXT = cv2.cvtColor(bottomTextTemp, cv2.COLOR_BGR2GRAY)

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
                elif np.array_equal(RGB[i,x], blue):
                    color = "BLUE"
                    done = True
                elif np.array_equal(RGB[i,x], red):
                    color = "RED"
                    done = True
                elif np.array_equal(RGB[i,x], cyan):
                    color = "CYAN"
                    done = True
                elif np.array_equal(RGB[i,x], purple):
                    color = "PURPLE"
                    done = True
                elif np.array_equal(RGB[i,x], yellow):
                    color = "YELLOW"
                    done = True
                elif np.array_equal(RGB[i,x], green):
                    color = "GREEN"
                    done = True

    print("COLOR - %s" % color)

    # -----------------------------------------------------------------------------

    filename = "text.png"
    cv2.imwrite(filename, TEXT)
    flipped = False

    colortext = pytesseract.image_to_string(Image.open("H:\\Misc\\Codes\\Random Stuff\\Testing\\%s" % filename), lang="eng").upper()
    os.remove(filename)

    # if not (colortext in colorArray) and color != "NONE" and not ("INVERTED" in bottomtext) and not ("DON'T SWITCH" in bottomtext):
    if not (colortext in colorArray) and color != "NONE":
        flipped = True
        TEXT = imutils.rotate(TEXT, 180)
        TEXT = cv2.flip(TEXT, 1)

        cv2.imwrite(filename, TEXT)
        colortext = pytesseract.image_to_string(Image.open("H:\\Misc\\Codes\\Random Stuff\\Testing\\%s" % filename), lang="eng").upper()
        os.remove(filename)

    # -----------------------------------------------------------------------------

    # filename = "bottomtext.png"
    # cv2.imwrite(filename, BOTTOMTEXT)
    #
    # bottomText = pytesseract.image_to_string(Image.open("H:\\Misc\\Codes\\Random Stuff\\Testing\\%s" % filename), lang="eng").upper()
    # topText = ""
    # os.remove(filename)

    # if flipped:
    #     filename = "toptext.png"
    #     TOPTEXT = imutils.rotate(TOPTEXT, 180)
    #     TOPTEXT = cv2.flip(TOPTEXT, 1)
    #
    #     cv2.imwrite(filename, TOPTEXT)
    #     topText = pytesseract.image_to_string(Image.open("H:\\Misc\\Codes\\Random Stuff\\Testing\\%s" % filename), lang="eng").upper()
    #     os.remove(filename)

    # -----------------------------------------------------------------------------

    # print("TOPTEXT - \"%s\"" % topText)
    print("COLORTEXT - \"%s\"" % colortext)
    # print("BOTTOMTEXT - \"%s\"" % bottomText)

    # -----------------------------------------------------------------------------

    if colortext == color:
        # if "INVERTED" in bottomText:
        #     win32api.mouse_event(win32con.MOUSEEVENTF_RIGHTDOWN,0,0)
        #     win32api.mouse_event(win32con.MOUSEEVENTF_RIGHTUP,0,0)
        # elif "DON'T SWITCH" in bottomText:
        #     t.sleep(2)
        # else:
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)
    elif color != "NONE" and colortext in colorArray:
        # if "INVERTED" in bottomText:
        #     win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
        #     win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)
        # elif "DON'T SWITCH" in bottomText:
        #     t.sleep(2)
        # else:
        win32api.mouse_event(win32con.MOUSEEVENTF_RIGHTDOWN,0,0)
        win32api.mouse_event(win32con.MOUSEEVENTF_RIGHTUP,0,0)

    # -----------------------------------------------------------------------------

    cv2.imshow('RGB', RGB)
    # cv2.imshow('TOPTEXT', TOPTEXT)
    cv2.imshow('TEXT', TEXT)
    # cv2.imshow('BOTTOMTEXT', BOTTOMTEXT)

    # -----------------------------------------------------------------------------

    if cv2.waitKey(25) & 0xFF == ord('q'):
        cv2.destroyAllWindows()
        break

    # t.sleep(0.1)