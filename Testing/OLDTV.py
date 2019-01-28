from PIL import Image
from mss import mss
import time as t
import numpy as np
import cv2
import win32api
import win32con
import pytesseract
import os
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files (x86)\Tesseract-OCR\tesseract.exe"

# -----------------------------------------------------------------------------

center = {'top': 500, 'left': 920, 'width': 80, 'height': 80}
text = {'top': 460, 'left': 580, 'width': 760, 'height': 160}
sct = mss()

# -----------------------------------------------------------------------------

red = np.array([0, 0, 255])
blue = np.array([255, 0, 0])
cyan = np.array([185, 164, 0])
purple = np.array([223, 0, 97])
yellow = np.array([0, 141, 132])
green = np.array([0, 255, 0])

# -----------------------------------------------------------------------------

while 1:
    sct.get_pixels(center)
    img = Image.frombytes('RGB', (sct.width, sct.height), sct.image)
    imgTemp = np.array(img)

    sct.get_pixels(text)
    img = Image.frombytes('RGB', (sct.width, sct.height), sct.image)
    textTemp = np.array(img)

    RGB = cv2.cvtColor(imgTemp, cv2.COLOR_BGR2RGB)
    TEXT = cv2.cvtColor(textTemp, cv2.COLOR_BGR2GRAY)

    print("\n" * 100)
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

    cv2.imshow('RGB', RGB)
    cv2.imshow('TEXT', TEXT)

    # -----------------------------------------------------------------------------

    filename = "text.png"
    cv2.imwrite(filename, TEXT)

    colortext = pytesseract.image_to_string(Image.open("H:\\Misc\\Codes\\Random Stuff\\Testing\\%s" % filename), lang="eng")
    os.remove(filename)
    print("TEXT - \"%s\"" % colortext.upper())

    # -----------------------------------------------------------------------------

    if colortext.upper() == color:
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)
    elif color != "NONE" and colortext.upper() in ["BLUE", "RED", "CYAN", "PURPLE", "YELLOW", "GREEN"]:
        win32api.mouse_event(win32con.MOUSEEVENTF_RIGHTDOWN,0,0)
        win32api.mouse_event(win32con.MOUSEEVENTF_RIGHTUP,0,0)

    # -----------------------------------------------------------------------------

    if cv2.waitKey(25) & 0xFF == ord('q'):
        cv2.destroyAllWindows()
        break

    t.sleep(0.5)