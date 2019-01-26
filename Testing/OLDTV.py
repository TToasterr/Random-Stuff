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

    RGB = cv2.cvtColor(imgTemp, cv2.COLOR_BGR2RGB)

    print(RGB[40,40])

    cv2.imshow('RGB', np.array(RGB))

    if cv2.waitKey(25) & 0xFF == ord('q'):
        cv2.destroyAllWindows()
        break