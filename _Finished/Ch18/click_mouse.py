import pyautogui

current_mouse_pos = pyautogui.position()


# pyautogui.click(10, 1040, duration=0)
#is the same as
pyautogui.mouseDown(1640, 1027)
pyautogui.mouseUp()

pyautogui.moveTo(current_mouse_pos)


# pyautogui.click(0, 1049)