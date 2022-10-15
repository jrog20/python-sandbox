import pyautogui, time

# https://pyautogui.readthedocs.io/en/latest/quickstart.html

# PyAutoGUI lets Python control the mouse and keyboard, and other GUI automation tasks
# pip install pyautogui

# moveRel(xOffset, yOffset, duration=num_seconds) moves mouse relative to its current position
# XY coordinates have 0, 0 origin at top left corner of the screen. 
# X increases going right, Y increases going down.

def make_busy():
    print('Press CTRL-C to quit.')
    try:
        while True:
            pyautogui.moveRel(10, 10)
            time.sleep(5)
    except KeyboardInterrupt:
        print('Process has quit...')

make_busy()