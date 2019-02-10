from keyboard import *
from datetime import *
from time import *
import win32api
import win32con

# -----------------------------------------------------------------------------

left_or_right = input("Do you use left or right click to place blocks?\n(please enter 'left' or 'right')\n")

# -----------------------------------------------------------------------------

if left_or_right == 'left':
    mouseDown = win32con.MOUSEEVENTF_LEFTDOWN
    mouseUp = win32con.MOUSEEVENTF_LEFTUP
else:
    mouseDown = win32con.MOUSEEVENTF_RIGHTDOWN
    mouseUp = win32con.MOUSEEVENTF_RIGHTUP

# -----------------------------------------------------------------------------

def click(amount, sleepTime):
    for i in range(amount):
        win32api.mouse_event(mouseDown,0,0)
        win32api.mouse_event(mouseUp,0,0)
        sleep(sleepTime)

# -----------------------------------------------------------------------------

print('Program Running..')

# -----------------------------------------------------------------------------

add_hotkey('m', lambda: (print('[%s] M was pressed' % datetime.now().time()), click(8, 0)))
add_hotkey('n', lambda: (print('[%s] N was pressed' % datetime.now().time()), click(10, 0.3)))

# -----------------------------------------------------------------------------

wait()