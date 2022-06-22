from pynput.keyboard import Key, Controller
import time

keyboard = Controller()

time.sleep(3)

while 1:

    keyboard.press('t')
    keyboard.release('t')
    keyboard.press('!')
    keyboard.release('!')
    keyboard.press('s')
    keyboard.release('s')
    keyboard.press('l')
    keyboard.release('l')
    keyboard.press('o')
    keyboard.release('o')
    keyboard.press('t')
    keyboard.release('t')
    keyboard.press('s')
    keyboard.release('s')
    keyboard.press(Key.space)
    keyboard.release(Key.space)
    keyboard.press('1')
    keyboard.release('1')
    keyboard.press('0')
    keyboard.release('0')
    keyboard.press(Key.enter)
    keyboard.release(Key.enter)
    time.sleep(7)
   

