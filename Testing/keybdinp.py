import keyboard as kbd
from time import sleep as s

def message(BSamount, message):
    for i in range(BSamount):
        kbd.send('backspace')
    kbd.write(message)
    kbd.send('return')

kbd.add_hotkey('a+s+d+f', lambda: message(4, 'ur mom big gay xd'))

kbd.wait()