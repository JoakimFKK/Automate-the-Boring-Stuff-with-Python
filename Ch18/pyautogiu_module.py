import pyautogui

"""
PyAutoGui also has a fail-safe feature. Moving the mouse cursor to the upper-left corner of the screen will cause PyAutoGUI to raise the pyautogui.FailSafeException exception.
Your program can either handle this exception with try and except statements or let the exception crash your program.
"""

# pyautogui.PAUSE = 1 # Here we import pyautogui and set pyautogui.PAUSE to 1 for a one-second pause after each function call
pyautogui.PAUSE = 1 # Here we import pyautogui and set pyautogui.PAUSE to 1 for a one-second pause after each function call
pyautogui.FAILSAFE = True # We set pyautogui.FAILSAFE to True to enable the fail-safe feature.

def get_screen_size():
    print(pyautogui.size()) # Size(width=1680, height=1050)


def move_mouse():
    width, height = pyautogui.size()
    width = int(width / 2)
    height = int(height / 2)

    for i in range(10):
        pyautogui.moveTo((width - 100), (height - 100), duration=0.25)
        pyautogui.moveTo((width), (height - 100), duration=0.25)
        pyautogui.moveTo((width), (height), duration=0.25)
        pyautogui.moveTo((width - 100), (height), duration=0.25)


def move_mouse_relative():
    for i in range(10):
        pyautogui.moveRel(100, 0, duration=0.25)
        pyautogui.moveRel(0, 100, duration=0.25)
        pyautogui.moveRel(-100, 0, duration=0.25)
        pyautogui.moveRel(0, -100, duration=0.25)

def get_mouse_position():
    import time
    for i in range(5):
        time.sleep(2)
        print(pyautogui.position())
    ## Output:
    # Point(x=1356, y=239)
    # Point(x=224, y=200)
    # Point(x=259, y=747)
    # Point(x=1307, y=621)
    # Point(x=1148, y=270)