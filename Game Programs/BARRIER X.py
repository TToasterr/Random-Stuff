from directkeys import PressKey, A, D
from PIL import Image
from mss import mss
import time as t
import numpy as np
import cv2
import win32api
import win32con
import os
import imutils
import keyboard

# -----------------------------------------------------------------------------

center = {'top': 500, 'left': 800, 'width': 320, 'height': 320}
sct = mss()
white = np.array([255, 255, 255])

# -----------------------------------------------------------------------------

while 1:
    sct.get_pixels(center)
    img = Image.frombytes('RGB', (sct.width, sct.height), sct.image)
    imgTemp = np.array(img)

    RGB = cv2.cvtColor(imgTemp, cv2.COLOR_BGR2RGB)
    FAKERGB = cv2.cvtColor(imgTemp, cv2.COLOR_BGR2RGB)

    print("\n" * 50)
    pixel = RGB[40, 160]
    print(pixel)

    cv2.line(FAKERGB, (160, 35), (160, 45), (0, 255, 0), 1)
    cv2.line(FAKERGB, (155,40), (165, 40), (0, 255, 0), 1)

    cv2.imshow("RGB", FAKERGB)

    # -----------------------------------------------------------------------------

    print(pixel)
    if np.array_equal(pixel, white):
        print("ITS WHITE")
        PressKey(D)

    # -----------------------------------------------------------------------------

    if cv2.waitKey(25) & 0xFF == ord('q'):
        cv2.destroyAllWindows()
        break