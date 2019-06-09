from keyboard import *
from datetime import *
from time import *
import win32api
import win32con

# -----------------------------------------------------------------------------

left_or_right = input("Do you use left or right click to place blocks?\n(please enter 'l' or 'r')\n")

# -----------------------------------------------------------------------------

if left_or_right == 'l':
    mouseDown = win32con.MOUSEEVENTF_LEFTDOWN
    mouseUp = win32con.MOUSEEVENTF_LEFTUP
    rmouseDown = win32con.MOUSEEVENTF_RIGHTDOWN
    rmouseUp = win32con.MOUSEEVENTF_RIGHTUP
else:
    mouseDown = win32con.MOUSEEVENTF_RIGHTDOWN
    mouseUp = win32con.MOUSEEVENTF_RIGHTUP
    rmouseDown = win32con.MOUSEEVENTF_LEFTDOWN
    rmouseUp = win32con.MOUSEEVENTF_LEFTUP

# -----------------------------------------------------------------------------

def click(amount, sleepTime):
    for i in range(amount):
        win32api.mouse_event(mouseDown,0,0)
        win32api.mouse_event(mouseUp,0,0)
        sleep(sleepTime)

def rclick(amount, sleepTime):
    for i in range(amount):
        win32api.mouse_event(rmouseDown,0,0)
        win32api.mouse_event(rmouseUp,0,0)
        sleep(sleepTime)

def realPrint(message):
    print('[%s] %s' % (datetime.now().time(), message))

# -----------------------------------------------------------------------------

print('Program Running..')

# -----------------------------------------------------------------------------

add_hotkey('m', lambda: (realPrint('M was pressed'), click(8, 0)))
add_hotkey('n', lambda: (realPrint('N was pressed'), click(11, 0.3)))

# -----------------------------------------------------------------------------

wait()