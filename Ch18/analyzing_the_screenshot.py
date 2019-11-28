import pyautogui

img = pyautogui.screenshot()

img.getpixel((50, 200)) # (33, 37, 43)

"""Only returns true on an exact match
"""

print(pyautogui.pixelMatchesColor(50, 200, (130, 135, 144))) # false
print(pyautogui.pixelMatchesColor(50, 200, (33, 37, 43))) # True
print(pyautogui.pixelMatchesColor(50, 200, (33, 37, 42))) # False